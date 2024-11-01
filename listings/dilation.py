def dilatate_mask(image, dilation_size=5):

    kernel = np.ones((dilation_size, dilation_size), np.uint8)
    dilatated_mask = cv2.dilate(image, kernel, iterations=1)
    return dilatated_mask

def apply_mask_dilatated_crop(image_path, output_path, dilation_size=5):

    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)
    mask_dilatated = dilatate_mask(image, dilation_size)
    cv2.imwrite(output_path, mask_dilatated)