# DAY 1
age : int = 32
name : str = "Anubhav"
salary : float = 4555.56
married: bool = True
address: list = ["Patna","Pune"]
ids: tuple = ("Adhar","PAN")
idsDetails: dict = {2:"Anu", 3:"Sup"}
mobile: set = {12345,1234,121}

print(type(age))
print(type(name))
print(type(salary))
print(type(married))
print(type(address))
print(type(ids))
print(type(idsDetails))
print(type(mobile))

#proagram print list 

for val in [3, 12, 7, 45, 9, 22]:
    if val%2 == 0:
        print('Even')
    else:
        print('Odd')
    if val > 10:
        print(f"{val} Greater than 10")
    else:
        print( f"{val} Not Greater than 10")
        

#Program to print 100 Fibonacci series 
print("===== Fibonacci series upto 100 =====")
a,b = 0 , 1
print(a)
while b <= 100:
    print(b)
    a,b = b , a+b
    
    
    
    
