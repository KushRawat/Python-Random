#pip install moviepy
import moviepy.editor
#replace parameter with location of video
video = moviepy.editor.VideoFileClip(r"location\xyz.mp4")
audio = video.audio
#Replace parameter with location of audio along with filename
audio.write_audiofile(r"location\xyz.mp3") #r makes the code raw to avoid unicode error