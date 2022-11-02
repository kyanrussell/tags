with open('tags/RAW_CODES.txt') as f:
	lines = f.readlines()
	for line in lines[1:]:
		stripped = line.strip('\n')
		species, code = stripped[:-5], stripped[-4:]
		print(f"{code} = \"{species}\"")
