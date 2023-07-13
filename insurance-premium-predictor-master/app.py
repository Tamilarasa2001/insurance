import flask
import pickle
import pandas as pd
# Use pickle to load in the pre-trained model.
path = r'C:\Users\Dell\Downloads\insurance-premium-predictor-master\insurance-premium-predictor-master\model\tamil_model.pkl'
with open(path, 'rb') as file:
    model=pickle.load(file)
app = flask.Flask(__name__, template_folder='templates')
# Set up the main route
@app.route('/', methods=['GET', 'POST'])
def main():
    if flask.request.method == 'GET':
        # Just render the initial form, to get input
        return(flask.render_template('main.html'))
    
    if flask.request.method == 'POST':
        # Extract the input
        Age = flask.request.form['Age']
        Diabetes = flask.request.form['Diabetes']
        Blood_Pressure_Problems = flask.request.form['Blood_Pressure_Problems']
        Any_Transplants = flask.request.form['Any_Transplants']
        Any_Chronic_Diseases = flask.request.form['Any_Chronic_Diseases']
        height_in_cm = flask.request.form['height_in_cm']
        Weight = flask.request.form['Weight']
        BMI = flask.request.form['BMI']
        Known_Allergies = flask.request.form['Known_Allergies']
        History_Of_Cancer_InFamily = flask.request.form['History_Of_Cancer_InFamily']
        Number_Of_Major_Surgeries = flask.request.form['Number_Of_Major_Surgeries']



        # Make DataFrame for model
        input_variables = pd.DataFrame([[Age,Diabetes,Blood_Pressure_Problems,Any_Transplants,Any_Chronic_Diseases,height_in_cm,Weight,BMI,Known_Allergies,History_Of_Cancer_InFamily,Number_Of_Major_Surgeries]],columns=['Age','Diabetes','Blood_Pressure_Problems','Any_Transplants','Any_Chronic_Diseases','height_in_cm','Weight','BMI','Known_Allergies','History_Of_Cancer_InFamily','Number_Of_Major_Surgeries'],dtype=float,index=['input'])
        # Get the model's prediction
        prediction = model.predict(input_variables)[0]
        # Render the form again, but add in the prediction and remind user
        # of the values they input before
        return flask.render_template('main.html',original_input={'Age':Age,'Diabetes':Diabetes,'Blood_Pressure_Problems':Blood_Pressure_Problems,'Any_Transplants':Any_Transplants,'Any_Chronic_Diseases':Any_Chronic_Diseases,'height_in_cm':height_in_cm,'Weight':Weight,'BMI':BMI,'Known_Allergies':Known_Allergies,'History_Of_Cancer_InFamily':History_Of_Cancer_InFamily,'Number_Of_Major_Surgeries':Number_Of_Major_Surgeries},result=prediction,)
