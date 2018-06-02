#!flask/bin/python

from flask import Flask, jsonify, abort, make_response
from flask import request

#from service.Client import *
import service.Client as ClientService

import cx_Oracle

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# create a file handler
handler = logging.FileHandler('app.log')
handler.setLevel(logging.INFO)

# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# add the handlers to the logger
logger.addHandler(handler)

app = Flask(__name__)

#Get list of clients from database
@app.route('/getClients', methods=['GET'])
def get_clients():
    clients = []
    clients = ClientService.getClients()

    logger.info("Returning clients")
    logger.info(jsonify({'clients': clients}))

    return jsonify({'clients': clients})

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

'''
@app.route('/getTasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})

@app.route('/getTasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/createTask', methods=['POST'])
def create_task():
    if not request.json or not 'title' in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201
'''

if __name__ == '__main__':
    app.run(debug=True)
