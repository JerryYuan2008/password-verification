#password verification
x = 3
password = 'a123456'
while x > 0:
    x = x-1
    pwd = input('please give your password:')
    if pwd == password:
        print('access successfully')
        break
    else:
        if x > 0:
            print('worng password!you still have', x,'times remaining opportunities to retry')
        else:
            print('you have already ran out of your opportunities')
