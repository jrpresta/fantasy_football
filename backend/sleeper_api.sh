#!/usr/bin/env bash

#curl "https://api.sleeper.app/v1/league/519637473127157760/users" > sleeper_response/users.json
#curl "https://api.sleeper.app/v1/league/519637473127157760/rosters" > sleeper_response/rosters.json
#curl "https://api.sleeper.app/v1/players/nfl" > sleeper_response/players.json

chmod +x sleeper_response/parsers.py
python sleeper_response/parsers.py