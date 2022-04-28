import cv2
import numpy as np
from ball import Ball


def draw_flow(img, flow, step=10):
    """
    Plot optical flow at sample points spaced step pixels apart.
    """
    h, w = img.shape[:2]
    y, x = np.mgrid[step / 2:h:step, step / 2:w:step].reshape(2, -1).astype(int)
    fx, fy = flow[y, x].T

    # create line endpoints
    lines = np.vstack([x, y, x + fx, y + fy]).T.reshape(-1, 2, 2)
    lines = np.int32(lines)

    # create image and draw
    vis = img.copy()

    for (x1, y1), (x2, y2) in lines:
        cv2.arrowedLine(vis, pt1=(x1, y1), pt2=(x2, y2), color=(255, 0, 0), thickness=1)
    return vis


def draw_ball(img, ball_position):
    """
    Plot ball in img at a given position
    """
    (xc, yc) = ball_position
    im = img.copy()
    cv2.circle(im, center=(xc, yc), radius=12, color=(0, 140, 255), thickness=-1)
    cv2.circle(im, center=(xc, yc), radius=12, color=(0, 0, 0), thickness=2)
    return im


# setup video capture
cap = cv2.VideoCapture(0)
ret, img = cap.read()
prev_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# initialize the ball in the game
ball = Ball(img)

while True:
    # get grayscale image
    ret, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # compute optical flow
    flow = cv2.calcOpticalFlowFarneback(prev_gray, gray, None, 0.5, 3, 15, 3, 5, 1.2, 0)
    prev_gray = gray

    # get new ball position
    ball_position = ball.get_position(img, flow)

    # plot the flow vectors
    vis = draw_flow(img, flow)
    cv2.imshow('Optical Flow', cv2.flip(vis, 1))

    # plot the ball in the game
    vis = img.copy()
    vis = draw_ball(vis, ball_position)
    cv2.imshow('Ball Control', cv2.flip(vis, 1))

    # plot ball + optical flow
    vis = img.copy()
    vis = draw_flow(img, flow)
    vis = draw_ball(vis, ball_position)
    cv2.imshow('Ball with Optical Flow', cv2.flip(vis, 1))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# frees up resources and closes all windows
cap.release()
cv2.destroyAllWindows()