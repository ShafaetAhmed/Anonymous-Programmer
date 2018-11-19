class calculator:

  def __init__(self):

    fun = input("\n 1.(+)\n 2.(-)\n 3.(X)\n 4.(÷) \n 5.(power) \n 6.(remainder) \n 7.(Quotient and remainder ) \n select : " )

    fun = int(fun)
    if fun == 1 :

      num_1 = input('First Number:')
      num_1 = int(num_1)

      num_2 = input('Second Number:')
      num_2 = int(num_2)
      print('Ans:')
      print(num_1+num_2)

    elif fun == 2 :

      num_1 = input('First Number:')
      num_1 = int(num_1)

      num_2 = input('Second Number:')
      num_2 = int(num_2)

      print('Ans:')
      print(num_1-num_2)

    elif fun == 3 :

      num_1 = input('First Number:')
      num_1 = int(num_1)

      num_2 = input('Second Number:')
      num_2 = int(num_2)

      print('Ans:')
      print(num_1*num_2)

    elif fun == 4 :

      num_1 = input('First Number:')
      num_1 = int(num_1)

      num_2 = input('Second Number:')
      num_2 = int(num_2)

      print('Ans:')
      print(int(num_1/num_2))

    elif fun == 5 :
      num_1 = input('Number:')
      num_1 = int(num_1)

      num_2 = input('Power:')
      num_2 = int(num_2)

      print('Ans:')
      print(num_2 ** num_1 )

    elif fun == 6 :

      num_1 = input('First Number:')
      num_1 = int(num_1)

      num_2 = input('Second Number:')
      num_2 = int(num_2)

      print('Ans:')
      print(num_1 % num_2) # %

    elif fun == 7 :

      num_1 = input('First Number:')
      num_1 = int(num_1)

      num_2 = input('Second Number:')
      num_2 = int(num_2)

      print('Ans:')
      print(divmod(num_1, num_2 )) #dimod prints both Quotient and remainder

    else:
        print('unknown')

calculator()        
