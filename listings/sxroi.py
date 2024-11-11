def detect_left_white_region(image):

    # Threshold the image to get the binary mask (white regions are 255)
    _, binary_mask = cv2.threshold(image, 254, 255, cv2.THRESH_BINARY)

    # Get image dimensions and calculate the midpoint
    height, width = binary_mask.shape
    x_mid = width // 2 

    # Mask out the right half by zeroing it
    left_half_mask = binary_mask.copy()
    left_half_mask[:, x_mid:] = 0

    x_min=0
    x_max=x_mid
    y_min=0
    y_max=height

    return x_min, y_min, x_max, y_max