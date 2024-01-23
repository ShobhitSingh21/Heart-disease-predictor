import pickle
from flask import url_for, flash, Flask,redirect, render_template, request
import sklearn
model = pickle.load(open('model.pkl', 'rb'))
# step 1

app = Flask(__name__)

app.secret_key = 'Nothing'

@app.route('/')
def index() :
    return render_template('index.html')

@app.route('/predict', methods = ['GET', 'POST'])
def predict() :
    age = (request.form.get('age'))
    sex = (request.form.get('sex'))
    cp = (request.form.get('cp'))
    trestbps = (request.form.get('trestbps'))
    chol = (request.form.get('chol'))
    fbs = (request.form.get('fbs'))
    restecg = (request.form.get('restecg'))
    thalach = (request.form.get('thalach'))
    exang = (request.form.get('exang'))
    oldpeak = (request.form.get('oldpeak'))
    slope = (request.form.get('slope'))
    if not all([age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope]):
        flash('Invalid Form Submission!', 'error')
        return redirect(url_for('index'))

    prediction = model.predict([[int(age),
                                 int(sex) ,
                                 int(cp),
                                 int(trestbps),
                                 int(chol),
                                 int(fbs),
                                 int(restecg),
                                 int(thalach),
                                 int(exang),
                                 float(oldpeak),
                                 int(slope)]])

    if(int(prediction) == 0) :
        return render_template('result.html', pred_text = 'No Heart Disease')
    else :
        return render_template('result.html', pred_text = 'Heart Disease')



if __name__ == '__main__' :
    app.run(debug = False, host = '0.0.0.0')


