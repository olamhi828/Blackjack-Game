import random
from art import logo


def play_game():
    user_card=[]
    computer_card=[]
    is_game_over=False
    user_score=-1
    computer_score=-1


    print(logo)
    def deal_cards():
        """Returning random card to the user"""
        cards=[11,2,3,4,5,6,7,8,9,10,10,10]
        card=random.choice(cards)
        return card

    for _ in range(2):
        user_card.append(deal_cards())
        computer_card.append(deal_cards())

    def calculate_score(cards):
        """Takes a list of cards and return the sum"""
        if sum(cards)==21 and len(cards)==2:
           return 0
        if 11 in cards and sum(cards)==2:
           cards.remove(11)
           cards.append(1)

        return sum(cards)
    def compare(u_score,c_score):
      if u_score==c_score:
        return "Draw"
      elif u_score==0:
        return "Win, You have a blackjack"
      elif c_score==0:
        return "Lose, Computer have a blackjack"
      elif u_score>21:
        return "You went over, You lose"
      elif c_score>21:
        return "Opponent went over, You win"
      elif u_score> c_score:
        return "You won"
      else:
        return "You lose"
    while not is_game_over:
       user_score=calculate_score(user_card)
       computer_score=calculate_score(computer_card)
       print(f"User_cards: {user_card}  current_score: {user_score}")
       print(f"Computer first card : {computer_card[0]}")
       print()

       if user_score==0 or user_score>20 or computer_score==0:
          is_game_over=True
       else:
          choice=input("Type 'y' to get another card,type 'n' to pass")
          if choice !="y":
            is_game_over=True
          user_card.append(deal_cards())
    
    while computer_score!=0 and computer_score <17:
         computer_card.append(deal_cards())
         computer_score=calculate_score(computer_card)
  



    print(f"Your final card: {user_card}: Final score: {user_score}")
    print(f"Computer final card: {computer_card}: computer final score: {computer_score}")
    print(compare(user_score,computer_score))


while input("Do you want to play the game?(yes/no) ").lower().strip()=="yes":
   print("\n" * 40)
   play_game()



    