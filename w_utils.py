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


def get_normed_errors(abs_errors):
   divider = sum(abs_errors)
   normed_errors = list([x/divider for x in abs_errors])
   return normed_errors


def get_lesser_errors_normed(normed_errors, index):
   etalon_error = normed_errors[index]
   lesser_errors = []
   for error in normed_errors:
      if error <= etalon_error:
         lesser_errors.append(error)
   return lesser_errors


def get_coined_entropy_mass_for_p_list(p_list):
   coined_entropy_mass = 0
   for p in p_list:
      coined_entr = entropy_coin(p)
      coined_entropy_mass += coined_entr
   return coined_entropy_mass

def W_no_u_adapt(vals, index, predicted_val):
   MAX_ENTROPY_COINED = MAX_ENTR_OF_COIN * len(vals)

   abs_errors = vals_to_absolute_errors(vals, predicted_val)
   normed_errors = get_normed_errors(abs_errors)

   lesser_errors_normed = get_lesser_errors_normed(normed_errors, index)
   ECLUDED_MASS = get_coined_entropy_mass_for_p_list(lesser_errors_normed)
   w_no_adapt = (MAX_ENTROPY_COINED - ECLUDED_MASS)/MAX_ENTROPY_COINED

   return w_no_adapt

