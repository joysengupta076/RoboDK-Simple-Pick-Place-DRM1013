# RoboDK Python Intermediate file to generate robot programs.
# Program name: MainProgram
# This file requires the post processor: 
#   Doosan_Robotics
# to generate your robot program.
# This is a temporary file and you can delete it once you have generated your program.
# 
# Post processor documentation: https://robodk.com/doc/en/PythonAPI/postprocessor.html

import sys
import os
import robodk
sys.path.append(os.path.abspath(r"""D:/Program Files/RoboDK/Posts/""")) # temporarily add path to POSTS folder

from Doosan_Robotics import *

try:
  from robodk.robomath import PosePP as p
except:
  # This will be removed in future versions of RoboDK
  from robodk import PosePP as p


print('Total instructions: 16')
r = RobotPost(r"""Doosan_Robotics""",r"""Doosan Robotics M1013""",6, axes_type=['R','R','R','R','R','R'], native_name=r"""Doosan Robotics M1013""", ip_com=r"""127.0.0.1""", api_port=20500, prog_ptr=2206901808624, robot_ptr=2206861492368)

r.ProgStart(r"""MainProgram""")
r.RunMessage(r"""Program generated by RoboDK v5.7.0 for Doosan Robotics M1013 on 17/03/2024 17:31:31""",True)
r.RunMessage(r"""Using nominal kinematics.""",True)
r.RunCode(r"""PickPart1""", True)
r.RunCode(r"""PlacePart2""", True)
r.RunCode(r"""PickPart2""", True)
r.RunCode(r"""PlacePart1""", True)
r.ProgFinish(r"""MainProgram""")
r.ProgStart(r"""PickPart1""")
r.setFrame(p(415.013,-336.796,0,0,0,0),-1,r"""Part1""")
r.setTool(p(0,0,180,0,0,0),-1,r"""RobotiQ 2F-85 Gripper (Open)""")
r.MoveJ(p(-0.434452,3.50053e-06,143.032,-179.5,-1.00782,179.991),[-42.4099,7.51193,117.81,-0.825516,55.4254,-42.4371],[1,1,1])
r.MoveL(p(-2.36741,9.1564e-06,33.1571,-179.5,-1.00783,179.991),[-24.6505,40.6643,80.4288,-0.486236,59.8238,-24.9028],[1,1,1])
r.RunMessage(r"""Attach to RobotiQ 2F-85 Gripper (Open)""",True)
r.MoveL(p(-0.434452,3.50053e-06,143.032,-179.5,-1.00782,179.991),[-42.4099,7.51193,117.81,-0.825516,55.4254,-42.4371],[1,1,1])
r.ProgFinish(r"""PickPart1""")
r.ProgStart(r"""PlacePart2""")
r.setFrame(p(401.361,55.1346,0,0,0,0),-1,r"""Part2""")
r.MoveJ(p(9.83385,-4.20552,143.091,-179.5,-1.00783,179.991),[2.25445,-3.22369,129.085,0.0483108,55.1461,1.72643],[1,1,1])
r.MoveL(p(7.88914,-4.20552,32.5495,-179.5,-1.00783,179.991),[2.26498,6.0898,135.085,0.0621814,39.8319,1.71681],[1,1,1])
r.RunMessage(r"""Detach from RobotiQ 2F-85 Gripper (Open)""",True)
r.MoveL(p(9.83385,-4.20552,143.091,-179.5,-1.00783,179.991),[2.25445,-3.22369,129.085,0.0483108,55.1461,1.72643],[1,1,1])
r.ProgFinish(r"""PlacePart2""")
r.ProgStart(r"""PickPart2""")

raise Exception("""Your license does not allow generating programs with more than 50 lines of code. Upgrade your license to unlock this feature.""")


