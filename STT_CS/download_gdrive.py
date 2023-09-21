import pandas as pd
from pathlib import Path
import os
import gdown

def read_spreadsheet():
    SHEET_ID = "1-WuaaWKIHJfGQhDXVSwG-v2qGqxQYVqqk7lFeHyxEzk"
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"
    df = pd.read_csv(url)
    return df

def create_folder(id):
    Path(id).mkdir(parents=True, exist_ok=True)

def download_audio(id, gd_url):
    print(id, gd_url)
    # gdown.download(gd_url, output_file, quiet=False)
    if not os.path.exists(f"./{id}/{id}.wav"):
        file_id = gd_url.split("/")[-2] if "drive.google.com" in gd_url else gd_url
        # Download the file
        gdown.download(f"https://drive.google.com/uc?id={file_id}", f"./{id}/{id}.wav", quiet=False)

if __name__ == "__main__":
    spreadsheet = read_spreadsheet()
    print(spreadsheet)
    
    for index, row in spreadsheet.iterrows():
        if index < 5:
            continue
        print(index,row)
        if index > 6:
            break
        # if not isinstance(row['Audio'], str) or not isinstance(row['STT_0000'], str):
        #     break
        # id = row['STT_0000']
        # gd_url = row['Audio']
        # sr_no = row['Sr.no']
        # if sr_no >= 1 and sr_no <= 206:
        #     create_folder(id)
        #     download_audio(id, gd_url)
