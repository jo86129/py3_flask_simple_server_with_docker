from flask import Blueprint

blueprint = Blueprint('activity', __name__)


@blueprint.get('/')
def index():
    return 'this is activity route'
