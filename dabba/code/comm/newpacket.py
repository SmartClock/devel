#!/usr/bin/python
# decription is added at the end of the other data.
data = ["lon","lat","temp", "humidity"] # other data which are to extreacted and stored in csv format in the file 'packet.dat'
def SHAS ():
			
	import fileinput, re
	for line in fileinput.input("../../data/weather.dat", inplace=True):
		print(line.replace(",", " , "))
	fileinput.close
	report = open ("../../data/weather.dat", "r")
	packet = open ("../../data/temp", "w")
	for line in report:
		for word in line.split():
			#print word
			for  match in data:
				if match+"\"" in word:
					packet.write (word + "\n")
	report = open ("../../data/weather.dat", "r")
	for line in report:
		i=0;
		list=line.split()
		size=len(list)
		while i < size:
			if "description"+"\"" in list[i]:
				packet.write(list[i] + " ")
				i +=1
				while True:
					if "\"" not in word:
						packet.write(list[i] + " ")
						i +=1
					else:
						packet.write(list[i] + "\n")
						break
				break
			i += 1			
	return


def packet ():
	

	import fileinput
	for line in fileinput.input("../../data/weather.dat", inplace = True):
		print(line.replace("\":{", " "))

	fileinput.close

	SHAS()

	for line in fileinput.input("../../data/temp", inplace = True):
		print(line.replace("\"main\":{", ""))

	fileinput.close

	for line in fileinput.input("../../data/temp", inplace = True):
		print(line.replace("}", ""))

	f = open ("../../data/temp",'a')


	f.write ('$')
	f.close


	f = open ("../../data/temp", 'r')
	f.seek (0)
	c = f.read(1)
	a = ''

	while c != '$':
		if c == ":":
			c = f.read (1)
			while c != '\n':
				a += c
				c = f.read(1)
			a += ','
			c = f.read(1)
		if (c == '$'):
			break
		c = f.read (1)
	#print a

	f.close

	packet = open ("../../data/packet.dat", 'w')

	packet.write (a)
	type(a)
	return a



