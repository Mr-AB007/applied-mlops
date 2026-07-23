def safe_divide(a:int, b:int)-> float | int | None:
    try:
        return a/b
    except ZeroDivisionError as e:
        print(f"Error in division{e}")