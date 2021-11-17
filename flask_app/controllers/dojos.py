#-----  Importing My "app" For "app.route" Using the Route of "from" flask_app.
from flask_app import app

#-----  Importing Render_Template, Redirect, Request, And Whatever Else I need For My app.routes to work "from" flask.
from flask import render_template, redirect, request

#-----  Importing Class Dojo 
from flask_app.models.dojo import Dojo

#-----  Importing Class Ninja
from flask_app.models.ninja import Ninja

#-----  Landing Page Redirect So I can Have A Word In Front Of My Forward Slash
@app.route('/')
def home():
    return redirect('/dojos')

#-----  Another Landing Page But Displaying the A Form
@app.route('/dojos')
def display_dojos():
    dojos = Dojo.show_all_dojos_query()
    return render_template('home.html', dojos = dojos)

#-----  Hidden Route
@app.route('/dojos/create', methods=['POST'])
def create_page():
    Dojo.create(request.form)
    return redirect('/')

#-----  Ninja form Landing Page
@app.route('/ninjas')
def show():
    dojos = Dojo.show_all_dojos_query()
    return render_template('ninjas.html', dojos = dojos)

#-----  Make A Ninja Instance Hidden Route
@app.route('/ninjas/make', methods=['POST'])
def make():
    Ninja.make(request.form)
    return redirect('/')

#-----  Landing Page For Dojo With Ninjas Info
@app.route('/dojos/<int:id>')
def view_dojo(id):
    data = {
    'id': id
    }
    dojo = Dojo.get_dojo_with_ninja(data)
    return render_template('dojos_view.html', dojo = dojo)