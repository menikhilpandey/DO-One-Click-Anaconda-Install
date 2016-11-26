import easygui

def run():
	SIZE = easygui.buttonbox(msg="Choose A Size",
		title="DARWIN | One-Click Ananconda2 on 14.04",
		choices=["512mb","1gb","2gb","4gb","8gb","16gb"],
		default_choice="512mb",
		cancel_choice="512mb" 
	)
	REGION = easygui.buttonbox(msg="Choose A Datacenter Region",
		title="DARWIN | One-Click Ananconda2 on 14.04",
		choices=["nyc1","nyc2","nyc3","sfo1","sfo2","ams2",
				"ams3","sgp1","lon1","fra1","tor1","blr1"],
		default_choice="blr1",
		cancel_choice="blr1" 
	)
	NAME = easygui.enterbox(msg="Enter a Hostname", 
		title="DARWIN | One-Click Ananconda2 on 14.04",
		default="anaconda-"+SIZE+'-'+REGION)
	
	return (NAME,REGION,SIZE)	
	
if __name__ == '__main__':
	print run()