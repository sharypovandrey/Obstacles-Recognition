#!/usr/bin/env python
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import Image
import numpy as np
import tensorflow as tf
from image_preprocessor import preprocess_image

# create publisher
pub = rospy.Publisher("/obstacles", String, queue_size=10)

# load model
model = tf.keras.models.load_model('../model/model.h5')
model._make_predict_function()


def callback_image_received(msg):
    rospy.logdebug("Image recieved: ", msg.header)
    # convert img to required shape for model
    img = preprocess_image(msg, msg.width, msg.height)
    input_arr = np.array([img])
    # make prediction is there obstacle on the image or not
    prediction = model.predict(input_arr)
    obstacle = "yes" if prediction[0][0] >= 0.5 else "no"
    # publish result to /obstacles topic
    pub.publish(String(obstacle))
    rospy.logdebug("Obstacle: " + obstacle)


def main():
    rospy.init_node("obstacle_detector")
    sub = rospy.Subscriber("/usb_cam/image_raw", Image, callback_image_received)
    rospy.spin()


if __name__ == "__main__":
    try:
        main()
    except rospy.ROSInterruptException as e:
        rospy.logdebug(e)
