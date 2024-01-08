import pandas as pd
from pathlib import Path
import os
import gdown

def read_spreadsheet():
    SHEET_ID = "107pF1LcHgbJtCGCdGwffqIyM70eImBmgPOjUuHQfZ7g"
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
        sr_no = row.iloc[0]
        if sr_no >= 225 and sr_no <= 244:
            download_audio(id, gd_url)
