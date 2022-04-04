# import rhinoscriptsyntax as rs
import ghpythonlib.components as gh
# import PeHash.stdlib as std

PLANE=gh.XYPlane(gh.ConstructPoint(0,0,0))

def Removedquotes(string):
    if string[0]!=string[-1] or (string[0]!="'" and string[0]!='"'):
        return string
    else:
        return string[1:-1]

def ColorByCode(Code):
    Code=int(Code)
    if Code==2:
        return gh.ColourRGB(255,150,200,12)

def SetColorFromKeys(ColorType,keys,default=(0,0,0)):
    Color=gh.ColourRGB(255,default[0],default[1],default[2])
    # print(ColorType+"ColorCode")
    # print(keys)
    ColorType=ColorType.upper()
    if ColorType+"COLORCODE" in keys:
        Color=ColorByCode(keys[ColorType+"COLORCODE"])
    elif ColorType+"COLORRGB" in keys:
        pass
    elif ColorType+"COLORCMYK" in keys:
        pass
    return Color

def Draw(line,ShapeOutput,ShapeColorOutput,TextOutput,TextPositionOutput,TextColorOutput):
    command,attrs=line.split(":")
    command=command.upper()
    attrs=attrs.split()
    attrs=(attribute.split("=") for attribute in attrs)
    keys={a[0].upper():Removedquotes(a[1]) for a in attrs}
    
    StrokeColor=SetColorFromKeys("Stroke",keys)
    TextColor=SetColorFromKeys("Text",keys,default=(0,200,128))
    
    if command=="REC":
        x0,y0,x1,y1=(float(k) for k in (keys["X0"],keys["Y0"],keys["X1"],keys["Y1"]))
        shape=gh.Rectangle2Pt(PLANE,gh.ConstructPoint(x0,y0,0),gh.ConstructPoint(x1,y1,0),0)[0]
        ShapeOutput.append(shape)
        ShapeColorOutput.append(StrokeColor)
        
        if "TEXT" in keys:
            TextOutput.append(keys["TEXT"])
            TextPositionOutput.append(gh.Area(shape)[1])
            TextColorOutput.append(TextColor)

        return
    if command=="LINE":
        x0,y0,x1,y1=(float(k) for k in (keys["X0"],keys["Y0"],keys["X1"],keys["Y1"]))
        shape=gh.Line(gh.ConstructPoint(x0,y0,0),gh.ConstructPoint(x1,y1,0))
        center=0
        if "THICKNESS" in keys and float(keys["THICKNESS"])>0:
            tx=float(keys["THICKNESS"])
            shape=gh.RuledSurface(gh.OffsetCurve(shape,tx/2,PLANE,0),gh.OffsetCurve(shape,-tx/2,PLANE,0))
            center=gh.Area(shape)[1]
        else:
            center=gh.CurveMiddle(shape)

        ShapeOutput.append(shape)
        #print(StrokeColor)
        ShapeColorOutput.append(StrokeColor)
        
        if "TEXT" in keys:
            TextOutput.append(keys["TEXT"])
            TextPositionOutput.append(center)
            TextColorOutput.append(TextColor)


if Activate:
    ShapeOutput=[]
    ShapeColorOutput=[]
    TextOutput=[]
    TextPositionOutput=[]
    TextColorOutput=[]
    
    for line in TBGE:
        Draw(line=line,
            ShapeOutput=ShapeOutput,
            ShapeColorOutput=ShapeColorOutput,
            TextOutput=TextOutput,
            TextPositionOutput=TextPositionOutput,
            TextColorOutput=TextColorOutput)
