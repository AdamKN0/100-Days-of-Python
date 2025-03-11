import random

print("Welcome to the Blackjack Game!")

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal_card():
    return random.choice(cards)

def calculate_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    while 11 in cards and sum(cards) > 21:
        cards[cards.index(11)] = 1
    return sum(cards)

def compare_scores(player_score, computer_score):
    if player_score == computer_score:
        return "It's a draw."
    elif computer_score == 0:
        return "Computer wins with a Blackjack."
    elif player_score == 0:
        return "You win with a Blackjack."
    elif player_score > 21:
        return "You went over. Computer wins."
    elif computer_score > 21:
        return "Computer went over. You win."
    elif player_score > computer_score:
        return "You win."
    else:
        return "Computer wins."

def play_game():
    player_cards = [deal_card(), deal_card()]
    computer_cards = [deal_card(), deal_card()]
    
    game_over = False

    while not game_over:
        player_score = calculate_score(player_cards)
        computer_score = calculate_score(computer_cards)
        
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if player_score == 0 or player_score > 21:
            game_over = True
        else:
            another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if another_card == "y":
                player_cards.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare_scores(player_score, computer_score))

play_game()
