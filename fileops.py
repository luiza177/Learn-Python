# File operations

#TODO create file ???

#counting characters
def countChars(text, char):
	count = 0
	for c in text:
		if c == char:
			count += 1
	return count


#open file in read mode, read, close
try:
	with open("shit.txt") as f:
		print(f.read())
		f.close()
except FileNotFoundError:
	print("File not found!")	

#open file in write mode, write shit, close
#try:
#	file = open("shit.txt", "w")
#	file.write("this shit's been PWNed")
#	f.close()
#except FileNotFoundError:
#	print("File not found!")

#open file in read mode, analyze, close
try:
	with open("shit.txt") as f:
		txt = f.read()
		print(countChars(txt, "a"))
		f.close()
except FileNotFoundError:
	print("File not found!")	

