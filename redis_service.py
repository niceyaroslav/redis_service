import js2py


class RedisService:

    @staticmethod
    def get_data_by_key(key, redis_object):
        byte_key = key.encode("utf-8")
        data = redis_object[byte_key].decode("utf-8")
        return data

    @staticmethod
    def console_log(code):
        result = js2py.eval_js("function (code) {console.log(code)}")
        result(code)


