from app import app
from app.view import *
if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True, port=5000)