#!/usr/bin/env python
# pylint: disable=C0116,W0613

from telegram.ext import Updater

class PBot:
    updater: Updater
        
    @staticmethod
    def init_bot(token):
        PBot.updater = Updater(token)
        return PBot.updater
