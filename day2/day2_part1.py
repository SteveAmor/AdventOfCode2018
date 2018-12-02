from collections import Counter

def get_input_list():
  return ["abcdef", "bababc", "abbcde", "abcccd", "aabcdd", "abcdee", "ababab"]

def is_duplicate(string):
	"""Return true on first duplicate character in string"""
	dup_dic = Counter(string)
	for key, value in dup_dic.items():
		if value == 2:
			return True
	return False
		
def is_triplicate(string):
	"""Return true on first triplicate character in string"""
	tri_dic = Counter(string)
	count = 0
	for key, value in tri_dic.items():
		if value == 3:
			return True
	return False


if __name__ == "__main__":

	duplicate_count = 0
	triplicate_count = 0

	input_list = get_input_list()

	for i in input_list:
		if is_duplicate(i):
			duplicate_count += 1
		if is_triplicate(i):
			triplicate_count += 1

	print(duplicate_count * triplicate_count)


