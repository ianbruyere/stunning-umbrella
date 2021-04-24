# Ex 09 - More list Stuff

# So now some terminilogy
# immutable and mutable, fancy sounding but simple
# immutable means UNCHANGEABLE
# muteable mean CHANGEABLE
# That's it.

# Strings, Integers, and Booleans are ALL IMMUTABLE Datatypes
# Lists, however, are MUTETABLE
# Let's throw back to ex01: there we had a variable called new_hw
new_hw = "hw #1"
# Than if you recall, I said the variable could have a new value
new_hw = "hw #2"
# the string did NOT change; we OVERWROTE it with the new assignment
# same with concatentation
concat_string = "Hooty " + "Hoo"
# we aren't changing the value "Hooty " or "Hoo", what's happening
# is Python creates a NEW string with the value of
# "Hooty Hoo" than assigns it to concat_string

# Don't worry if that didn't make sense; I'm not doing a good job explaning
# this is more so you can Google and find someone else
# Now on to why this matters for lists

# As mentioned above, list's are MUTEABLE, unlike str,int, bool
# first let's make a list with one item in it
mostly_empty_grocery_list = ["pizza"]
# Why not make a str variable with value "pizza"? let's do that
#TODO make a variable called grocery_string with a value of pizza

# if all we were going to get at the grocery store was pizza that'd be fine
# but if we looked in our larder and realized we were out of onions, well that
# HAS to go on the list
#TODO use your variable grocery_string and add "onions" to it.

# than we looked in our fridge and realized we were out of yoghurt
#TODO add "yoghurt" to your grocery_string variable

# not TOO bad, you can (or should be :) using concatentation and reassignment
# But what if you realize you're not in the mood for yoghurt anymore 
# how do you get it off the list without rewriting the entire string
# when it's just three items long, but make it 1000 and than we'll talk
# first let's add to our exisiting list onions
mostly_empty_grocery_list.append("onions") # ["pizza", "onions"]
#NOTE We didn't use assignment here; assignment OVERWRITES
# This .add we appended onto our list variable name is in the list library
# we'll get into all that later, for now adding .append() and putting a value
# between the parathesis adds that value to the list, at the end

#TODO add yoghurt to the mostly_empty_grocery_list

# Alright, now yoghurt's there, how do we get it off?
mostly_empty_grocery_list.pop() # ["pizza", "onions"]

# same idea as append, except we if don't specify an index number
# it simply takes the item off the end
#TODO go ahead and remove onions AND pizza from the list


