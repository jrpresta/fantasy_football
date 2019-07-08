from app import application
from flask import render_template


@application.route('/')
def index():
   return render_template('frontpage.html')


# TODO: Maybe add the team name to pass as a parameter to return the
@application.route('/teams/jon_ross')
def jon_ross():
    return render_template('teams/jon_ross.html')


@application.route('/home')
def homepage():
    return render_template('home.html')



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