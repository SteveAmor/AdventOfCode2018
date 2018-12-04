from operator import add

def get_input_list():
	return ['[1518-11-01 00:00] Guard #10 begins shift',
'[1518-11-01 00:05] falls asleep',
'[1518-11-01 00:25] wakes up',
'[1518-11-01 00:30] falls asleep',
'[1518-11-01 00:55] wakes up',
'[1518-11-01 23:58] Guard #99 begins shift',
'[1518-11-02 00:40] falls asleep',
'[1518-11-02 00:50] wakes up',
'[1518-11-03 00:05] Guard #10 begins shift',
'[1518-11-03 00:24] falls asleep',
'[1518-11-03 00:29] wakes up',
'[1518-11-04 00:02] Guard #99 begins shift',
'[1518-11-04 00:36] falls asleep',
'[1518-11-04 00:46] wakes up',
'[1518-11-05 00:03] Guard #99 begins shift',
'[1518-11-05 00:45] falls asleep',
'[1518-11-05 00:55] wakes up',
]

if __name__ == "__main__":

	input_list = sorted(get_input_list())

	guard_sleep_dict = {}

	guard_on_duty = 0
	minute_falls_asleep = 0
	most_tired_guard = 0
	most_slept_minutes = 0

	for i in range(len(input_list)): # Create dictionary entry for each guard in list with no sleep logged
		if "Guard" in input_list[i]:
			guard_number = int(input_list[i].split("#")[1].split(" ")[0])
			if guard_number not in guard_sleep_dict:
				guard_sleep_dict[guard_number] = [0 for minute in range(60)]

	for i in range(len(input_list)):
		if "Guard" in input_list[i]:
			guard_on_duty = int(input_list[i].split("#")[1].split(" ")[0])
			minutes_asleep = 0
		if "falls" in input_list[i]:
			minute_falls_asleep = int(input_list[i].split("00:")[1].split("]")[0])
		if "wakes" in input_list[i]:
			minute_awakes = int(input_list[i].split("00:")[1].split("]")[0])
			minutes_asleep = minute_awakes - minute_falls_asleep
			
			saved_sleep_list = guard_sleep_dict[guard_on_duty]
			current_sleep_list = [0 for minute in range(60)]
			for i in range(minute_falls_asleep, minute_awakes):
				current_sleep_list[i] += 1
			guard_sleep_dict[guard_on_duty] = list(map(add, saved_sleep_list, current_sleep_list))

	for guard in guard_sleep_dict:
		if max(guard_sleep_dict[guard]) > most_slept_minutes:
			most_slept_minutes = max(guard_sleep_dict[guard])
			most_tired_guard = guard

	print("Most tiered guard:", most_tired_guard)
	print("Most slept minute:", guard_sleep_dict[most_tired_guard].index(max(guard_sleep_dict[most_tired_guard])))



	




