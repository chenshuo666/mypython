
import sys, random, argparse
import numpy as np
import math
import turtle
from turtle import *
import random
from PIL import Image
from datetime import datetime
from fractions import gcd


# A class that draws a spirograph
class Spiro:
    # constructor
    def __init__(self, xc, yc, col, R, r, l):

        # create own turtle
        self.t = turtle.Turtle()
        # set cursor shape
        self.t.shape('turtle')
        # set step in degrees
        self.step = 5
        # set drawing complete flag
        self.drawingComplete = False
        #确定画图是否完成

        # set parameters
        self.setparams(xc, yc, col, R, r, l)

        # initiatize drawing
        self.restart()

    # set parameters初始化对象
    def setparams(self, xc, yc, col, R, r, l):
        # spirograph parameters
        self.xc = xc
        self.yc = yc
        self.R = int(R)
        self.r = int(r)
        self.l = l
        self.col = col
        # reduce r/R to smallest form by dividing with GCD
        gcdVal = gcd(self.r, self.R)#最大公约数
        self.nRot = self.r // gcdVal
        # get ratio of radii
        self.k = r / float(R)
        # set color
        self.t.color(*col)
        # current angle
        self.a = 0

    # restart drawing重置Spiro对象的绘制参数，准备好重画
    def restart(self):
        # set flag
        self.drawingComplete = False
        # show turtle
        self.t.showturtle()#显示海龟图标，防止被隐藏

        # go to first point
        self.t.up()#提起笔，
        R, k, l = self.R, self.k, self.l
        #获取曲线的起点
        a = 0.0
        x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))

        #绘制实际的线
        self.t.setpos(self.xc + x, self.yc + y)
        self.t.down()

    # draw the whole thing
    def draw(self):
        # draw rest of points
        R, k, l = self.R, self.k, self.l
        for i in range(0, 360 * self.nRot + 1, self.step):#确定图标的绘制范围和跳跃单位5度
            a = math.radians(i)
            x = R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
            y = R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
            self.t.setpos(self.xc + x, self.yc + y)
        # done - hide turtle
        self.t.hideturtle()

    # update by one step
    def update(self):#确定停止的时间
        # skip if done
        if self.drawingComplete:
            return
        # increment angle
        self.a += self.step
        # draw step
        R, k, l = self.R, self.k, self.l
        # set angle
        a = math.radians(self.a)
        x = self.R * ((1 - k) * math.cos(a) + l * k * math.cos((1 - k) * a / k))
        y = self.R * ((1 - k) * math.sin(a) - l * k * math.sin((1 - k) * a / k))
        self.t.setpos(self.xc + x, self.yc + y)
        # check if drawing is complete and set flag
        if self.a >= 360 * self.nRot:
            self.drawingComplete = True
            # done - hide turtle
            self.t.hideturtle()

    # clear everything
    def clear(self):
        self.t.clear()


# A class for animating spirographs
class SpiroAnimator:#同时绘制多个曲线
    # constructor
    def __init__(self, N):
        # timer value in milliseconds
        self.deltaT = 1#设定绘制的时间间隔，ms为单位
        # get window dimensions
        self.width = turtle.window_width()
        self.height = turtle.window_height()
        # create spiro objects
        self.spiros = []
        for i in range(N):
            # generate random parameters
            rparams = self.genRandomParams()
            # set spiro params
            spiro = Spiro(*rparams)#rparams是一个元组，需要传入Spiro构造函数，构造函数需要参数列表，利用python中的* 运算符将元组转化成参数列表
            self.spiros.append(spiro)
        # call timer
        turtle.ontimer(self.update, self.deltaT)#每隔deltaT毫秒调用函数update()

    # restart sprio drawing
    def restart(self):
        for spiro in self.spiros:
            # clear
            spiro.clear()
            # generate random parameters
            rparams = self.genRandomParams()
            # set spiro params
            spiro.setparams(*rparams)
            # restart drawing
            spiro.restart()

    # generate random parameters
    def genRandomParams(self):
        width, height = self.width, self.height
        R = random.randint(50, min(width, height) // 2)
        r = random.randint(10, 9 * R // 10)
        l = random.uniform(0.1, 0.9)
        xc = random.randint(-width // 2, width // 2)
        yc = random.randint(-height // 2, height // 2)
        col = (random.random(),random.random(),random.random())
        return (xc, yc, col, R, r, l)

    def update(self):
        # update all spiros
        nComplete = 0
        for spiro in self.spiros:
            # update
            spiro.update()
            # count completed ones
            if spiro.drawingComplete:
                nComplete += 1
        # if all spiros are complete, restart
        if nComplete == len(self.spiros):
            self.restart()
        # call timer
        turtle.ontimer(self.update, self.deltaT)

    # toggle turtle on/off
    def toggleTurtles(self):
        for spiro in self.spiros:
            if spiro.t.isvisible():
                spiro.t.hideturtle()
            else:
                spiro.t.showturtle()


# save spiros to image
def saveDrawing():
    # hide turtle
    turtle.hideturtle()
    # generate unique file name
    dateStr = (datetime.now()).strftime("%d%b%Y-%H%M%S")
    fileName = 'spiro-' + dateStr
    print('saving drawing to %s.eps/png' % fileName)
    # get tkinter canvas
    canvas = turtle.getcanvas()
    # save postscipt image
    canvas.postscript(file=fileName + '.eps')
    # use PIL to convert to PNG
    img = Image.open(fileName + '.eps')
    img.save(fileName + '.png', 'png')
    # show turtle
    turtle.showturtle()


# main() function
def main():
    # use sys.argv if needed
    print('generating spirograph...')
    # create parser
    descStr = """This program draws spirographs using the Turtle module. 
    When run with no arguments, this program draws random spirographs.

    Terminology:
    R: radius of outer circle.
    r: radius of inner circle.
    l: ratio of hole distance to r.
    """
    parser = argparse.ArgumentParser(description=descStr)#设置参数解释器对象

    # add expected arguments向解释器中添加--sparams可选参数
    parser.add_argument('--sparams', nargs=3, dest='sparams', required=False,help="The three arguments in sparams: R, r, l.")

    # parse args调用函数进行实际的解析
    args = parser.parse_args()

    # set to 80% screen width
    turtle.setup(width=0.8)

    # set cursor shape
    turtle.shape('turtle')

    # set title
    turtle.title("Spirographs!")
    # add key handler for saving images
    turtle.onkey(saveDrawing, "s")#按下s保存图片
    # start listening
    turtle.listen()

    # hide main turtle cursor
    turtle.hideturtle()

    # checks args and draw
    if args.sparams:
        params = [float(x) for x in args.sparams]
        # draw spirograph with given parameters
        # black by default
        col = (0.0, 0.0, 0.0)
        spiro = Spiro(0, 0, col, *params)
        spiro.draw()
    else:
        # create animator object
        spiroAnim = SpiroAnimator(4)
        # add key handler to toggle turtle cursor
        turtle.onkey(spiroAnim.toggleTurtles, "t")#按钮监听
        # add key handler to restart animation
        turtle.onkey(spiroAnim.restart, "space")

    # start turtle main loop
    turtle.mainloop()


# call main
if __name__ == '__main__':
    main()