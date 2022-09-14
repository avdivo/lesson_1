from redisworks import Root

root = Root()
# r = redis.Redis(host='127.0.0.1', port=6379, db=0)

lst = [1, 2, 3]
root.list = lst

print(root.ip_address)