import moviepy.editor

video = moviepy.editor.VideoFileClip("Video.mp4")
audio = video.audio
audio.write_audiofile("Audio.mp3")

