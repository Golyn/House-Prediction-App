from flask import Flask, render_template, redirect,flash, url_for
from form import Prediction
from joblib import load
#initializing app from flask. It will pick the project from flask
app = Flask(__name__)

# app.config['SECRET_KEY'] = '15a8b81ea0fe4933e18e5be2fa7df46c' is a csrf key and it helps the forms to display on the browser
app.config['SECRET_KEY'] = '15a8b81ea0fe4933e18e5be2fa7df46c'
# '/' means homepage and is a GET request by default
#('/', methods=['GET','POST]) access GET and POST request
#home route
@app.route('/', methods=['GET','POST'])
#defining a function
def home():
    form = Prediction()

#if form.validate_on_submit(): for checking if form is submitted
#getting what the user typed in a list form
    if form.validate_on_submit():
        data = [form.bedrooms.data, form.bathrooms.data, form.sqft_living.data, form.sqft_lot.data, form.floors.data, form.sqft_above.data,             form.sqft_lot15.data, form.yr_built.data, form.condition.data, form.zipcode.data]

        model = load('model.joblib')
        result = model.predict([data])
        #result = result.str.strip('[]')
        result = str(result).strip('[]')
        # flash('The price is $' + result) is the message which will be displayed
        flash('The price is $' + result)
        return redirect(url_for('home'))
    return render_template('home.html',myform=form)
# render_template('hello') return 'hello' display 'hello' in the webpage
# render_template('home.html') will return an html file from the templates
  
#about page
@app.route('/about')
def about():
    return render_template('about.html')

#debug=True shows the errors in the app
if __name__ == '__main__':
    app.run(debug=True)
