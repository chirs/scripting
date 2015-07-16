# Based on a script found via Google search for TryFitCircleTTT:
# http://www.grasshopper3d.com/forum/topics/cycle-operations-in-gh

import Rhino
import scriptcontext

CIRCLES = []

tolerance = scriptcontext.doc.ModelAbsoluteTolerance


def helper(curve, px, circle, last):
	param = curve.ClosestPoint(px, 0.0)[1]
	
	domain = Rhino.Geometry.Interval(curve.Domain[0], param)
	dist = curve.GetLength(domain) + last_circle.Radius
	if dist >= curve.GetLength():
		return None, None
		
	point = curve.PointAtLength(dist)
	param = curve.ClosestPoint(point, 0.0)[1]
	
	if param < last:
		return None, None
		
	return point, param
	


first = True

while True:
	
  # step 1

  if first:
    first = False
    
    crv_X = Rhino.Geometry.Line( CURVE_A.PointAtStart, CURVE_B.PointAtStart).ToNurbsCurve()
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
    
		
    pt_A, param_A = helper(CURVE_A, pt_X, last_circle, last_A)
    if pt_A is None:
		break

		
    pt_B, param_B = helper(CURVE_B, pt_X, last_circle, last_B)
    if pt_B is None:
		break
        
        
  # step 2

  circle = Rhino.Geometry.Circle.TryFitCircleTTT(crv_X, CURVE_A, CURVE_B, param_X, param_A, param_B)
  
  if circle == Rhino.Geometry.Circle.Unset:
    break
  else:
    if circle.Radius > tolerance: 
      CIRCLES.append(circle)
      last_A = param_A
      last_B = param_B
    last_circle = circle
    
  
 
