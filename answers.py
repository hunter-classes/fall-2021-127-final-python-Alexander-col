# ------------------- Question 1 ----------------
# some brief description of what the output should be

# Write a function named isIncreasing that takes a list of integers as a parameter. isIncraasing should return True if it continually increases. That is given a parameter list L, then L[0] < L[1] < L[2] etc. otherwise return False.
# if all of them are true then that means that the thing is countisuly adding
def isIncreasing(num_list):
  up_count = 0
  down_count = 0
  same = 0
  total = (len(num_list)-1)
  base = num_list[0]
  for i in num_list:
    if i < base:
      down_count = down_count + 1
    elif i > base:
      up_count = up_count + 1
    else:
      same = same + 1
  base = i

  if down_count > 0 :
    return False
  else:
    return True

    
      
# ------------------- Question 2 ----------------
# some brief description of what the output should be
# Write a function named NumConvert. It should take a list of single digit numbers and convert it to an integer and return it.


# For example NumConvert([3,5,1]) would return the number 351.
def numConvert(num_list):
  result = ""
  for i in num_list:
    result = result +(str(i)) 
  result = (int(result) )
  return (result)

def binConvert(b_num):
  result = 0 
  val = 1
  for i in b_num[::-1]: 
      if i == '1':
        result  =val**2 + result
  return result

ex_up = [1,2,3,4,5,6,7,8,9]
ex_down = [9,8,7,6,5,4,3,2,1]
ex_2 = [3,5,1,1,5,3]


print(''' ------------------- Question 1 ----------------
There is a counter that keep track of the values that incresed and those that decreased. If there is a single value that decreased the the function will return false.''')
print("When the function isIncreasing is given the increasing values of", ex_up,"then it will return", isIncreasing(ex_up))
print("when the function is isIncreasing is give the values of dcreasing numbers of", ex_down, "then it will return", isIncreasing(ex_down))

# question2 presentation and response
print('''------------------- Question 2 ----------------
The list of numbers are turned into strings and then they are put together and the final result is then turned back into an integer!''')
print('when given the list numbers of',ex_2,"the numConvert functiion then turns it into", numConvert(ex_2))

print('''------------------- Question 2 ----------------
Attempted to move the numbers into reverse order and then square them in the case that they were a 1 and add it to result''')
print(binConvert("1011"))

