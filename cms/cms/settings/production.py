from .base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','wt.liuxing3169.cn']
try:
    from .local import *
except ImportError:
    pass
