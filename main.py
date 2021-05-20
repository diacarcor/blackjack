from replit import clear
from art import logo
import random


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(hand):
    """Take a hand and calculates the score in it"""
    score = sum(hand)
    # To check if ther is a Blackjack
    if len(hand) == 2 and score == 21:
        return 0
    # To check if there is an AS
    if score > 21 and 11 in hand:
        index = hand.index(11)
        hand[index] -= 10
        score -= 10
    return score


def compare_scores(player_score, computer_score):
    if player_score == computer_score:
        return "It's a draw. 🙃"
    elif computer_score == 0:
        return "Computer wins with a Blackjack. 😱"
    elif player_score == 0:
        return "Win with a Blackjack 😎"
    elif computer_score > 21:
        return "Computer went over. You win. 😃"
    elif player_score > 21:
        return "You went over. You lose. 😭 "
    elif player_score > computer_score:
        return "You win. 😃"
    else:
        return "You lose. 😭"


def to_bet(player_hand, computer_hand, player_score):
    print(f"  Your cards: {player_hand}, current score: {player_score}")
    print(f"  Computer's first card:  {computer_hand[0]}")

    another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
    if another_card == "y":
        player_hand.append(deal_card())
        player_score = calculate_score(player_hand)
        if player_score < 21:
            to_bet(player_hand, computer_hand, player_score)

    return player_hand


def start_game():
    """Creates the initial hands for player and computer"""
    clear()
    print(logo)
    player_hand = []
    computer_hand = []

    for number in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())

    # Get player an computer score
    player_score = calculate_score(player_hand)
    computer_score = calculate_score(computer_hand)

    if computer_score != 0 and player_score != 0:
        player_hand = to_bet(player_hand, computer_hand, player_score)
        player_score = calculate_score(player_hand)
        while computer_score < 17 and player_score < 21:
            computer_hand.append(deal_card())
            computer_score = calculate_score(computer_hand)

    print(f"  Your final hand: {player_hand}, final score: {player_score}")

    print(f"  Computer's final hand: {computer_hand}, final score: {computer_score}")

    print(compare_scores(player_score, computer_score))


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    start_game()
