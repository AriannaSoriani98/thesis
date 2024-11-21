def match_images(des1, des2, method='BF'):
    if des1 is None or des2 is None:
        return []  # No matches if descriptors are invalid

    # Use Hamming distance for ORB descriptors
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)

    # Ensure descriptors are valid and have the same shape
    if des1.shape[1] != des2.shape[1]:
        return []  # No matches if descriptor dimensions don't match

    matches = bf.knnMatch(des1, des2, k=2)

    # Apply ratio test
    good_matches = []
    for m, n in matches:
        if m.distance < 0.85 * n.distance:  # Lowe's ratio test
            good_matches.append(m)
    return good_matches