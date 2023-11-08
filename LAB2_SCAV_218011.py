#!/usr/bin/env python
# coding: utf-8

# # Task 1
# 

# In[2]:


import subprocess

def convert_to_mp2(input_file, output_file):
    try:
        # Construct the ffmpeg command
        cmd = [
            'ffmpeg',
            '-i', input_file,  # Input video file
            '-c:v', 'mpeg2video',  # Codec for video
            '-b:v', '2M',  # Video bitrate (adjust as needed)
            '-f', 'mp2',  # Output format
            output_file
        ]

        # Run the ffmpeg command
        subprocess.run(cmd, check=True)

        print(f"Conversion successful. Output video saved as {output_file}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

input_video_file = r"C:\Users\MARIA\Downloads\BBB.mp4" 
output_video_file = r"C:\Users\MARIA\Downloads\BBB_mp2.mp2" 

convert_to_mp2(input_video_file, output_video_file)


# # Task 2 

# In[2]:


import subprocess

def modify_resolution(input_file, output_file, new_width, new_height):
    try:
        # Construct the ffmpeg command to change resolution
        cmd = [
            'ffmpeg',
            '-i', input_file,  # Input video file
            '-vf', f'scale={new_width}:{new_height}',  # Set new resolution
            output_file
        ]

        # Run the ffmpeg command
        subprocess.run(cmd, check=True)

        print(f"Resolution modification successful. Output video saved as {output_file}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Example usage:
input_video_file = r"C:\Users\MARIA\Downloads\BBB.mp4" 
output_video_file = r"C:\Users\MARIA\Downloads\BBB_resolucion.mp4"  
new_width = 640  # New width
new_height = 480  # New height

modify_resolution(input_video_file, output_video_file, new_width, new_height)


# # Task 3

# In[9]:


import subprocess

def change_chroma_subsampling(input_file, output_file, subsampling='4:2:2'):
    try:
        # Construct the ffmpeg command to change chroma subsampling
        cmd = [
            'ffmpeg',
            '-i', input_file,  # Input video file
            '-vf', f'format=yuv422p',  # Set chroma subsampling
            '-c:v', 'libx264',  # Video codec (change as needed)
            '-b:v', '2M',  # Video bitrate (adjust as needed)
            '-c:a', 'aac',  # Audio codec (change as needed)
            output_file
        ]

        # Run the ffmpeg command
        subprocess.run(cmd, check=True)

        print(f"Chroma subsampling modification successful. Output video saved as {output_file}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Example usage:
input_video_file = r"C:\Users\MARIA\Downloads\BBB.mp4" 
output_video_file = r"C:\Users\MARIA\Downloads\BBB_chromaSubsampling.mp4" 
new_subsampling = '4:2:2'  

change_chroma_subsampling(input_video_file, output_video_file, new_subsampling)


# # Task 4

# In[23]:


import subprocess
import json

def get_video_info(input_file):
    try:
        # Construir el comando ffprobe para obtener información del video
        cmd = [
            'ffprobe',
            '-v', 'error',
            '-select_streams', 'v:0',
            '-show_entries', 'stream=width,height,duration,bit_rate,codec_name,chroma_location',
            '-of', 'json',
            input_file
        ]

        result = subprocess.check_output(cmd, stderr=subprocess.STDOUT, universal_newlines=True)

        video_info = json.loads(result)

        print("Video Information:")
        print(f"Width: {video_info['streams'][0]['width']} pixels")
        print(f"Height: {video_info['streams'][0]['height']} pixels")
        print(f"Duration: {video_info['streams'][0]['duration']} seconds")
        print(f"Bit Rate: {video_info['streams'][0]['bit_rate']} bps")
        print(f"Codec: {video_info['streams'][0]['codec_name']}")
        print(f"Chroma Location: {video_info['streams'][0]['chroma_location']}")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred: {e}")

# Ejemplo de uso:
input_video_file = r"C:\Users\MARIA\Downloads\BBB.mp4" 
get_video_info(input_video_file)


# # Task 5

# In[29]:


# Importante tener LAB1_SCAV_218011 en la misma carpeta que LAB2_SCAV_218011
import LAB1_SCAV_218011

from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip
from PIL import Image

# Extraemos un frame (el 10, por ejemplo) del video BBB
def extract_tenth_frame(input_video, output_image):
    try:
        video_clip = VideoFileClip(input_video)
        frame = video_clip.get_frame(10)  # Obtenemos el frame número 10 

        image = Image.fromarray(frame)  # Convierte el frame 10 en un objeto de imagen Pillow
        image.save(output_image, 'JPEG')  # Guarda la imagen como formato JPEG

        print(f"Décimo fotograma extraído y guardado como {output_image}")

    except Exception as e:
        print(f"Ocurrió un error: {e}")


# Ejemplo:
input_video_file =  r"C:\Users\MARIA\Downloads\BBB.mp4" 
output_image_file =  r"C:\Users\MARIA\Downloads\frame.jpg" 

extract_tenth_frame(input_video_file, output_image_file)

# Usamos el frame extraido anteriormente y lo pasamos a blanco y negro con funciones del lab anterior
input_file = r"C:\Users\MARIA\Downloads\frame.jpg" 
output_file = r"C:\Users\MARIA\Downloads\frame_bw.jpg" 

LAB1_SCAV.convert_to_bw_and_compress(input_file, output_file);


# In[ ]:




