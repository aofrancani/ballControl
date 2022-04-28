import numpy as np
import cv2


class Ball(object):
    """
    Represents the ball in the game.
    """

    def __init__(self, img):
        """
        Creates the Ball.

        input:
            vis: image to draw the ball
        """
        self.r = 12  # radius of the ball
        h, w = img.shape[:2]
        self.h = h - 50
        self.w = w - 50
        self.xc = np.random.randint(low=self.r + 10, high=self.w - self.r - 10)
        self.yc = np.random.randint(low=self.r + 10, high=self.h - self.r - 10)
        self.vx = 0.0
        self.vy = 0.0
        self.max_speed = 4
        self.factor = 0.8

    def update_position(self, img, flow):
        """
        Updates the position of the ball.

        input:
            boundary: a list representing a position (h, w) of the image, limiting the initialization
            flow: optical flow vectors
        """

        # new position of the ball based on the optical flow vectors
        self.clip_position(self.xc, self.yc)
        self.vx = self.vx + self.factor*flow[self.yc, self.xc, 0]
        self.vy = self.vy + self.factor*flow[self.yc, self.xc, 1]
        self.clip_velocity()

        # correct ball position if out of the window
        xc = round(self.xc + self.vx)
        yc = round(self.yc + self.vy)
        self.clip_position(xc, yc)

    def get_position(self, img, flow):
        self.update_position(img, flow)
        return self.xc, self.yc

    def clip_position(self, new_xc, new_yc):
        # limit ball position in window
        if new_xc >= self.w - self.r:
            new_xc = self.w - self.r
            if self.vx > 0:
                self.vx = -self.vx
        if new_xc <= self.r:
            new_xc = self.r
            if self.vx > 0:
                self.vx = -self.vx
        if new_yc >= self.h - self.r:
            new_yc = self.h - self.r
            if self.vy > 0:
                self.vy = -self.vy
        if new_yc <= self.r:
            new_yc = self.r
            if self.vy > 0:
                self.vy = -self.vy
        self.xc = new_xc
        self.yc = new_yc

    def clip_velocity(self):
        # limit linear speed
        if self.vx > self.max_speed:
            self.vx = self.max_speed
        elif -self.vx < - self.max_speed:
            self.vx = - max_speed

        if self.vy > self.max_speed:
            self.vy = self.max_speed
        elif -self.vy < - self.max_speed:
            self.vy = - max_speed
