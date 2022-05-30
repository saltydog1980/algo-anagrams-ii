# Don't forget to run the tests (and create some of your own)

def anagrams_for(word, list_of_words):
	#removing any spaces taking to upper and casting to a list
	s1 = list(word.replace(" ", "").upper())
	sort_list1 = []
	ans_list = []
#while loop to take the min character append to sort list and remove from unsort list
#to put them in order
	while s1:
		smallest = min(s1)
		sort_list1.append(smallest)
		s1.pop(s1.index(smallest))
#for loop to loop through list of words
	for words in list_of_words:
		#creating a temp dump list to compare to target list
		sort_list_compare = []
		#taking the word, removing spaces, to upper and cast to list
		s2 = list(words.replace(" ", "").upper())
		#nested while loop to remove each element in order and pump into the
		#temp dump list to compare
		while s2:
			smallest = min(s2)
			sort_list_compare.append(smallest)
			s2.pop(s2.index(smallest))
		#comparing target sort list and sorted words from list one loop at a time
		# if they match I am appending them into ans_list and returning it
		if sort_list1 == sort_list_compare:
			ans_list.append(words)
					
	return ans_list
