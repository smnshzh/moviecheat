import streamlit as st
from moviepy.editor import VideoFileClip

# Page title
st.title('Video Downloader and Player')

# Video download section
st.header('Download Video')
video_link = st.text_input('Enter the video link:')
if st.button('Download'):
    if video_link:
        video = VideoFileClip(video_link)
        video.write_videofile("downloaded_video.mp4")
        st.success('Video downloaded successfully!')

