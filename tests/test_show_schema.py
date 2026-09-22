"""Module: show_schema
Description: Показывает JSON Schema, построенную из модели Pydantic.
"""

import json

from src.lib.models import TicketClassification


def main() -> None:
    """Вывести контракт классификации в читаемом виде."""
    schema = TicketClassification.model_json_schema()
    print(json.dumps(schema, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
