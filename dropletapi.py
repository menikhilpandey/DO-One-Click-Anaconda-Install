# Module to create Droplet on digital Ocean

import digitalocean 
import time

def createDroplet(TOKEN,CONFIG):

	# Creates droplet with all existing ssh keys

	manager = digitalocean.Manager(token=TOKEN)
	keys = manager.get_all_sshkeys()

	NAME = CONFIG[0]
	REGION = CONFIG[1]
	SIZE = CONFIG[2]

	# No block storage, additional options, multiple droplets options included

	droplet = digitalocean.Droplet(token=TOKEN,
    	                           name=NAME,
        	                       region=REGION, 
            	                   image="ubuntu-14-04-x64", 
                	               size_slug=SIZE,
                    	           backups=False,
                    	           ssh_keys=keys)

	droplet.create()

	time.sleep(70) # Put script to halt for 80 seconds while the droplet is being created.

	actions = droplet.get_actions()
	for action in actions:
	    	action.load()
    		return action.status


def listDroplets(TOKEN):
	manager = digitalocean.Manager(token=TOKEN)
	my_droplets = manager.get_all_droplets()
	return(my_droplets)	

if __name__ == '__main__':
	createDroplet(TOKEN, CONFIG)
	listDroplets(TOKEN)