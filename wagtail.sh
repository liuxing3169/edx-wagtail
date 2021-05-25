#!/usr/bin/env bash

# This file is created and updated by ansible, edit at your peril



export PORT="8020"
export ADDRESS="127.0.0.1"
export LANG="en_US.UTF-8"
export DJANGO_SETTINGS_MODULE="cms.settings.production"
export SERVICE_VARIANT="wagtail"
export PATH="/edx/app/edx-wagtail/env/bin:/edx/app/edxapp/venvs/edxapp/bin:/edx/app/edxapp/edx-platform/bin:/edx/app/edxapp/edx-platform/node_modules/.bin:/edx/app/edxapp/nodeenvs/edxapp/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin"
export BOTO_CONFIG="/edx/app/edxapp/.boto"
#export EDX_REST_API_CLIENT_NAME="default_env-default_deployment-lms"

export WAGTAIL_CFG="/edx/etc/wagtail.yml"
source /edx/app/edx-wagtail/env/bin/activate
# We exec so that gunicorn is the child of supervisor and can be managed properly
exec /edx/app/edx-wagtail/env/bin/gunicorn -c /edx/app/edx-wagtail/wagtail_gunicorn.py cms.wsgi
