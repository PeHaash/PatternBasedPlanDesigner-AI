import ghpythonlib.components as gh

PLANE=gh.XYPlane(gh.ConstructPoint(0,0,0))

def Removedquotes(string):
    if string[0]!=string[-1] or (string[0]!="'" and string[0]!='"'):
        return string
    else:
        return string[1:-1]

def ColorByCode(Code):
    ## 125 Color! [0,124]
    Code=int(Code)
    base5=[Code%5,(Code//5)%5,(Code//25)]
    convert=[0,63,127,191,255]
    rgb=[convert[b] for b in base5]
    return gh.ColourRGB(255,rgb[0],rgb[1],rgb[2])
    """
    0:0
    1:64
    2:127
    3:
    4:256
    """

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
    ## Set command & keys
    command,attrs=line.split(":")
    command=command.upper()
    attrs=attrs.split()
    attrs=(attribute.split("=") for attribute in attrs)
    keys={a[0].upper():Removedquotes(a[1]) for a in attrs}

    ##Main Variables:
    HasStroke=False if "NOSTROKE" in keys and keys["NOSTROKE"].upper()=="YES" else True
    # print(HasStroke,keys["NOSTROKE"])
    GeoStrokeShape=None ####
    GeoStrokeColor=SetColorFromKeys("Stroke",keys)

    HasFill=False if ("NOFILL" in keys and keys["NOFILL"].upper()=="YES") else True
    GeoFillShape=None ###
    GeoFillColor=SetColorFromKeys("Fill"  ,keys,default=(0,0,0))
    
    HasText=True if "TEXT" in keys else False
    GeoTextPosition=None ####
    GeoTextData=keys["TEXT"] if HasText else None
    GeoTextColor=SetColorFromKeys("Text"  ,keys,default=(0,200,128))
    
    if command=="RECTANGLE":
        x0,y0,x1,y1=(float(k) for k in (keys["X0"],keys["Y0"],keys["X1"],keys["Y1"]))
        GeoStrokeShape=gh.JoinCurves(gh.Rectangle2Pt(PLANE,gh.ConstructPoint(x0,y0,0),gh.ConstructPoint(x1,y1,0),0)[0],False)
        GeoFillShape=gh.BoundarySurfaces(GeoStrokeShape) if HasFill else None
        GeoTextPosition=gh.Area(GeoStrokeShape)[1] if HasText else None
    if command=="LINE":
        HasFill=False
        x0,y0,x1,y1=(float(k) for k in (keys["X0"],keys["Y0"],keys["X1"],keys["Y1"]))
        GeoStrokeShape=gh.Line(gh.ConstructPoint(x0,y0,0),gh.ConstructPoint(x1,y1,0))
        GeoTextPosition=gh.CurveMiddle(GeoStrokeShape)

    if "THICKNESS" in keys and float(keys["THICKNESS"])>0:
        tx=float(keys["THICKNESS"])
        if command=="LINE":
            GeoStrokeShape=gh.RuledSurface(
                gh.OffsetCurve(GeoStrokeShape,tx/2,PLANE,1),gh.OffsetCurve(GeoStrokeShape,-tx/2,PLANE,1))
        if command=="RECTANGLE":
            pass
            # GeoStrokeShape=gh.JoinCurves(gh.OffsetCurve(GeoStrokeShape, tx/2,PLANE,0),False)
            # GeoStrokeShape=gh.BoundarySurfaces([
            #     gh.JoinCurves(gh.OffsetCurve(GeoStrokeShape, tx/2,PLANE,0),True),
            #     gh.JoinCurves(gh.OffsetCurve(GeoStrokeShape,-tx/2,PLANE,0),True)
            #     ])
        if HasFill:
            pass
            ### WE CAN CORRECT FILL SHAPE IF WE CAN
    # print(HasFill,HasStroke,HasText)
    if HasFill:
        ShapeOutput.append(GeoFillShape)
        ShapeColorOutput.append(GeoFillColor)
    if HasStroke:
        ShapeOutput.append(GeoStrokeShape)
        ShapeColorOutput.append(GeoStrokeColor)
    if HasText:
        TextOutput.append(GeoTextData)
        TextPositionOutput.append(GeoTextPosition)
        TextColorOutput.append(GeoTextColor)




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




def oldDraw(line,ShapeOutput,ShapeColorOutput,TextOutput,TextPositionOutput,TextColorOutput):
    ## Set command & keys
    command,attrs=line.split(":")
    command=command.upper()
    attrs=attrs.split()
    attrs=(attribute.split("=") for attribute in attrs)
    keys={a[0].upper():Removedquotes(a[1]) for a in attrs}
    ##
    # if ["NOSTROKE"] in 
    ## Set Color
    StrokeColor=SetColorFromKeys("Stroke",keys)
    TextColor  =SetColorFromKeys("Text"  ,keys,default=(0,200,128))
    FillColor  =SetColorFromKeys("Fill"  ,keys,default=(0,0,0))
    ## ,nostroke="yes",nofill="yes"
    ## params
    GeoStrokeShape=None
    GeoStrokeColor=None
    GeoFillShape=None
    GeoFillColor=None
    GeoTextPosition=None
    GeoTextData=None
    Text =None
    TextPos=None
    TexColor=None
    # HasFill= True if "HASFILL" in keys and keys["HASFILL"]=="YES"

    if command=="RECTANGLE":
        x0,y0,x1,y1=(float(k) for k in (keys["X0"],keys["Y0"],keys["X1"],keys["Y1"]))
        ShapeStroke=gh.Rectangle2Pt(PLANE,gh.ConstructPoint(x0,y0,0),gh.ConstructPoint(x1,y1,0),0)[0]
        
        # if HasFill:

    elif command=="LINE":
        x0,y0,x1,y1=(float(k) for k in (keys["X0"],keys["Y0"],keys["X1"],keys["Y1"]))
        shape=gh.Line(gh.ConstructPoint(x0,y0,0),gh.ConstructPoint(x1,y1,0))


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
