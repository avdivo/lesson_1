import redis

r = redis.Redis(host='127.0.0.1', port=6379, db=0)
# r.set('ip_address', '127.0.0.0')
# r.set('test_py_key', 'test py value')
a = [1, 2, 3]
r.lpush('list', *a)
# r.set('digit', 5)
# r.set('string', 'word')
redis_get = r.get('ip_address')

print(redis_get, r.get('test_py_key'))

print(r.lrange('list', 0, -1))
r.delete('list')

print(r.get('string').decode('utf-8'))

print(r.get('digit').decode())