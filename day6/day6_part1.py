def get_input_list():
  return [(1,1), (1,6), (8,3), (3,4), (5,5), (8,9)]

def get_coord_dict(input_list):
  char = ord("A")
  coord_dict = {}
  for coord in input_list:
    coord_dict[coord] = chr(char)
    char += 1
  return coord_dict

def get_x_max_y_max(input_list):
  x_max = 0
  y_max = 0
  for i in input_list:
    x_max = max(i[0], x_max)
    y_max = max(i[1], y_max)
  return (x_max, y_max)
 
def build_grid(input_list):
  x_max, y_max = get_x_max_y_max(input_list)
  grid = [[0 for x in range(x_max+2)] for y in range(y_max+2)]
  return grid

def not_infinite(grid, coord_dict, char):
  if char in grid[0]:
    return False
  if char in grid[len(grid)-1]:
    return False

  for i in grid:
    if char in i[0]:
      return False
    if char in i[len(i)-1]:
      return False
  return True

def count_chars(grid, char):
  count = 0
  for i in grid:
    for j in i:
      if j == char:
        count += 1
  return count


if __name__ == "__main__":

  input_list = get_input_list()
  grid = build_grid(input_list)
  coord_dict = get_coord_dict(input_list)
  x_max, y_max = get_x_max_y_max(input_list)

  for x in range(x_max+2):
    for y in range(y_max+2):
      if (x,y) in input_list:
        grid[y][x] = coord_dict[(x,y)]
      else:
        dist = 10000
        for coord in input_list:
          a, b = coord
          man_dist = abs(a-x) + abs(b-y)
          if man_dist < dist:
            dist = man_dist
            grid[y][x] = coord_dict[(a,b)]
          elif man_dist == dist:
            grid[y][x] = "."

  largest_area = 0

  for coord in input_list:
    char = coord_dict[coord]
    if not_infinite(grid, coord_dict, char):
      chars = count_chars(grid, char)
      largest_area = max(chars, largest_area)

  print(largest_area)
