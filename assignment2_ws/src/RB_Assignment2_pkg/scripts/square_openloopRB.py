#Citation : This code has been derived based on the move in straight line and make a turn code in the ROS website

#!/usr/bin/env python3
import rospy
from geometry_msgs.msg import Twist
import math

def turtle_square(speed,spin):
    # Starts a new node
    rospy.init_node('turtlesim', anonymous=True)
    #Define the publisher
    pub = rospy.Publisher('/turtle1/cmd_vel',Twist, queue_size=10)
    rate = rospy.Rate(10)
    vel = Twist()
    current_distance = 0 # Current Distance Travelled
    
    ti = rospy.Time.now().to_sec() # Time before Start of Maneouver
    
    #first side of square
    while(current_distance <= 2):

      
       
        vel.linear.x = speed
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
        pub.publish(vel)  # publishes the velocity value
        tf=rospy.Time.now().to_sec()  # Time Elapsed
        current_distance = speed*(tf-ti)
     
    vel.linear.x = 0 # Setting the Linear Velocity back to 0
    pub.publish(vel)


     # First 90 degree Rotation      
    current_angle= 0
    ti = rospy.Time.now().to_sec() # Time before Start of Maneouver
    
                
    while(current_angle<=(math.radians(90))): # angle is in degree
            
        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = spin
            
        pub.publish(vel)
        tf = rospy.Time.now().to_sec() # Time Elapsed
        current_angle = spin*(tf-ti) # current angle
        
    vel.angular.z = 0 # Setting the rotation angle back to 0
    pub.publish(vel)
    
    #Second side of square
    
    current_distance = 0
    ti = rospy.Time.now().to_sec() 
    while(current_distance <= 2):

      
       
        vel.linear.x = speed
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
     
        pub.publish(vel) 
            
        tf=rospy.Time.now().to_sec()
            
        current_distance = speed*(tf-ti)
     
     
    vel.linear.x = 0
    pub.publish(vel)


    #Second 90 degree turn    
    current_angle= 0
    ti = rospy.Time.now().to_sec()
    
                
    while(current_angle<=(math.radians(90))):
            
        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = spin
            
        pub.publish(vel)
        tf = rospy.Time.now().to_sec()
        current_angle = spin*(tf-ti)
        
    vel.angular.z = 0
    pub.publish(vel)
    
    #Third side of square
    
    current_distance = 0
    ti = rospy.Time.now().to_sec() 
    while(current_distance <= 2):

      
       
        vel.linear.x = speed
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
     
        pub.publish(vel) 
            
        tf=rospy.Time.now().to_sec()
            
        current_distance = speed*(tf-ti)
     
     
    vel.linear.x = 0
    pub.publish(vel)


    #Third 90 degree turn        
    current_angle= 0
    ti = rospy.Time.now().to_sec()
    
                
    while(current_angle<=(math.radians(90))):
            
        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = spin
            
        pub.publish(vel)
        tf = rospy.Time.now().to_sec()
        current_angle = spin*(tf-ti)
        
    vel.angular.z = 0
    pub.publish(vel)
    
    #Fourth side of square
    current_distance = 0
    ti = rospy.Time.now().to_sec() 
    while(current_distance <= 2):
      
       
        vel.linear.x = speed
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = 0
     
        pub.publish(vel) 
            
        tf=rospy.Time.now().to_sec()
            
        current_distance = speed*(tf-ti)
     
     
    vel.linear.x = 0
    pub.publish(vel)
      
    #Fourth 90 degree turn        
    current_angle= 0
    ti = rospy.Time.now().to_sec()
    
                
    while(current_angle<=(math.radians(90))):
            
        vel.linear.x = 0
        vel.linear.y = 0
        vel.linear.z = 0
        vel.angular.x = 0
        vel.angular.y = 0
        vel.angular.z = spin
            
        pub.publish(vel)
        tf = rospy.Time.now().to_sec()
        current_angle = spin*(tf-ti)
        
    vel.angular.z = 0
    pub.publish(vel)  
    
if __name__ == '__main__':
    try:
        #Testing our function
        turtle_square(0.2,0.2)
        
    except rospy.ROSInterruptException: pass

