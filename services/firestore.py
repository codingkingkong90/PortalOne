import requests

from .firebase_config import FIREBASE_CONFIG

def create_user_documents(user_id, name, email, id_token):

    url = (
        f"https://firestore.googleapis.com/v1/projects/"
        f"{FIREBASE_CONFIG['projectId']}/databases/(default)/documents/users"
        f"?documentId={user_id}"
    )

    headers = {
        "Authorization": f"Bearer {id_token}",
        "Content-Type": "application/json"
    }

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

    response = requests.post(
        url, 
        json=data,
        headers=headers
    )

    print(response.status_code)
    print(response.text)

    return response

def create_group_documents(group_id, name, group_type, creator_id, id_token):

    url = (
        f"https://firestore.googleapis.com/v1/projects/"
        f"{FIREBASE_CONFIG['projectId']}/databases/(default)/documents/users"
        f"?documentId={group_id}"
    )

    headers = {
        "Authorization": f"Bearer {id_token}",
        "Content-Type": "application/json"
    }

    data = {
        "fields": {
            "name": {
                "stringValue": name
            },
            "type": {
                "stringValue": group_type
            },
            "created_by": {
                "stringValue": creator_id
            }
        }
    }

    response = requests.post(
        url, 
        json=data,
        headers=headers
    )

    print(response.status_code)
    print(response.text)

    return response