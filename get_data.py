import os
import wget

# data from https://www.sciencedirect.com/science/article/pii/S2352340920303048

# Download the dataset
url = "https://www.research-collection.ethz.ch/bitstream/handle/20.500.11850/383116/rawdata_new.csv?sequence=1&isAllowed=y"
file_name = "data_raw.csv"
wget.download(url, file_name)

# # Unzip it and standardize the .csv filename
# import zipfile
# with zipfile.ZipFile(zip_name,"r") as zip_ref:
#     zip_ref.filelist[0].filename = 'data_raw.csv'
#     zip_ref.extract(zip_ref.filelist[0])

# os.remove(zip_name)