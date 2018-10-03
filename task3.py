def access_lst(file):
	fin=open(file)
	a=[]
	for line in fin:
		line=line.strip()
		for i in line.split():
			if i=='global_access' or i=='fw-management_access_in':
                 a.append(line)

	return a
print(access_lst('running-config.cfg'))