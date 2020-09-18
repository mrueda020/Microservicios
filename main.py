from flask import Flask, jsonify, request
import json

server = Flask(__name__)


def leerArchivo(nombreArchivo):
    f = open(nombreArchivo)
    texto = f.read()
    f.close()
    return texto


@server.route('/api/sps/helloworld/v1', methods=['GET'])
def obtenerEmpleados():
    archivo = leerArchivo('Empleados.json')

    Empleados = json.loads(archivo)
    return jsonify({'response': 'Hola Mundo'}, {'Empleados': Empleados})


@server.route('/api/sps/helloworld/v1/<string:nombreEmpleado>', methods=['GET'])
def obtenerEmpleado(nombreEmpleado):
    archivo = leerArchivo('Empleados.json')
    Empleados = json.loads(archivo)

    Empleado = [empleado for empleado in Empleados if empleado['nombre'].lower()
                == nombreEmpleado.lower()]
    print(Empleado)
    if len(Empleado) > 0:
        return jsonify({'Empleado': Empleado})

    return jsonify({'error': 'Empleado no encontrado'})


if __name__ == '__main__':

    server.run(debug=True, port=8090)
