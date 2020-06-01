from app import application
from flask import render_template, request

import pandas as pd


class RosterRow:
    def __init__(self, owner_name, owner, player, number, college, position, age, team, trade_block):
        self.owner_name = owner_name
        self.owner = owner
        self.player = player
        self.number = number
        self.college = college
        self.position = position
        self.age = age
        self.team = team
        self.trade_block = trade_block


@application.route('/')
def index():
   return render_template('frontpage.html')


@application.route('/teams/<owner_name>', methods=['GET', 'POST'])
def team(owner_name):
    flip_trade_block()
    # TODO: Sort rosters by position, team, player, etc.
    return render_template(f'teams/{owner_name}.html', roster_rows=get_roster(owner_name))


@application.route('/home')
def homepage():
    return render_template('home.html')


@application.route('/trade_block')
def trade_block():
    rosters = get_all_rosters()
    return render_template('trade_block.html', rosters=rosters)


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

def get_roster(user_str, filter_for_trade_block=False):
    df = pd.read_csv('./backend/sleeper_response/owners_and_rosters.csv')
    df = df[df['owner_name'] == user_str]

    if filter_for_trade_block:
        df = df[df['trade_block']]

    roster_rows = []

    for row in df.itertuples():
        roster_rows.append(RosterRow(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

    return roster_rows


# TODO: Maintain separate csv with trade block info so it doesn't get reset after every data refresh
# TODO: Probably join this info with the incoming data initially
def flip_trade_block():
    df = pd.read_csv('./backend/sleeper_response/owners_and_rosters.csv')
    player = request.form.get('the_checkbox')

    if player:
        current_val = df[df['player'] == player]['trade_block']
        df.loc[df['player'] == player, 'trade_block'] = bool(1 - int(current_val))
        df.to_csv('./backend/sleeper_response/owners_and_rosters.csv', index=False)


def get_trade_block(user):
    df = pd.read_csv('./backend/sleeper_response/owners_and_rosters.csv')
    df = df[df['owner_name'] == user]

    roster_rows = []

    for row in df.itertuples():
        roster_rows.append(RosterRow(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8], row[9]))

    return roster_rows


def get_all_rosters():
    users = 'alex bill christian clayton jacob james jarod jon_ross sam tyler'.split()
    return {u: (get_roster(u, filter_for_trade_block=True)) for u in users}
