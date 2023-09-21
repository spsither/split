import pandas as pd
from pathlib import Path
import os
import gdown

from_id = 124
to_id = 160

def read_spreadsheet():
    SHEET_ID = "17HKtVQMxJ5YwG8YBaLtOszsPk4jOYrcr7HuFhNnX4Gk"
    url = f"https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv"
    df = pd.read_csv(url)
    return df

def create_folder(id):
    Path(id).mkdir(parents=True, exist_ok=True)

def download_audio(id, gd_url):
    # os.system(
    #     f"""yt-dlp --extract-audio --audio-quality 0 --audio-format wav --postprocessor-args "-ar 16000 -ac 1" {gd_url} -o './{id}/{id}.%(ext)s'"""
    # )
    print(id, gd_url)
    # gdown.download(gd_url, output_file, quiet=False)
    if not os.path.exists(f"./full_audio/{id}.wav"):
        file_id = gd_url.split("/")[-2] if "drive.google.com" in gd_url else gd_url
        # Download the file
        # gdown.download(f"https://drive.google.com/uc?id={file_id}", output_file, quiet=False)
        gdown.download(f"https://drive.google.com/uc?id={file_id}", f"./full_audio/{id}.wav", quiet=False)

if __name__ == "__main__":
    spreadsheet = read_spreadsheet()
    for index, row in spreadsheet.iterrows():
        if not isinstance(row['Audio'], str) or not isinstance(row['STT_0000'], str):
            break
        id = row['STT_0000']
        gd_url = row['Audio']
        sr_no = row['Sr.no']
        if sr_no >= from_id and sr_no <= to_id:
            download_audio(id, gd_url)
