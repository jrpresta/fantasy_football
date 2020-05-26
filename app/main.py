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


@application.route('/teams/jon_ross')
def jon_ross():
    return render_template('teams/jon_ross.html', roster_rows=get_roster('Jon-Ross'))

@application.route('/teams/bill')
def bill():
    return render_template('teams/bill.html', roster_rows=get_roster('Bill'))

@application.route('/teams/alex')
def alex():
    return render_template('teams/alex.html', roster_rows=get_roster('Alex'))

@application.route('/teams/christian')
def christian():
    return render_template('teams/christian.html', roster_rows=get_roster('Christian'))

@application.route('/teams/clayton')
def clayton():
    return render_template('teams/clayton.html', roster_rows=get_roster('Clayton'))

@application.route('/teams/jacob')
def jacob():
    return render_template('teams/jacob.html', roster_rows=get_roster('Jacob'))

@application.route('/teams/james')
def james():
    return render_template('teams/james.html', roster_rows=get_roster('James'))

@application.route('/teams/jarod')
def jarod():
    return render_template('teams/jarod.html', roster_rows=get_roster('Jarod'))

@application.route('/teams/sam')
def sam():
    return render_template('teams/sam.html', roster_rows=get_roster('Sam'))

@application.route('/teams/tyler')
def tyler():
    return render_template('teams/tyler.html', roster_rows=get_roster('Tyler'))



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


############
# MISC FUNCS
############

# TODO: MOVE LATER

def get_roster(user_str):
    df = pd.read_csv('./backend/sleeper_response/owners_and_rosters.csv')
    df = df[df['owner_name'] == user_str]

    roster_rows = []

    for row in df.itertuples():
        roster_rows.append(RosterRow(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8]))

    return roster_rows
