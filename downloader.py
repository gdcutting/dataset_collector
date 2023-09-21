import requests
import pandas as pd
import os
import kaggle
import json
import yaml
import re
from bs4 import BeautifulSoup
from json.decoder import JSONDecodeError

# set default config values
# will deprecate at some point
download_limit_mb = 20
max_kaggle_downloads = 3

# instantiate tracking
download_refs = {}

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
	max_kaggle_downloads = config['sources']['kaggle']['max_session_downloads']

def read_dataset_status():
	"""
	read_dataset_status() checks datasets.json to get lists of downloaded datasets
	"""
	# open JSON file
	file = open('datasets.json')
	
	# read JSON file into dict
	datasets = json.load(file)  

	# Getting the list of values of the dictionary with the list comprehension
	# demoDictionary[dict_key] represents dictionary value
	datasets_list = [datasets[dict_value] for dict_value in datasets]
	print(datasets_list)

def log_download(source, ref, size, files):
	# construct dict for dataset item
	dataset_dict = {
		"source": "kaggle",
		"ref" : ref,
		"size" : size,
		"files" : files
	}

	print(dataset_dict)

	json_file_path = 'datasets.json'

	# Check if the JSON file exists
	try:
		with open(json_file_path, 'r') as json_file:
			json_data = json.load(json_file)
	except FileNotFoundError:
		# If the file doesn't exist, initialize it as an empty list
		json_data = []

		# Append the new data to the existing list
		json_data = json_data.append(dataset_dict)
		print(json_data)

		# Write the updated data back to the JSON file
		with open(json_file_path, 'w') as json_file:
			json.dump(json_data, json_file, indent=4)

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
			log_download("kaggle",dataset.ref,dataset.size,str(dataset.files))
			#kaggle.api.dataset_download_files(dataset.ref, path=download_path, unzip=True, quiet=False)
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
	kaggle_download()

if __name__ == "__main__":
	main()



