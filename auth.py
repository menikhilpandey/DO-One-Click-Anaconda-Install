import easygui

def run():
	choice = easygui.buttonbox(msg="Personal Access Token for DigitalOcean API",
		title = "DARWIN | One-Click Ananconda2 on 14.04",
		choices= ["Load Existing Token file", "Create New Token"],
		default_choice="Create New Token")

	if choice=="Load Existing Token file":
		location = str(easygui.fileopenbox(msg="Browse Token File", 
			title="DARWIN | One-Click Ananconda2 on 14.04",
			default="*.token")
		)
		return open(location).read()

	elif choice=="Create New Token":
		tokenInp = easygui.enterbox(msg="Enter Your Personal Access Token",
			title="DARWIN | One-Click Ananconda2 on 14.04")
		saveOrNot = easygui.boolbox(msg="Do you want to save this Token?",
			title="DARWIN | One-Click Ananconda2 on 14.04")

		if saveOrNot:
			location = str(easygui.filesavebox(msg="Browse Location",
				title="DARWIN | One-Click Ananconda2 on 14.04",
				default="*.token")
			)
			with open(location,'w') as fileToken:
				fileToken.write(tokenInp)
		
		return tokenInp

if __name__ == '__main__':
	print run()