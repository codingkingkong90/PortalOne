import pyrebase
from dotenv import load_dotenv

#firebase config--------------------------------------------------------------
config = {
  "apiKey": "AIzaSyCLj3LOswV0j2ItWzkF4_iVAJ_p_tw3Bro",
  "authDomain": "portalone-f78e5.firebaseapp.com",
  "projectId": "portalone-f78e5",
  "storageBucket": "portalone-f78e5.firebasestorage.app",
  "messagingSenderId": "508949836739",
  "appId": "1:508949836739:web:b2fd4bf63a9bd591e30376",
  "measurementId": "G-324KRG7CZ8",
  "databaseURL": ""
}

#initialise-------------------------------------------------------------------
firebase = pyrebase.initialize_app(config)
auth = firebase.auth()

#functions--------------------------------------------------------------------
def login_user(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email, password)
        return {"success": True, "user": user}
    
    except Exception as e:
        error_message = str(e)
        return {"success": False, "error": error_message}

def signup_user(email, password):
    try:
        user = auth.create_user_with_email_and_password
        return {"success": True, "user": user}
    
    except Exception as e:
        error_message = str(e)
        return {"success": False, "error": error_message}