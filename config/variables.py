"""
Module: variables
Description: Загружает переменные окружения для подключения к YandexGPT.
"""

import os
from dotenv import load_dotenv

load_dotenv()

TICKET = (
    "С карты дважды списали оплату за сентябрь. "
    "Верните, пожалуйста, лишний платеж как можно быстрее."
)

YC_API_KEY = os.getenv("YC_API_KEY", "")
YC_FOLDER_ID = os.getenv("YC_FOLDER_ID", "")
YC_MODEL_URI = os.getenv("YC_MODEL_URI", "")
YC_BASE_URL = os.getenv("YC_BASE_URL", "")
