#!/usr/bin/python

import threading, time

class rss:
	def __init__(self):
		threading.Thread(target=self.rss).start()
		return

	def rss(self):
		import os
		#bashcommand = "echo Aman | sponge ../../data/rss"
		print "rss Thread running"
		bashcommand = "rsstail -P -u http://feeds.reuters.com/reuters/INtopNews -i 30 > ../../data/rss"
		os.system(bashcommand)
		return

rss_thread = rss()
