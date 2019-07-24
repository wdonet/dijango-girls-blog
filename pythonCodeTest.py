def hi(name):
    print('Hi ' + name)

def repeat(list):
    for n in list:
        hi(n)
        print('-----')
# comment here
if 3 < 2:
    hi('Ozz')
elif 5 > 40:
    repeat(['Mark', 'Beck'])
else:
    for n in range(1,6):
        print(n)
