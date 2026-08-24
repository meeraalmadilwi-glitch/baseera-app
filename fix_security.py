import re

with open('dashboard/security.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix issue_access_token
new_issue = '''
def issue_access_token(user):
    # Bind token to user's password hash to prevent hijacking after password reset
    pwd_hash = user.password[-10:] if user.password else "nopwd"
    return signing.dumps({"user_id": user.pk, "pwd_hash": pwd_hash}, salt=f"baseera-mobile-{pwd_hash}")
'''

content = re.sub(r'def issue_access_token\(user\):[\s\S]*?return signing\.dumps[^}]*salt="baseera-mobile-auth"\)', new_issue.strip(), content)

# Fix token_required
old_token_required_str = '''
        try:
            payload = signing.loads(
                authorization[7:].strip(),
                salt="baseera-mobile-auth",
                max_age=60 * 60 * 12,
            )
            request.user = User.objects.get(pk=payload["user_id"], is_active=True)
        except (signing.BadSignature, signing.SignatureExpired, KeyError, User.DoesNotExist, TypeError, ValueError):
'''

new_token_required_str = '''
        try:
            # First, extract payload without verification to get the pwd_hash
            token_str = authorization[7:].strip()
            # In Django, signing format is base64: payload:signature:timestamp
            # We can use TimestampSigner to just unsign and check, or we can catch user early
            import base64
            import json
            
            # Proper way: we don't know pwd_hash yet. But we can extract user_id.
            # Let's decode the payload
            payload_b64 = token_str.split(':')[0]
            
            # Since Django's default serializer might be JSON, we try to parse it.
            # A simpler approach is to decode it ignoring signature just to get user_id,
            # then fetch user, then do full validation with signing.loads.
            # But signing.loads needs the salt.
            # Let's just use a fixed salt for the token but include the password hash inside the payload and verify it manually!
'''

# Wait, my previous plan for JWT used user.password[-10:] as salt. But to decode it, we need to know the salt!
# Since we don't know the user before decoding, we shouldn't use it as salt unless we parse the token first.
# A better way is: use fixed salt, put pwd_hash in payload, and check if it matches after decoding.
