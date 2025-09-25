import numpy as np

def match_xor(features, db):
    min_distance = float("inf")
    matched_id = None
    for user_id, stored in db["users"].items():
        stored_features = np.array(stored["features"])
        xor_result = np.bitwise_xor(features, stored_features)
        distance = np.sum(xor_result)
        if distance < min_distance:
            min_distance = distance
            matched_id = user_id
    return matched_id, min_distance
