from flask import Flask, request, abort, Blueprint
from statistics import mean
import uuid

get_filename = lambda route_uuid : f'data/{route_uuid}.csv'
convert_v_grade = lambda v : v[1:]

grade_save = Blueprint('grade_save', __name__)

@grade_save.route('/add_route', methods=['POST'])
def add_route():
    route_uuid = str(uuid.uuid4())
    with open(get_filename(route_uuid), 'w+'):
        return route_uuid


@grade_save.route('/add_grade/<string:route_id>', methods=['POST'])
def add_grade(route_id: str):
    v_grade = request.json.get('grade')
    if v_grade is None:
        abort(400, 'Grade must be included in payload')
    with open(get_filename(route_id), 'a') as fp:
        fp.write(convert_v_grade(v_grade) + '\n')
    return route_id


@grade_save.route('/generate_average/<string:route_id>', methods=['GET'])
def generate_average(route_id: str):
    with open(get_filename(route_id), 'r') as file:
        average_grade = mean(int(row) for row in file.read().splitlines())
        return 'v' + str(average_grade)
            

@grade_save.route('/ping', methods=['GET'])
def ping():
    return 'pong'
