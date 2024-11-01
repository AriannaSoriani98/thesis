def remove_isolated_gray_regions(mask):

    # Threshold the mask to define gray (128-254), white (255), and black (0) regions
    gray_mask = ((mask > 0) & (mask < 255)).astype(np.uint8) * 255
    white_mask = (mask == 255).astype(np.uint8) * 255

    # Find contours for gray regions
    contours, _ = cv2.findContours(gray_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Create a copy of the mask to modify
    result = mask.copy()
    
    for cnt in contours:
        # Check if the gray region is near a white area
        # Create a mask for this specific gray region
        gray_region_mask = np.zeros_like(mask, dtype=np.uint8)
        cv2.drawContours(gray_region_mask, [cnt], -1, 255, thickness=cv2.FILLED)

        # Dilate the gray region slightly to check if it touches any white region
        dilated_gray = cv2.dilate(gray_region_mask, np.ones((3, 3), np.uint8))
        touching_white = cv2.bitwise_and(dilated_gray, white_mask)

        # If there's no white area touching the gray region, remove it (set it to black)
        if cv2.countNonZero(touching_white) == 0:
            cv2.drawContours(result, [cnt], -1, 0, thickness=cv2.FILLED)
    
    return result
