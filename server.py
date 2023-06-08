from flask import Flask,render_template,request,jsonify,Markup
import numpy as np
import pickle

crop_recommendation_model_path = '../models/RandomForest1.pkl'
crop_recommendation_model = pickle.load(
    open(crop_recommendation_model_path, 'rb'))

app=Flask(__name__)




@app.route('/')
def home():
    return render_template('crop.html')


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')

@ app.route('/predict', methods=['GET','POST'])
def crop_prediction(): 

    if request.method == 'POST':
        N = int(request.form['nitrogen'])
        P = int(request.form['phosphorus'])
        K = int(request.form['potassium'])
        ph = float(request.form['ph'])
        rainfall = float(request.form['rainfall'])
        temperature = float(request.form['temperature'])
        humidity = float(request.form['humidity'])
        

        data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])
        my_prediction = crop_recommendation_model.predict(data)
        final_prediction = my_prediction[0]

        input_features = [N,P,K,
                          temperature, humidity, ph, rainfall]

        # for i in input_features:
        #     print(i)
       
        
        value = final_prediction
        print(value)

        return render_template('result.html', value=value)
    
    else:
        return render_template('predict.html')


@app.route('/login', methods=['GET','POST'])
def login():
    return "hi" 



@app.route('/register', methods=['GET','POST'])
def register():
    return "hi" 
    
        

if __name__=="__main__":
    print("Starting python flask server")
    app.debug=True
    app.run()