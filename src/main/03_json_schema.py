"""Module: 03_json_schema
Description: Получает schema-constrained ответ и отдельно проверяет его по контракту Pydantic.
"""

import json

from pydantic import ValidationError

from config.variables import TICKET
from src.lib.models import TicketClassification
from src.lib.llm_client import OutputMode, generate


def main() -> None:
    """Передать JSON Schema модели и проверить ответ так же, как в json_object."""
    schema = TicketClassification.model_json_schema()
    raw_result = generate(TICKET, OutputMode.JSON_SCHEMA, schema)
    parsed_result = json.loads(raw_result)
    print(json.dumps(parsed_result, ensure_ascii=False, indent=2))

    try:
        classification = TicketClassification.model_validate(parsed_result)
    except ValidationError as error:
        print("\nJSON валиден, контракт нарушен:")
        print(error)
        return

    print("\nКонтракт пройден:")
    print(classification.model_dump_json(indent=2))


if __name__ == "__main__":
    main()
