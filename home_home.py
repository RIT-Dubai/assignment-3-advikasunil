
dg={'p':['3 Pack garden flower','$5.0'],'l':['Hanging light wire','$10.0'],'b':['Garden bench','$35.0'],'n':['None and next','$0']}
di={'t':['Small table lamp','$5.0'],'f1':['City picture frame','$7.0'],'r':['4x5 Entry rug','$35.0'],'f2':['Flower vase','$14.0'],'n':['None and next','$0']}
db = {'c':['Shower curtain','$8.0'],'m':['Wall mounted mirror','$20.0'],'s':['Marble sink','$40.0'],'n':['None and next','$0']}

class home:
    pass
    #__slots__ = [basket]

class home_category:
    __slots__ = ['type','name','code','price']
    def __init__(self,type,code,name):
        self.type=type
        self.code=code
        self.name= name
        self.price=0
def print_home_category(item):
    print('one '+ item.name+' is added to your home for '+item.price)
def garden_menu():
        print('Garden Options:')
        for i in dg:
           print(dg[i][0],'(',i,')', ':',dg[i][1])
def indoor_menu():
        print('Indoor Options:')
        for i in di:
           print(di[i][0],'(',i,')', ':',di[i][1])
def bathroom_menu():
        print('Bathroom Options:')
        for i in db:
           print(db[i][0],'(',i,')', ':',db[i][1])
def add_basket(basket,item):
    basket.append(item)


def main():
    basket=list()
    print('Welcome to Home Ideas Center, where all orders include a new home feeling!')
    print('For your new Home space ...')

    while True:
        x=input('Choose one type of garden idea (O for options, n for next category):')
        if x=='n' or x=='N':
            break
        elif x=='o' or x=='O':
            garden_menu()
            cd=input('Enter code of item')
            cd=cd.split()

            for i in range(len(cd)):
                if cd[i] =='n':
                   break

                else:
                  cod=cd[i]
                  basket.append(cod)
                  nm=dg[cod][0]
                  itm=home_category('garden',cod,nm)
                  itm.price=dg[cod][1]
                  print_home_category(itm)
        else:
            print('Invalid option. Enter O for options, n for next category ')


    while True:
        y=input('Choose one type of indoor idea (O for options, n for next category):')
        if y=='n' or y=='N':
            break
        elif y=='o' or y=='O':
            indoor_menu()
            cd=input('Enter code of item')
            cd=cd.split()
            for i in range(len(cd)):
             if cd[i] == 'n':
                   break
             else:
                  cod=cd[i]
                  basket.append(cod)
                  nm=di[cod][0]
                  itm=home_category('indoor',cod,nm)
                  itm.price=di[cod][1]
                  print_home_category(itm)
        else:
            print('Invalid option. Enter O for options, n for next category ')

    while True:
        z=input('Choose one type of bathroom idea (O for options, n for exit category):')
        if z=='n' or z=='N':
            break

        elif z=='o' or z=='O':
            bathroom_menu()
            cd=input('Enter code of item')
            cd=cd.split()
            for i in range(len(cd)):
              if cd[i] =='n':
                   break
              else:
                  cod=cd[i]
                  basket.append(cod)
                  nm=db[cod][0]
                  itm=home_category('bathroom',cod,nm)
                  itm.price=db[cod][1]
                  print_home_category(itm)
        else:
            print('Invalid option. Enter O for options, n for next category ')

main()

