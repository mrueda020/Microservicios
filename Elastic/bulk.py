
from flask import Flask, jsonify
from elasticsearch import Elasticsearch, helpers
import requests
import json


elastic = Elasticsearch(cloud_id="elastic-enterprise-search-deployment:ZWFzdHVzMi5henVyZS5lbGFzdGljLWNsb3VkLmNvbTo5MjQzJDhhMjQzYTFlNzY4ZDQxNmFiZmZkYmQ5OGYzYjQxNDZlJGRhNTE4NGY5ZjUwNzQxNDRhYzA3OTE5NzFiYmVlODQ0",
                        http_auth=("elastic", "WnqbZyzUf0pZK4UoTjz1jDul"),)


Archivo = "Employee.json"


def leerArchivo(nombreArchivo):
    f = open(nombreArchivo)
    texto = f.read()
    f.close()
    return texto


archivo = leerArchivo(Archivo)

Empleados = json.loads(archivo)


helpers.bulk(elastic, Empleados)
