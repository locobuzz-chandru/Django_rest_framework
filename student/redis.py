import redis


class Redis:

    def __init__(self):
        self.r = redis.Redis(host='localhost', port=6379)

    def getter(self, key):
        return self.r.get(key)

    def setter(self, key, value):
        return self.r.set(key, value)
