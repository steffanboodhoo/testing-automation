from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from models import Base, Test, Project, ProjectTest, TestResults
import core
import traceback
from auto_app import config
engine = create_engine(config.DB_URI, echo=False)
Base.metadata.create_all(engine)
LIMIT = 50

def create_test(test):
    session = Session(engine)
    status = core.insert(session, Test, test)
    session.close()
    return status

def create_project(project):
    session = Session(engine)
    status = core.insert(session, Project, project)
    session.close()
    return status

def create_project_test(project_test):
    session = Session(engine)
    status = core.insert(session, ProjectTest, project_test)
    session.close()
    return status

def get_test(test_id):
    session = Session(engine)
    resp = core.get(session, Test, filters={'test_id':test_id})
    return clean_records(resp)[0]

def get_tests():
    session = Session(engine)
    tests = core.get(session, Test)
    return clean_records(tests)

def get_project_and_tests(project_id):
    session = Session(engine)
    project = core.get(session, Project, filters={'project_id':project_id})
    tests = core.get_project_tests(session, project_id, Test, ProjectTest)
    return {'project':project, 'tests':tests}

def clean_records(dirty_records):
    clean_records = []
    for rec in dirty_records:
        rec = rec.__dict__
        rec.pop('_sa_instance_state')
        clean_records.append(rec)
    return clean_records

# def get_test(test_id):