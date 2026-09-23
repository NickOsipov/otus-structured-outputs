"""
Module: variables
Description: Загружает переменные окружения для подключения к Ollama.
"""

import os
from dotenv import load_dotenv

load_dotenv()

TICKET = (
    "С карты дважды списали оплату за сентябрь. "
    "Верните, пожалуйста, лишний платеж как можно быстрее."
)

OLLAMA_BASE_URL = os.getenv("OLLAMA_BASE_URL", "http://localhost:11434/v1")
OLLAMA_MODEL = os.getenv("OLLAMA_MODEL", "llama3.2:3b")
OLLAMA_API_KEY = os.getenv("OLLAMA_API_KEY", "ollama")
