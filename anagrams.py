'''
Construct an algorithm to check whether two words (or phrases) are anagrams or not!

"An anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
typically using all the original letters exactly once"

For example: restful and fluster
'''

#For we to check this, we will need to sort each words in alphabetical order first, then compare the equality of the two words

#Using sorted() and then join() to convert the list to strings, without a separator 
def sortString(str):
	return ''.join(sorted(str))

#Allowing user to pick their own words/phrase
first_word = input("Type in a word or phrase: ")
second_word = input("Type in another word or phrase: ")
#Assigning and calling the user-defined function above, which arranges the words/phrase in alphabetical order
sort_first_word = sortString(first_word)
sort_second_word = sortString(second_word)
#Now lets compare their equality
if sort_first_word == sort_second_word:
  print("\nTrue")
else:
  print("\nFalse")
