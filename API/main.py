from flask import Flask, jsonify, request
import json

server = Flask(__name__)
Archivo = "API/Empleados.json"


def leerArchivo(nombreArchivo):
    f = open(nombreArchivo)
    texto = f.read()
    f.close()
    return texto


@server.route('/api/sps/helloworld/v1', methods=['GET'])
def obtenerEmpleados():
    archivo = leerArchivo(Archivo)

    Empleados = json.loads(archivo)
    print(type(Empleados))
    return jsonify({'response': 'Hola Mundo'}, {'Empleados': Empleados})


@server.route('/api/sps/helloworld/v1/<string:nombreEmpleado>', methods=['GET'])
def obtenerEmpleado(nombreEmpleado):
    archivo = leerArchivo(Archivo)
    Empleados = json.loads(archivo)

    Empleado = [empleado for empleado in Empleados if empleado['nombre'].lower()
                == nombreEmpleado.lower()]
    print(Empleado)
    if len(Empleado) > 0:
        return jsonify({'Empleado': Empleado})

    return jsonify({'error': 'Empleado no encontrado'})


if __name__ == '__main__':
    # Se pone
    server.run(host="0.0.0.0", port=8080, debug=True)
