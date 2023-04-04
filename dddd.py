class Demp (Exception):
    pass

def fun(x):
    try:
        type_var=type(x)
        if (x is not  str):
            raise ValueError("Value error is there")
        else:
            print(x)
    except Exception as e:
        print(e)


fun(121)
