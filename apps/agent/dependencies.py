from agent.services.ai_service import AIService
from agent.services.evolution_service import EvolutionApiService
from agent.services.webhook_service import WebhookService

evolution_service = EvolutionApiService()
ai_service = AIService()
webhook_service = WebhookService(
    evolution_service=evolution_service,
    ai_service=ai_service,
)


def get_evolution_service() -> EvolutionApiService:
    return evolution_service


def get_ai_service() -> AIService:
    return ai_service


def get_webhook_service() -> WebhookService:
    return webhook_service
