from openravepy import *
import time
env = Environment()
env.Load('../environment/rm_without_obstacle.env.xml')
env.SetViewer('qtcoin')
robot = env.GetRobots()[0]
current_pos = robot.GetDOFValues()
init_pos = current_pos
time.sleep(2)
current_pos[0]=0.01
current_pos[1]=0.01
robot.SetDOFValues(current_pos)
RaveSetDebugLevel(DebugLevel.Debug)
goal_pos = [0.01,0.01,0.0,1.15,1.2]
manipprob = interfaces.BaseManipulation(robot)
manipprob.MoveManipulator(goal=goal_pos)

robot.WaitForController(0)
time.sleep(5)
