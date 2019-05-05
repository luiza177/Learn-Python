while True:
	user = input('enter your life: ')
	try:
		x = int(user)
		break
	except ValueError:
		print("enter a fucking number, idiot.")		
x -= 1
y = x + 3
print(y)

if y > 4:
	print("you're an idiot.")
	if x > 10:
		print("asdfghjkl")
elif y <= 0:
	print("HURR!")
else:
	print("you're still an idiot")
print("also, fuck you.")
input()