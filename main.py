import time
#trying to make a calculator,4 days of python
num = int(input("what number should be first"))
num_2 = int(input("what about second"))
operation = input("enter an operation").strip()

if operation == "+":
    print(f"The answer is {num+num_2}")

if operation == "-":
    print(f"The answer is {num-num_2}")

if operation == "*":
    print(f"The answer is {num*num_2} ")

if operation == "/":
    print(f"The answer is {num/num_2} ")

time.sleep(1)

print("that's my attempt at a calculator")
time.sleep(2)
print("sorry if its scuffed")