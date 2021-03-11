try:
    age = int(input('Age: '))
    income = 20000
    risk = income/age
    print(age)
except ValueError:
    print('Invalid value ')
except ZeroDivisionError:
    print('Age cannot be "0"')
except SyntaxError:
    print('fjhggjkf')

# so many types of errors are in the except error u can call an dcheck required to your  code syntax
