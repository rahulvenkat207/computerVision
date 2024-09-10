import cv2
import numpy as np
import random
from moviepy.editor import VideoFileClip
# Define video settings
frame_width = 640  # Width of the video frame
frame_height = 480  # Height of the video frame
fps = 0.1 # Frames per second 
num_frames = 15 # Total number of frames in the video

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 5
thickness = 6

words = ["Good", "Times"]

# Color generator function
def random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))


output_path = 'blinking_good_times_video.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')  
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))


for i in range(num_frames):
    # Create a blank background with a random color
    background_color = random_color()
    frame = np.full((frame_height, frame_width, 3), background_color, dtype=np.uint8)

    
    text = words[i % 2]  

    # Choose a random color for the text
    text_color = random_color()

    # Get the text size to calculate the centered position
    text_size = cv2.getTextSize(text, font, font_scale, thickness)[0]
    text_x = (frame_width - text_size[0]) // 2 
    text_y = (frame_height + text_size[1]) // 2  

    # Add the text to the frame
    cv2.putText(frame, text, (text_x, text_y), font, font_scale, text_color, thickness)

    #
    out.write(frame)


out.release()

print(f"Video saved as {output_path}")

vedioclip =  VideoFileClip(output_path)

output_gif_path = "blinking_good_times.gif"
vedioclip.write_gif(output_gif_path,fps = fps)

print(f"Gif saved as {output_gif_path }")