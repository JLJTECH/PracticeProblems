#Day 8

n = int(input())
na_nu = [input().split() for _ in range(n)]
pb = {k: v for k,v in na_nu}
while True:
    try:
        name = input()
        if name in pb:
            print('%s=%s' % (name, pb[name]))
        else:
            print('Not found')
    except:
        break