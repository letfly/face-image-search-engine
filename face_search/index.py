# import the necessary packages
from pyimagesearch.colordescriptor import ColorDescriptor
import argparse
import glob
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
#print ap  #ArgumentParser(prog='index.py', usage=None, description=None, version=None, formatter_class=<class 'argparse.HelpFormatter'>, conflict_handler='error', add_help=True)
ap.add_argument("-d", "--dataset", required = True,
	help = "Path to the directory that contains the images to")
#print ap.parse_args()  #Namespace(dataset='dataset')
ap.add_argument("-i", "--index", required = True,
	help = "Path to where the computed index will be Stored")
#print ap.parse_args()  #Namespace(dataset='dataset', index='index.csv')

args = vars(ap.parse_args())
#print args  #{'index': 'index.csv', 'dataset': 'dataset'}

# initialize the color descriptor
cd = ColorDescriptor((8, 12, 3))

# open the output index file for writing
output = open(args["index"], "w")
#print output  #<open file 'index.csv', mode 'w' at 0x7f3d30b66540>

# use glob to grab the image path and loop over them
for imagePath in glob.glob(args["dataset"] + "/*.png"):
	# extract the image ID (i.e. the unique filename) from
	# path and load the image itself
	#print glob.glob(args["dataset"]+"/*.png")  #return path of images
	#print imagePath  #dataset/107701.png
	imageID = imagePath[imagePath.rfind("/") + 1:]
	#print imagePath.rfind("/")#7
	#print imageID  #107701.png
	image = cv2.imread(imagePath)
	#print image

	# describe the image
	features = cd.describe(image)
	#print features;break

	#write the features to file
	features = [str(f) for f in features]
	output.write("%s,%s\n" % (imageID, ",".join(features)))

# close the index file
output.close()
