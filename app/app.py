from flask import Flask
from app.config.main import nana_config
app = Flask(__name__)

app.register_blueprint(nana_config)


@app.route('/')
def hello_world():
    return {'hello': 'world'}


if __name__ == '__main__':
    app.run()
