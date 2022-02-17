#!/usr/bin/env python
# pylint: disable=C0116,W0613

import asyncio
from .bot import PBot
from telegram import Update
from telegram.ext import (
    CallbackContext,
    CommandHandler
)

def aexec(func):
    def wrapper(update: Update, context: CallbackContext):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(func(update, context))
        loop.close()
    return wrapper

def async_command(**kwargs):
    def wrapper(func):
        updater = PBot.updater
        updater.dispatcher.add_handler(CommandHandler(kwargs["name"], func, run_async=True))
    return wrapper

def command(**kwargs):
    def wrapper(func):
        updater = PBot.updater
        updater.dispatcher.add_handler(CommandHandler(kwargs["name"], func))
    return wrapper
