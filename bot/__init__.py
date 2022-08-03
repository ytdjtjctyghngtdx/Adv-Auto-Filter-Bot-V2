#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) @AlbertEinsteinTG

import os
import logging
import time

from logging.handlers import RotatingFileHandler

from .translation import Translation

# Change Accordingly While Deploying To A VPS
APP_ID = 13820773

API_HASH = 14dd075422f501a91407231fc98af817

BOT_TOKEN = 5375408785:AAFEK3MBMF4YjDvF-yeNgH7zCcsvxvltA3c

DB_URI = mongodb+srv://ishan:ishan@cluster0.de5wk.mongodb.net/?retryWrites=true&w=majority

USER_SESSION = BQAjXCwapG2TqnvPp9gmxvSOh8aj7-nLUVu6edSIwVoNXZTlQTO1Kii-LHuW5RobLSyLH4tByVm2e7cLUHm8dWu_rMsn4H43lLBIG1yz1aWM-WPxFAuCtEUaHbAm0EK8N26RSkzzQlGHn95KPfFcWl0D4y9g77t49ZpgaRGpgoKE9d9O_L9TX8mNVZbq6Y1jT40dwF7Nw0u5BozDtGV2i1cyYRkGZLRhVf56ugAZlnVHwTMgn2WBwEjYaWzp8BvYtE7OP7ZGbqHWNtmiOmjJ7Yg5R2WCFcUonUDzLf9on7dyqSEH9lJhGRwoFTWOzO5EXtTaqPt-KYIWlMUUsACoCaJLAAAAAT4wwvYA

VERIFY = {}

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            "autofilterbot.txt",
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

start_uptime = time.time()


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
