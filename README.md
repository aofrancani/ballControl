# Ball Control with Optical Flow

This is a game in which you can control a ball using your webcam and your body movements or fingers. The position of the ball is given by the optical flow of the movements in the camera.

<img src="gif/ball_control.gif" width="400"/> <img src="gif/ball_control_with_optical_flow.gif" width="400"/> 

I was studying Optical Flow and I remembered a game where a guy controlled a ball with his fingers. I decided to implement it by myself using the dense optical flow using Gunnar Farneback's algorithm implemented on OpenCV. The goal of this game was to explore and understand the features of this algorithm.

This code was highly inspired by Chapter 10 of "Solem, Jan Erik. *Programming Computer Vision with Python: Tools and algorithms for analyzing images*. "O'Reilly Media, Inc.", 2012.". 

To test the code on your own computer with a webcam, just run the following command on your command prompt or terminal:

```
python ball_control.py
```

I hope you like it :)
