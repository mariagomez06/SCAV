#!/usr/bin/env python
# coding: utf-8

# # Lab 1: JPEG & MPEG

# Maria Gómez - 218011

# # Task 1

# In[ ]:


def rgb_to_yuv():

    print('Inserta un valor R: ')
    R = float(input());
    print('Inserta un valor G: ')
    G = float(input());
    print('Inserta un valor B: ')
    B = float(input());

    # fòrmules vistes a teoria
    Y = 0.257 * R + 0.504 * G + 0.098 * B + 16;
    U = -0.148 * R - 0.291 * G + 0.439 * B + 128;
    V = 0.439 * R - 0.368 * G - 0.071 * B + 128;
    
    print(Y, U, V)

def yuv_to_rgb():
    
    print('Inserta un valor Y: ')
    Y = float(input());
    print('Inserta un valor U: ')
    U = float(input());
    print('Inserta un valor V: ')
    V = float(input());
    
    # fòrmules vistes a teoria
    R = 1.164 * (Y - 16)  + 1.596 * (V - 128);
    G = 1.164 * (Y - 16)  - 0.813 * (V - 128) - 0.391 * (U - 128);
    B = 1.164 * (Y - 16)  + 2.018 * (U - 128);
    
    print(R, G, B) 


# In[7]:


# exemple
rgb_to_yuv()


# In[8]:


# exemple
yuv_to_rgb()


# # Task 2

# In[16]:


import subprocess

def resize_and_reduce_quality(input_file, output_file, width, height, quality):
    
    # Utilitzem ffmpeg per reduïr i redimensionar la imatge
    cmd = [
        'ffmpeg',
        '-i', input_file,           # imatge d'input
        '-vf', f'scale={width}:{height}',  # redimensionem 
        '-q:v', str(quality),        # regulem la qualitat (valors de 0-51, 0 es la millor qualitat)
        output_file                 # imatge d'output
    ]

    try:
        subprocess.run(cmd, check=True)
        print(f'Successfully resized and reduced quality: {input_file} -> {output_file}')
    except subprocess.CalledProcessError as e:
        print(f'Error: {e}')
        


# In[17]:


# exemple
input_file = r"C:\Users\MARIA\OneDrive\Escritorio\tortuga.jpg"
output_file = r"C:\Users\MARIA\OneDrive\Escritorio\output.jpg"
width = 800  # nou width
height = 600  # nou height
quality = 20  # qualitat desitjada

resize_and_reduce_quality(input_file, output_file, width, height, quality)


# # Task 3

# In[28]:


def serpentina(file_path):
    try:
        with open(file_path, 'rb') as file:
            byte_count = 0
            zigzag = 1  # direcció inicial de zig-zag, 1 d'esquerra a dreta, -1 de dreta a esquerra

            while True:
                byte = file.read(1)
                if not byte:
                    break

                # processem el byte
                # print(byte) # descomentar aquesta linea per veure tots els bytes que llegeix
                byte_count += 1

                # actualitzem la direcció del zigzag
                zigzag *= -1

        print(f"Total bytes read: {byte_count}")
    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"Error: {e}")

# exemple
file_path = r"C:\Users\MARIA\OneDrive\Escritorio\tortuga.jpg"

serpentina(file_path)


# # Task 4

# In[29]:


import subprocess

def convert_to_bw_and_compress(input_file, output_file):
    try:
        # usem ffmpeg per convertir la imatge a blanc i negre i comprimir-la
        ffmpeg_command = [
            'ffmpeg',
            '-i', input_file,
            '-vf', 'format=gray',
            '-q:v', '0',  # compressió màxima (0 és la màxima compressió)
            output_file
        ]

        subprocess.run(ffmpeg_command, check=True)
        print(f'Successfully converted and compressed: {input_file} -> {output_file}')
        
    except Exception as e:
        print(f'An error occurred: {e}')
        
        
# exemple
input_file = r"C:\Users\MARIA\OneDrive\Escritorio\tortuga.jpg"
output_file = r"C:\Users\MARIA\OneDrive\Escritorio\output_bw.jpg"

convert_to_bw_and_compress(input_file, output_file)


# # Task 5 

# In[31]:


def run_length_encoding(data):
    if not data:
        return bytes()

    encoded_data = bytearray()
    current_byte = data[0]
    count = 1

    for byte in data[1:]:
        if byte == current_byte:
            count += 1
        else:
            encoded_data.append(count)
            encoded_data.append(current_byte)
            current_byte = byte
            count = 1

    encoded_data.append(count)
    encoded_data.append(current_byte)

    return bytes(encoded_data)

def run_length_decoding(data):
    if not data:
        return bytes()

    decoded_data = bytearray()
    i = 0

    while i < len(data):
        count = data[i]
        value = data[i + 1]
        decoded_data.extend([value] * count)
        i += 2

    return bytes(decoded_data)

# exemple
original_data = bytes([1, 1, 1, 2, 2, 3, 3, 3, 4, 4])
encoded_data = run_length_encoding(original_data)
decoded_data = run_length_decoding(encoded_data)

print("Original Data:", original_data)
print("Encoded Data:", encoded_data)
print("Decoded Data:", decoded_data)


# # Task 6

# In[34]:


import numpy as np
from scipy.fftpack import dct, idct

class DCTDecoder:
    def __init__(self):
        self.block_size = 8

    def decode(self, input_data):
        # converteix les dades d'entrada en un array 2D
        input_data = np.array(input_data).reshape(-1, self.block_size)

        # aplica DCT a cada bloc
        dct_blocks = dct(dct(input_data.T, norm='ortho').T, norm='ortho')

        # fem la inversa DCT per obtenir les dades originals
        output_data = idct(idct(dct_blocks.T, norm='ortho').T, norm='ortho')

        # converteix les dades de sortida a un array 1D
        output_data = output_data.reshape(-1)

        return output_data.tolist()


# In[35]:


# exemple
decoder = DCTDecoder()

input_data = [231, 32, 233, 161, 24, 71, 140, 245,
              8, 213, 98, 114, 248, 128, 199, 242,
              58, 210, 228, 24, 188, 252, 152, 125,
              67, 87, 149, 56, 12, 35, 201, 18,
              146, 248, 70, 234, 121, 242, 223, 183,
              194, 52, 143, 156, 247, 249, 252, 57]

# decofica l'entrada
output_data = decoder.decode(input_data)

# impremix les dades codificades
print(f"Dades codificades: {output_data}")


# In[ ]:




