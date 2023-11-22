#!/usr/bin/env python
# coding: utf-8

# # Task 1

# In[14]:


import subprocess

class VideoProcessor:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file

    def visualize_motion_vectors(self):
        # Use ffmpeg to generate a video with motion vectors visualization
        command = [
            "ffmpeg",
            "-i", self.input_file,
            "-vf", "drawgrid=w=iw/20:h=ih/20:t=green@1",
            "-c:v", "libx264",
            "-pix_fmt", "yuv420p",
            self.output_file
        ]

        # Run the ffmpeg command
        subprocess.run(command)

if __name__ == "__main__":
    # Reemplaza "input_video.mp4" con tu archivo de video de entrada
    input_file = r"C:\Users\MARIA\Downloads\BBB_9sec.mp4"

    # Reemplaza "output_visualized_video.avi" con el nombre de tu archivo de salida
    output_file = r"C:\Users\MARIA\Downloads\BBB_9sec_output.avi"

    # Crea una instancia de VideoProcessor
    video_processor = VideoProcessor(input_file, output_file)

    # Llama al método para visualizar vectores de movimiento
    video_processor.visualize_motion_vectors()


# # Task 2

# In[15]:


import subprocess
import os

def create_video_container(input_video_path, output_container_path):
    # Create a temporary directory to store intermediate files
    temp_dir = "temp_dir"
    os.makedirs(temp_dir, exist_ok=True)

    try:
        # Step 1: Cut the video into 50 seconds
        output_video_path = os.path.join(temp_dir, "cut_video.mp4")
        subprocess.run(['ffmpeg', '-i', input_video_path, '-t', '50', '-c', 'copy', output_video_path])

        # Step 2: Export video audio as MP3 mono track
        output_audio_mono_path = os.path.join(temp_dir, "audio_mono.mp3")
        subprocess.run(['ffmpeg', '-i', output_video_path, '-vn', '-ac', '1', '-q:a', '2', output_audio_mono_path])

        # Step 3: Export video audio in MP3 stereo with lower bitrate
        output_audio_stereo_path = os.path.join(temp_dir, "audio_stereo.mp3")
        subprocess.run(['ffmpeg', '-i', output_video_path, '-vn', '-q:a', '5', output_audio_stereo_path])

        # Step 4: Export video audio in AAC codec
        output_audio_aac_path = os.path.join(temp_dir, "audio_aac.aac")
        subprocess.run(['ffmpeg', '-i', output_video_path, '-vn', '-c:a', 'aac', '-strict', 'experimental', output_audio_aac_path])

        # Step 5: Package everything in an mp4 container
        subprocess.run(['ffmpeg', '-i', output_video_path, '-i', output_audio_mono_path, '-i', output_audio_stereo_path, '-i', output_audio_aac_path, '-c', 'copy', output_container_path])

    finally:
        # Cleanup: Remove the temporary directory and its contents
        if os.path.exists(temp_dir):
            for file in os.listdir(temp_dir):
                file_path = os.path.join(temp_dir, file)
                os.remove(file_path)
            os.rmdir(temp_dir)

# Exemple
input_video_path = r"C:\Users\MARIA\Downloads\BBB.mp4"
output_container_path = r"C:\Users\MARIA\Downloads\Lab3_BBB.mp4"
create_video_container(input_video_path, output_container_path)


# # Task 3

# In[16]:


import subprocess
import json

def get_track_count(mp4_file_path):
    try:
        # Run ffprobe to get information about the input MP4 file
        result = subprocess.run(['ffprobe', '-v', 'error', '-show_entries', 'stream=codec_type', '-select_streams', 'a', '-of', 'json', mp4_file_path], capture_output=True, text=True)

        # Parse the JSON output
        data = json.loads(result.stdout)

        # Count the audio tracks
        audio_track_count = len([stream for stream in data['streams'] if stream['codec_type'] == 'audio'])

        return audio_track_count

    except Exception as e:
        print(f"Error: {e}")
        return None

# Example usage:
mp4_file_path = r"C:\Users\MARIA\Downloads\Lab3_BBB.mp4"
track_count = get_track_count(mp4_file_path)

if track_count is not None:
    print(f"The MP4 container contains {track_count} audio track(s).")
else:
    print("Failed to determine the track count.")


# # Task 4

# In[23]:


#Executar per instalar youtube-d1

import subprocess

subprocess.run(['pip', 'install', 'youtube-dl'])


# In[9]:


import subprocess
import os
import requests

def subtitles(input_file, output_file):
    subtitles_url = 'https://github.com/mariagomez06/SCAV/blob/main/big_buck_bunny.eng.srt'
    subtitles_file = r"C:\Users\MARIA\Downloads\big_buck_bunny.eng.srt"
    response = requests.get(subtitles_url)
    
    if response.status_code == 200:
        with open(subtitles_file, 'wb') as file:
            file.write(response.content)
    else:
        print(f'Failed to download subtitles')
        return
    
    merge_command = [
        'ffmpeg',
        '-i', input_file,
        '-vf', f'subtitles={subtitles_file}',
        '-c:a', 'copy',
        output_file
    ]
    
    # Run the ffmpeg command
    subprocess.run(merge_command)

# Example usage:
input_file = r"C:\Users\MARIA\Downloads\BBB.mp4"
output_file = r"C:\Users\MARIA\Downloads\BBB_SUBTITLES.mp4"
subtitles(input_file, output_file)


# # Task 5

# In[ ]:


# Importante tener LAB1_SCAV_218011 en la misma carpeta que LAB2_SCAV_218011
import LAB2_SCAV_218011

input_file = r"C:\Users\MARIA\Downloads\Lab3_BBB.mp4" 

# Como ejemplo usaremos la función de get_video_info() con el container
LAB2_SCAV_218011.get_video_info(input_file)

