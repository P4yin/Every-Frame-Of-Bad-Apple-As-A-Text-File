from PIL import Image

if __name__ == '__main__':
	WHITE = 50   # adjust this value. Higher for less white pixels. (Youmus sword gets a bit weird)
	PATH = "text_files\\"  # change this to wherever you want the text to go
	BAD_APPLE = "EveryBadAppleframe\\frame"  # change to where ever the png's are stored
	
	choice = str(input("What frame would you like (1-6561 inclusive)? Type 'all' for all the frames. Otherwise, a frame number is all thats needed.\n"))
	if choice.lower() == 'all':
		for num in range(1, 6561):
			filenum = "0"*(5-len(str(num))) + str(num)
			f = open(PATH + filenum + ".txt", 'w')
			im = Image.open(BAD_APPLE+ filenum + ".png")
			px = im.load()
			string = ""
			for i in range(368):
				for j in range(496):
					a = px[j, i]
					r = a[0]
					g = a[1]
					b = a[2]
					if r < WHITE and g < WHITE and b < WHITE:
						string+='.'
					else:
						string+='@'
				string+="\n"
			f.write(string)
			f.close()
	else:
		try:  # im not sure how to handel this error just yet
			if 1<= int(choice) and 6561 >= int(choice):
				filenum = "0"*(5-len(choice)) + choice
				f = open(PATH + filenum + ".txt", 'w')
				im = Image.open(BAD_APPLE + filenum + ".png")
				px = im.load()
				string = ""
				for i in range(368):
					for j in range(496):
						a = px[j, i]
						r = a[0]
						g = a[1]
						b = a[2]
						if r < WHITE and g < WHITE and b < WHITE:
							string+='.'
						else:
							string+='@'
					string+="\n"
				f.write(string)
				f.close()
		except:
			print('Invalid input. Bye.')