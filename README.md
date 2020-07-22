### How does it works

First, let us see how a slow-motion video works. Generally, when we capture or shoot a video, it is nothing but a series of pictures (or frames) in a short span of time. The video we take is normally in 25 or 60 frames per second. But when we take a Slow motion video it will be in 240 or more frames per second. What this means is that more the frames slower will be the video. Creating a slow-motion video depends on the capability of the camera, whether it can capture a video in higher fps or not.

### Execution 

>>> python G:\SlowMotion\Super-SloMo-master\video_to_slomo.py --ffmpeg G:\SlowMotion\ffmpeg-20190716-806ac7d-win64-static\bin\ --video G:\SlowMotion\SampleVideo.mp4 --sf 4 --checkpoint G:\SlowMotion\Super-SloMo-master\SuperSloMo.ckpt --fps 120 --output G:\SlowMotion\newVideo120.mp4 --batch_size 1

If you want you can change the fps in your command to make the video slower. (Higher the fps slower the video will be)

