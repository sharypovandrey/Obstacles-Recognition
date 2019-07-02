import cv2
import numpy as np
from cv_bridge import CvBridge, CvBridgeError

stereo_image_width = 320
image_height = 120
image_width = int(stereo_image_width / 2)


def check_frame_sizes(w, h):
    assert (w == 2560 and h == 720) or \
	(w == 1280 and h == 480) or \
	(w == 640 and h == 240), \
	"ImageSizeError, width is {}, height is {}. It should be one of the next sizes: 2560x720, 1280x480, 640x240".format(w, h)


def preprocess_image(image_msg, width, height):

    check_frame_sizes(width, height)
    # TODO: add method for frame resizing with different proportions

    # convert ROS Image to OpenCV frame
    bridge = CvBridge()
    try:
	    cv_frame = bridge.imgmsg_to_cv2(image_msg, "rgb8")
    except CvBridgeError as e:
	    print e

    # RGB to to gray, to reduce dimensions
    gray = cv2.cvtColor(cv_frame, cv2.COLOR_RGB2GRAY)

    # resize frame for faster recognition
    resized_frame = cv2.resize(gray, (stereo_image_width, image_height))

    # stereo image from camera is just combination of two images
    # thats why size of the image is 640x240
    # if to split this image we get left and right cameras images
    split = np.split(resized_frame, 2, axis=1)
    left = split[0]
    right = split[1]
    abs_dif = np.abs(np.subtract(left, right))
    concatenated_img = np.dstack((left, right, abs_dif))

    return concatenated_img.astype("float32")
