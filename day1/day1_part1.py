start_freq = 0

def adjust_freq(running_freq, freq_list):
  for i in freq_list:
    running_freq += i
  return running_freq

def get_freq_list():
  return [+1, -2, +3, +1]

print(adjust_freq(start_freq, get_freq_list()))

