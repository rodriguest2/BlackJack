from random import shuffle


'''''''''''''''''''''''''''Variables'''''''''''''''''''''''''''

suits = ('hearts','diamonds','spades','clubs')

value_dict = {
    'two':2,
    'three':3,
    'four':4,
    'five':5,
    'six':6,
    'seven':7,
    'eight':8,
    'nine':9,
    'ten':10,
    'jack':10,
    'queen':10,
    'king':10,
    'ace':11,
}

ranks = ('two','three','four','five','six','seven','eight','nine','ten','jack','queen','king','ace')



'''''''''''''''''''''''''''Classes and Functions'''''''''''''''''''''''''''

#Player name, hits, and draws a card.  Also doubles up as the house by default.
class Player():
    def __init__(self,name="The House"):
        self.name = name
        self.hand = []

    #Player draws a card
    def draw(self,card):
        self.hand.append(card)
        return self.hand

    #Player decides if they want to hit
    def hit_me(self,deck):
        hit = True

        while hit:
            hitme = input('\nDo you want to hit? ')

            if hitme.lower() == 'no' or hitme.lower() == 'n':
                print('\nAlright, no hitting this round.')

                return self.hand

                break

            #Player hits
            elif hitme.lower() == 'yes' or hitme.lower() == 'y':
                while hitme:
                    hitcard = deck.deal()
                    self.draw(hitcard)
                    print("\n{}'s hand: ".format(self.name))

                    for card in self.hand:
                        print(card)

                    break

            else:
                print('\nPlease enter either yes or no.')

    def ace(self,total):
        for card in self.hand:
            if 'ace' in card.value and total > 21:
                total -= 10
        return total

    def __str__(self):
        return self.name

#Card is determined by its suit and value variables
class Card():
    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def __str__(self):
        return self.value + ' of ' + self.suit

#List of cards, generates a deck, shuffles, and deals a single card
class Deck():
    def __init__(self):
        self.deck = []

    #New 52 card deck generated
    def generate_deck(self):
        for suit in suits:
            for value in ranks:
                card = Card(suit=suit,value=value)
                self.deck.append(card)

        return self.deck

    #Shuffles deck randomly
    def shuffle_deck(self):
        return shuffle(self.deck)

    #Single card is dealt
    def deal(self):
        return self.deck.pop(0)

#display for final hand
def final_hand_display(name,playerhand,househand):
    print("{}'s hand:".format(name))
    for card in playerhand:
        print(card)
    print("\nThe House's hand:")
    for card in househand:
        print(card)







'''''''''''''''''''''''''''Game Logic'''''''''''''''''''''''''''

#Start Game Loop
game = True

while game:
    play=input('\nDo you want to play Black Jack? ')

    #Player doesn't want to play
    if play.lower() == 'no' or play.lower() == 'n':
        print('\nToo bad.....see ya next time!')
        game = False
        break

    #Game on! Enter the player name
    elif play.lower() == 'yes' or play.lower() == 'y':
        playername = input("\nWhat's your name? ")
        player = Player(playername)
        house = Player()



#Player loop
        while play:
            gameround = True


#Round loop
            while gameround:

                #Deck is generated and shuffled
                deck = Deck()
                deck.generate_deck()
                deck.shuffle_deck()

                #Player hand dealt
                for num in range(2):
                    handcard = deck.deal()
                    player.draw(handcard)

                #House hand dealt
                for num in range(2):
                    handcard = deck.deal()
                    house.draw(handcard)

                #Player and house hands displayed
                print("\n{0} cards: \n{1} \n{2}\n\nHouse cards: \n{3} \nXXX".format(player.name,player.hand[0],player.hand[1],house.hand[0]))

                #Player hit and win logic
                player.hit_me(deck)

                totalplayer = 0
                for card in player.hand:
                    totalplayer += value_dict[card.value]

                totalplayer = player.ace(totalplayer)

                totalhouse = 0
                for card in house.hand:
                    totalhouse += value_dict[card.value]

                if totalhouse == 21:
                    print("\n**********{} loses. The house hit black jack.**********\n".format(player.name))
                    pfinal_hand_display(player.name,player.hand,house.hand)

                elif totalplayer == 21:
                    print("\n**********{} wins! Black Jack!**********\n".format(player.name))
                    final_hand_display(player.name,player.hand,house.hand)

                elif totalplayer > 21:
                    print("\n**********{} busted. The house wins.**********\n".format(player.name))
                    final_hand_display(player.name,player.hand,house.hand)

                elif totalhouse >= totalplayer:
                    print("\n**********{} loses. The house wins.**********\n".format(player.name))
                    final_hand_display(player.name,player.hand,house.hand)


#House hit and win loop
                elif totalhouse < totalplayer:
                    househit = True
                    while househit:
                        hitcard = deck.deal()
                        house.draw(hitcard)

                        totalhouse += value_dict[hitcard.value]

                        totalhouse = house.ace(totalhouse)

                        if totalhouse > 21:
                            print("\n**********{} wins! The house busted!**********\n".format(player.name))
                            final_hand_display(player.name,player.hand,house.hand)
                            break

                        elif totalhouse == 21:
                            print("\n**********{} loses. The house hit black jack.**********\n".format(player.name))
                            final_hand_display(player.name,player.hand,house.hand)
                            break

                        elif totalhouse >= totalplayer:
                            print("\n**********{} loses. The house wins.**********\n".format(player.name))
                            final_hand_display(player.name,player.hand,house.hand)
                            break


#Replay loop
                again = True

                while again:
                    replay = input("\n{} do you want to play again? Yes, no, or quit. ".format(player.name))

                    if replay.lower() == 'yes' or replay.lower() == 'y':
                        player.hand.clear()
                        house.hand.clear()
                        break

                    elif replay.lower() == 'no' or replay.lower() == 'n':
                        gameround = False
                        play = False
                        break

                    elif replay.lower() == 'quit' or replay.lower() == 'q':
                        gameround = False
                        play = False
                        game = False
                        break

                    else:
                        print('\nPlease enter either yes, no, or quit.')

    else:
        print('\nPlease enter either yes or no.')
