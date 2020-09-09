from flask import jsonify, Blueprint
from app.helper.parse import parse_json

nana_config = Blueprint('config_api', __name__)


@nana_config.route('/repo')
def repo_list():
    return jsonify(parse_json('/config/json_file/repo.json'))


@nana_config.route('/theme')
def theme_list():
    return jsonify(parse_json('/config/json_file/theme.json'))
