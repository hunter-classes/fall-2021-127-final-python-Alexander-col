# ------------------- Question 1 ----------------
# some brief description of what the output should be

# Write a function named isIncreasing that takes a list of integers as a parameter. isIncraasing should return True if it continually increases. That is given a parameter list L, then L[0] < L[1] < L[2] etc. otherwise return False.
# if all of them are true then that means that the thing is countisuly adding
def isIncreasing(num_list):
  up_count = 0
  down_count = 0
  same = 0
  total = (len(num_list)-1)
  print (total)
  base = num_list[0]
  for i in num_list:
    if i > base:
      up_count = up_count + 1
    elif i < base:
      down_count = down_count + 1
    else:
      same = same + 1
  base = i
  print (up_count, down_count, same)

    
      
# ------------------- Question 2 ----------------
# some brief description of what the output should be
# Write a function named NumConvert. It should take a list of single digit numbers and convert it to an integer and return it.


# For example NumConvert([3,5,1]) would return the number 351.
def numConvert(num_list):
  result = ""
  for i in num_list:
    result = result +(str(i)) 
  result = (int(result) )
  print (result)

# Assume all items in the list are positive single digits.

# If you are totally stuck on this, DM me on Zulip and I will provide a hint but you won’t be able to get full credit if you take the hint.

# ------------------- Question 3 ----------------
# some brief description of what the output should be

ex_up = [1,2,3,4,5,6,7,8,9]
ex_down = [9,8,7,6,5,4,3,2,1]
ex_2 = [3,5,1,1,2,3,4,5,6,7,8,9]
isIncreasing(ex_up)
numConvert(ex_2)
