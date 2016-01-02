#!/bin/sh

PROJECT_BASE="$HOME/pi"
PROJECT_HOME="$PROJECT_BASE/www"
PROJECT_BIN="$PROJECT_HOME/bin"
PROJECT_LOG="$PROJECT_HOME/log"
PATH="$PATH:$PROJECT_BIN"
DJANGO_SETTINGS_MODULE=www.settings
export DJANGO_SETTINGS_MODULE CWD PROJECT_BASE PROJECT_HOME PROJECT_BIN PATH PROJECT_LOG
