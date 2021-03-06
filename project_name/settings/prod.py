# production settings for {{ project_name }}
from {{ project_name }}.settings.base import *

import os
import dj_database_url

# this must not change in production
DEBUG = False
TEMPLATE_DEBUG = DEBUG

# in production set DATABASE_URL env variable to:
# postgres://user:password@host:port/dbname
DATABASES = {
    'default': dj_database_url.config()
}

# set SECRET_KEY env variable to something random
SECRET_KEY = os.environ.get('SECRET_KEY', None)

