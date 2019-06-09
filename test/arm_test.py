from arm_interface import *
import arm_control.joint_trajectory_controller as jointHandler
from arm_description import jointMsg
import time as tm


def toLog(time, level, path, info):
    LEVEL = ["WARNING", "ERROR", "INFO"]
    print(time+" "+LEVEL[level]+" "+path+" "+info)

def testUpperArmMove():
    jointMsg jm = jointMsg("test")
    init(jm, jointHandler)
    target = jointHandler.highest()
    upperArmMove(target, jointHandler)
    if jointHander.pos.equal(target): 
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 2
       info = "succeed" 
    else:
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 1
       info = "upperArmMove test failed"
        
    print(toLog(time, level , "arm_interface", info))

    target = jointHandler.lowest()
    upperArmMove(target, jointHandler)
    if jointHander.pos.equal(target): 
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 2
       info = "succeed" 
    else:
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 1
       info = "upperArmMove test failed"
        
    print(toLog(time, level , "arm_interface", info))
    
    target = jointHandler.randomUnreachable()
    try:
       upperArmMove(target, jointHandler)
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 1
       info = "upperArmMove test failed"
    finally:
       time = tm.strftime("%Y-%m-%d %H:%M:%S", tm.localtime())
       level = 2
       info = "succeed" 
        
    print(toLog(time, level , "arm_interface", info))

def testLowerArmMove():
    jointMsg jm = jointMsg("test")
    init(jm, jointHandler)
    target = jointHandler.highest()
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

    target = jointHandler.lowest()
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

if __name__ == "__main__":
    testLowerArmMove()
    testupperArmMove()
    print("Test Arm Succeed")
