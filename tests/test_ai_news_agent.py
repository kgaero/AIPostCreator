
import unittest
import asyncio
from unittest.mock import patch, MagicMock
from google.adk.runners import InMemoryRunner
from google.adk.models.llm_response import LlmResponse
from google.genai import types
from agents.ai_news_agent import agent

class TestAINewsAgent(unittest.TestCase):
    @patch('google.adk.models.registry.LLMRegistry.new_llm')
    def test_ai_news_agent_with_news(self, mock_new_llm):
        async def run_test():
            # This is a simplified mock of the LLM response.
            mock_llm_response = LlmResponse(
                content={
                    "parts": [
                        {
                            "text": "Here is the latest AI news: New AI Model by Google. Read more at https://google.blog/new-ai"
                        }
                    ]
                }
            )

            async def async_generator():
                yield mock_llm_response

            mock_llm = MagicMock()
            mock_llm.generate_content_async.return_value = async_generator()
            mock_llm.model = 'gemini-2.0-flash'
            mock_new_llm.return_value = mock_llm

            runner = InMemoryRunner(agent=agent.root_agent, app_name='ai_news_agent')
            await runner.session_service.create_session(
                app_name='ai_news_agent', user_id='test_user', session_id='test_session'
            )

            response_generator = runner.run(
                user_id='test_user',
                session_id='test_session',
                new_message=types.Content(parts=[types.Part(text='latest advancements in large language models')])
            )

            for _ in response_generator:
                pass
        asyncio.run(run_test())

    @patch('google.adk.models.registry.LLMRegistry.new_llm')
    def test_ai_news_agent_no_news(self, mock_new_llm):
        async def run_test():
            mock_llm_response = LlmResponse(content={"parts": [{"text": "no news"}]})

            async def async_generator():
                yield mock_llm_response

            mock_llm = MagicMock()
            mock_llm.generate_content_async.return_value = async_generator()
            mock_llm.model = 'gemini-2.0-flash'
            mock_new_llm.return_value = mock_llm

            runner = InMemoryRunner(agent=agent.root_agent, app_name='ai_news_agent')
            await runner.session_service.create_session(
                app_name='ai_news_agent', user_id='test_user', session_id='test_session'
            )

            response_generator = runner.run(
                user_id='test_user',
                session_id='test_session',
                new_message=types.Content(parts=[types.Part(text='some obscure topic')])
            )
            for _ in response_generator:
                pass
        asyncio.run(run_test())

if __name__ == '__main__':
    unittest.main()
