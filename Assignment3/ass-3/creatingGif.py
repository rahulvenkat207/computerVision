import cv2
import numpy as np
import random
from moviepy.editor import VideoFileClip

## video settings
frame_width = 640  
frame_height = 480  
fps = 10  
num_frames_per_letter = 10  
total_letters = 9
num_frames = total_letters * num_frames_per_letter  # Total frames in the video

text_good_x=122
text_good_y=190
text_times_x=94
text_times_y=340

font = cv2.FONT_HERSHEY_SIMPLEX
font_scale = 5
thickness = 6

words = ["Good", "Times"]

# HSV to RGB conversion function
def hsv_to_rgb(h, s, v):
   rgb_color = cv2.cvtColor(np.uint8([[[h, s, v]]]), cv2.COLOR_HSV2BGR)[0][0]
   blue = int(rgb_color[0])
   green = int(rgb_color[1])
   red = int(rgb_color[2])
   return (blue, green, red)


def random_hue():
    return random.randint(0, 179), 200, 255

output_path = 'slower_blinking_letter_and_background.mp4'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
out = cv2.VideoWriter(output_path, fourcc, fps, (frame_width, frame_height))

# Initialize letter colors
letter_colors = []

for i in range(num_frames):
    """I think many have seen this implementation in circular queue to  ensures that after
     reaching the last letter, it cycles back to the first."""
    letter_index = (i // num_frames_per_letter) % total_letters

   
    
    # Change the background color every 10 frames
    if i % num_frames_per_letter == 0:
        h, s, v = random_hue()
        background_color = hsv_to_rgb(h, s, v)

        letter_colors = []

        for j in range(total_letters):
            if j == letter_index:
                letter_colors.append(hsv_to_rgb(*random_hue()))
            else:
                letter_colors.append((255, 255, 255))

    frame = np.full((frame_height, frame_width, 3), background_color, dtype=np.uint8)



    """For Good - words[0]"""
    x = text_good_x
    for j, letter in enumerate(words[0]):
        letter_color = letter_colors[j]  
        cv2.putText(frame, letter, (x, text_good_y), font, font_scale, letter_color, thickness)
        letter_size = cv2.getTextSize(letter, font, font_scale, thickness)[0]
        x += letter_size[0]  

    """For times"""
    x = text_times_x
    for j, letter in enumerate(words[1]):
        letter_color = letter_colors[len(words[0]) + j] 
        cv2.putText(frame, letter, (x, text_times_y), font, font_scale, letter_color, thickness)
        letter_size = cv2.getTextSize(letter, font, font_scale, thickness)[0]
        x += letter_size[0]  

    """Instead of two for loop we can also simply this by writing one fuc for this"""
   
    out.write(frame)


out.release()



# Convert video to GIF
vedioclip = VideoFileClip(output_path)
output_gif_path = "output.gif"
vedioclip.write_gif(output_gif_path, fps=fps)

print(f"Gif saved as {output_gif_path}")

