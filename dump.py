# read the user's credentials from the config file
with open('config.yaml', 'r') as file:
    config = yaml.safe_load(file)

credentials_file = config['kaggle']['credentials_file']
cf = open(credentials_file)
credentials_data = json.load(cf)
kaggle_username = credentials_data['username']
kaggle_key = credentials_data['key']

for i in credentials_data:
    print(i)



print("Downloading " + str(dataset))
    download_path = "datasets/" + dataset
    kaggle.api.dataset_download_files(dataset, path=download_path,unzip=True)