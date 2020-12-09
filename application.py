from flask import Flask
input("Informe os 4 valores separados por virgula: ")

app = Flask(__name__)

@app.route("/")
import test

def hello():
    return "Hola Python 2!"

# import pickle
# input("Informe os 4 valores separados por virgula: ")
#pkl_filename = '/notebook/pickle_model.pkl'
#with open(pkl_filename, 'rb') as file:
# pickle_model = pickle.load(file)

#vLista = []
#while True:
# input_str = input("Informe os 4 valores separados por virgula: ")
# str_List = input_str.split(',')
# values = [float(item) for item in str_list]
# res = pickle_model.predict([values])
# print(res)
# values
