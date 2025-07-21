from appwrite.client import Client
from appwrite.services.databases import Databases
from flask import Flask, request, jsonify

app = Flask(__name__)

client = Client()
client.set_endpoint('https://fra.cloud.appwrite.io/v1')
client.set_project('680c76af0037a7d23e44')

databases = Databases(client)

@app.route('/')
def route_root():
    return ''

@app.get("/mail")
def get_mail():
    result = databases.list_documents(
    database_id = '680c778b000f055f6409',
    collection_id = '687a15df000014dff513',
    queries = []
    )
    return result

@app.get("/inventory")
def get_inventory():
    result = databases.list_documents(
    database_id = '680c778b000f055f6409',
    collection_id = '6876282f0003d93246fe',
    queries = []
    )
    return result

@app.post("/inventory")
def post_inventory():
    resquest_data = request.get_json()
    result = databases.create_document(
        database_id = '680c778b000f055f6409',
        collection_id = '6876282f0003d93246fe',
        document_id = 'unique()',
        data = resquest_data,
    )
    return result

@app.get("/subscription")
def get_subscription():
    result = databases.list_documents(
    database_id = '680c778b000f055f6409',
    collection_id = '687250d70020221fb26c',
    queries = []
    )
    return result
