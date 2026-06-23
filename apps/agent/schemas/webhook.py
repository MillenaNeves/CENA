from pydantic import BaseModel


class WebhookResponse(BaseModel):
    status: str
    user: str
    message_received: str
    reply_sent: str


class WebhookIgnoredResponse(BaseModel):
    status: str = "ignored"
    reason: str


class ErrorResponse(BaseModel):
    status: str = "error"
    detail: str
