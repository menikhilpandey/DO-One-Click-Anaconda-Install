# Module to deal with ssh connections and command execution using plink and cmd
import os
import easygui

def run():
	hostIP = easygui.enterbox(msg="Enter Host IP Address", 
		title="DARWIN | One-Click Ananconda2 on 14.04"
		)
	os.system('plink -ssh -t root@'+hostIP)
	#wget -O <path> <download path>

if __name__ == '__main__':
	run()