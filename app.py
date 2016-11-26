import easygui # Module to create GUI Based Application
import dropletapi # Module to use digitalocean api to create a droplet
import config # Module to set name, region, size of Droplet
import auth  # Module to check for Personal Access TOKEN
import sshagent # Module for ssh connection with Droplet

def main():
	
	TOKEN = auth.run()
	
	confirm = easygui.ccbox(msg="Continue to Install Anancoda on Ubuntu 14.04 ?",
						  title="DARWIN | One-Click Ananconda2 on 14.04")

	if confirm:
		CONFIG = config.run()
		dropletapi.createDroplet(TOKEN,CONFIG)
		easygui.msgbox(msg="Awesome! \
			\nYour Ubuntu 14.04 droplet has been created.\
			\nHOSTNAME and Password for root user have been mailed.\
			\nCreate New Password on First login, Then click OK",
			title="DARWIN | One-Click Ananconda2 on 14.04")
		sshagent.run()
		easygui.msgbox(msg="Good to go! \
			\nDroplet with Anaconda2 on Ubuntu 14.04 Created.\
			\nDeploy your data science projects now!",
			title="DARWIN | One-Click Ananconda2 on 14.04")
	else:
		easygui.msgbox(msg="Thanks For using me!",
						title="DARWIN | One-Click Ananconda2 on 14.04")

if __name__ == '__main__':
	main()
	