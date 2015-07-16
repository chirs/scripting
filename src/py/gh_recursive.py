#Based on a script found via Google search for TryFitCircleTTT:

import Rhino
import scriptcontext

CIRCLES_CONTAINER = []

tolerance = scriptcontext.doc.ModelAbsoluteTolerance

line = Rhino.Geometry.Line( CURVE_A.PointAtStart, CURVE_B.PointAtStart )

count = False

while True:

  if count == False:
    crv_X = line.ToNurbsCurve()
    length = crv_X.GetLength() * 0.5
    
    pt_X = crv_X.PointAtLength(length)
    param_X = crv_X.ClosestPoint(pt_X, 0.0)[1]
    
    pt_A = CURVE_A.PointAtLength(length)
    param_A = CURVE_A.ClosestPoint(pt_A, 0.0)[1]
    
    pt_B = CURVE_B.PointAtLength(length)
    param_B = CURVE_B.ClosestPoint(pt_B, 0.0)[1]

  else:
    crv_X = last_circle.ToNurbsCurve()
    length = crv_X.GetLength() * 0.5
    
    pt_X = crv_X.PointAtLength(length)
    param_X = crv_X.ClosestPoint(pt_X, 0.0)[1]
    
    param_A = CURVE_A.ClosestPoint(pt_X, 0.0)[1]
    pt_A = CURVE_A.PointAt(param_A)
    
    domain = Rhino.Geometry.Interval(CURVE_A.Domain[0], param_A)
    dist_A = CURVE_A.GetLength(domain) + last_circle.Radius
    if dist_A >= CURVE_A.GetLength(): 
      break
    else:
      pt_A = CURVE_A.PointAtLength(dist_A)
      param_A = CURVE_A.ClosestPoint(pt_A, 0.0)[1]
      if param_A <= last_A:
        break

    param_B = CURVE_B.ClosestPoint(pt_X, 0.0)[1]
    pt_B = CURVE_B.PointAt(param_B)
    
    domain = Rhino.Geometry.Interval(CURVE_B.Domain[0], param_B)
    dist_B = CURVE_B.GetLength(domain) + last_circle.Radius
    if dist_B >= CURVE_B.GetLength(): 
      break
    else:
      pt_B = CURVE_B.PointAtLength(dist_B)
      param_B = CURVE_B.ClosestPoint(pt_B,0.0)[1]
      if param_B  <= last_B:
        break

  circle = Rhino.Geometry.Circle.TryFitCircleTTT(crv_X, CURVE_A, CURVE_B, param_X, param_A, param_B)
  
  if circle == Rhino.Geometry.Circle.Unset:
    break
  else:
    if circle.Radius > tolerance: 
      CIRCLES_CONTAINER.append(circle)
      last_A = param_A
      last_B = param_B
    last_circle = circle
    
  count = True
  
CIRCLES = CIRCLES_CONTAINER
