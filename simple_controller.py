def control_vehicle(obj_detected):
    if obj_detected:
        return "STOP"
    else:
        return "MOVE_FORWARD"
