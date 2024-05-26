import cv2
import os

# Get video from specified path
video = cv2.VideoCapture('bad_apple_video.mp4')

# Creates folder named bad_apple_frames
try: 
	if not os.path.exists("bad_apple_frames"): 
		os.makedirs("bad_apple_frames") 

# 
except OSError: 
	print ("Error creating file director named bad_apple_frames.") 

# Frame number
current_frame = 0

while(True): 
	
	# Reading from frame
	ret,frame = video.read() 

	if ret: 
		# If video is still playing continue creating images
		name = "./bad_apple_frames/frame" + str(current_frame) + ".jpg"
		print ("Creating..." + name) 

		# Writing the extracted images 
		cv2.imwrite(name, frame) 

		# Increasing frame count to show how many total frames have been created
		current_frame += 1
	else: 
		break

# Release all space and windows once done 
video.release() 
cv2.destroyAllWindows() 