# High Level Overview
In _Elements of Style_ by William Strunk Jr. and E.B. White they reason that your writing should follow a rhythm, allowing things to breathe when necessary, making allowances for semicolons and such.  
The takeaway from the above is that long sentences themselves aren’t bad, but successive one’s CAN be. There’s no hard and fast rules when it comes to Style, but analytics can at least alert us to potential bad habits.  
Also Strunk give a list of words that should be used with care. These aren’t forbidden, but care should be used.  
We are going to build a tool that checks the lengths of sentences, how far it is over/under the average and changes the color of the sentence to correspond to one of three categories:
* Short 
* Average
* Long

It will output the following metrics as well:
* Average Sentence Length
* Longest Sentence
* Shortest Sentence
* Most used word excluding common place ones like the, a, etc.

If the manpower is present we will also make one that finds the “caution” words and overrides any sentence text. Also it will keep a running tally of how many of these words get used.  

## Pending Design Decisions
* We need to decide on what number of word deviation from average sentence length dictates long/short.
* Colors of the output
* A topic of discussion is how we will handle semi-colons.
	* My Current Ideas are:
		1. Sentences with semi-colons highlighted a different color
		2. Not included in average
		3. Counts for two sentences
* Any other thoughts people have?
## Future Considerations/Improvements
* Options for Command Line
	* User decideds what deviation is
	* User decides colors
	* User decides rules for semi-colons

## Components
* Command Line Interface - Python
* Sentence Averager - Python
* Sentence Tagger - Python
* Caution Word Tagger - Python
* Output Different Colors - Shell(Ian)
