weights = [55, 53, 50, 48, 46]
w_iter = iter(weights)
now = next(w_iter)
for i in w_iter:
    print((now-i) / (now / 100))
    now = i