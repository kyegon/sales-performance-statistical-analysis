import os
import pandas as pd
import urllib.error
import urllib.request
from pathlib import Path
def extract_files(url, dst, filename):
    """
     Download and save raw files locally from GitHub. 
     Returns a DataFrame loaded from the downloaded Excel file
     url -- excel document URL
     dst -- destination to save the file
     filename - target member file name
    """
    try:
        dst_path = Path(dst)
        dst_path.mkdir(parents=True, exist_ok=True)
        filepath = dst_path / filename
        print(f"Destination: {filepath}")
        print(f"Downloading from: {url}")
        with urllib.request.urlopen(url) as fin:
            data = fin.read() 
        with open(filepath, mode='wb') as fout:
            fout.write(data)
            print(f"Data size: {len(data):,} bytes ({len(data)/1024/1024:.2f} MB)")
            print(f"Success! File '{filename}' saved to {dst}")
      
        print(f"Loading File into DataFrame...")
        return pd.read_csv(filepath)
        
    except urllib.error.URLError as e:
        print(f"Network Error: Unable to download from {url}")
        print(f"   Details: {e.reason}")
        raise
        
    except FileNotFoundError:
        print(f"File Error: Cannot access {filepath}")
        raise
    except Exception as e:
        print(f"Error: {type(e).__name__}: {str(e)}")
        raise
