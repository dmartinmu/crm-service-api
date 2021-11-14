#!/bin/bash
set -e
case "$1" in
    develop)
        python src/app.py
        ;;
    test)
        uwsgi --http 0.0.0.0:8000 --chdir . --pythonpath src --wsgi-file src/app.wsgi --enable-threads --processes 1 --threads 2 --master --stats :9001 --stats-http --http-timeout 900 --logto results/api.log & sleep 15;
        pytest -v 
        ;;
    start-api)
        uwsgi --http 0.0.0.0:8000 --chdir . --pythonpath src --wsgi-file src/app.wsgi --enable-threads --processes 4 --threads 8 --master --stats :9001 --stats-http --http-timeout 900 --disable-logging
        ;;
    start-service)
        python src/app.py
        ;;
    *)
        echo "Usage develop | test | start-service | start-api "
esac
