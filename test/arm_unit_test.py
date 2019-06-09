from arm_interface import *
import arm_control.joint_trajectory_controller as jointHandler
from arm_description import jointMsg
import time as tm


def toLog(time, level, path, info):
    LEVEL = ["WARNING", "ERROR", "INFO"]
    print(time+" "+LEVEL[level]+" "+path+" "+info)

def unitTestInit():
    jointMsg jm = jointMsg("test")
    if init(jm, jointHandler) == True:
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 2
       info = "succeed"
    else: 
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 1
       info = "init unit test failed"
    
    print(toLog(time, level , "arm_interface", info))

    jointMsg jmWrong = jointMsg("testWrong")
    if init(jmWrong, jointHandler) == True:
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 1
       info = "init unit test failed"
    else: 
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 2
       info = "succeed"
        
    print(toLog(time, level , "arm_interface", info))

def unitTestLowerArmMove():
    jointMsg jm = jointMsg("test")
    init(jm, jointHandler)
    target = jointHandler.randomAvailable()
    lowerArmMove(target, jointHandler)
    if jointHander.pos.equal(target): 
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 2
       info = "succeed" 
    else:
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 1
       info = "lowerArmMove test failed"
        
    print(toLog(time, level , "arm_interface", info))
    
    target = jointHandler.randomUnreachable()
    try:
       lowerArmMove(target, jointHandler)
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 1
       info = "lowerArmMove test failed"
    finally:
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 2
       info = "succeed" 
        
    print(toLog(time, level , "arm_interface", info))

def unitTestUpperArmMove():
    jointMsg jm = jointMsg("test")
    init(jm, jointHandler)
    target = jointHandler.randomAvailable()
    upperArmMove(target, jointHandler)
    if jointHander.pos.equal(target): 
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 2
       info = "succeed" 
    else:
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 1
       info = "lowerArmMove test failed"
        
    print(toLog(time, level , "arm_interface", info))
    
    target = jointHandler.unreachable()
    try:
       upperArmMove(target, jointHandler)
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 1
       info = "lowerArmMove test failed"
    finally:
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 2
       info = "succeed" 
        
    print(toLog(time, level , "arm_interface", info))


if __name__ == "__main__":
    unitTestInit()
    unitTestLowerArmMove()
    unitTestupperArmMove()
    print("Unit Test Arm Succeed")
