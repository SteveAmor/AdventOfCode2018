def get_input_list():
	return ["abcde", "fghij", "klmno", "pqrst", "fguij", "axcye", "wvxyz"]

def remove_nth_char_from_string(string, n):
	short_string = string[:n] + string[n+1:]
	return short_string

def compare_strings(string1, string2):
	"""Return the short string iff one character mismatch between strings in the same position else return None"""
	for n in range(len(string1)):
		_string1 = remove_nth_char_from_string(string1, n)
		_string2 = remove_nth_char_from_string(string2, n)			
		if _string1 == _string2:
			return _string1
	return None

def answer(input_list):
	for i in range(len(input_list)):
		for j in range(i+1, len(input_list)):
			answer_string = compare_strings(input_list[i], input_list[j]) 
			if answer_string is not None:
				return(answer_string)


if __name__ == "__main__":

	input_list = get_input_list()

	print(answer(input_list))
				

		
