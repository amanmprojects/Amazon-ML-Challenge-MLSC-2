import os
import re
import pandas as pd
from download_and_preprocess import download_and_preprocess
from ocr_image_pytesseract import ocr_image

def predictor(image_link, category_id, entity_name):
    image = download_and_preprocess(image_link)
    text_split = ocr_image(image)
    
    print(text_split)

range_start = 158
range_end = 159

if __name__ == "__main__":
    DATASET_FOLDER = './dataset/'
    
    test = pd.read_csv(os.path.join(DATASET_FOLDER, 'test.csv'))
    # test = test.head(10)

    test = test.iloc[[158]]
    
    test['prediction'] = test.apply(
        lambda row: predictor(row['image_link'], row['group_id'], row['entity_name']), axis=1)
    
    output_filename = os.path.join(DATASET_FOLDER, 'test_out.csv')
    test[['index', 'prediction']].to_csv(output_filename, index=False)