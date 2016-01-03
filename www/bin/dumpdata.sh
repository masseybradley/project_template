#!/bin/sh

# output directory is relative to the PATH of the manage.py command
$PROJECT_HOME/manage.py dumpdata --format=json -o veggy_pi/fixtures/rpi_pin.json
$PROJECT_HOME/manage.py dumpdata --format=yaml -o veggy_pi/fixtures/rpi_pin.yaml
