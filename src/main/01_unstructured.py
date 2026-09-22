"""Module: 01_unstructured
Description: Демонстрирует свободный текстовый ответ без гарантий формата.
"""

from config.variables import TICKET
from src.lib.llm_client import OutputMode, generate


def main() -> None:
    """Запросить и напечатать неструктурированный ответ модели."""
    result = generate(TICKET, OutputMode.TEXT)
    print(result)


if __name__ == "__main__":
    main()
