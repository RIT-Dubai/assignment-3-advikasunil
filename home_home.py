
dg={'p':['3 pack garden flower','$5.0'],'l':['hanging light wire','$10.0'],'b':['garden bench','$35.0'],'n':['none and next','$0']}
di={'t':['Small table lamp','$5.0'],'f1':['City picture frame','$7.0'],'r':['4x5 entry rug','$35.0'],'f2':['flower vase','$14.0'],'n':['none and next','$0']}
db = {'c':['shower curtains','$8.0'],'m':['wall mounted mirror','$20.0'],'s':['marble sink','$40.0'],'n':['none and next','$0']}

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
    print(item.type+' category ,'+item.code+', '+item.name)
def garden_menu():
        print('Garden Options:')
        for i in dg:
           print(dg[i][0],'(',i,')', ':',dg[i][1])
def indoor_menu():
        print('Indoor Options:')
        for i in di:
           print(di[i][0],'(',i,')', ':',di[i][1])
def bathroom_menu():
        print('Indoor Options:')
        for i in db:
           print(db[i][0],'(',i,')', ':',db[i][1])
def add_basket(basket,item):
    basket.append(item)


def main():
    basket=list()
    print('Welcome to Home Ideas Center, where all orders include a new home feeling!')
    print('For your new Home space ...')
    x=input('Choose one type of garden idea (O for options, n for next category):')
    if x=='O' or x=='o':
        garden_menu()
        cd=input('Enter code of item')
        cd=cd.split()
        for i in range(len(cd)):
            cod=cd[i]
            nm=dg[cod][0]
            it1=home_category('garden',cod,nm)
            print_home_category(it1)
    else:
        print('bye')
    # elif x=='N' or x=='n':
    #     pass

main()

