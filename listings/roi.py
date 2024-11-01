#FRONTAL IMG
def get_central_part_of_bbox(image, bbox, central_ratio=0.5):
    x_min, y_min, x_max, y_max = bbox

    # Calculate bounding box width and height
    bbox_width = x_max - x_min

    # Calculate central region dimensions
    central_width = int(bbox_width * central_ratio)

    # Calculate the central region coordinates
    x_central_min = x_min + (bbox_width - central_width) // 2
    y_central_min = y_min 
    x_central_max = x_central_min + central_width
    y_central_max = y_max 

    # Create a blank mask with the same size as the original image
    central_mask = np.zeros_like(image)

    # Copy the central region to the central mask
    central_mask[y_central_min:y_central_max, x_central_min:x_central_max] = image[y_central_min:y_central_max, x_central_min:x_central_max]
    
    return central_mask