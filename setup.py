from subprocess import check_output
import os.path
from os import path

print('Beginning file download with urllib2...')

if not path.isdir('./bcidatasetIV2a'):
	cmd = '!git clone https://github.com/bregydoc/bcidatasetIV2a/archive/master.zip .'
	check_output(cmd, shell=True).decode()
