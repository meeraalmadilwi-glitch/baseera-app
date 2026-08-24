with open('dashboard/urls.py', 'r', encoding='utf-8') as f:
    content = f.read()

missing_paths = '''
    # Impersonation and dataset actions
    path("impersonate/<int:user_id>/", views.impersonate_user, name="impersonate_user"),
    path("stop-impersonate/", views.stop_impersonate, name="stop_impersonate"),
    path("datasets/delete/<int:file_id>/", views.delete_dataset, name="delete_dataset"),
'''

if 'impersonate_user' not in content:
    content = content.replace('path("datasets/", views.datasets, name="datasets"),', 'path("datasets/", views.datasets, name="datasets"),\n' + missing_paths)
    
with open('dashboard/urls.py', 'w', encoding='utf-8') as f:
    f.write(content)
