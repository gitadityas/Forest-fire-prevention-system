from flask import Flask, render_template, request, redirect, url_for
import pickle as my_pickle

app = Flask(__name__)

with open('forest_fire_model.pkl', 'rb') as model_file:
    model = my_pickle.load(model_file)

@app.route('/about')
def about():
    return render_template('about_project.html')

@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username == 'admin' and password == 'password':
            return redirect(url_for('forest_fire_predictor'))
        else:
            return "Invalid credentials. Please try again."

    return render_template('login.html')

@app.route('/forest_fire_predictor')
def forest_fire_predictor():
    return render_template('forest_fire_predictor.html')

@app.route('/logout')
def logout():
    return render_template('logout.html')


@app.route('/')
def index():
    return render_template('forest_fire_predictor.html')

@app.route('/predict', methods=['POST'])
def predict():
    temperature = float(request.form['temperature'])
    humidity = float(request.form['humidity'])
    oxygen_level = float(request.form['oxygen'])

    prediction = model.predict([[temperature, humidity, oxygen_level]])
    if prediction[0] == 1:
        result = "Forest fire may occur."
    else:
        result = "Forest fire is less likely to occur."

    return render_template('result.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
