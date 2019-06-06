from WIFIServo import write_claw

def clawOpen():
    write_claw(1)

def clawClose():
    write_claw(0)
