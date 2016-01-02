#!/bin/sh

celery -A veggy_pi.tasks worker --loglevel=info
