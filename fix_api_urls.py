with open('dashboard/urls.py', 'r', encoding='utf-8') as f:
    content = f.read()

missing_apis = '''
    # API endpoints
    path("api/insights/chat", views.chat_api, name="chat_api"),
    path("api/record-ai-usage/", views.record_ai_usage, name="record_ai_usage"),
    path("api/committee/save-thread/", views.api_committee_save_thread, name="api_committee_save_thread"),
    path("api/committee/get-threads/", views.api_committee_get_threads, name="api_committee_get_threads"),
    path("api/dynamic-chat/", views.api_dynamic_chat, name="api_dynamic_chat"),
    path("api/custom-agents/create/", views.api_create_custom_agent, name="api_create_custom_agent"),
    path("api/custom-agents/delete/<int:agent_id>/", views.api_delete_custom_agent, name="api_delete_custom_agent"),
    path("api/boardroom/debate/", views.api_boardroom_debate, name="api_boardroom_debate"),
    path("api/goals/update/", views.api_update_sales_goal, name="api_update_sales_goal"),
    path("api/notifications/mark-read/", views.api_mark_notifications_read, name="api_mark_notifications_read"),
    path("api/notifications/delete/<int:notif_id>/", views.api_delete_notification, name="api_delete_notification"),
    path("api/anomalies/dismiss/<int:alert_id>/", views.api_dismiss_anomaly, name="api_dismiss_anomaly"),
    path("api/weekly-digest/", views.api_get_weekly_digest, name="api_get_weekly_digest"),
    path("api/receipt/save/", views.save_receipt_record, name="save_receipt_record"),
'''

if 'api/insights/chat' not in content:
    content = content.replace('path("api/save_file/", api_views.save_file_api, name="save_file_api"),', missing_apis + '\n    path("api/save_file/", api_views.save_file_api, name="save_file_api"),')
    
with open('dashboard/urls.py', 'w', encoding='utf-8') as f:
    f.write(content)
