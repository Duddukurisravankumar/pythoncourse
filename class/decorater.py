def decorater(func):
    def wrapper(*args):
        print(f"the sum of given numbers are")
        func(*args)
        print("thankyou u can leav")
    return wrapper
@decorater
def addition(a,b):
    print(a+b)
    
addition(20,34)

#