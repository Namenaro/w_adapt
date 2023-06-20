import math



def entropy_coin(p):
   p1 = p
   p2 = 1 - p
   if p1 == 0 or p2 == 0:
      return 0
   entropy = -p1* math.log(p1) - p2* math.log(p2)
   return entropy

MAX_ENTR_OF_COIN = entropy_coin(0.5)


def vals_to_absolute_errors(vals, val_predicted):
   abs_errors = []
   for val in vals:
      val_err = abs(val - val_predicted)
      abs_errors.append(val_err)

   return abs_errors


def get_normed_errors_to_p(abs_errors):
   divider = sum(abs_errors)
   if divider == 0:
      return [0]* len(abs_errors)
   normed_errors = list([x/divider for x in abs_errors])
   return normed_errors


def get_lesser_errors_normed(normed_errors, index):
   etalon_error = normed_errors[index]
   lesser_errors = []
   for error in normed_errors:
      if error <= etalon_error:
         lesser_errors.append(error)
   return lesser_errors

def get_bigges_errors_normed(normed_errors, index):
   etalon_error = normed_errors[index]
   bigges_errors = []
   for error in normed_errors:
      if error > etalon_error:
         bigges_errors.append(error)
   return bigges_errors

def get_coined_entropy_mass_for_p_list(p_list):
   coined_entropy_mass = 0
   for p in p_list:
      coined_entr = entropy_coin(p)
      coined_entropy_mass += coined_entr
   return coined_entropy_mass


def get_worst_abs_error_imaginary(vals):
   return max(vals)

def get_normed_errors(abs_errors, worst_abs_error_imaginary):
   divider = worst_abs_error_imaginary
   if divider == 0:
      return [0] * len(abs_errors)
   normed_errors = list([x / divider for x in abs_errors])
   return normed_errors

def W_no_u_adapt(vals, index, predicted_val):
   MAX_ENTROPY_COINED = MAX_ENTR_OF_COIN * len(vals)

   worst_abs_error_imaginary = get_worst_abs_error_imaginary(vals)
   abs_errors = vals_to_absolute_errors(vals, predicted_val)
   normed_errors = get_normed_errors(abs_errors, worst_abs_error_imaginary)

   bigges_errors_normed = get_bigges_errors_normed(normed_errors, index)
   BIG_MASS = get_coined_entropy_mass_for_p_list(bigges_errors_normed)
   w_no_adapt = BIG_MASS/MAX_ENTROPY_COINED

   return w_no_adapt


def vals_to_w_no_adapts(vals, predicted_val):
   w_no_adapts = []
   for index in range(len(vals)):
      w_no_adapt = W_no_u_adapt(vals, index, predicted_val)
      w_no_adapts.append(w_no_adapt)
   return w_no_adapts




def W_u_adapt_for_other_index(vals, predicted_index, predicted_val, other_index):
   w_no_adapts = vals_to_w_no_adapts(vals, predicted_val)
   w_no_adapts_of_area = get_ws_of_area(predicted_index, other_index)
   max_w_no_adapt_in_area = max(w_no_adapts_of_area)
   ...
