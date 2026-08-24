import re

with open('dashboard/views.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix chat_api
content = re.sub(
    r'def chat_api\(request\):', 
    r'@login_required\n@csrf_exempt\ndef chat_api(request):', 
    content
)

# Fix api_committee_save_thread (might be missing decorators?)
if 'def api_committee_save_thread(request):' in content and '@login_required' not in content.split('def api_committee_save_thread(request):')[0][-50:]:
    content = re.sub(
        r'def api_committee_save_thread\(request\):', 
        r'@login_required\n@csrf_exempt\ndef api_committee_save_thread(request):', 
        content
    )

with open('dashboard/views.py', 'w', encoding='utf-8') as f:
    f.write(content)
