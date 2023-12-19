from flask import Flask, request, abort
from grade_save.grade_save import grade_save

def create_app():
    app = Flask(__name__)
    app.register_blueprint(grade_save)
    return app

            
if __name__ == '__main__':
    create_app().run(debug=False, host='0.0.0.0')