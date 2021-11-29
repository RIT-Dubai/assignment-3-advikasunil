
dg={'p':['3 Pack garden flower','$5.0'],'l':['Hanging light wire','$10.0'],'b':['Garden bench','$35.0'],'n':['None and next','$0']}
di={'t':['Small table lamp','$5.0'],'f1':['City picture frame','$7.0'],'r':['4x5 Entry rug','$35.0'],'f2':['Flower vase','$14.0'],'n':['None and next','$0']}
db = {'c':['Shower curtain','$8.0'],'m':['Wall mounted mirror','$20.0'],'s':['Marble sink','$40.0'],'n':['None and next','$0']}

class home:
     """home_category class comprise of the type (which is garden, indoor and bathroom), name (of all the items) code
     (which uniquely identifies an item) and price (of each item). since the fields are private we have functions used to
     get and set the values, so that we can access it outside the class. Finally, it prints the cost individual items order by the user"""

     __slots__ = ['__basket']
     def __init__(self):
         self.__basket= list()

     def order(self):     # prints the price of each item
      print('your order is for a new home experience:')
      for i in self.__basket:
        print(i.get_name(),'- $',i.get_price())

     def add_basket(self,item):  # adds the selected item by the user into the basket
       self.__basket.append(item)

     def total(self):  # prints the total price of all purchased items with the additional $50 base service
        pr_g,pr_i,pr_b=0,0,0           #initialising price of each category to 0
        count_g,count_i,count_b=0,0,0  #initialising count of each category to 0
        for i in self.__basket:

            if i.get_type()=='garden':
                if count_g==0:
                  base_price=i.get_price()+50  #for the 1st item an additional $50 is added
                  i.set_price(base_price)
                  pr_g=i.get_price()
                  count_g+=1
                else:   #from the second item onwards the total price of the category is as mentioned in the dictionary
                  pr_g+=i.get_price()

            elif i.get_type()=='indoor':
              if count_i==0:
                  base_price=i.get_price()+50 #for the 1st item an additional $50 is added
                  i.set_price(base_price)
                  pr_i=i.get_price()
                  count_i+=1
              else:   #from the second item onwards the total price of the category is as mentioned in the dictionary
                pr_i+=i.get_price()

            elif i.get_type()=='bathroom':
                if count_b==0:
                  base_price=i.get_price()+50   #for the 1st item an additional $50 is added
                  i.set_price(base_price)
                  pr_b=i.get_price()
                  count_b+=1
                else:   #from the second item onwards the total price of the category is as mentioned in the dictionary
                  pr_b+=i.get_price()


        print('total price= ',pr_g+pr_i+pr_b)


class home_category:
    """" Home class comprises of the basket/cart where users can store the items
that they purchased for the garden, indoor and bathroom categories, Finally it
returns the total price with the additional $50 BASE PRICE for each category"""

    __slots__ = ['__type','__name','__code','__price']  #fields are made private
    def __init__(self,type,code,name):
        self.__type=type
        self.__code=code
        self.__name= name
        self.__price=0

    def get_name(self):          #returns name of item using getters because the field is private
        return self.__name

    def get_code(self):          #returns code of item using getters because the field is private
        return self.__code

    def set_price(self,price):    #can set price of item using setters because the field is private
         self.__price= price

    def get_price(self):        #returns price of item using getters because the field is private
        return self.__price

    def get_type(self):        #returns type of item using getters because the field is private
        return self.__type


    def print_home_category(self):
      return('one '+ self.__name+' is added to your home for '+'$'+str(self.__price))

def garden_menu():    #menu to display the garden menu items
        print('Garden Options:')
        for i in dg:
           print(dg[i][0],'(',i,')', ':',dg[i][1])
def indoor_menu():     #menu to display the indoor menu items
        print('Indoor Options:')
        for i in di:
           print(di[i][0],'(',i,')', ':',di[i][1])

def bathroom_menu():   #menu to display the bathroom menu items
        print('Bathroom Options:')
        for i in db:
           print(db[i][0],'(',i,')', ':',db[i][1])

if __name__ == '__main__':
    basket=home()
    print('Welcome to Home Ideas Center, where all orders include a new home feeling!')
    print('For your new Home space ...')

    while True:
        x=input('Choose one type of garden idea (O for options, n for next category):')
        if x=='n' or x=='N':      #if user enters 'n' it will go to next category
            break
        elif x=='o' or x=='O':
            garden_menu()
            code=input('Enter code of item')
            code=code.split()     #split the code if the user enters multiple codes of different items in 1 line

            for i in range(len(code)):
                if code[i] =='n':
                   break

                else:
                  cod=code[i]
                  nm=dg[cod][0]
                  pr=dg[cod][1]
                  itm=home_category('garden',cod,nm)
                  basket.add_basket(itm)
                  itm.set_price(float(pr.lstrip('$')))   #removes $ and sets price as a float value
                  print(itm.print_home_category())
        else:
            print('Invalid option. Enter O for options, n for next category ')

    while True:
        y=input('Choose one type of indoor idea (O for options, n for next category):')
        if y=='n' or y=='N':
            break
        elif y=='o' or y=='O':
            indoor_menu()
            code=input('Enter code of item')
            code=code.split()
            for i in range(len(code)):
             if code[i] == 'n':
                   break
             else:
                  cod=code[i]
                  nm=di[cod][0]
                  pr=di[cod][1]
                  itm=home_category('indoor',cod,nm)
                  basket.add_basket(itm)
                  itm.set_price(float(pr.lstrip('$')))
                  print(itm.print_home_category())
        else:
            print('Invalid option. Enter O for options, n for next category ')

    while True:
        z=input('Choose one type of bathroom idea (O for options, n for exit category):')
        if z=='n' or z=='N':
            break

        elif z=='o' or z=='O':
            bathroom_menu()
            code=input('Enter code of item')
            code=code.split()
            for i in range(len(code)):
              if code[i] =='n':
                   break
              else:
                  cod=code[i]
                  nm=db[cod][0]
                  pr=db[cod][1]
                  itm=home_category('bathroom',cod,nm)
                  basket.add_basket(itm)
                  itm.set_price(float(pr.lstrip('$')))
                  print(itm.print_home_category())
        else:
            print('Invalid option. Enter O for options, n for next category ')

    basket.order()
    basket.total()



