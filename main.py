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
    #To check if ther is a Blackjack
    if len(hand)== 2 and score == 21:
        return 0
    #To check if there is an AS
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
          
def finish(player, computer):
    print(f"  Your final hand: {player['hand']}, final score: {player['score']}")

    print(f"  Computer's final hand: {computer['hand']}, final score: {computer['score']}")

def validate_scores (player_hand,computer_hand):
    
    player_score = calculate_score(player_hand)

    computer_score = calculate_score(computer_hand)

    print(f"  Your cards: {player_hand}, current score: {player_score}")

    print(f"  Computer's first card:  {computer_hand[0]}")

    if computer_score == 0 or player_score == 0 or player_score > 21 :
        print(f"  Your final hand: {player_hand}, final score: {player_score}")

        print(f"  Computer's final hand: {computer_hand}, final score: {computer_score}")

        print(compare_scores(player_score, computer_score))
    else:
        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if another_card == "y":
            player_hand.append(deal_card())
            validate_scores(player_hand, computer_hand)
        else:
            while computer_score < 17:
                computer_hand.append(deal_card())
                computer_score = calculate_score(computer_hand)

            print(f"  Your final hand: {player_hand}, final score: {player_score}")

            print(f"  Computer's final hand: {computer_hand}, final score: {computer_score}")

            print(compare_scores(player_score, computer_score))
            
def start_game():
    """Creates the initial hands for player and computer"""
    clear()
    print(logo)
    player_hand = []
    computer_hand = []

    for number in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())

    validate_scores(player_hand,computer_hand)


while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y":
    start_game()



# def black_jack_validation(player_hand,computer_hand):
#     """Validate if there is a black jack. Return 0 if computer wins. Return 1 if player wins. Return 2 if nobody has blackjack """
#     if 10 in computer_hand and 11 in computer_hand:
#         print("Computer Wins") 
#         return True
#     elif 10 in player_hand and 11 in player_hand:
#         print("Player Wins")
#         return True
#     else:
#         return False

# def validate_score(score, hand):
#     if score > 21:
#         for card in hand:
#             if card == 11:
#                 score = score -10
#                 if score > 21:
#                     print("Player lose")
#             else:
#                 return score
#     else:
#         return score

# def initial_hands():
    
    
#     player_score = 0
#     computer_score = 0

#     is_black_jack = black_jack_validation( computer_hand,player_hand)

#     if not is_black_jack:
        
#         player_score = player_hand[0] + player_hand[1]

#         computer_score = computer_hand[0] + computer_hand[1]

#         validate_score(player_score, player_hand)

#         print(f"Your cards: {player_hand}, current score: {player_score}")

#         print(f"Computer cards: {computer_hand}, current score: {computer_score}")   

        







############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


