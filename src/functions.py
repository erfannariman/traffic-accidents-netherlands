import os
from src.get_files import GetFiles
import pandas as pd


def check_files_downloaded():
    if len(os.listdir()) == 0:
        GetFiles().download_csvs()


files = os.listdir("../data")
file = files[0]
df = pd.read_csv(f"../data/{file}")
print(df)






