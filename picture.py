"""
picture.py
Author: Kezar
Credit: Kotz, xnimblenavigatorx

Assignment:picture

Use the ggame library to "paint" a graphical picture of something (e.g. a house, a face or landscape).

Use at least:
1. Three different Color objects.
2. Ten different Sprite objects.
3. One (or more) RectangleAsset objects.
4. One (or more) CircleAsset objects.
5. One (or more) EllipseAsset objects.
6. One (or more) PolygonAsset objects.

See:
https://github.com/HHS-IntroProgramming/Standards-and-Syllabus/wiki/Displaying-Graphics
for general information on how to use ggame.

See:
http://brythonserver.github.io/ggame/
for detailed information on ggame.

"""
from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset

# add your code here \/  \/  \/
yellow = Color(0xfff400, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)
# Define a line style that is a thin (1 pixel) wide black line
Thinline = LineStyle(1, black)
thinline = LineStyle(0, black)
# A graphics asset that represents a rectangle
rectangle = RectangleAsset(150, 150, Thinline, yellow)
rectangle1 = RectangleAsset(25, 25 ,Thinline, black) 
rectangle2 = RectangleAsset(100,1 ,Thinline, black)
rectangle3 = RectangleAsset(100, 35, Thinline, blue)
rectangle4 = RectangleAsset(35, 100, Thinline, blue)
rectangle5 = RectangleAsset(35, 100, Thinline, blue)
rectangle6 = RectangleAsset(50, 25, thinline, red)
rectangle7 = RectangleAsset(30, 100, thinline, red)
rectangle8 = RectangleAsset(30, 100, thinline, red)
rectangle9 = RectangleAsset(20, 70, thinline, yellow)
rectangle10 = RectangleAsset(20, 90, thinline, black)
rectangle11 = RectangleAsset(20, 90, thinline, blue)
rectangle12 = RectangleAsset(20, 60, thinline, green)
rectangle13 = RectangleAsset(65, 20, thinline, green)
rectangle14 = RectangleAsset(65, 20, thinline, green)
rectangle15 = RectangleAsset(20, 100, thinline, green)
rectangle16 = RectangleAsset(25, 115, thinline, green)
rectangle17 = RectangleAsset(20, 60, thinline, blue)
rectangle18 = RectangleAsset(20, 80, thinline, black)
rectangle19 = RectangleAsset(75, 30, thinline, black)
rectangle20 = RectangleAsset(40, 15, thinline, white)
rectangle21 = RectangleAsset(25, 110, thinline, yellow)
rectangle22 = RectangleAsset(60, 25, thinline, yellow)
rectangle23 = RectangleAsset(17, 110, thinline, red)
rectangle24 = RectangleAsset(60, 10, thinline, red)
rectangle25 = RectangleAsset(10, 55, thinline, red)
rectangle26 = RectangleAsset(20, 110, thinline, yellow)
rectangle27 = RectangleAsset(20, 70, thinline, black)
rectangle28 = RectangleAsset(20, 70, thinline, blue)
rectangle29 = RectangleAsset(50, 20, thinline, blue)
rectangle30 = RectangleAsset(20, 110, thinline, blue)
rectangle31 = RectangleAsset(50, 20, thinline, blue)
rectangle32 = RectangleAsset(25, 90, thinline, green)
rectangle33 = RectangleAsset(25, 100, thinline, black)





ellipse = EllipseAsset(12,30, Thinline, black)
ellipse2 = EllipseAsset(50, 7, Thinline, black)
circle = CircleAsset(30, Thinline, blue)
circle1 = CircleAsset(40, Thinline, blue)
circle2 = CircleAsset(40, Thinline, blue)
circle3 = CircleAsset(35, thinline, yellow)
circle4 = CircleAsset(25, thinline, white)
circle5 = CircleAsset(30, thinline, black)
circle6 = CircleAsset(22, thinline, white)
circle7 = CircleAsset(30, thinline, blue)
circle8 = CircleAsset(22, thinline, white)
circle9 = CircleAsset(35, thinline, green)
circle10 = CircleAsset(35, thinline, green)
circle11 = CircleAsset(20, thinline, white)
circle12 = CircleAsset(20, thinline, white)
circle13 = CircleAsset(10, thinline, blue)
circle14 = CircleAsset(30, thinline, yellow)
circle15 = CircleAsset(22, thinline, white)
circle16 = CircleAsset(35, thinline, black)
circle17 = CircleAsset(25, thinline, white)
circle18 = CircleAsset(15, thinline, green)

polygon = PolygonAsset([(1166, 310), (1166, 345), (1266, 345), (1230, 327.5), (1266, 310)], Thinline, blue)




# Now display a rectangle
Sprite(rectangle, (1000, 100))
Sprite(rectangle1, (1020, 125))
Sprite(rectangle1, (1100, 125))
Sprite(rectangle2, (1020, 135))
Sprite(ellipse, (1073, 177))
Sprite(ellipse2, (1073, 225))
Sprite(circle, (1073, 280))
Sprite(circle1, (1125, 325))
Sprite(circle2, (1020, 325))
Sprite(polygon)
Sprite(rectangle3, (880, 310))
Sprite(rectangle4, (1002, 365))
Sprite(rectangle5, (1110, 365))
Sprite(rectangle6, (50, 100))
Sprite(rectangle7, (20, 63))
Sprite(rectangle8, (100, 63))
Sprite(circle3, (200, 125))
Sprite(circle4, (202, 127))
Sprite(rectangle9, (215, 90))
Sprite(rectangle10, (275, 90))
Sprite(circle5, (305, 117))
Sprite(circle6, (307, 119))
Sprite(rectangle11, (370, 90))
Sprite(circle7, (400, 117))
Sprite(circle8, (402, 119))
Sprite(rectangle12, (470, 90))
Sprite(rectangle13, (470, 130))
Sprite(rectangle14, (470, 170))
Sprite(rectangle15, (515, 90))
Sprite(rectangle16, (20, 242))
Sprite(circle9, (65, 275))
Sprite(circle10, (65, 325))
Sprite(circle11, (65, 270))
Sprite(circle12, (65, 325))
Sprite(rectangle17, (150, 300))
Sprite(circle13, (160, 275))
Sprite(rectangle18, (200, 280))
Sprite(rectangle19, (200, 270))
Sprite(rectangle20, (220, 285))
Sprite(rectangle21, (330, 250))
Sprite(rectangle22, (312.5, 270))
Sprite(rectangle23, (410, 250))
Sprite(rectangle24, (410, 305))
Sprite(rectangle25, (470, 305))
Sprite(rectangle26, (540, 250))
Sprite(circle14, (525, 330))
Sprite(circle15, (526, 331))
Sprite(circle16, (615, 319))
Sprite(circle17, (613, 318))
Sprite(rectangle27, (630, 285))
Sprite(rectangle28, (675, 285))
Sprite(rectangle29, (675, 335))
Sprite(rectangle30, (725, 285))
Sprite(rectangle31, (675, 375))
Sprite(rectangle32, (775, 260))
Sprite(circle18, (787.5, 380))
Sprite(rectangle33, (20, 440))



# add your code here /\  /\  /\


myapp = App()
myapp.run()
