#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
from IPython.display import clear_output as co


class Deck:
    
    def __init__(self):
        self.suits = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
        self.ranks = ['A', 
                     '2', 
                     '3', 
                     '4', 
                     '5', 
                     '6', 
                     '7', 
                     '8', 
                     '9',
                    '10',
                    'Jack',
                    'Queen',
                    'King']
        self.cards = [(suit, rank) for suit in self.suits for rank in self.ranks]
        
#     def __repr__(self):
#         print(f'{self.rank} of {self.suit}') #need s on rank and suit?
            
    def shuffle_cards(self):
        print('The Dealer is shuffling...')
        if len(self.cards) > 1:
            random.shuffle(self.cards)
            
    
    
class Player:
    
    def __init__(self):
        self.hand = []
        self.value = 0
        
#     def add_card(self, card):
#         self.hand.append(card)
       
    def calc_total(self):
        #Find total w/ ace value
        self.value = 0
        has_ace = False
        for card in self.hand:
            if card[1].isnumeric():
                self.value += int(card[1])
            else:
                if card[1] == 'A':
                    has_ace = True
                    self.value += 11
                else:
                    self.value += 10
        if has_ace and self.value > 21:
            self.value =-10
        return self.value
            
    def bust(self):
        return f'{self.__class__.__name__} busted' 
    
#     def get_value(self):
#         self.calc_value()
#         print(self.value)
        
#     def has_blackjack():
#         player = False
#         dealer = False
#         if #human hand == 21:
#             player = True
#         if #dealer hand == 21:
#             dealer = True
#         return player, dealer
    
class Dealer(Player):
    
    def deal(self, a_deck, p):
        if isinstance(p, Human):
            if len(p.hand) >= 2:
                p.hand.append(a_deck.cards.pop())
            else:
                for i in range(2):
                    p.hand.append(a_deck.cards.pop())
        elif isinstance(p, Dealer):
            if len(p.hand) >= 2:
                p.hand.append(a_deck.cards.pop())
            else:
                for i in range(2):
                    p.hand.append(a_deck.cards.pop())
        
#     def display_dealer():
#         print('hidden')
#         print(self.cards[1])

class Human(Player):
    pass
#     def display_human():
#         for card in self.hand:
#             print(card)
#         print ("Value:". self.get_value())
        
        
class Game:
    
    def show_instructions():
        print('''Welcome to PyJack!
The Goal: Beat the dealer's hand without going over 21.
When the game begins, the dealer will shuffle a standard 52 card deck. 
The dealer will deal both themself and the player two cards.
When you receive your cards you will need to count them. The points are tallied as followed: \n
A = Determined by the card total. Either 1 or 11 points.
2 = 2 points
3 = 3 points
4 = 4 points
5 = 5 points
6 = 6 points
7 = 7 points
8 = 8 points
9 = 9 points
10 = 10 points
Jack = 10 points
Queen = 10 points
King = 10 points\n
You will need to determine whether you would like to 'hit' (ask for another card) or 'stand' (not ask for another card).
If you go over 21, you bust and the dealer wins.
If you are dealt a 21 from the start (Ace & 10), you win.
The Dealer will hit until their cards total 17 or higher.\n
''')
        
    def run():
        print("Let's play Blackjack!")  
        Game.show_instructions()
        begin_game = input("Press any key to begin").lower()
        co()
        
        done = False
        
        while not done:
            begin_game = input("Would you like to play? Enter Y/N \n").lower()
            deck = Deck()
            dealer = Dealer()
            human = Human()
            
        #Shuffle cards
            deck.shuffle_cards()
            
            if begin_game == 'n':
                print('Thanks for playing! \n')
                done = True
            elif begin_game == 'y':
                #Deal cards to player and dealer
                dealer.deal(deck, human)
                dealer.deal(deck, dealer)
                
                print('Player hand:\n' + str(human.hand))
                print(f'Your total: {Player.calc_total(human)}\n')
                print('Dealer hand:\n' + str(dealer.hand))
                print(f'Dealer total: {Player.calc_total(dealer)}\n')

                
                player_bust = False
                dealer_bust = False
                hit_or_stand = input("Would you like to 'hit' or 'stand'? \n")
                if hit_or_stand == 'hit' or hit_or_stand =='h':
                    dealer.deal(deck, human)
                    print('Player hand:\n' + str(human.hand))
                    print(f'Your total: {Player.calc_total(human)}\n')
                    if Player.calc_total(human) > 21:
                        print('You busted!')
                        player_bust = True
                if Player.calc_total(dealer) < 17 and player_bust == False: 
                    dealer.deal(deck, dealer)
                    print('Dealer hand:\n' + str(dealer.hand))
                    print(f'Dealer total: {Player.calc_total(dealer)}\n')
                    if Player.calc_total(dealer) > 21:
                        print('Dealer busted!')
                        dealer_bust = True
                if player_bust == False and dealer_bust == False and Player.calc_total(human) > Player.calc_total(dealer):
                    print('Congratulations, you won!')
                else: 
                    print('You lost!')
        

            
#         #Display cards
#             dealer.display_hand(self.hand)
#             human.display_hand(self.hand)
#         #See if human hand equals 21
#             if human.calc_total == 21:
#                 print('Blackjack! You win!')
#             else:
#                 choice = input("Would you like to 'hit' or 'stand'?\n")
                
        
Game.run()


# In[ ]:





# In[ ]:




