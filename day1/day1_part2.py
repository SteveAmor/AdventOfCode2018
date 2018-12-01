running_freq = 0
first_freq = [0]

def get_freq_list():
  return [+7, +7, -2, -7, -4]

def answer():
  global running_freq
  while True:
    freq_list = get_freq_list()
    for i in range(len(freq_list)):
      running_freq += freq_list[i]
      if running_freq in first_freq:
        return(running_freq)
      first_freq.append(running_freq)

print(answer())


