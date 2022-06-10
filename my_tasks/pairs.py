

class list(list):
    def my_count(self, arg):
        return super().count(arg) - 1


a = list([1, 2, 3])

print(a.my_count(2))