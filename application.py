from flask import Flask, request
import pickle

app = Flask(__name__)

@app.route("/", methods=['GET'])
def hello():
    return "Bienvenido, esta es mi api para predecir el sentimiento de un tweet\n consulta el endpoint /sentiment y envía el texto en el cuerpo de la petición en forma de array o lista dentro del valor 'texto' para predecir el sentimiento."

@app.route("/sentiment", methods=['GET'])
def predecir():
    dato = request.get_json()["texto"]
    with open("model/sentiment_model", "rb") as f:
        modelo = pickle.load(f)
    prediccion = modelo.predict(dato)
    resultado = []
    for x in prediccion: 
        if x ==1 :
            resultado.append("El texto es positivo")
        elif x == 0:
            resultado.append("El texto es negativo")
    return str(resultado)
if __name__ == "__main__":
    app.debug = True
    app.run()