from flask_wtf import FlaskForm
# IntegerField for integer input
from wtforms import IntegerField, DecimalField, SubmitField
# gives the user a limit and forces him to provide an input since it is a requirement for the features model
from wtforms.validators import DataRequired 

#blueprint for the form
class Prediction(FlaskForm):
    bedrooms = IntegerField('Number of Bedrooms', validators=[DataRequired()])
    bathrooms = IntegerField('Number of bathrooms', validators=[DataRequired()])
    sqft_living = DecimalField('sqft_living', validators=[DataRequired()])
    sqft_lot = DecimalField('sqft_lot', validators=[DataRequired()])
    floors = IntegerField('floors', validators=[DataRequired()])
    sqft_above = DecimalField('sqft_above', validators=[DataRequired()])
    sqft_lot15 = DecimalField('sqft_lot15', validators=[DataRequired()])
    yr_built = IntegerField('Year built', validators=[DataRequired()])
    condition = IntegerField('condition', validators=[DataRequired()])
    zipcode = IntegerField('Zipcode', validators=[DataRequired()])
    submit = SubmitField('Predict')


    
