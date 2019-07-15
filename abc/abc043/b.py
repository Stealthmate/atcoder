s = input()
news = ""
for c in s:
    if c == 'B':
        news = news[:-1]
    else:
        news = news + c
print(news)
