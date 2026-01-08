import time

age = int(input("How old are you!: "))
date_of_birth = int(input('whats your date of birth? '))

while age != 2025-date_of_birth:
    print("you are lying about your age,be honest")
    time.sleep(0.5)
    print("please be honest")
    time.sleep(1)
    age = int(input("How old are you!: "))
    date_of_birth = int(input('whats your date of birth? '))

real_age= age
time.sleep(1)
print(f'you are {real_age} years old,\n'+ "thanks for participating!!!")
