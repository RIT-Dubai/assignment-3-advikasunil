import home_home as h
def test_home_category():
   category_inst1=h.home_category('garden','p','3 Pack garden flower')
   assert(category_inst1.get_type()=='garden')
   assert(category_inst1.get_code()=='p')
   assert(category_inst1.get_name()=='3 Pack garden flower')
   category_inst1.set_price(5.0)
   assert(category_inst1.get_price()==5.0)







