import arrow

def main():
	print("MAIN")
	this_monday = arrow.now()
	monday = this_monday.format("MM/DD/YYYY")
	today = arrow.now().format("MM/DD/YYYY")
	sunday = this_monday.replace(days =+ 7)
	#print(monday + "\n" + today)
	if monday == today:
	    print("ONE")
	else:
	    print("ZERO")
	print("DONE")

if __name__ == "__main__":
	main()