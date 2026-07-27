from errors import *

if __name__ == "__main__":
    print(safe_divide(8,0))

    #CHECK AGE
    try:
        print(f"Age is : {validate_age(-23)}")
    except ValueError as e:
        print(e)

