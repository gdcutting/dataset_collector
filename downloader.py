"""
File: downloader.py
Author: Guy Cutting
Date: 9/23/2023
Description: performs dataset downloads using public APIs
"""

import requests
import pandas as pd
import os
import kaggle
import json
import yaml
import re
import sqlite3
from bs4 import BeautifulSoup
from json.decoder import JSONDecodeError

# set default config values
# will deprecate at some point
download_limit_mb = 20
max_kaggle_downloads = 3

# instantiate tracking
download_refs = {}
con = None
cur = None

def read_config():
	"""
	read_config() reads the configuration values from config.yaml
	"""
	# read the user's credentials from the config file
	with open('config.yaml', 'r') as file:
		config = yaml.safe_load(file)

	# set the file size limit from the config
	print('Download limit: ' + str(config['download_limit_mb']) + "MB")
	download_limit_mb = config['download_limit_mb']

	# set max kaggle downloads
	print(config['sources'])
	max_kaggle_downloads = config['sources']['kaggle']['max_session_downloads']

def init_storage():
	# establish sqlite connection and create cursor
	# this will create the db if it does not already exist
	con = sqlite3.connect("datasets.db")
	cur = con.cursor()

	# create the downloads table
	try:
		cur.execute("CREATE TABLE downloads(source, reference, size, files)")
	except sqlite3.OperationalError:
		print('Downloads table exists. Skipping creation.')

	# close the connection
	con.close()

def download_exists(source, ref, size, files):
	# create connection and cursor
	# we know datasets.db exists now since init_storage has run
	con = sqlite3.connect("datasets.db")
	cur = con.cursor()

	params = (source, ref, size, files)

	# check for existing download
	select_str = "SELECT * FROM downloads WHERE source = 'kaggle' AND reference = '" + ref + "'"
	print(select_str)
	cur.execute(select_str)

	# if the above statement returns a record, then the download already exists
	# if not, we will get a type error with this assignment and we know to insert the download record
	try:
		record_exists = cur.fetchone()[0]
		return_value = True
	except TypeError:
		print("No existing record.")
		return_value = False
	
	# close the connection
	con.close()

	return return_value

def log_download(source, ref, size, files):
	# create connection and cursor
	# we know datasets.db exists now since init_storage has run
	con = sqlite3.connect("datasets.db")
	cur = con.cursor()

	params = (source, ref, str(size), files)
	print(size)
	print("log_download() files: " + str(files))

	try:
		cur.execute("INSERT INTO downloads VALUES(?, ?, ?, ?)", params)
		con.commit()
		con.close()

		return True
	except:
		return False
	
# default Kaggle download - fetch small number of 'hot' datasets
def kaggle_download():
	"""
	kaggle_download() performs downloads from the kaggle data source.
	Uses the Kaggle API to generate candidate downloads.
	Authentication is handled automatically by the kaggle package
	You will need to go to the kaggle website and create an API token.
	See https://github.com/Kaggle/kaggle-api under 'API Credentials'.
	"""

	# fetch list of datasets - default sort is 'hottest' so this will fetch datasets of current interest/activity
	dataset_list = kaggle.api.dataset_list()

	#iterate through dataset list and download relevant files
	for dataset in dataset_list[0:max_kaggle_downloads]:
		# print("Checking " + dataset.ref + "\n")
		# print("Size: " + dataset.size + "\n")
		if filesize_check(dataset.size):
			# print("Passed size check\n")
			# print(vars(dataset))

			# set source-appropriate download directory
			download_path = "datasets/kaggle/" + dataset.ref
			dataset_files = kaggle.api.dataset_list_files(dataset.ref).files
			dataset_size = dataset.size
			print("Downloading from " + dataset.ref + " (" + dataset.size + ")")
			print("Dataset files: " + str(dataset_files))
			if not download_exists("kaggle",dataset.ref,dataset.size,str(dataset_files)):
				kaggle.api.dataset_download_files(dataset.ref, path=download_path, unzip=True, quiet=False)
				log_download("kaggle", dataset.ref, dataset.size, dataset_files)
		else:
			print(dataset.ref + " failed size check. Skipping.")
		
		# print("---------")

def separate_num_char(s):
	"""
	separate_num_chars(s) accepts a string containing letters and numbers and splits it into numeric and character components
	"""
	res = re.split('([-+]?\d+\.\d+)|([-+]?\d+)', s.strip())
	res_f = [r.strip() for r in res if r is not None and r.strip() != '']
	return res_f

def filesize_check(filesize):
	"""
	filesize_check() compares filesize to the download_limit_mb which can be set in config.yaml
	"""
	size, unit = separate_num_char(filesize)
	size = int(size)

	if unit == 'KB':
		return True
	elif unit == 'MB':
		if size <= download_limit_mb:
			return True
		else:
			return False
	else:
		return False

def track_dataset():
	# JSON file
	return 0

def main():
	# read_status()
	read_config()
	init_storage()
	kaggle_download()

if __name__ == "__main__":
	main()



