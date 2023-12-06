#!/usr/bin/env python
# coding: utf-8

# In[ ]:


FROM alpine:latest

RUN apk --no-cache add ffmpeg

WORKDIR /app
COPY your_python_script.py 

CMD ["python", "LAB4_GUI.py"]

docker build -t ffmpeg-container 

# Reemplazar /Users/MARIA/Downloads con tu path
docker run -v /Users/MARIA/Downloads:/app -it ffmpeg-container

