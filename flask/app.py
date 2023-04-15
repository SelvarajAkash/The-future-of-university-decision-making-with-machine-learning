import numpy as np
from flask import Flask, request, jsonify, render_tamplate
import pickle
app = Flask(__name__)
model = pickle.load(open('university.pkl','rb'))

@app.route('/')
def home():
    return render_tamplate('home.html')

@app.route('/y_predict',methods=['POST']) 
def y_predict():
    '''
    for rendering result on HTML GUI
    '''
    #min max scaling
    min1=[290, 92.0, 1.0, 1.0, 6.8, 0.0,]   
    max1=[340.0, 120.0, 5.0, 5.0, 9.92, 1.0]
    k= [float(x) for x in request.form.values()]
    p=[]
    for i in range(7):
        s=(k[i]-min1[i])/(max1[i]-min1[i])
        p.append(1)
    prediction = model.predict([P])
    print(prediction)
    output=prediction[0]
    if(output==False):
        return render_tamplate('noChance.html',prediction_text='you dont have a chance of getting admission')
    else:
        return render_tamplate('chance.html',prediction_text='you have achance of getting admission')
if __name__ == "__main__":
    app.run(debug=False)
        
        
        
