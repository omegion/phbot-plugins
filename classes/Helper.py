from threading import Timer


class Helper(object):
    def __init__(self):
        pass

    def get_message_type(self, t):
        if t == 1:
            return None
            return "all"
        elif t == 2:
            return "private"
        elif t == 9:
            return None
            return "stall"
        elif t == 4:
            return None
            return "party"
        elif t == 16:
            return None
            return "academy"
        elif t == 5:
            return None
            return "guild"
        elif t == 11:
            return None
            return "union"
        else:
            return None
            return "global"

    def run_thread(self, fnc, args, delay=1.0):
        Timer(delay, fnc, args).start()
