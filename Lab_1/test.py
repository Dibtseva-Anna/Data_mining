import pandas


def f():
    pass


def m():
    return 1 + 5


arr = [1, 2, 3]
arr = arr + [4]

for x in arr:
    print(x, end='')
print()
for i in range(len(arr)):
    print(arr[i])

print(m())
word = 'a'
count = 8
s = {word: count, 'b': 3}
print(s['1'])


table = pandas.read_csv(filepath_or_buffer='sms-spam-corpus.csv', encoding='1251')
print(list(table.v1))



