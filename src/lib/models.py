"""Module: models
Description: Описывает строгий контракт классификации обращения в поддержку.
"""

from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field


class TicketCategory(StrEnum):
    """Допустимые категории обращений."""

    BILLING = "billing"
    BUG = "bug"
    FEATURE = "feature"
    ACCESS = "access"
    OTHER = "other"


class TicketPriority(StrEnum):
    """Допустимые уровни приоритета."""

    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"
    CRITICAL = "critical"


class TicketClassification(BaseModel):
    """Результат классификации одного обращения."""

    model_config = ConfigDict(extra="forbid")

    category: TicketCategory = Field(description="Категория обращения")
    priority: TicketPriority = Field(description="Приоритет обработки")
    summary: str = Field(min_length=10, max_length=160, description="Краткое описание проблемы")
    requires_human: bool = Field(description="Нужна ли ручная проверка сотрудником")
