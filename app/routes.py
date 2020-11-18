from app import app
from flask import render_template, session, redirect, url_for, request
import pickle

from app.forms import DataForm
from app.predict import preprocess, predict, postprocess

app.config['SECRET_KEY'] = 'DAT158'


@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])

def index():
    
    # Handle request from form
    form = DataForm()
    if form.validate_on_submit():

        # If the form is submitted and validated, store all the 
        # inputs in session
        for fieldname, value in form.data.items():
            session[fieldname] = value

        # Preprocess data
        data = preprocess(session)

        # Get model outputs 
        pred = predict(data)

        # Postprocess results
        pred = postprocess(pred)

        # Create the payload (we use session)
        session['pred'] = pred


        return redirect(url_for('index'))

    return render_template('index.html', form=form)