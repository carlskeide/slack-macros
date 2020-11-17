# coding=utf-8
from .. import (
    trigger_achoo,
    trigger_neat,
    trigger_yolo,
    trigger_nein,
    trigger_shame,
    trigger_hmm,
    trigger_clap,
)


def test_achoo():
    assert "appropriate reply" in trigger_achoo()


def test_canned_reactions():
    response = trigger_neat()
    assert response.fallback == "Neat!"
    assert response.image_url.startswith("http")
    assert trigger_neat().image_url.startswith("http")
    assert trigger_yolo().image_url.startswith("http")
    assert trigger_nein().image_url.startswith("http")
    assert trigger_shame().image_url.startswith("http")
    assert trigger_hmm().image_url.startswith("http")
    assert trigger_clap().image_url.startswith("http")
