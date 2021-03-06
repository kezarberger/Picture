from ggame import App, Color, LineStyle, Sprite, RectangleAsset, CircleAsset, EllipseAsset, PolygonAsset


yellow = Color(0xfff400, 1.0)
red = Color(0xff0000, 1.0)
green = Color(0x00ff00, 1.0)
blue = Color(0x0000ff, 1.0)
black = Color(0x000000, 1.0)
white = Color(0xffffff, 1.0)

Thinline = LineStyle(1, black)
thinline = LineStyle(0, black)

rectangle = RectangleAsset(150, 150, Thinline, yellow)
rectangle1 = RectangleAsset(25, 25 ,Thinline, black) 
rectangle2 = RectangleAsset(100, 1 ,Thinline, black)
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
rectangle33 = RectangleAsset(25, 200, thinline, black)
rectangle34 = RectangleAsset(100, 25, thinline, black)
rectangle35 = RectangleAsset(25, 200, thinline, black)
rectangle36 = RectangleAsset(100, 25, thinline, black)
rectangle37 = RectangleAsset(25, 140, thinline, yellow)
rectangle38 = RectangleAsset(100, 25, thinline, yellow)
rectangle39 = RectangleAsset(25, 115, thinline, yellow)
rectangle40 = RectangleAsset(25, 140, thinline, green)
rectangle41 = RectangleAsset(100, 50, thinline, green)
rectangle42 = RectangleAsset(50, 25, thinline, white)
rectangle43 = RectangleAsset(140, 140, thinline, blue)
rectangle44 = RectangleAsset(90, 90, thinline, white)
rectangle45 = RectangleAsset(25, 140, thinline, red)
rectangle46 = RectangleAsset(100, 50, thinline, red)
rectangle47 = RectangleAsset(50, 25, thinline, white)
rectangle48 = RectangleAsset(35, 35, thinline, red)
rectangle49 = RectangleAsset(35, 35, thinline, yellow)
rectangle50 = RectangleAsset(35, 35, thinline, green)
rectangle51 = RectangleAsset(35, 35, thinline, blue)
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
circle19 = CircleAsset(70, thinline, black)
circle20 = CircleAsset(50, thinline, white)
polygon = PolygonAsset([(986, 220), (986, 255), (1086, 255), (1050, 237.5), (1086, 220)], Thinline, blue)


Sprite(rectangle, (820, 10))
Sprite(rectangle1, (840, 35))
Sprite(rectangle1, (930, 35))
Sprite(rectangle2, (840, 45))
Sprite(ellipse, (893, 87))
Sprite(ellipse2, (893, 135))
Sprite(circle, (893, 190))
Sprite(circle1, (945, 235))
Sprite(circle2, (840, 235))
Sprite(polygon)

Sprite(rectangle4, (822, 275))
Sprite(rectangle5, (930, 275))
Sprite(rectangle6, (50, 50))
Sprite(rectangle7, (20, 13))
Sprite(rectangle8, (100, 13))
Sprite(circle3, (200, 75))
Sprite(circle4, (202, 77))
Sprite(rectangle9, (215, 40))
Sprite(rectangle10, (275, 40))
Sprite(circle5, (305, 67))
Sprite(circle6, (307, 69))
Sprite(rectangle11, (370, 40))
Sprite(circle7, (400, 67))
Sprite(circle8, (402, 69))
Sprite(rectangle12, (470, 40))
Sprite(rectangle13, (470, 80))
Sprite(rectangle14, (470, 120))
Sprite(rectangle15, (515, 40))
Sprite(rectangle16, (20, 192))
Sprite(circle9, (65, 225))
Sprite(circle10, (65, 275))
Sprite(circle11, (65, 220))
Sprite(circle12, (65, 275))
Sprite(rectangle17, (150, 250))
Sprite(circle13, (160, 225))
Sprite(rectangle18, (200, 230))
Sprite(rectangle19, (200, 220))
Sprite(rectangle20, (220, 235))
Sprite(rectangle21, (330, 200))
Sprite(rectangle22, (312.5, 220))
Sprite(rectangle23, (410, 200))
Sprite(rectangle24, (410, 255))
Sprite(rectangle25, (470, 255))
Sprite(rectangle26, (540, 200))
Sprite(circle14, (525, 280))
Sprite(circle15, (526, 281))
Sprite(circle16, (615, 269))
Sprite(circle17, (613, 268))
Sprite(rectangle27, (630, 235))
Sprite(rectangle28, (675, 235))
Sprite(rectangle29, (675, 285))
Sprite(rectangle30, (725, 235))
Sprite(rectangle31, (675, 325))
Sprite(rectangle32, (765, 220))
Sprite(circle18, (777.5, 350))
Sprite(rectangle33, (20, 390))
Sprite(rectangle34, (20, 390))
Sprite(rectangle35, (120, 390))
Sprite(rectangle36, (20, 450))
Sprite(rectangle37, (200, 450))
Sprite(rectangle38, (200, 565))
Sprite(rectangle39, (275, 450))
Sprite(rectangle40, (350, 450))
Sprite(rectangle41, (350, 450))
Sprite(rectangle42, (375, 475))
Sprite(rectangle43, (500, 450))
Sprite(rectangle44, (525, 475))
Sprite(rectangle45, (700, 450))
Sprite(rectangle46, (700, 450))
Sprite(rectangle47, (725, 475))
Sprite(circle19, (900, 520))
Sprite(circle20, (900, 520))
Sprite(rectangle48, (940, 450))
Sprite(rectangle49, (940, 485))
Sprite(rectangle50, (940, 520))
Sprite(rectangle51, (940, 555))


myapp = App()
myapp.run()
