
def get_input_list():
  return [(1,1), (1,6), (8,3), (3,4), (5,5), (8,9)]

def get_x_max_y_max(input_list):
  x_max = 0
  y_max = 0
  for i in input_list:
    x_max = max(i[0], x_max)
    y_max = max(i[1], y_max)
  return (x_max, y_max)

def build_grid(input_list):
  x_max, y_max = get_x_max_y_max(input_list)
  grid = [['.' for x in range(x_max+2)] for y in range(y_max+2)]
  return grid

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
  x_max, y_max = get_x_max_y_max(input_list)

  for x in range(x_max+2):
    for y in range(y_max+2):
      total_distance = 0
      max_distance = 32
      for coord in input_list:
        a, b = coord
        man_dist = abs(a-x) + abs(b-y)
        total_distance += man_dist
        if total_distance >= max_distance:
          grid[y][x] = "."
          break
        elif total_distance < max_distance:
          grid[y][x] = "#"

print(count_chars(grid, "#"))
