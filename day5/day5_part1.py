def get_input_list():
	return "dabAcCaCBAcCcaDA"

def get_pair_index(input_list):
	for i in range(0, len(input_list)-1):
		if abs(ord(input_list[i])-ord(input_list[i+1])) == 32:
			return i
	return None


if __name__ == "__main__":

	input_list = get_input_list()

	while True:
		i = get_pair_index(input_list)
		if i is None:
			print(len(input_list))
			exit()
		input_list = input_list[:i] + input_list[i+2:]
