import os
import re

def get_url_names_from_urls():
    with open('dashboard/urls.py', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Match name="url_name" or name='url_name'
    pattern = r'name=[\"\'\']([^\"\'\']+)[\"\'\']'
    return set(re.findall(pattern, content))

def get_url_usages_from_templates():
    template_dir = 'dashboard/templates'
    url_usages = set()
    
    for root, dirs, files in os.walk(template_dir):
        for file in files:
            if file.endswith('.html'):
                with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # Match {% url 'url_name' ... %} or {% url "url_name" ... %}
                    pattern = r'{%\s*url\s+[\"\'\']([^\"\'\']+)[\"\'\']'
                    matches = re.findall(pattern, content)
                    url_usages.update(matches)
                    
    return url_usages

defined = get_url_names_from_urls()
used = get_url_usages_from_templates()

missing = used - defined
unused = defined - used

print("--- Missing URLs in urls.py (Used in templates but not defined) ---")
if missing:
    for m in missing:
        print(f"- {m}")
else:
    print("None! All template URLs are perfectly mapped in urls.py")

print("\n--- Unused URLs in templates (Defined in urls.py but not used in HTML) ---")
if unused:
    for u in unused:
        print(f"- {u}")
else:
    print("None!")
