def get_input_list():
	return "dabAcCaCBAcCcaDA"

def get_pair_index(input_list):
	for i in range(0, len(input_list)-1):
		if abs(ord(input_list[i])-ord(input_list[i+1])) == 32:
			return i
	return None

def reduced_polymer_length(input_list):
	while True:
		i = get_pair_index(input_list)
		if i is None:
			return(len(input_list))
		input_list = input_list[:i] + input_list[i+2:]

def remove_char(input_list, char):
	shorter_list = ""
	for i in range(len(input_list)):
		if chr(char) not in input_list[i] and chr(char+32) not in input_list[i]:
			shorter_list += input_list[i]
	return shorter_list


if __name__ == "__main__":

	input_list = get_input_list()
	min_length = 35

	for i in range(ord("A"),ord("Z")+1):
		temp_list = remove_char(input_list, i)
		length = reduced_polymer_length(temp_list)
		if length < min_length:
			min_length = length

	print(min_length)
