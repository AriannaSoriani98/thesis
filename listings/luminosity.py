def adjust_luminosity(image_path, target_luminosity=70):
    # Read image
    image = cv2.imread(str(image_path))

    # Convert image to LAB color space for lightness adjustment
    lab_image = cv2.cvtColor(image, cv2.COLOR_BGR2LAB)

    # Split into LAB channels
    l_channel, a, b = cv2.split(lab_image)

    # Calculate the current mean luminosity
    current_luminosity = l_channel.mean()

    # Adjust the luminosity by scaling the L channel to the target luminosity
    l_channel = cv2.normalize(
        l_channel, None,
        alpha=target_luminosity - (current_luminosity - l_channel.min()),
        beta=target_luminosity + (l_channel.max() - current_luminosity),
        norm_type=cv2.NORM_MINMAX
    )

    # Merge channels back
    lab_image = cv2.merge((l_channel, a, b))

    # Convert back to BGR color space
    result_image = cv2.cvtColor(lab_image, cv2.COLOR_LAB2BGR)

    return result_image
