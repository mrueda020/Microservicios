from flask import Flask, jsonify, request
import json

server = Flask(__name__)


def leerArchivo(nombreArchivo):
    f = open(nombreArchivo)
    texto = f.read()
    f.close()
    return texto


@server.route('/api/sps/helloworld/v1', methods=['GET'])
def ping():
    archivo = leerArchivo('Empleados.json')
    print(archivo)
    return jsonify({'response': 'Hola Mundo'})


if __name__ == '__main__':

    server.run(debug=True, port=8090)
