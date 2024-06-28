from flask import ( Blueprint )

from tutorIA_docretrieval.redis import get_redis

bp = Blueprint('api', __name__, url_prefix='/api/embedding/')

@bp.route('/save', methods=('GET', 'POST'))
def save_embedding():
    redis = get_redis()
    return "<p>Hello, World!</p>"