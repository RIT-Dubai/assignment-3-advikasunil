
dg={'p':['3 Pack garden flower','$5.0'],'l':['Hanging light wire','$10.0'],'b':['Garden bench','$35.0'],'n':['None and next','$0']}
di={'t':['Small table lamp','$5.0'],'f1':['City picture frame','$7.0'],'r':['4x5 Entry rug','$35.0'],'f2':['Flower vase','$14.0'],'n':['None and next','$0']}
db = {'c':['Shower curtain','$8.0'],'m':['Wall mounted mirror','$20.0'],'s':['Marble sink','$40.0'],'n':['None and next','$0']}

class home:
     __slots__ = ['__basket']
     def __init__(self):
         self.__basket= list()

     def order(self):
      print('your order is for a new home experience:')
      for i in self.__basket:
        print(i.get_name(),'- $',i.get_price())

     def add_basket(self,item):
       self.__basket.append(item)

     def total(self):
        pr_g,pr_i,pr_b=0,0,0
        c_g,c_i,c_b=0,0,0
        for i in self.__basket:
            if i.get_type()=='garden':

                if c_g==0:
                  base_price=i.get_price()+50
                  i.set_price(base_price)
                  pr_g=i.get_price()
                  c_g+=1
                else:
                    pr_g+=i.get_price()


            elif i.get_type()=='indoor':
              if c_i==0:
                  base_price=i.get_price()+50
                  i.set_price(base_price)
                  pr_i=i.get_price()
                  c_i+=1
              else:
                    pr_i+=i.get_price()

            elif i.get_type()=='bathroom':
                if c_b==0:
                  base_price=i.get_price()+50
                  i.set_price(base_price)
                  pr_b=i.get_price()
                  c_b+=1
                else:
                    pr_b+=i.get_price()


        print('total price= ',pr_g+pr_i+pr_b)


class home_category:
    __slots__ = ['__type','__name','__code','__price']
    def __init__(self,type,code,name):
        self.__type=type
        self.__code=code
        self.__name= name
        self.__price=0

    def get_name(self):
        return self.__name

    def get_price(self):
        return self.__price

    def get_type(self):
        return self.__type

    def set_price(self,price):
         self.__price= price

    def print_home_category(self):
     return('one '+ self.__name+' is added to your home for '+'$'+str(self.__price))



    # def base_service(self,t_price):
    #     if self.__type=='garden':
    #         t_price+=self.__price
        #t_price=t_price+50
        # if self.type=='indoor':
        #     self.price+=50
        # if self.type=='bathroom':
        #     self.price+=50
        # return self.price




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



def main():
    #basket=list()
    basket=home()
    print('Welcome to Home Ideas Center, where all orders include a new home feeling!')
    print('For your new Home space ...')

    while True:
        x=input('Choose one type of garden idea (O for options, n for next category):')
        if x=='n' or x=='N':
            break
        elif x=='o' or x=='O':
            garden_menu()
            code=input('Enter code of item')
            code=code.split()

            for i in range(len(code)):
                if code[i] =='n':
                   break

                else:
                  cod=code[i]
                  nm=dg[cod][0]
                  pr=dg[cod][1]
                  itm=home_category('garden',cod,nm)
                  basket.add_basket(itm)
                  itm.set_price(float(pr.lstrip('$')))
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
                  #print(itm.base_service())
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
                  #print(itm.base_service())
        else:
            print('Invalid option. Enter O for options, n for next category ')

    basket.order()
    basket.total()
    #x=home_category

main()

