from utils import is_even,factorial
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

    
