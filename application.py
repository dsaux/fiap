from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

#import pickle
#pkl_filename = 'pickle_model.pkl'
#with open(pkl_filename, 'rb') as file:
#    pickle_model = pickle.load(file)

#res = pickle_model.predict([[5.7, 3.2, 1.1, 3.6]])
#res

