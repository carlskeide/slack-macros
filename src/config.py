# coding=utf-8
import sec

LOG_LEVEL = sec.load("log_level", fallback="INFO").upper()

# Flask
DEBUG = False

# Flask-Caching
CACHE_TYPE = "redis"
CACHE_REDIS_URL = sec.load("redis_url", fallback="redis://localhost")
CACHE_DEFAULT_TIMEOUT = 600

# Flack
FLACK_URL_PREFIX = "/"
FLACK_DEFAULT_NAME = "TzBot"
FLACK_TOKEN = sec.load("slack_token")

# App
RESOURCES_DIR = "./resources"
