def performance_rating(load_time: float):

    if load_time < 1:
        rating = "Excellent"
    elif load_time < 3:
        rating = "Good"
    elif load_time < 5:
        rating = "Average"
    else:
        rating = "Poor"

    return {
        "load_time": load_time,
        "rating": rating
    }