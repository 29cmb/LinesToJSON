# TXT Lines to JSON array
A simple python script which downloads a raw file and converts all of the file lines into a json array

Ex.
```json
[
    "item1",
    "item2",
    "item3"
]
```

## How to set up packages

Run the following command in your command shell to install all the required packages
```
pip install -r requirements.txt
```

Then, run `python main.py` to download the file.

## Configuration

All configuration are in config.json and must be changed before executed

`downloadURL` - Must be a raw file (a file which only has data and is seperated into different lines, such as a Github raw file of a txt document)

`fileName` - Must end in .json, the file will be uploaded with this name