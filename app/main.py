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


# def generic_team(user):
#     @application.route('/teams/'+user, methods=['GET', 'POST'])
#     def team_page():
#         flip_trade_block()
#         return render_template(f'teams/{user}', roster_rows=get_roster(user))


@application.route('/teams/jon_ross', methods=['GET', 'POST'])
def jon_ross():
    flip_trade_block()
    return render_template('teams/jon_ross.html', roster_rows=get_roster('Jon-Ross'))

@application.route('/teams/bill', methods=['GET', 'POST'])
def bill():
    flip_trade_block()
    return render_template('teams/bill.html', roster_rows=get_roster('Bill'))

@application.route('/teams/alex', methods=['GET', 'POST'])
def alex():
    flip_trade_block()
    return render_template('teams/alex.html', roster_rows=get_roster('Alex'))

@application.route('/teams/christian', methods=['GET', 'POST'])
def christian():
    flip_trade_block()
    return render_template('teams/christian.html', roster_rows=get_roster('Christian'))

@application.route('/teams/clayton', methods=['GET', 'POST'])
def clayton():
    flip_trade_block()
    return render_template('teams/clayton.html', roster_rows=get_roster('Clayton'))

@application.route('/teams/jacob', methods=['GET', 'POST'])
def jacob():
    flip_trade_block()
    return render_template('teams/jacob.html', roster_rows=get_roster('Jacob'))

@application.route('/teams/james', methods=['GET', 'POST'])
def james():
    flip_trade_block()
    return render_template('teams/james.html', roster_rows=get_roster('James'))

@application.route('/teams/jarod', methods=['GET', 'POST'])
def jarod():
    flip_trade_block()
    return render_template('teams/jarod.html', roster_rows=get_roster('Jarod'))

@application.route('/teams/sam', methods=['GET', 'POST'])
def sam():
    flip_trade_block()
    return render_template('teams/sam.html', roster_rows=get_roster('Sam'))

@application.route('/teams/tyler', methods=['GET', 'POST'])
def tyler():
    flip_trade_block()
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
