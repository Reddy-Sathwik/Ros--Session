#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import time

def move_turtle():
    # Initialize the ROS node
    rospy.init_node('move_turtle_rectangle_node', anonymous=True)

    # Create a publisher to send velocity commands to the turtle
    velocity_publisher = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)

    # Create a Twist message to control linear and angular velocities
    vel_msg = Twist()

    # Define a function to move the turtle forward
    def move_forward(distance, speed):
        vel_msg.linear.x = speed
        vel_msg.angular.z = 0.0
        duration = distance / speed
        t_start = time.time()
        while time.time() - t_start < duration and not rospy.is_shutdown():
            velocity_publisher.publish(vel_msg)
            rospy.sleep(0.1)
        vel_msg.linear.x = 0.0
        velocity_publisher.publish(vel_msg)

    # Define a function to rotate the turtle 90 degrees
    def turn(angle_speed):
        vel_msg.linear.x = 0.0
        vel_msg.angular.z = angle_speed
        duration = 1.57 / abs(angle_speed)  # Rotate 90 degrees (1.57 radians)
        t_start = time.time()
        while time.time() - t_start < duration and not rospy.is_shutdown():
            velocity_publisher.publish(vel_msg)
            rospy.sleep(0.1)
        vel_msg.angular.z = 0.0
        velocity_publisher.publish(vel_msg)

    rospy.loginfo("Moving the turtle in a rectangle...")

    # Parameters for the rectangle
    length = 2.0  # Length of the rectangle
    width = 1.0   # Width of the rectangle
    speed = 1.0   # Speed of forward motion
    angle_speed = 0.5  # Speed of rotation

    # Move in a rectangular pattern (4 sides)
    for _ in range(2):
        move_forward(length, speed)
        turn(angle_speed)
        move_forward(width, speed)
        turn(angle_speed)

if __name__ == '__main__':
    try:
        # Call the function to move the turtle in a rectangle
        move_turtle()
    except rospy.ROSInterruptException:
        pass
