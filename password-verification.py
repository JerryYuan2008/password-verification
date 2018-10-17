#password verification
x = 3
password = 'a123456'
while x > 0:
    pwd = input('please give your password:')
    if pwd == password:
        print('access successfully')
        break
    else:
        x = x-1
        print('wrong password!you still have ', x,'times remaining opportunities to retry')
