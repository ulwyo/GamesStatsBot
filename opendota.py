import requests
from models import create_session

def get_objects(model):
    response = requests.get(f"https://api.opendota.com/api/{model.__tablename__}")
    data = response.json()

    with create_session() as session:
        try:
            for item in data:
                model.create(item, session)
            session.commit()
        except Exception as e:
            session.rollback()
            print(f"An error occurred: {e}")

def get_object(model, object_id):
    with create_session() as session:
        obj = session.query(model).filter_by(id=object_id).first()

        if obj is None:
            print("Getting data from OpendotaAPI")
            response = requests.get(f"https://api.opendota.com/api/{model.__tablename__}/{object_id}")
            if response.status_code == 200:
                data = response.json()
                obj = model.create(data)
                session.commit()
            else:
                raise Exception(f"Object with ID {object_id} not found in OpendotaAPI database.")

    return obj

