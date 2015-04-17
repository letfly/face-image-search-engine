# import the necessary packages
import numpy as np
import cv2

class ColorDescriptor:
	def __init__(self, bins):
		# Store the number of bins for the 3D histogram
		self.bins = bins
	
	def describe(self, image):
		# Convert the image to the HSV color space and initialize
		# the feature used to quantify the image
		#return cv2.COLOR_RGB2HSV  #41
		image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
		return image.shape
		feature = []

		# grab the dimensions and compute the center of the image
		(h, w) = image.shape[:2]
		#return h,w  #(300, 400)

		(cX, cY) = (int(w*0.5), int(h*0.5))

		# divide the image into four rectangles/segments (top-left,
		# top-right, bottom-right, bottom-left)
		segments = [(0, cX, 0, cY), (cX, w, 0, cY), (cX, w, cY, h),
					(0, cX, cY, h)]
		
		# construct an elliptical mask representing the center of the
		# image
		(axesX, axesY) = (int(w*0.75)/2, int(h*0.75)/2)
		#return axesX,axesY  #(150, 112)
		
		ellipMask = np.zeros(image.shape[:2], dtype = 'uint8')
		#return ellipMask  #uint8 = unsigned int
		cv2.ellipse(ellipMask, (cX, cY), (axesX, axesY), 0, 0, 360, 255, -1)

		# loop over the segments
		for (startX, endX, startY, endY) in segments:
			# construct a mask for each corner of the image, subtracting the elliptical center from it
			#return segments
			cornerMask = np.zeros(image.shape[:2], dtype = 'uint8')
			cv2.rectangle(cornerMask, (startX, startY), (endX, endY), 255, -1)
			# extract a color histogram from the image, then update 
			# the feature vector
			hist = self.histogram(image, cornerMask)
			return hist
			feature.extend(hist)

	def histogram(self, image, mask):
		# extract a 3D color histogram from the masked region on the
		# image, using the supplied number of bins per channel; then
		# normalize the histogram
		hist = cv2.calcHist([image], [0, 1, 2], mask, self.bins,
							[0, 180, 0, 256, 0, 256])
		hist = cv2.normalize(hist).flatten()

		# return the histogram
		return hist
