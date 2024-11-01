def image_detect_and_compute(sift, image_path, mask_path=None):
    img = cv2.imread(str(image_path), 0)  # Read in grayscale
    mask = None
    if mask_path:  # Load mask if provided
        mask = cv2.imread(str(mask_path), 0)

        # Ensure that mask size matches the image size
        if mask is not None and (mask.shape != img.shape):
            raise ValueError(f"Mask size {mask.shape} does not match image size {img.shape}")

    keypoints, descriptors = sift.detectAndCompute(img, mask)
    return img, keypoints, descriptors