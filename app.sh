#!/bin/sh
/opt/conda/envs/rasa-env/bin/python -m rasa_core.run -d /app/models/current/dialogue -u /app/models/FateBOT/current --endpoints ./rasa_core/endpoints.yml -o models/out.log --enable_api