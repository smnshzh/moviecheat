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

# Video player and search section
st.header('Search and Play Videos')

video_folder = "download/video"
video_files = [os.path.join(video_folder, file) for file in os.listdir(video_folder) if file.endswith('.mp4')]

search_query = st.text_input('Search for a video:')
filtered_videos = [video for video in video_files if search_query.lower() in video.lower()]
selected_video = st.selectbox('Select a video to play', options=filtered_videos)

if selected_video:
    st.video(open(selected_video, 'rb').read())