def sum_matches(total_matches):
    result_array = []
    # Helper function to update the dictionary with array values
    def update_dict(array):
        result_dict = {}
        for num, string in array:
            if string in result_dict:
                result_dict[string.stem] += num
            else:
                result_dict[string.stem] = num
        # Sort by values in descending order
        sorted_by_values = sorted(result_dict.items(), key=lambda item: item[1], reverse=True)
        return sorted_by_values

    # Update the dictionary with all arrays
    for (img, matches) in total_matches:
      result_array.append([img, update_dict(matches)]) #matches ( (p, ()), (p, ()), ...)
    return result_array