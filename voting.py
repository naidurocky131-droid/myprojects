import cv2
import os

def match_fingerprint(input_fp, db_path="fingerprints"):
    for file in os.listdir(db_path):
        db_fp = cv2.imread(os.path.join(db_path, file), 0)
        input_img = cv2.imread(input_fp, 0)

        if db_fp is None or input_img is None:
            continue

        
        diff = cv2.absdiff(db_fp, input_img)
        score = diff.mean()

        if score < 10:  
            return file  

    return None
