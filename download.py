from src.utils import download_image
import pandas as pd

def download_dataset(dataset_path):
    dataset = pd.read_csv(dataset_path)
    image_links = dataset['image_link'].iloc[0:100].tolist()
    for image_link in image_links:
        download_image(image_link=image_link, save_folder='./images')

if __name__ == "__main__":
    download_dataset('./dataset/train.csv')