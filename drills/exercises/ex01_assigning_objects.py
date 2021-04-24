#!/bin/env python

# Lets first look the title of this exercise: Assigning Objects.
# We'll start at the end: What's an Object?
# An Object is ubiquitous thing in Coding World, 
# For now, know that everything in Python IS an Object. 
# You'll get the feel as we go along.

# Assignment is done by the "=" symbol. 
new_hw = "hw #1"

# lets focus on what these things are on either side of the "=" symbol.
# on the left side of the "=" is whats known as the variable.
# in our example above first_assignment is the variable.
# you can name a variable ALMOST anything you want, as long as there are no spaces
# notice how in new_assignment I used the "_"(underscore) to denote a "space"

# On the right side of the "=" is what's known as the value.
# assignment is the variable set to the value, so it can be saved for later.

#TODO change the variable name below
change_me = "Don't Change Me!"

#TODO change the value of the variable below
dont_change = "Please change me!"

# one more thing about variables they can CHANGE
# I'll change new_hw
new_hw = "hw #2"
# new_hw has OVERWRITTEN the value "hw #1" with "hw #2"

# Now new_hw has the value of "hw #2"
# this might not seem useful, but we'll get there.

# Finally, you can assign a new variable to another variables value
# merely by putting the variable name in the value side of the 
# assignment statement
hw_2 = new_hw
# Now hw_2 has the latest value of new_hw
# if new_hw is OVERWRITTEN, we have the value it was before via hw_2
#TODO Change the value of new_hw to whatever you want, but DO change it

# Now hw_2 still has the value of "hw #2" while
# new_hw is whatever value you assigned it
