fun = input("\n 1.(+)\n 2.(-)\n 3.(X)\n 4.(÷) \n 5.(power) \n 6.(remainder) \n 7.(Quotient and remainder ) \n select : " )
fun = int(fun)

def add(num1, num2):
  a = num1 + num2
  return a

def sub(num1, num2):
  a = num1 - num2
  return a 
  
def mul(num1, num2):
  a = num1 * num2
  return a

def div(num1, num2):
  a = num1 / num2
  return a

def power(num1, num2):
  a = num1 ** num2
  return a

def remainder(num1, num2):
  a = num1 % num2
  return a

def rem(num1, num2):
  a = divmod(num1, num2)
  return a

if fun == 1:
  ans = add(num1=int(input('first number:')), 
           num2=int(input('second number:')))
  print(ans)

if fun == 2:
  ans = sub(num1=int(input('first number:')), 
           num2=int(input('second number:')))
  print(ans)

if fun == 3:
  ans = mul(num1=int(input('first number:')), 
           num2=int(input('second number:')))
  print(ans)

if fun == 4:
  ans = div(num1=int(input('first number:')), 
            num2=int(input('second number:')))
  print(ans)

if fun == 5:
  ans = power(num1=int(input('first number:')), 
              num2=int(input('second number:')))
  print(ans)

if fun == 6:
  ans = remainder(num1=int(input('first number:')), 
                  num2=int(input('second number:')))
  print(ans)

if fun == 7:
  ans = rem(num1=int(input('first number:')), 
            num2=int(input('second number:')))
  print(ans)
