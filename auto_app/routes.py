from flask import request, session 
from auto_app import config, auto_app as app
from functools import wraps
import gateway
import jwt, json

def store_username(session, username):
    token = jwt.encode({'username':username}, config.JWT_SECRET)
    session['SID'] = token

def read_username(session):
    token = session['SID']
    data = jwt.decode(token, config.JWT_SECRET)
    return data['username']

def auth_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        username = -1
        try:
            print session['SID']
            username = read_username(session)
        except Exception as e:
            return json.dumps({'message':'Token is invalid/missing'}), 401
        return f(*args, **kwargs)
    return decorated

@app.route('/authenticate', methods=['POST'])
def authenticate():
    data = request.get_json()
    resp = gateway.handle_authenticate(data['username'], data['password'])
    if resp['status'] == 'success':
        store_username(session, data['username'])
        return json.dumps(resp), 200
    return json.dumps(resp), 401

@app.route('/logout', methods=['POST'])
def logout():
    print session['SID']
    session.pop('SID')
    return json.dumps({'status':'success'})

@app.route('/test', methods=['GET','POST','DELETE'])
@auth_required
def handle_test():
    if request.method=='GET':
        return gateway.handle_get_tests()
    elif request.method=='POST':
        meta = request.form
        test_file = request.files['test_file']
        username = read_username(session)
        test_description = None if not 'test_description' in meta else meta['test_description']
        timeout = None if not 'timeout' in meta else meta['timeout']
        return gateway.handle_create_test(meta['test_name'], meta['application_uri'], meta['expected_text'], test_file, username, test_description, timeout)
    elif request.method=='DELETE':
        return 'UNIMPLEMENTED', 204
    print request.method

@app.route('/project', methods=['GET', 'POST', 'PUT', 'DELETE'])
@auth_required
def handle_project():
    if request.method == 'GET':
        return 'UNIMPLEMENTED', 204
    elif request.method == 'POST':
        data = request.get_json()
        username = read_username(session)
        return gateway.handle_create_project(data['project_name'], username)
    else:
        return 'UNIMPLEMENTED', 204

@app.route('/project_test', methods=['GET', 'POST', 'PUT', 'DELETE'])   
@auth_required
def handle_project_test():
    if request.method == 'GET':
        return 'UNIMPLEMENTED', 204
    elif request.method == 'POST':
        return 'UNIMPLEMENTED', 204
    else:
        return 'UNIMPLEMENTED', 204

@app.route('/run/single', methods=['GET'])
@auth_required
def handle_run_single():
    test_id = request.args['test_id']
    return gateway.handle_test_single_run(test_id)

@app.route('/run/project', methods=['GET'])
@auth_required
def handle_run_project():
    project_id = request.args['project_id']
    return gateway.handle_test_project_run(project_id)


@app.route('/', methods=['GET'])
def index():
    return 'test', 200

@app.route('/test-sess')
def test_sess():
    print session['SID']