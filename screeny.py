################################################################################################
# Name: Screeny.                                                                               #
# Description: A tool to take screen shots and upload them to imgur from within the Terminal.  #
# Author: Phage (phage@evilzone.org)                                                           #  
################################################################################################

import argparse
import os
import pyimgur

import pyscreenshot as ImageGrab

class Screeny(object):

	def __init__(self, args):
		self.args = args

	def upload_to_imgur(self):
		CLIENT_ID = ""

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

    args = parser.parse_args()
    screeny = Screeny(args)
    screeny.upload_to_imgur()
