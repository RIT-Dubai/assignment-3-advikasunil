# class cards():
#     __slots__=["rank","suit","face"]
#     def __init__(self,rank,suit,face):
#         self.rank=rank
#         self.suit=suit
#         self.face-face
import random
import time

def make_flippable(rank,suit,name,shorthand,bool=False):
    rec=[(rank,suit,name,shorthand),bool]
    return rec

def is_match(card1,card2):
    if card1[1]==card2[1]==True:
        if card1[0][0]==card2[0][0]:
            if card1[0][1]==card2[0][1]:
                print("is match!")

def select_cards(number,deck):
    list1=[]
    try:
        if number<deck:
            for i in range(0,(number//2)+1):
                list1.append(deck[i])
                list1.append(deck[i])
            # list2=list1
            # list1.append(list2)
            random.shuffle(list1)
        elif  number>deck:
            raise ValueError("Cards cannot be selected !!")
    except ValueError:
        print("Please enter even numbers less than deck. ")
    return list1

def make_board(rows,coloumns,decks):
    deck=["D03","D01","D02","H01","H02","H03","C01","C02","C03","S01","S02","S03"]
    number=int(input("Enter the number of cards for game"))
    cards=select_cards(number,deck)
    for i in cards:
        list1=[i for _ in range(coloumns)]
    print(list1)

make_board(4,2,1)
