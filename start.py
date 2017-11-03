import os.path

path = '/app/number'

if not os.path.isfile(path):
	with open(path, 'w') as f:
		f.write('0')

with open(path, 'r') as f:
	n = int(f.readline())

print(n)

n = n+1

with open(path, 'w') as f:
	f.write(str(n))
