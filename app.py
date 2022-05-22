from flask import Flask, request
import redis
from redis_service import RedisService


app = Flask(__name__)
redis = redis.Redis()
service = RedisService()


@app.route('/js/script.js', methods=["GET"])
def gleb_test():
    db_query = request.args.get("key")
    key_data = redis.hgetall(db_query)
    code = service.get_data_by_key("code", key_data)
    count = int(service.get_data_by_key("count", key_data))
    redis.hmset("new_key", {"code": "Very Secret Code", "count": count + 1})
    resp = f"{code}, count is {count}..."
    service.console_log(code)
    return resp


if __name__ == '__main__':
    app.run(debug=True)
