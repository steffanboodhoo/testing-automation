from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

Base = declarative_base()

class Test(Base):
    __tablename__ = 'test'
    test_id = Column(Integer, primary_key=True)
    test_name = Column(String(50), unique=True)
    test_description = Column(String(350))
    test_file_path = Column(String(100), nullable=False)
    application_uri = Column(String(100), nullable=False)
    timeout = Column(Integer, default=3)
    expected_text = Column(String(350), nullable=False)
    created_date = Column(Integer, nullable=False)
    created_by = Column(String(8), nullable=False)
    
class Project(Base):
    __tablename__ = 'project'
    project_id = Column(Integer, primary_key=True)
    project_name = Column(String(100), unique=True)
    project_description = Column(String(350))
    created_by = Column(String(8), nullable=False)

class ProjectTest(Base):
    __tablename__ = 'project_test'
    project_id = Column(Integer, primary_key=True)
    test_id = Column(Integer, primary_key=True)

class TestResults(Base):
    __tablename__ = 'test_results'
    test_result_id = Column(Integer, primary_key=True)
    test_id = Column(Integer)