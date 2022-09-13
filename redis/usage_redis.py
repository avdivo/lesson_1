import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
r.set('ip_address', '127.0.0.0')
# r.set('test_py_key', 'test py value')

redis_get = r.get('ip_address')
print(redis_get)
