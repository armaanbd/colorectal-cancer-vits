
# setup_datasets.py

def setup_kvasir_and_seg():
    import os
    import zipfile
    from google.colab import drive

    # Mount Google Drive
    drive.mount('/content/drive')

    # -------- Kvasir Dataset --------
    kvasir_zip_path = "/content/drive/MyDrive/ThesisArman/kvasir-dataset.zip"
    kvasir_extract_path = "/content/kvasir_dataset"
    kvasir_nested = os.path.join(kvasir_extract_path, "kvasir-dataset")

    if not os.path.exists(kvasir_nested):
        print("Extracting Kvasir dataset...")
        with zipfile.ZipFile(kvasir_zip_path, 'r') as zip_ref:
            zip_ref.extractall(kvasir_extract_path)
        print("✅ Kvasir dataset extracted to:", kvasir_extract_path)
    else:
        print("✅ Kvasir dataset already extracted at:", kvasir_nested)

    # -------- Kvasir-SEG Dataset --------
    seg_zip_path = "/content/drive/MyDrive/ThesisArman/kvasir-segmentation.zip"
    seg_extract_path = "/content/kvasir_seg"
    seg_images_path = os.path.join(seg_extract_path, "images")

    if not os.path.exists(seg_images_path):
        print("Extracting Kvasir-SEG dataset...")
        with zipfile.ZipFile(seg_zip_path, 'r') as zip_ref:
            zip_ref.extractall(seg_extract_path)
        print("✅ Kvasir-SEG dataset extracted to:", seg_extract_path)
    else:
        print("✅ Kvasir-SEG dataset already extracted at:", seg_images_path)

# Run setup
setup_kvasir_and_seg()
