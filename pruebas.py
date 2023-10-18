from vimeo_downloader import Vimeo

# Replace these two variables to different URL to download that video

vimeo_url = 'https://player.vimeo.com/video/771975263'
embedded_on = 'https://learning.tokioschool.com/mod/videotime/view.php?id=17330'
# embedded_on is  the URL of site video is embedded on without query parameters.

v = Vimeo(vimeo_url, embedded_on)

stream = v.streams  # List of available streams of different quality
# >> [Stream(240p), Stream(360p), Stream(540p), Stream(720p), Stream(1080p)]

# Download best stream
stream[-1].download(download_directory='video', filename='test_stream')

# Download video of particular quality, example '540p'
for s in stream:
    if s.quality == '540p':
        s.download(download_directory='video', filename='test_stream')
        break
else:  # If loop never breaks
    print("Quality not found")