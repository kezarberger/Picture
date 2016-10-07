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

polygon = PolygonAsset([(966, 310), (966, 345), (1066, 345), (1030, 327.5), (1066, 310)], Thinline, blue)




# Now display a rectangle
Sprite(rectangle, (800, 100))
Sprite(rectangle1, (820, 125))
Sprite(rectangle1, (900, 125))
Sprite(rectangle2, (820, 135))
Sprite(ellipse, (873, 177))
Sprite(ellipse2, (873, 225))
Sprite(circle, (873, 280))
Sprite(circle1, (925, 325))
Sprite(circle2, (820, 325))
Sprite(polygon)
Sprite(rectangle3, (680, 310))
Sprite(rectangle4, (802, 365))
Sprite(rectangle5, (910, 365))
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



# add your code here /\  /\  /\


myapp = App()
myapp.run()
