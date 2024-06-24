def FizzBuzz(num):
    for i in range(num):
        if i % 3 == 0 and i % 5 != 0:
            print('Fizz')
        elif i % 3 != 0 and i % 5 == 0:
            print('Buzz')
        elif i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz')
        else:
            print(i)


def clean_FizzBuzz(num):

    def F(i):
        return i % 3 == 0
    
    def B(i):
        return i % 5 == 0
    
    def Fizz(i):
        return F(i) and not B(i)
    
    def Buzz(i):
        return not F(i) and B(i)

    def FizzBuzz(i):
        return F(i) and B(i)
    
    def notFizzBuzz(i):
        return not F(i) and not B(i)
    
    def manage(i):
        a = Fizz(i)
        b = Buzz(i)
        c = FizzBuzz(i)
        d = notFizzBuzz(i)
        # дальше все равно надо сравнивать. 
    





FizzBuzz(16)
