from arm_interface import *
import arm_control.joint_trajectory_controller as jointHandler
import time as tm


def toLog(time, level, path, info):
    LEVEL = ["WARNING", "ERROR", "INFO"]
    print(time+" "+LEVEL[level]+" "+path+" "+info)

def unitTestClawOpen():
    clawClose()
    clawOpen()
    if jointHander.clawstate == 1: 
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 2
       info = "succeed" 
    else:
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 1
       info = "lowerArmMove test failed"
        
    print(toLog(time, level , "arm_interface", info))

def unitTestClawClose():
    clawOpen()
    clawClose()
    if jointHander.clawstate == 0: 
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 2
       info = "succeed" 
    else:
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 1
       info = "lowerArmMove test failed"
        
if __name__ == "__main__":
    unitTestClawOpen()
    unitTestClawClose()
    print("Unit Test Claw Succeed")
