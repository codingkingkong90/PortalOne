import requests

from .firebase_config import FIREBASE_CONFIG

def create_user_documents(user_id, name, email):

    url = (
        f"https://firestore.googleapis.com/v1/projects/"
        f"{FIREBASE_CONFIG['projectId']}/databases/(default)/documents/users"
        f"?documentId={user_id}"
    )

    data = {
        "fields": {
            "name": {
                "stringValue": name
            },
            "email": {
                "stringValue": email
            },
            "groupId": {
                "nullValue": None
            }
        }
    }