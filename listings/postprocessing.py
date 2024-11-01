def apply_central_rectangle_mask(mask, mask_ratio=0.6):

    # Get mask dimensions
    height, width = mask.shape[:2]

    # Calculate the central rectangle dimensions
    central_width = int(width * mask_ratio)
    central_height = int(height * mask_ratio)
    
    # Determine the starting and ending coordinates for the central rectangle
    x_start = (width - central_width) // 2
    y_start = (height - central_height) // 2
    x_end = x_start + central_width
    y_end = y_start + central_height

    # Create a blank mask and fill in the central rectangle area
    central_mask = np.zeros_like(mask, dtype=np.uint8)
    central_mask[y_start:y_end, x_start:x_end] = 255

    # Apply the central mask to the input mask
    result_mask = cv2.bitwise_and(mask, central_mask)
    return result_mask

