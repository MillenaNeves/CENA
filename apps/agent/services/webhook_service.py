from loguru import logger

from agent.core.exceptions import WebhookPayloadError, WebhookIgnoredError
from agent.schemas.webhook import WebhookResponse
from agent.services.ai_service import AIService
from agent.services.evolution_service import EvolutionApiService
from agent.utils.extract_user_number import extract_user_number


class WebhookService:
    def __init__(
        self,
        evolution_service: EvolutionApiService,
        ai_service: AIService,
    ) -> None:
        self._evolution = evolution_service
        self._ai = ai_service

    async def handle(self, body: dict) -> WebhookResponse:
        user_number, message = self._parse_payload(body)
        logger.info(f"Processing message from {user_number}: {message}")

        ai_response = await self._ai.generate_response(user_message=message)
        logger.info(f"AI response generated: {ai_response}")

        await self._evolution.send_text_message(user_number, ai_response)
        logger.info(f"Message sent successfully to {user_number}")

        return WebhookResponse(
            status="ok",
            user=user_number,
            message_received=message,
            reply_sent=ai_response,
        )

    def _parse_payload(self, body: dict) -> tuple[str, str]:
        try:
            key = body["data"]["key"]
        except (KeyError, TypeError) as e:
            raise WebhookPayloadError("invalid payload (missing key)") from e

        user_number = extract_user_number(key)
        if not user_number:
            raise WebhookIgnoredError("masked user (LID) - cannot respond")

        remote_jid = key.get("remoteJid", "")
        if "@g.us" in remote_jid:
            raise WebhookIgnoredError("message from group")

        if key.get("fromMe", False):
            raise WebhookIgnoredError("message from bot")

        message_data = body["data"].get("message", {})
        message = (
            message_data.get("conversation")
            or message_data.get("extendedTextMessage", {}).get("text")
        )

        if not message:
            raise WebhookIgnoredError("empty or unsupported message type")

        return user_number, message
