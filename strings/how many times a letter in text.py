text = "hello world"
a = []
b = []
for i in text:
    if i not in a:
        a.append(i)
        b.append(text.count(i))
subset = dict(zip(a,b))
print(subset)