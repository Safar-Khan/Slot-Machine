MAX_LINES = 3
BET_MIN = 1
BET_MAX = 100

def deposit():
    while True:
        amount = input("Please Enter deposit amount $:")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print("Amount must b greater than zero")
        else:
            print("Please enter a number")
    return amount


def number_of_lines():
    while True:
        lines = input("Please Enter nmuber of lines: (1-" + str(MAX_LINES)  + ")")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines")
        else:
            print("Please enter a number")
    return lines
    

def bet():
    while True:
        amount = input("Enter the amount you want to bet on each line $: ")
        if amount.isdigit():
            amount = int(amount)
            if BET_MIN <= amount <= BET_MAX:
                break
            else:
                print(f"Please enter amount between{BET_MIN} and {BET_MAX}")
        else:
            print("Please enter a valid number")
    return amount

def main():
    balance = deposit()
    lines = number_of_lines()
    while True:
        bet_amount = bet()
        total_bet = bet_amount*lines
        if total_bet > balance:
            print(f"You do not have sufficient balance. You balance is ${balance}")
        else:
            break

    total_bet = bet_amount*lines
    print(f"You  are betting ${bet_amount} on {lines} lines. Total amount = ${total_bet}")

main()