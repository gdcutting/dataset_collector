"""
File: uploader.py
Author: Guy Cutting
Date: 9/23/2023
Description: uploads files already downloaded with downloader, to a GitHub repo or elsewhere
"""
import sqlite3

class DatasetUploader:
	def __init__(self, name, age):
		self.active = True

def check_upload_status():
	"""
	check_upload_status() checks the SQLite db to see if files have already been downloaded for a given dataset
	"""
    # establish sqlite connection and create cursor
	# this will create the db if it does not already exist
	con = sqlite3.connect("datasets.db")
	cur = con.cursor()

	# create the downloads table if it does not exist
	try:
		cur.execute("CREATE TABLE downloads(source, reference, size, files)")
		print("Nothing downloaded yet. Run the downloader first.")
	except sqlite3.OperationalError:
		print('Downloads table exists. Checking uploads.')

	# build the string for SELECT query for all existing downloads
	select_str = "SELECT * FROM downloads"
	# execute the query
	cur.execute(select_str)

	# Fetch the rows
	rows = cur.fetchall()
	# Check the number of rows returned
	row_count = len(rows)

	print("There are currently " + str(row_count) + " downloads:")
	for row in rows:
    	# Each row is a tuple, and you can access columns by index
		column1_value = row[0]
		column2_value = row[1]

    	# You can also access columns by name if you use a named tuple
    	# (assuming your query returned named columns)
		# column1_value_test = row['column1']
    	# column2_value = row['column2']

   		# Perform operations with the data as needed
		print(column1_value, column2_value)
		print(column1_value_test)

	# close the connection
	con.close()

def main():
	print("This is uploader.py.")
	check_upload_status()

if __name__ == "__main__":
	main()