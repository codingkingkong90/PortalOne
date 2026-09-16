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
