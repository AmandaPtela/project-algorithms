def study_schedule(permanence_period, target_time):
    times = 0
    if type(target_time) != int:
        return None
    for login, logout in permanence_period:
        if type(login) != int or type(logout) != int:
            return None
        if target_time >= login and target_time <= logout:
            times += 1
    return times
# study_schedule([(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)], 5)

