#First line is track_folder
#Second line is target_folder
#Third line are suffixes separated by space

def write_settings(path, data):
	f = open(path, 'w+')
	f.write(data[0] + '\n')
	f.close()

	f = open(path, 'a')
	
	f.write(data[1] + '\n')
	suffixes = ''
	for s in data[2]: suffixes += s + ' '	
	f.write(suffixes)

	f.close()

def read_settings(path):
	try:	
		f = open(path, 'r')
	except Exception:
		f = open(path, 'w+')
		f.close()

	f = open(path, 'r')

	data = []
	line = f.readline()
	line = line[:len(line)-1]
	data.append(line)

	line = f.readline()
	line = line[:len(line)-1]
	data.append(line)	

	line = f.readline()	
	suffixes_raw = line.split(' ')
	suffixes = [s for s in suffixes_raw]
	suffixes.pop(len(suffixes)-1)
	data.append(suffixes)

	f.close()
	return data