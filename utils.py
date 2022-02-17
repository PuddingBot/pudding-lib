#!/usr/bin/env python
# pylint: disable=C0116,W0613

from telegram.utils.helpers import escape_markdown
from telegram import Update
from telegram.ext import CallbackContext

def escape_md(text):
    return escape_markdown(text, version=2)

def private_none(func, text="Run this command in a group."):
    def wrapper(update: Update, context: CallbackContext):
        if update.message.chat.type == "private":
            update.message.reply_text(text)
        else:
            func(update, context)
    return wrapper

def private_only(func, text="Run this command in my DMs. 😸"):
    def wrapper(update: Update, context: CallbackContext):
        if update.message.chat.type != "private":
            update.message.reply_text(text)
        else:
            func(update, context)
    return wrapper
