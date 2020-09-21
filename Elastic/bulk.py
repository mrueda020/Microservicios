
from elasticsearch import Elasticsearch, helpers
import requests
import json


elastic = Elasticsearch(
    'https://da5184f9f5074144ac0791971bbee844.eastus2.azure.elastic-cloud.com:9243/login?next=%2Fapp%2Fhome#/')


Archivo = "Employee.json"


def leerArchivo(nombreArchivo):
    f = open(nombreArchivo)
    texto = f.read()
    f.close()
    return texto


archivo = leerArchivo(Archivo)

Empleados = json.loads(archivo)


helpers.bulk(elastic, Empleados)
