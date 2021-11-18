
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

def garden_menu():
        for i in dg:
           print(dg[i][0],'(',i,')', ':',dg[i][1])
def main():
    print('Welcome to Home Ideas Center, where all orders include a new home feeling!')
    print('For your new Home space ...')
    x=input('Choose one type of garden idea (O for options, n for next category):')
    if x=='O' or 'o':
        garden_menu()





    #item1=item_state('p')
main()

