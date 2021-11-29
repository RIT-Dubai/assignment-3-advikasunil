import home_home as h
def test_home_category():
   category_inst1=h.home_category('garden','p','3 Pack garden flower')
   assert(category_inst1.get_type()=='garden')
   assert(category_inst1.get_code()=='p')
   assert(category_inst1.get_name()=='3 Pack garden flower')
   category_inst1.set_price(5.0)
   assert(category_inst1.get_price()==5.0)

   category_inst2=h.home_category('indoor','f1','City picture frame')
   assert(category_inst2.get_type()=='indoor')
   assert(category_inst2.get_code()=='f1')
   assert(category_inst2.get_name()=='City picture frame')
   category_inst2.set_price(7.0)
   assert(category_inst2.get_price()==7.0)

   category_inst3=h.home_category('bathroom','c','Shower curtain')
   assert(category_inst3.get_type()=='bathroom')
   assert(category_inst3.get_code()=='c')
   assert(category_inst3.get_name()=='Shower curtain')
   category_inst3.set_price(8.0)
   assert(category_inst3.get_price()==8.0)






