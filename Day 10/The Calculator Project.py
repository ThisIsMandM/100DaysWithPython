from art import logo

print(logo)

def add(n1, n2):
    return n1 + n2
def minus(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2

first_number = float(input("What is your first number? "))
operations = {
    "+" : add,
    "-" : minus,
    "*" : multiply,
    "/" : divide,
}
calculater_on = True
while calculater_on:
    operation_choice = str(input("+\n-\n*\n/\n Which operation do you want to perform: "))
    if operation_choice in operations:
        print(operations[operation_choice](first_number, float(input("What is your second number? "))))
        while True:
            cal_again = str(input("Do you wish to use calculator now, again? 'y for yes and n for no' ")).lower()
            if cal_again == "n":
                calculater_on = False
                print("See You Yext Time!")
                break
            if cal_again == "y":
                calculater_on = True
                break
            else:
                print("Invalid input, try again. ")
    else:
        calculater_on = True
