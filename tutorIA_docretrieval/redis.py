from flask import g
from redis import Redis

def get_redis():
    if 'redis' not in g:
        g.redis = Redis(host="localhost", port=6379)

    return g.redis

def close_redis(e=None):
    redis = g.pop('redis', None)

    if redis is not None:
        redis.close()

def init_app(app):
    app.teardown_appcontext(close_redis)