import os
from auto_app import config
import core 

def save_test_file(filename, test_file):
    path = os.path.join(config.FILE['upload_path'], filename)
    test_file.save(path)
    return path

def run_single_test(test):
    status = core.run_test(test['application_uri'], test['test_file_path'], test['expected_text'])
    return status

def run_project_tests(project, tests):
    results = []
    for test in tests:
        status = run_single_test(test)
        results.append(status)
    return results

