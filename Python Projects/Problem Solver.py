def input_name():
    name=input("What is your name? ")
    return name

def get_numbers():
    import random
    num1 = random.randint(1,500)
    num2 = random.randint(1,500)
    return num1, num2

def get_answer():
    name = input_name()
    print()
    right_counter=0
    for i in range(10):
        num1 = get_numbers()[0]
        num2=get_numbers()[1]
        print(f"Problem {i+1}")
        print("What is the answer to the following equation? ")
        print(f"ans {num1+num2}")
        print(f"{num1}+{num2}")
        answer=int(input("What is the sum: "))
        if check_answer(num1, num2, answer) == True:
            print("Right"'\n')
            right_counter+=10
        else:
            print("Wrong"'\n')
    display_info(right_counter, results(right_counter), name)
        

def check_answer(num1, num2, answer):
    if num1+num2 == answer:
        right = True
    else:
        right = False
    return right

def results(right):
    return right*.1

def display_info(right, average_right, student_name):
    print(f"Information for student: {student_name}")
    print(f"The number right: {right}")
    print(f"The average right is: {average_right} or {average_right*10}%")


get_answer()