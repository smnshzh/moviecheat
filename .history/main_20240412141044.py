import streamlit as st
from moviepy.editor import VideoFileClip
import requests
# Page title
st.title('Video Downloader and Player')

# Video download section
st.header('Download Video')
video_link = st.text_input('Enter the video link:')
if st.button('Download'):
    if video_link:
        try:
            with st.spinner('Downloading...'):
                response = requests.get(video_link, stream=True)
                total_length = int(response.headers.get('content-length'))
                downloaded = 0
                with open("downloaded_video.mp4", "wb") as file:
                    for data in response.iter_content(chunk_size=1024):
                        downloaded += len(data)
                        file.write(data)
                        percentage = int(downloaded / total_length * 100)
                        st.progress(percentage)
                st.success('Video downloaded successfully!')
        except Exception as e:
            st.error(f"An error occurred during the download: {e}")

# Video player and search section
st.header('Search and Play Videos')

video_folder = "download/video"
video_files = [os.path.join(video_folder, file) for file in os.listdir(video_folder) if file.endswith('.mp4')]

search_query = st.text_input('Search for a video:')
filtered_videos = [video for video in video_files if search_query.lower() in video.lower()]
selected_video = st.selectbox('Select a video to play', options=filtered_videos)

if selected_video:
    st.video(open(selected_video, 'rb').read())