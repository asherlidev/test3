websoc=None
def get_web_socket(sock):
    global websoc
    websoc=sock
def retr_web_soc():
    return websoc