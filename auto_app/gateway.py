import test_files, test_db, authentication as auth
import json, time

def handle_authenticate(username, password):
    resp = auth.authenticate(username, password)
    return resp

def handle_get_tests():
    resp = test_db.get_tests()
    return json.dumps(resp)

def handle_create_test(test_name, application_uri, expected_text, test_file, created_by, test_description=None, timeout=None):
    test_file_path = test_files.save_test_file(test_name, test_file)
    resp = test_db.create_test({'test_name':test_name, 'application_uri':application_uri, 'test_file_path':test_file_path, 'expected_text':expected_text, 'created_by':created_by, 'created_date':int(time.time()), 'test_description':test_description, 'timeout':timeout})
    return resp, 200

def handle_create_project(project_name, created_by, project_description=None):
    resp = test_db.create_project({'project_name':project_name, 'created_by':created_by, 'project_description':project_description})
    return resp, 200

def handle_add_project_test(project_id, test_id):
    resp = test_db.create_project_test({'project_id':project_id, 'test_id':test_id})
    return resp, 200

def handle_test_single_run(test_id):
    test = test_db.get_test(test_id)
    print test
    resp = test_files.run_single_test(test)
    return resp, 200

def handle_test_project_run(project_id):
    data = test_db.get_project_and_tests(project_id)
    resp = test_files.run_project_tests(data['project'], data['tests'])
    return resp, 200

