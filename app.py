import easygui # Module to create GUI Based Application
import dropletapi # Module to use digitalocean api to create a droplet
import config # Module to set name, region, size of Droplet
import auth  # Module to check for Personal Access TOKEN
#import sshagent # Module for ssh connection with Droplet

def main():
	
	TOKEN = auth.run()
	
	confirm = easygui.ccbox(msg="Continue to Install Anancoda on Ubuntu 14.04 ?",
						  title="DARWIN | One-Click Ananconda2 on 14.04")

	if confirm:
		CONFIG = config.run()
		dropletapi.createDroplet(TOKEN,CONFIG)
		#sshagent.run()
	else:
		easygui.msgbox(msg="Thanks For using me!",
						title="DARWIN | One-Click Ananconda2 on 14.04")

if __name__ == '__main__':
	main()
