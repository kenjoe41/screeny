################################################################################################
# Name: Screeny.                                                                               #
# Description: A tool to take screen shots and upload them to imgur from within the Terminal.  #
# Author: Phage (phage@evilzone.org)                                                           #  
################################################################################################

import argparse
import os
import pyimgur
import time

import pyscreenshot as ImageGrab

class Screeny(object):

	def __init__(self, args):
		self.args = args
	
	def upload_to_imgur(self):
		CLIENT_ID = "5c6af8a99249f98"

		ImageGrab.grab_to_file(args.upload)
		im = pyimgur.Imgur(CLIENT_ID)
		uploaded_image = im.upload_image(args.upload, title="Uploaded with PyImgur")
		print(uploaded_image.link)

		try:
			os.remove(args.upload)
		except OSError, e:
			print ("Error: %s - %s." % (e.filename,e.strerror))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog="Screeny")
    parser.add_argument('-u', '--upload', help="upload the screenshot to imgur")
    parser.add_argument('-t', '--timer', help="Sets a timer on the screenshot.", type=int, required=False)

    args = parser.parse_args()

    if args.timer:
    	time.sleep(args.timer)

    screeny = Screeny(args)
    screeny.upload_to_imgur()
