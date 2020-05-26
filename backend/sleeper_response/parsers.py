#!/usr/bin/env python3

import json
import pandas as pd


class OwnerExtraction:
    def __init__(self, owner_id, player_ids):
        self.owner_id = owner_id
        self.player_ids = player_ids

    def __repr__(self):
        return f'Owner: {self.owner_id}\nPlayers: {self.player_ids}'

    def __str__(self):
        return self.__repr__()


class PlayerExtraction:
    def __init__(self, player_id, name, number, college, position, age, team):
        self.player_id = player_id
        self.name = name
        self.number = number
        self.college = college
        self.position = position
        self.age = age
        self.team = team

    def __repr__(self):
        return f'Player: {self.name}\nPosition: {self.position}\n'



# FOR ROSTER, EXTRACT OWNER ID AND PLAYER IDS
with open('./sleeper_response/rosters.json', 'r') as f:
    rosters_json = f.read()


rosters = json.loads(rosters_json)
owners = []

for roster in rosters:
    owner = OwnerExtraction(roster['owner_id'], roster['players'])
    owners.append(owner)


# FOR PLAYER, EXTRACT PLAYER ID, NAME, NUMBER, COLLEGE, POSITION, AGE
with open('./sleeper_response/players.json', 'r') as f:
    players_json = f.read()

players = json.loads(players_json)


player_extract = {}

for player_id in players:
    player = players[player_id]

    p = PlayerExtraction(player_id=player_id,
                         name=player.get('full_name'),
                         number=player.get('number'),
                         college=player.get('college'),
                         position=player.get('fantasy_positions'),
                         age=player.get('age'),
                         team=player.get('team')
                        )

    # print(player)

    player_extract[p.player_id] = p


id_owner_map = {"430542268483518464": "Bill",
                "436611612091084800": "Clayton",
                "433663340871413760": "Sam",
                "421315193381867520": "Alex",
                "428013718316531712": "Tyler",
                "456672293167296512": "Jacob",
                "432744742489423872": "Jarod",
                "427371783864193024": "James",
                "433723175537209344": "Christian",
                "456741202809581568": "Jon-Ross"}


# Badly-performaning way of building dataframe

owner_names_ = []
owners_      = []
players_     = []
numbers_     = []
colleges_    = []
positions_   = []
ages_        = []
teams_       = []

for o in owners:
    for p in o.player_ids:
        try:
            # Attempt to convert id to int, if fails, then id is a defense
            int(p)
            player = player_extract[p]

            owner_names_.append(id_owner_map[o.owner_id])
            owners_.append(o.owner_id)
            players_.append(player.name)
            numbers_.append(player.number)
            colleges_.append(player.college)
            ages_.append(player.age)
            teams_.append(player.team)

            # print(player)

            positions_.append(player.position[0])

        # TODO: Fix position NaN issue
        except:
            owner_names_.append(id_owner_map[o.owner_id])
            owners_.append(o.owner_id)
            players_.append(p)
            numbers_.append("-")
            colleges_.append("-")
            positions_.append("DEF")
            ages_.append("-")
            teams_.append(p)

df = pd.DataFrame({'owner_name': owner_names_, 'owner': owners_, 'player': players_, 'number': numbers_, 'college': colleges_, 'position': positions_, 'age': ages_, 'team': teams_})
df.to_csv('./sleeper_response/owners_and_rosters.csv', index=False)
