#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import sys


def move_circle_turtle(linear_vel, angular_vel):
	rospy.init_node('turtlemove', anonymous=True)
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rate = rospy.Rate(10)

	vel = Twist()

	while True:

		vel.linear.x = linear_vel
		vel.linear.y = 0
		vel.linear.z = 0

		vel.angular.x = 0
		vel.angular.y = 0
		vel.angular.z = angular_vel

		pub.publish(vel)
		rate.sleep()

move_circle_turtle(4.0,4.0)

		


