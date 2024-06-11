from art import *
print(logo)
import random
def sum(a):
    """Function to add elements."""
    sum=0
    for n in a:
        sum+=n
    return sum
def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card
def play_game():
    """Function to play the game."""
    computer_card = []
    while sum(computer_card) < 17:
        computer_card.append(deal_card())
    game_is_on = True
    your_card = [deal_card(), deal_card()]
    while game_is_on:
        print(f"Your cards : {your_card}, current score is : {sum(your_card)}")
        print(f"Computers first card : {computer_card[0]}")
        #print(f"Your score is : {sum(your_card)}\nComputer score is : {sum(computer_card)}")
        if  sum(your_card)<21 :
            if input("Type y to get another card, type n to pass : ") == "n":
                game_is_on=False
            else :
                computer_card.append(deal_card())
                your_card.append(deal_card())
        else :
            game_is_on=False
    print(f"Your score is : {sum(your_card)}\nComputer score is : {sum(computer_card)}")
    if sum(your_card) == sum(computer_card):
        print("Equal score. It's a Tie! :0")
    elif sum(your_card) > 21 and sum(computer_card)>21 :
        print("Both players busted! It's a tie. :|")
    elif sum(your_card)==21:
        print("Blackjack! You Win! :)")
    elif sum(your_card)>21:
        print("Busted! You lose. :(")
    elif sum(computer_card)>21:
        print("Computer Busted! You Win! :)")
    elif sum(your_card)>sum(computer_card):
        print("Greater score! You Win! :)")
    elif sum(computer_card)==21:
        print("Blackjack! Computer Wins! :(")
    else :
        print("Lower Score . Computer wins ! :(")
    if input("Press y if you want to play again or n if not : ")=="y":
        play_game()
    else:
        print("GoodBye!")
if input("Do you want to play the game ? Press y for yes or n for no : ")=="y":
    play_game()
else:
    print("GoodBye!")