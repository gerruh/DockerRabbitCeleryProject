import json
import os

import redis

from app.celery_app import celery_app


@celery_app.task
def load_json_to_redis():
    r = redis.Redis(host=os.getenv("REDIS_HOST"), port=os.getenv("REDIS_PORT"), db=0, decode_responses=True)

    with open("app/data.json", "r") as f:
        data = json.load(f)

    for key, value in data.items():

        if isinstance(value, dict):
            r.hset(key, mapping={
                k: json.dumps(v) if isinstance(v, (list, dict))
                else str(v)
                for k, v in value.items()
            })

        elif isinstance(value, list):
            r.delete(key)
            r.rpush(key, *[json.dumps(v) for v in value])

        else:
            r.set(key, value)

    return f"Saved {len(data)} records"
