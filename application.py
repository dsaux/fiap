from flask import Flask
app = Flask(__name__)

#import test

@app.route("/")
def hello():
    return "Hola Python!"
import pickle

pkl_filename = 'pickle_model.pkl'
with open(pkl_filename, 'rb') as file:
 pickle_model = pickle.load(file)

vLista = []
while True:
 input_str = input("Informe os 4 valores separados por virgula: ")
 str_List = input_str.split(',')
 values = [float(item) for item in str_list]
 res = pickle_model.predict([values])
 print(res)
