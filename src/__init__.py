# coding=utf-8
import logging
import random
import json
from pathlib import Path

from flask import Flask
from flask_caching import Cache
from flack import Flack
from flack.message import Attachment

from . import config

logging.basicConfig(level=config.LOG_LEVEL)
logger = logging.getLogger(__name__)

app = Flask(__name__)
app.config.from_object(config)

flack = Flack(app)

cache = Cache(app)


@cache.memoize(timeout=50)
def _load_resource(filename):
    base_path = Path(config.RESOURCES_DIR)
    with open(base_path / f"{filename}.json") as f:
        return json.load(f)


@flack.trigger("!achoo", as_user="Gesundroid")
def trigger_achoo(**kwargs):
    responses = _load_resource("achoo")

    return ("[_{lang}_] {resp}\n"
            "[_English_] {resp_trans}"
            "The appropriate reply is:\n"
            "[_{lang}_] {reply}\n"
            "[_English_] {reply_trans}".format(
                **random.choice(responses)))


def _canned_reaction(key):
    reactions = _load_resource("reactions")

    try:
        reaction = reactions[key]
        if isinstance(reaction, list):
            reaction = random.choice(reaction)

        return reaction

    except KeyError:
        raise ValueError("Unknown reaction: {}".format(key))


@flack.trigger("!neat", as_user="Bender Bending Rodríguez")
def trigger_neat(**kwargs):
    return Attachment(fallback="Neat!",
                      image_url=_canned_reaction("neat"))


@flack.trigger("!yolo", as_user="Lonely Island")
def trigger_yolo(**kwargs):
    return Attachment(fallback="YOLO",
                      image_url=_canned_reaction("yolo"))


@flack.trigger("!nein", as_user="German Accent")
def trigger_nein(**kwargs):
    return Attachment(fallback="NeinNeinNein", color="danger",
                      image_url=_canned_reaction("nein"))


@flack.trigger("!shame", as_user="Septa Unella")
def trigger_shame(**kwargs):
    return Attachment(fallback="Shame!", color="warning",
                      image_url=_canned_reaction("shame"))


@flack.trigger("!hmm", as_user="Suspicious Cat")
def trigger_hmm(**kwargs):
    return Attachment(fallback="Hmm...", color="warning",
                      image_url=_canned_reaction("hmm"))


@flack.trigger("!clap", as_user="Sigh")
def trigger_clap(**kwargs):
    return Attachment(fallback="*Sarcastic Clapping*",
                      image_url=_canned_reaction("clap"))
