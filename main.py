from replit import clear
from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def compare_scores(player, computer):
    if player["score"] > computer["score"]:
        finish(player, computer)
        print("You win. :)")
        new_game()
    elif player["score"] <  computer["score"]:
        finish(player, computer)
        print("You lose. :(")
        new_game()
    else:
        finish(player, computer)
        print("It's a draw.")
        new_game()
      
def finish(player, computer):
    print(f"  Your final hand: {player['hand']}, final score: {player['score']}")

    print(f"  Computer's final hand: {computer['hand']}, final score: {computer['score']}")

def validate_scores (player,computer):
    
    player["score"] = calculate_score(player)

    computer["score"] = calculate_score(computer)

    print(f"  Your cards: {player['hand']}, current score: {player['score']}")

    print(f"  Computer's first card:  {computer['hand'][0]}")

    if len(computer["hand"])== 2 and 10 in computer["hand"] and 11 in computer["hand"]:
        print("Computer wins with a Blackjack. :(")
        new_game()
    elif len(player["hand"]) == 2 and 10 in player["hand"] and 11 in player["hand"]:
        print("Player wins with a Blackjack. :)")
        new_game()
    else:
        if player["score"] > 21:
                finish(player,computer)
                print("You went over. You lose :(")
                new_game()
        else:
            hit_card(player, computer)

def hit_card(player, computer):
# To check
    another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

    if another_card == "y":
        player["hand"].append(random.choice(cards))

        validate_scores(player, computer)
    else:
        while computer["score"] < 17:
            computer["hand"].append(random.choice(cards))
            computer["score"] = calculate_score(computer)

        if computer["score"] > 21:
            finish(player, computer)
            print("Computer went over. You win! :)")
            new_game()
        else:
            compare_scores(player, computer)

def calculate_score(player):
    score = 0
    for card in player["hand"]:
        score += card
        if score > 21 and 11 in player["hand"]:
            index = player["hand"].index(11)
            player["hand"][index] -= 10
            score -= 10
    return score

def start_game():
    clear()
    print(logo)
    
    player_hand = []
    computer_hand = []

    for number in range(2):
        player_hand.append(random.choice(cards))
        computer_hand.append(random.choice(cards))
    
    player = {
        "hand" : player_hand,
        "score" : 0
    }

    computer = {
        "hand" : computer_hand,
        "score" : 0
    }
    
    validate_scores(player,computer)

def new_game():
    start = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if start == 'y':
        start_game()
        
new_game()


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

