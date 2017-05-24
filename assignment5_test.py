import numpy as np
import cv2
import unittest

from assignment5 import imageGradientX
from assignment5 import imageGradientY
from assignment5 import computeGradient

class Assignment5Test(unittest.TestCase):
    def setUp(self):
        self.testImage = cv2.imread("test_image.jpg", cv2.IMREAD_GRAYSCALE)

        if self.testImage == None:
            raise IOError("Error, image test_image.jpg not found.")
    
    def test_imageGradientX(self):
        gradientX = imageGradientX(self.testImage)
        self.assertEqual(type(gradientX),
                         type(self.testImage))
        print "\n\nSUCCESS: imageGradientX returns the correct output type.\n"
        cv2.imwrite("test_image_gradientX.jpg", gradientX)

    def test_imageGradientY(self):
        gradientY = imageGradientY(self.testImage)
        self.assertEqual(type(gradientY),
                         type(self.testImage))
        print "\n\nSUCCESS: imageGradientY returns the correct output type.\n"
        cv2.imwrite("test_image_gradientY.jpg", gradientY)

    def test_computeGradient(self):
        avg_kernel = np.ones((3, 3)) / 9

        gradient = computeGradient(self.testImage, avg_kernel)
        # Test the output.
        self.assertEqual(type(gradient), type(self.testImage))
        # Test 
        self.assertEqual(gradient.shape, self.testImage.shape)
        
        print "\n\nSUCCESS: computeGradient returns the correct output type.\n"
        
        cv2.imwrite("test_image_computeGradient.jpg", gradient)
if __name__ == '__main__':
	unittest.main()
