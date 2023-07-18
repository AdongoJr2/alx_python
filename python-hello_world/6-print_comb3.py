for i in range(100):
	if str(i).zfill(2)[0] != str(i).zfill(2)[1] and int(str(i).zfill(2)[0]) < int(str(i).zfill(2)[1]):
		if i == 89:
			print("{}".format(str(i).zfill(2)))
		else:
			print("{}".format(str(i).zfill(2)), end=", ")
