#ARES Engine Control Software

def fill():
    #TODO Wills
    safety_check()

def start_up():
#TODO Greg
def safety_check():
    #TODO Jon
    if read_pressure(1) >= 626:
        return 1
    else:
        return 0
    # TODO research voting systems
    if read_pressure(2) >= 525:
        return 1
    else:
        return 0
    if read_pressure(3) >= 25:
        return 0
    else:
        return 1


def shut_down():
#TODO Greg
def lox_valve(signal):
#TODO Sean and AJ
def met_valve(signal):
#TODO Sean and AJ
def engine_operation():
#TODO Greg
def vote():
#TODO Greg
def read_temperature():
#TODO Grant
def read_pressure(loc)
#TODO Grant
    if loc == 1:
        p_list = [636,625,611]
        vote(p_list)
    elif loc == 2:
        p_list = [535, 520, 515]
    elif loc == 3:
        p_list = [25, 30, 27]

def main():
#TODO Greg