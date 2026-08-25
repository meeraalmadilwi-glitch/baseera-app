import os
import sys
import django
from google import genai

# Setup django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'baseera_web.settings')
django.setup()

from dashboard.services.ai_service import GeminiAIService

ai = GeminiAIService()
messages = [{"role": "user", "content": "hello! just testing! answer with one word."}]
agent_ids = ["general", "financial"]

stream = ai.generate_multi_agent_stream(agent_ids, messages, user_id=None)
for chunk in stream:
    print(chunk.strip())
