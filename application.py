from flask import Flask, pickle
#import pickle

app = Flask(_name_)
@app.route('/')

pkl_filename = 'pickle_model.pkl'
with open(pkl_filename, 'rb') as file:
    pickle_model = pickle.load(file)

res = pickle_model.predict([[5.7, 3.2, 1.1, 3.6]])
res

