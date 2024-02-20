import random

def ticket_input():
    ticket = []
    while len(ticket) < 7:
        player_num = int(input("Put a number 1-100"))
        ticket.append(player_num)
    return ticket    
    
    
def generate_lottery():
    winning_numbers = [random.randint(1,100) for num in range(7)]
    return winning_numbers


def compare(winning_numbers,ticket):
    match = 0
    for num in ticket:
        if num in winning_numbers:
            match +=1
    return match        

        
def check_prize(match):
    if match == 3:
        print("You have won £20")
    elif match == 4:
        print("You have won £40")
    elif match == 5:    
        print("Congratulations, you have won £100")
    elif match == 6:
        print("Lucky numbers! You have won £10000")
    elif match == 7:
        print("Hurray! You have won the main prize £1000000 !!!")
    else:
        print("Sorry you haven't won anything this time, try again!")


def game():
    ticket = ticket_input()
    lottery_numbers = generate_lottery()
    num_of_matches = compare(lottery_numbers,ticket)
    check_prize(num_of_matches)
    
    
game()    
    