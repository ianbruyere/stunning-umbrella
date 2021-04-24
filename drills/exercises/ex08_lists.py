# Ex 8 - Lists

# Now things are getting exciting!
# Lists are another Data Type, all their own.
# Let's learn how to assign one.
list_0 = []

# So, what's that do?
# a list is a list of values
list_1 = [1,1,2,3,5,8,13,21]
list_2 = ["It can hold", "strings", "as well"]
list_3 = [True, False, True, True, True, False, False, False, True, False] # you didn't forget bools did ya ;)
# lists can have multiple types too
list_4 = ["it can have strings inside", "it can have numbers", 1, 88, "booleans", True, False]
# But if we have a say, we want our lists to have only one datatype in it
list_of_integers = [1,1,2,3,5,8,13]
list_of_strs = ["I've got", "a lovely", "bunch of...", "coconuts"]
list_of_bools = [False, True, True, False, False, False]

#TODO make a list of at least 5 items below
your_list = []
#TODO please make scrambled_list a list of one type
scrambled_list = ["eggs are good for", 8, True, "or", False]

# So lists DO allow you to access one item from them at a time
# There's a little knowdlege that we need to begin with

# Lets start with what an index is
# an index is a number that corresponds with an items place in the overall list
# but there's a caveat, in Python(and most other languages) lists start with 0
# so instead of the first item of the list being associated with the index of 1
# it is associated with 0.
understanding_indexes = ["zero", "one", "two"]
# so in the above list, the value "zero" corresponds to index 0
# here's how we grab just the zero value from the list
understanding_indexes[0] # ["zero"]

#TODO go ahead and grab the value "two" and print it to console

# now grabbing one item from anywhere in the list via index number is useful
# but what if wanted only a slice of the values; not ALL of them
# let's make a longer list first
slice_list = ["zero", "one", "two", "three", "four", "five", "six"]

# now I just want to grab the strings "one" and "two"
slice_list[1:3] # ["one", "two"]

# Before we get into the weirdness, just know that ":" is the slice operator
# It can be used a myriad of cool ways but for now we are only going to foc:wqus on this method
# Lets get into the weirdness: The fact that my slice values are 1 and 3 and we returned the values
# for indexes 1 and 2 seems a little off.
# Here's how it works here's the slice operation abstracted a little: [START : END]
# so Python looks at the value associated with the START index than grabs every value 
# UP to but NOT including the END index. So it leaves the END index value hanging
# Weird I know, and tricky to explain.
# Try it on for yourself:
#TODO Grab the values "three", "four, and "five" but not anything before or after them
# print to console

#TODO take the pizza below, and take the "sausage" and "peppronini" pieces for yourself
pizza_slices = ["cheese", "pineapple", "pepper", "3 meat", "sausage", "pepperoni", "onions", "hair of the dog"]

