from langchain_groq import ChatGroq
from loguru import logger

from agent.core.config import settings
from agent.prompts.whatsapp_system_prompt import SYSTEM_PROMPT


class AIService:
    def __init__(self) -> None:
        self.model = ChatGroq(
            model="llama-3.1-8b-instant",
            temperature=0.0,
            api_key=settings.groq_api_key,
        )

    async def generate_response(self, user_message: str) -> str:
        messages = [
            ("system", SYSTEM_PROMPT),
            ("human", user_message),
        ]

        try:
            response = await self.model.ainvoke(messages)
            logger.debug(f"AI response generated: {response.content[:100]}...")
            return response.content
        except Exception as e:
            logger.error(f"Error generating AI response: {e}", exc_info=True)
            return "Desculpe, ocorreu um erro ao processar sua mensagem. Tente novamente."
