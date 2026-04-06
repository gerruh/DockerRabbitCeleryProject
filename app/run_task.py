from app.tasks import load_json_to_redis

if __name__ == "__main__":
    result = load_json_to_redis.delay()
    print(f"Task sent: {result.id}")
