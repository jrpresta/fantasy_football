from app import application
from flask import render_template

import pandas as pd


class RosterRow:
    def __init__(self, owner_name, owner, player, number, college, position, age, team):
        self.owner_name = owner_name
        self.owner = owner
        self.player = player
        self.number = number
        self.college = college
        self.position = position
        self.age = age
        self.team = team


@application.route('/')
def index():
   return render_template('frontpage.html')


# TODO: Maybe add the team name to pass as a parameter to return the
@application.route('/teams/jon_ross')
def jon_ross():
    df = pd.read_csv('./backend/sleeper_response/owners_and_rosters.csv')
    df = df[df['owner_name'] == 'Jon-Ross']

    roster_rows = []

    for row in df.itertuples():
        roster_rows.append(RosterRow(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    return render_template('teams/jon_ross.html', roster_rows=roster_rows)


@application.route('/home')
def homepage():
    return render_template('home.html')


# TODO: Maybe add login system
# @application.route('/login')
# def login():
#     return render_template('login.html')


###############
# TESTING PAGES
###############

@application.route('/testing')
def testing():
    return render_template('base.html')


@application.route('/testing2')
def testing2():
    return render_template('child_test.html')

@application.route('/testing3')
def testing3():
    return render_template('team_parent.html')