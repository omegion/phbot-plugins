def get_message_type_by_id(message_type_id):
    if message_type_id == 1:
        return "all"
    elif message_type_id == 2:
        return "private"
    elif message_type_id == 3:
        return "gm"
    elif message_type_id == 4:
        return "party"
    elif message_type_id == 5:
        return "guild"
    elif message_type_id == 6:
        return "global"
    elif message_type_id == 7:
        return "notice"
    elif message_type_id == 9:
        return "stall"
    elif message_type_id == 11:
        return "union"
    elif message_type_id == 16:
        return "academy"
    else:
        return ""
