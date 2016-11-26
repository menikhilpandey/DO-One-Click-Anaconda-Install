def run():
	try:
		from pexpect import pxssh
		s = pxssh.pxssh()

	   	hostname = easygui.enterbox(msg="Enter Host IP", 
			title="DARWIN | One-Click Ananconda2 on 14.04")
	   	username = easygui.enterbox(msg="Enter Username", 
			title="DARWIN | One-Click Ananconda2 on 14.04")
	   	password = easygui.passwordbox(msg="Enter Password",
	    	title="DARWIN | One-Click Ananconda2 on 14.04")
	   	
	   	s.login(hostname, username, password)
		
		commands = open("commands.txt").read().split('\n')
		commands = [command for command in commands if command!='']
		for command in commands:
			s.sendline(command)    # run a command
	   		s.prompt()             # match the prompt
	   		print(s.before)        # print everything before the prompt.
	   	
	   	s.logout()

	except pxssh.ExceptionPxssh as e:
		print("pxssh failed on login.")
		print(e)

	finally:
		return None

if __name__ == '__main__':
	run()