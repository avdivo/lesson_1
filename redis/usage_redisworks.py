from redisworks import Root

root = Root()
root = Root(host='localhost', port=6379, db=1)

lst = [1, 2, 3]
root.list = lst

set_ = {15, 45}
root.set = set_

root.int = 125

print(root.list, root.set)
digit = root.int
print(digit, type(digit))

root['new_key'] = 'new_key'
print(root.new_key, root['new_key'])

keys = ['а____', 'б____']
root[keys[0]] = ['word1', 'word2', 'word3']
root[keys[1]] = ['word_1', 'word_2']

for i in keys:
    print(i, root[i])
