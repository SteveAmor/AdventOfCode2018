def get_input_list():
	return ['#1 @ 1,3: 4x4', '#2 @ 3,1: 4x4', '#3 @ 5,5: 2x2']

def get_claim_id(string):
	return string.split(" @")[0]

def get_x(string):
	return int(string.split("@ ",1)[1].split(",")[0])

def get_y(string):
	return int(string.split(",",1)[1].split(": ")[0])

def get_x_width(string):
	return int(string.split(": ",1)[1].split("x")[0])

def get_y_height(string):
	return int(string.split("x",1)[1])


if __name__ == "__main__":

	input_list = get_input_list()
	
	max_x = 0
	max_y = 0

	for position in input_list:
		x = get_x(position)
		x_width = get_x_width(position)
		y = get_y(position)
		y_height = get_y_height(position)

		if x + x_width > max_x:
			max_x = x + x_width

		if y + y_height > max_y:
			max_y = y + y_height

	cloth_array = [[0 for x in range(max_x)] for y in range(max_y)]

	for position in input_list:
		x = get_x(position)
		y = get_y(position)
		x_width = get_x_width(position)
		y_height = get_y_height(position)
		
		for i in range(y_height):
			for j in range(x_width):
				cloth_array[y+i][x+j] += 1

	for position in input_list:
		x = get_x(position)
		y = get_y(position)
		x_width = get_x_width(position)
		y_height = get_y_height(position)
		claim_id = get_claim_id(position)
		
		claim_counter = 0

		for i in range(y_height):
			for j in range(x_width):
				claim_counter += cloth_array[y+i][x+j]
		if claim_counter == (x_width * y_height):
				print(claim_id)
				exit()
			

