def safe_divide(a:int, b:int)-> float | int | None:
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f"Error in division{e}")


def validate_age(age:int)-> int | None:
    if age < 1:
        raise ValueError('Age must be greater than 0')
    return age