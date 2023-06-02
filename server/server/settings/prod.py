import os
from .base import *

DEBUG = os.environ.get("DEBUG", False)

ALLOWED_HOSTS = ["*"]

CSRF_TRUSTED_ORIGINS = [f'{os.environ.get("CSRF_TRUSTED_ORIGINS")}']