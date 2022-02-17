#!/usr/bin/env python
# pylint: disable=C0116,W0613

from . import __path__ as ROOT_PATH
import json

def get_current():
    with open(ROOT_PATH[0]+"/app.json", "r") as f:
        version = json.load(f)["version"]
    return version
