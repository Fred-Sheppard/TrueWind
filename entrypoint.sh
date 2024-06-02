#!/bin/sh

if [ "$FLASK_DEBUG" = "true" ]; then
    exec python3 -m flask run --host=0.0.0.0 --debug
else
    exec python3 -m flask run --host=0.0.0.0
fi
