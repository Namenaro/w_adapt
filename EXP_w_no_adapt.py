from w_utils import W_no_u_adapt

def float_to_str(num):
   return "{:.2f}".format(num)

def t_1(w_func):
   print("")
   print('\033[95m' + "===================================================")
   print("                Должно уменьшаться:    " + '\033[0m')
   vals_ = [1, 3, 3, 3]
   index_ = 0
   predicted_val_ = 0.7
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

   vals_ = [1, 1, 1, 3]
   index_ = 0
   predicted_val_ = 0.7
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))


def t_2(w_func):
   print("")
   print('\033[95m' +"===================================================")
   print ( "                Должно уменьшаться:    " + '\033[0m')
   vals_ = [1, 3, 3, 3, 3, 3, 3, 3, 3, 3]
   index_ = 0
   predicted_val_ = 0.8
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

   vals_ = [1, 3, 3, 3]
   index_ = 0
   predicted_val_ = 0.8
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))



def t_3(w_func):
   print("")
   print('\033[95m' +"===================================================")
   print ( "                Примерно одинаково    " + '\033[0m')
   vals_ = [1, 2, 3, 4]
   index_ = 0
   predicted_val_ = 0.8
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

   vals_ = [1, 3, 3, 3]
   index_ = 0
   predicted_val_ = 0.8
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))


def t_4(w_func):
   print("")
   print('\033[95m' +"===================================================")
   print ( "                Должно увеличиваться    " + '\033[0m')
   vals_ = [1, 2, 3, 4]
   index_ = 0
   predicted_val_ = 0.8
   w = w_func(vals_, index_, predicted_val_)

   print("    w = " + float_to_str(w))

   vals_ = [1, 2, 3, 4]
   index_ = 0
   predicted_val_ = 1
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

def t_5(w_func):
   print("")
   print('\033[95m' +"===================================================")
   print ( "                Должно увеличиваться    " + '\033[0m')
   vals_ = [1, 1, 1, 1, 1, 1, 1, 1, 2, 3, 4]
   index_ = 0
   predicted_val_ = 0.8
   w = w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

   vals_ = [1, 1, 1, 1, 2, 3, 4]
   index_ = 0
   predicted_val_ = 0.8
   w=w_func(vals_, index_, predicted_val_)
   print("    w = " + float_to_str(w))

if __name__ == '__main__':
   w_func = W_no_u_adapt
   t_1(w_func)
   t_2(w_func)
   t_3(w_func)
   t_4(w_func)
   t_5(w_func)
