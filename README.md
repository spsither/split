# SPLIT

Split does the following
- download audio files from google drive and youtube 
- split the full audio files into ~ 6s segments 
- run inference on the audio segments
- make a csv file to be uploaded to the stt.pecha.tools posgres database

## STT_CS

### 1) `download_gdrive.ipynb`
```python
if id >= 492 and id <= 513:
    print(id, gd_url)
    download_audio(gd_url)
```

change the id from and to range by looking at the [google sheet](https://docs.google.com/spreadsheets/d/1-WuaaWKIHJfGQhDXVSwG-v2qGqxQYVqqk7lFeHyxEzk/edit?usp=sharing)

### 2) `split.py`
Split the full audio into segments.
That will put the split files in after_split folder
make sure to activate the python env by running `ac` at `/media/monlamai/SSD/GitHub/split`

### 3) `collect_segments.py`. 
Collect all the segments into one foler.
Change the group in `collect_segments.py`.

### 4) upload all the segments to s3
`aws s3 cp segments_cs_gf  s3://monlam.ai.stt/stt_pecha_tools/ --recursive`

### 5) `make_csv.ipynb`
```python
group = "gf"
group_id = 6
last_db_id = 320082
```
make sure to update the group, group_id according to where you want to put the new segemnts.
Also update the `last_db_id` by running `select max(id) from "Task" t;`

### 6) upload using dbeaver-ce
Open a connection to the postgres db on render using dbeaver-ce and import using the csv file created in step 5.

