import os 

for file in os.listdir():
	name,extension = os.path.splitext(file)
	extension = extension.replace('.','').upper()

	if not extension == '':
		if not os.path.exists(extension):
			os.makedirs(extension)

		os.rename(file, extension + "\\" + file )