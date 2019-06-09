import arm_control.joint_trajectory_controller as jointHandler

def init(jointMsg, jointHandler):
    # check joint message
    if jointHandler.check(jointMsg) == False):
        return False

    jointHander.init()
    # check TF-Tree
    if not jointHandler.TFtree.valid():
        return False
    return True

def lowerArmMove(target, jointHandler):
    init()
    for location in target:
        jointHandler.desire_state.enQueue(location)
    jointHandler.plan_upper.setFalse()
    jointHandler.plan_lower.setTrue()

    for location in jointHandler.queue:
    jointHandler.updateCommand(
        jointHandler.calTime(),     # time
        jointHandler.calDuration(), # period
        jointHandler.cur_target,
        jointHander.error_Handler
    )
    return jointHandler.starting()

def upperArmMove(target, jointHandler):
    init()
    for location in target:
        jointHandler.desire_state.enQueue(location)
    jointHandler.plan_upper.setTrue()
    jointHandler.plan_lower.setFalse()

    for location in jointHandler.queue:
    jointHandler.updateCommand(
        jointHandler.calTime(),     # time
        jointHandler.calDuration(), # period
        jointHandler.cur_target,
        jointHander.error_Handler
    )
    return jointHandler.starting()

