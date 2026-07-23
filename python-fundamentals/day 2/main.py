from utils import is_even,factorial

def greet(name,greeting="Hello")-> str:
    return f"{greeting} {name}!"
numbers = [3, 12, 7, 45, 9, 22, 8, 14]

if __name__ == "__main__":  

    print(greet("Anubhav"))
     #use a list comprehension to build a list of only the even numbers.
    print(f"12 is Even ? {is_even(12)}")
    print(f"Factorial of 5: {factorial(5)}")
    evenNumbers = [x for x in numbers if x % 2 == 0]
    print(f"Even Numbers: {evenNumbers}")
    
    #Use a dict comprehension to build {number: "Even"/"Odd"} for every number in the list.
    evenOrOdd = {x:'Even' if x%2==0 else 'Odd' for x in numbers}
    print(f"Dictionary: {evenOrOdd}")
    
    #Use a list comprehension to get the square of every number greater than 10.
    squares = [x*x  for x in numbers if x > 10]
    print(f"Sqaure numbers: {squares}")

    users = [
    {"username": "alice_99", "is_active": True, "is_vip": True},
    {"username": "bob_builder", "is_active": False, "is_vip": True},
    {"username": "charlie_dev", "is_active": True, "is_vip": False},
    {"username": "dana_boss", "is_active": True, "is_vip": True},
    {"username": "evan_cool", "is_active": False, "is_vip": False}
    ]
    #Using comprehension filter unique usernames who is active and vip
    user_names = {user["username"] for user in users if user["is_active"] and user["is_vip"]}
    print(user_names)

    
