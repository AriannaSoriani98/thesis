def post_process_mask(binary_mask):
    # 1. Convert to binary image (in case it isn't already)
    _, binary_mask = cv2.threshold(binary_mask, 127, 255, cv2.THRESH_BINARY)

    # 2. Morphological Opening to remove small noise
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    cleaned_mask = cv2.morphologyEx(binary_mask, cv2.MORPH_OPEN, kernel)

    # 3. Remove small connected components (outliers)
    num_labels, labels, stats, _ = cv2.connectedComponentsWithStats(cleaned_mask, connectivity=8)

    # Define minimum area to keep
    min_area = 100
    filtered_mask = np.zeros_like(binary_mask)

    # Image dimensions
    height, width = binary_mask.shape

    for i in range(1, num_labels):  # Skip the background (label 0)
        area = stats[i, cv2.CC_STAT_AREA]
        x = stats[i, cv2.CC_STAT_LEFT]
        y = stats[i, cv2.CC_STAT_TOP]
        w = stats[i, cv2.CC_STAT_WIDTH]
        h = stats[i, cv2.CC_STAT_HEIGHT]

        # Check if component touches the border
        touches_border = (x == 0 or y == 0 or x + w == width or y + h == height)

        # Keep components based on area and if they don't touch the border
        if area >= min_area and not touches_border:
            filtered_mask[labels == i] = 255

    return filtered_mask