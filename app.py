import os
from flask import Flask

app = Flask(__name__)

# SECURE: Pulling the password from an Environment Variable
db_password = os.environ.get("DB_PASSWORD", "default_placeholder")
db_user = os.environ.get("DB_USER", "default_placeholder")

@app.route('/')
def home():
    return "Connected to the database securely!"

if __name__ == '__main__':
    app.run(debug=True)
