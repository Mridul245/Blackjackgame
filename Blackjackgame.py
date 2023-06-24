import random

from blakjackart import logo

def deal_cards():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card
def calculate_score(cards):
    sumlist = sum(cards)
    if sum(cards) ==21 and len(cards) == 2:
        return 0
    if 11 in cards and sum == 11:
        cards.remove(11)
        cards.append(1)
    return sumlist
def compare(user_score , computer_score):
    if user_score == computer_score:
        return "DRAW"
    elif computer_score == 0:
        return "LOSE! Computer has a blackjack"
    elif user_score == 0:
        return "WIN! with A blackjack"
    elif user_score > 21:
        return "LOSE! Yow went over 21"
    elif computer_score >21:
        return  "WIN! Computer went over"
    elif user_score>computer_score:
        return "YOU WIN!"
    else:
        return "YOU LOSE!"
def blackjackgame():
    global computer_scores, user_score
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    for i in range(2):
        computer_cards.append(deal_cards())
        user_cards.append(deal_cards())
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_scores = calculate_score(computer_cards)
        print(f"Your cards: {user_cards} and sum = {user_score}")
        print(f"computer first card: {computer_cards[0]} ")
        if user_score == 0 or computer_scores == 0 or user_score>21:
            is_game_over = True
        else:
            user_should_deal = input("Do you want to draw another card??  type 'y' for yes 'n' for no")
            if user_should_deal == "y":
                user_cards.append(deal_cards())
            else:
                is_game_over = True
    while computer_scores !=0 and computer_scores<17:
        computer_cards.append(deal_cards())
        computer_scores = calculate_score(computer_cards)
    print(f"Your final hand{user_cards}, and final score was {user_score}")
    print(f"Computer final hand{computer_cards}, and final score was {computer_scores}")
    print(compare(user_score,computer_scores))

while input("Do you want to play the game of blackjack??: type 'y' for yes 'n' for no") == "y":
    blackjackgame()






