
dg={'p':['3 pack garden flower','$5.0'],'l':['hanging light wire','$10.0'],'b':['garden bench','$35.0'],'n':['none and next','$0']}
di={'t':['Small table lamp','$5.0'],'f1':['City picture frame','$7.0'],'r':['4x5 entry rug','$35.0'],'f2':['flower vase','$14.0'],'n':['none and next','$0']}
db = {'c':['shower curtains','$8.0'],'m':['wall mounted mirror','$20.0'],'s':['marble sink','$40.0'],'n':['none and next','$0']}

class home:
    __slots__ = []

class home_category:
    __slots__ = ['garden','indoor','bathroom']

class item_state():
    __slots__ = ['name','code','price']
    def __init__(self,code):
        self.code=code
        self.name= name
        self.price= price


class home_avatar:
    pass

def menu():
    for i in dg:
       print(i,', item=',dg[i][0],', price=',dg[i][1])

menu()

def main():
    item1=item_state('p')
