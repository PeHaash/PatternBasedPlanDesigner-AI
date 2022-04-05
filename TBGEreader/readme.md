# TBGEreader

My program, outputs different plans with a format named **.TBGE** (Text-Based Graphic Export) This folder, has a simple tool to visualize **.TBGE** files.
But, what is a .TBGE file?
.TBGE files has simple rules.
The file is comprise different frames. Each frame has some commands in it. Frames can be show individualy or altoghether.

Every lines starts with a ALL**CAPS**AND**NO**SPACE command, followed by a colon (:) After colon, we have files description's of that graphic.

For example
```python
LINE: X0=0 Y0=0 X1=100 Y1=0
```
Denotes that there is a line from (0,0) to (100,0)
There are three comnands (yet)
- FRAME: denotes start of a frame
- LINE: draw a line
- RECTANGLE: draw a rectangle

Also, every command has multible optional arguments such as Text (to show a caption on the shape) Thickness, or Background, Stroke colors etc..
```python
FRAME: Code=0
LINE: x0=653 y0=770 x1=653 y1=1244 Thickness=20  Text='Door'  StrokeColorCode=8  TextColorCode=9 
RECTANGLE: x0=0 y0=0 x1=99 y1=278 Thickness=0  FillColorCode=47  StrokeColorCode=1  Text='1--4' 
RECTANGLE: x0=99 y0=0 x1=647 y1=278 Thickness=0  FillColorCode=47  StrokeColorCode=1  Text='1--2' 
```

TL;DR you can use grasshopper file to open my code outputs in rhino. Further information is available in grasshopper file.
