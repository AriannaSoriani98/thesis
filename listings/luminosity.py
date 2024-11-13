def uniform_luminosity_contrast(image_path,target_luminosity=50):
    image = cv2.imread(str(image_path))

    # Convert image to LAB color space for more effective contrast control
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Split into channels
    l_channel, a, b = cv2.split(lab_image)

    # Apply CLAHE to L channel for better contrast and uniformity
    clahe = cv2.createCLAHE(clipLimit=1.0, tileGridSize=(8, 8))

    # Calculate the current mean luminosity
    current_luminosity = l_channel.mean()

    # Adjust the luminosity by scaling the L channel to the target luminosity
    l_channel = cv2.normalize(
        l_channel, None,
        alpha=target_luminosity - (current_luminosity - l_channel.min()),
        beta=target_luminosity + (l_channel.max() - current_luminosity),
        norm_type=cv2.NORM_MINMAX
    )
    # Apply CLAHE to L channel for better contrast and uniformity
    l_channel = clahe.apply(l_channel)

    # Merge channels back
    lab_image = cv2.merge((l_channel, a, b))

    # Convert back to BGR color space
    result_image = cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)

    return result_image