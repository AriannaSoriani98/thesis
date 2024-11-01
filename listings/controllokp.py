def match_images(des1, des2, method='FLANN', k=2):
    # Skip matching if ortho image has des2=1
    if des2 is None or len(des2) == 1:
        print(f"Skipping matching: Ortho image has only 1 descriptor (des2=1).")
        return []

    if des1 is None or len(des1) == 0:
        print("Frontal image descriptor array (des1) is empty.")
        return []

    if len(des1) < k or len(des2) < k:
        print(f"Not enough descriptors to perform knn matching: des1={len(des1)}, des2={len(des2)}")
        return []

    # Convert to float32 if necessary
    if des1.dtype != np.float32:
        des1 = des1.astype(np.float32)
    if des2.dtype != np.float32:
        des2 = des2.astype(np.float32)