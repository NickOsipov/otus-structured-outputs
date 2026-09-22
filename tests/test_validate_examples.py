"""Module: validate_examples
Description: Локально показывает типовые нарушения контракта без вызова LLM.
"""

from typing import Any

from pydantic import ValidationError

from src.lib.models import TicketClassification

EXAMPLES: dict[str, dict[str, Any]] = {
    "valid": {
        "category": "billing",
        "priority": "high",
        "summary": "Клиент просит вернуть повторно списанный платеж",
        "requires_human": True,
    },
    "wrong_enum": {
        "category": "payment",
        "priority": "urgent",
        "summary": "Клиент просит вернуть повторно списанный платеж",
        "requires_human": True,
    },
    "missing_field": {
        "category": "billing",
        "priority": "high",
        "summary": "Клиент просит вернуть повторно списанный платеж",
    },
    "extra_field": {
        "category": "billing",
        "priority": "high",
        "summary": "Клиент просит вернуть повторно списанный платеж",
        "requires_human": True,
        "customer_card": "0000 0000 0000 0000",
    },
}


def validate_examples(examples: dict[str, dict[str, Any]]) -> tuple[int, int]:
    """Проверить примеры и вернуть число принятых и отклоненных объектов."""
    accepted = 0
    rejected = 0

    for name, data in examples.items():
        try:
            TicketClassification.model_validate(data)
        except ValidationError:
            rejected += 1
            print(f"{name}: контракт отклонен")
        else:
            accepted += 1
            print(f"{name}: контракт пройден")

    return accepted, rejected


def main() -> None:
    """Запустить локальную демонстрацию валидации."""
    accepted, rejected = validate_examples(EXAMPLES)
    print(f"Итого: {accepted} принято, {rejected} отклонено")


if __name__ == "__main__":
    main()
