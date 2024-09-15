from src.utils import download_image
from PIL import Image, ImageFilter
import os
from pathlib import Path
from tracemalloc import BaseFilter

# Increase the maximum image pixels limit
Image.MAX_IMAGE_PIXELS = None

def download_and_preprocess(image_link):
    image_path = os.path.join('images', Path(image_link).name)

    # Download image if it doesn't exist
    if not os.path.exists(image_path):
        download_image(image_link, save_folder='images')
        if not os.path.exists(image_path):
            raise FileNotFoundError(f"Image could not be downloaded: {image_path}")

    print("Processing image: ", image_path)
    
    # Load image
    image = Image.open(image_path)

    image = image.resize([100 * _ for _ in image.size], resample=Image.LANCZOS)  # Scale up the image with lanczos resampling
    image = image.filter(ImageFilter.MedianFilter())  # Apply median filter
    
    # grayscale image
    image = image.convert('L')
    
    # Save the image with different name
    image_path_processed = os.path.join('images_processed', Path(image_link).name)
    image.save(image_path_processed)

    return image