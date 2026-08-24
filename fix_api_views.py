import re

with open('dashboard/api_views.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add login_required to imports if missing
if 'from django.contrib.auth.decorators import login_required' not in content:
    content = 'from django.contrib.auth.decorators import login_required\n' + content

# Fix live_sync_api
content = re.sub(
    r'@csrf_exempt\ndef live_sync_api', 
    r'@login_required\n@csrf_exempt\ndef live_sync_api', 
    content
)

# Fix save_file_api
content = re.sub(
    r'@csrf_exempt\n@rate_limit\(requests_per_minute=20, key_prefix="save_file"\)\ndef save_file_api', 
    r'@login_required\n@csrf_exempt\n@rate_limit(requests_per_minute=20, key_prefix="save_file")\ndef save_file_api', 
    content
)

# Fix workspace_files_api
content = re.sub(
    r'@csrf_exempt\ndef workspace_files_api', 
    r'@login_required\n@csrf_exempt\ndef workspace_files_api', 
    content
)

# Fix mobile_toggle_user_status
content = re.sub(
    r'@csrf_exempt\ndef mobile_toggle_user_status', 
    r'@token_required\n@csrf_exempt\ndef mobile_toggle_user_status', 
    content
)

with open('dashboard/api_views.py', 'w', encoding='utf-8') as f:
    f.write(content)
