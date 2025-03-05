import os
import zipfile
import requests

# Configuration
ZENODO_RECORD_ID = "14967221"
ZENODO_API_URL = f"https://zenodo.org/api/records/{ZENODO_RECORD_ID}"
EXTRACTED_DIR = os.path.join(os.getcwd(), "extracted_data")

def get_zip_file_url():
    """Fetch ZIP file download URL from Zenodo API."""
    response = requests.get(ZENODO_API_URL)
    if response.status_code == 200:
        record = response.json()
        for file in record.get("files", []):
            if file["key"].endswith(".zip"):  # Look for a ZIP file
                return file["key"], file["links"]["self"]
        print("No ZIP file found in the Zenodo record.")
        exit(1)
    else:
        print("Failed to fetch file information from Zenodo.")
        exit(1)

def download_zip(file_name, file_url):
    """Download the ZIP file if it does not already exist."""
    file_path = os.path.join(os.getcwd(), file_name)

    if os.path.exists(file_path):
        print(f"ZIP file already exists: {file_path}")
    else:
        print(f"Downloading {file_name} from {file_url}...")
        response = requests.get(file_url, stream=True)

        if response.status_code == 200:
            with open(file_path, "wb") as file:
                for chunk in response.iter_content(chunk_size=1024):
                    file.write(chunk)
            print(f"Download complete: {file_path}")
        else:
            print("Failed to download the file.")
            exit(1)

    return file_path

def extract_zip(zip_path):
    """Extract the ZIP file into 'extracted_data' directory."""
    if not os.path.exists(EXTRACTED_DIR):
        os.makedirs(EXTRACTED_DIR)

    print(f"Extracting {zip_path} to {EXTRACTED_DIR}...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(EXTRACTED_DIR)
    print(f"Extraction complete: {EXTRACTED_DIR}")

if __name__ == "__main__":
    zip_file_name, zip_file_url = get_zip_file_url()
    zip_file_path = download_zip(zip_file_name, zip_file_url)
    extract_zip(zip_file_path)
