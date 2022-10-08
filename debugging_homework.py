#%%
print("Problem 1.a")
'''
1.a
Using the print() function only, get the wrong_add_function to print out where
it is making a mistake, given the expected output for ex, "we are making an error 
in the loop", which you would put near the loop. 
Structure the print() statement to show what the expected output ought to be
via f-strings: ie "The correct answer is supposed to be: [...]".
1.b
Then, changing as little as possible, modify the function, using the same 
general structure to output the correct answer. Call this new function 
correct_add_function() 
'''
def wrong_add_function(arg1,arg2):
   '''
   The function takes in two lists of integers, then it adds
   all of arg2 to each item of arg1.
   
   Example:
      > wrong_add_function([1,2,3],[1,1,1])
      > [6,9,12]
   whereas the expected correct answer is, [2,3,4]
   Parameters
   ----------
   arg1 : list
      list of integers.
   arg2 : list
      list of integers.
   Returns
   -------
   arg1 : list
      Elements of arg1, with each element having had the contents of 
      arg2 added to it.
   '''
   arg1_index=0
   while arg1_index < len(arg1):
      arg_2_sum = 0
      for arg2_elements in arg2:
         arg_2_sum = sum([arg1[arg1_index]+i for i in arg2])
         print("We are making an error in the loop here.")
      arg1[arg1_index]=arg_2_sum  
      arg1_index+=1
   return arg1
arg1 = [1,2,3]
arg2 = [1,1,1]
if wrong_add_function(arg1, arg2) != [2,3,4]:
    print("We expect the outcome to be [2,3,4]")

# %%
print("Problem 1.b")
def correct_add_function(arg1, arg2):
    arg1_index = 0
    while arg1_index < len(arg1):
        arg_2_sum = 0
        for arg2_elements in arg2:
            arg_2_sum = arg1[arg1_index] + arg2[arg1_index]
            print(arg_2_sum)
        arg1[arg1_index] = arg_2_sum
        arg1_index += 1
    return arg1
arg1 = [1,2,3]
arg2 = [1,1,1]
print(correct_add_function(arg1, arg2))
# %%

# %%
