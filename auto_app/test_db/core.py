def get(session, Model, filters=None, offset=None, limit=None):
    records = []
    print filters
    query = session.query(Model)
    if filters != None:
        for key, val in filters.items():
            query = query.filter(getattr(Model, key) == val)
    if limit != None and offset != None:
        query = query.slice(offset, limit)
    for rec in query:
        records.append(rec)
    return records


def insert(session, Model, data):
    new_entity = Model(**data)
    session.add(new_entity)
    session.commit()
    return {'status': 'success'}


def delete(session, Model, filters):
    query = session.query(Model)
    for key, val in filters.items():
        query = query.filter(getattr(Model, key) == val)
    for rec in query:
        session.delete(rec)
    session.commit()
    return {'status': 'success'}


def update(session, Model, filters, update):
    query = session.query(Model)
    for key, val in filters.items():
        query = query.filter(getattr(Model, key) == val)

    for key, val in update.items():
        for rec in query:
            setattr(rec, key, val)
    session.commit()
    return {'status': 'success'}

def get_project_tests(session, project_id, Test, ProjectTest):
    query = session.query(Test).join(ProjectTest).filter(ProjectTest.project_id == project_id)
    for rec in query:
        records.append(rec)
    return records