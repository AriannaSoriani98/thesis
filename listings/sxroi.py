def detect_left_white_region(image):

    # Threshold the image to get the binary mask (white regions are 255)
    _, binary_mask = cv2.threshold(image, 254, 255, cv2.THRESH_BINARY)

    # Get image dimensions and calculate the midpoint
    height, width = binary_mask.shape
    x_mid = width * 2//5

    # Mask out the right half by zeroing it
    left_half_mask = binary_mask.copy()
    left_half_mask[:, x_mid:] = 0

    # Find contours in the left half mask
    contours, _ = cv2.findContours(left_half_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # If no contours are found, return None
    if not contours:
        return None

    # Initialize bounding box coordinates for the left white region
    x_min, y_min, x_max, y_max = np.inf, np.inf, -np.inf, -np.inf

    # Calculate bounding box for contours in the left half only
    for contour in contours:
        x, y, w, h = cv2.boundingRect(contour)
        x_min = min(x_min, x)
        y_min = min(y_min, y)
        x_max = max(x_max, x + w)
        y_max = max(y_max, y + h)

    return x_min, y_min, x_max, y_max