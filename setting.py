#First line is track_folder
#Second line is target_folder
#Third line are suffixes separated by space

def write_settings(data):
	f = open('settings.txt', 'w')
	f.write(data[0] + '\n')
	f.close()

	f = open('settings.txt', 'a')
	
	f.write(data[1] + '\n')
	suffixes = ''
	for s in data[2]: suffixes += s + ' '
	f.write(suffixes)

	f.close()

def read_settings():
	f = open('settings.txt', 'r')

	data = []
	data.append(f.readline())
	data.append(f.readline())
	

	f.close()