
# setup_kvasir.py

def mount_and_extract_kvasir():
    import os
    import zipfile
    from google.colab import drive

    # Mount Google Drive
    drive.mount('/content/drive')

    # Paths
    zip_path = "/content/drive/MyDrive/ThesisArman/kvasir-dataset.zip"
    extract_path = "/content/kvasir_dataset"
    nested_dir = os.path.join(extract_path, "kvasir-dataset")

    # Extract only if not already extracted
    if not os.path.exists(nested_dir):
        print("Extracting Kvasir dataset...")
        with zipfile.ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
        print("Dataset extracted to:", extract_path)
    else:
        print("Dataset already extracted at:", nested_dir)

# Run setup
mount_and_extract_kvasir()
