# Based on a script found via Google search for TryFitCircleTTT:
# http://www.grasshopper3d.com/forum/topics/cycle-operations-in-gh

import Rhino
import scriptcontext


def closest_point(curve, length):
	"""Get the closest point on a curve at a given length"""
	return curve.ClosestPoint(curve.PointAtLength(length), 0.0)[1]


def create_param(curve, point, radius, last):
	"""Create a param given input"""
	
	domain = Rhino.Geometry.Interval(curve.Domain[0], curve.ClosestPoint(point, 0.0)[1])
	dist = curve.GetLength(domain) + radius
	
	if dist >= curve.GetLength():
		return None
		
	param = closest_point(curve, dist)
	
	if param >= last:
		return param
	else:
		return None
	

CIRCLES = []
circle = None


while True:
	
  if circle is None:
    curve_X = Rhino.Geometry.Line( CURVE_A.PointAtStart, CURVE_B.PointAtStart).ToNurbsCurve()
    param_A, param_B, param_X = [closest_point(crv, curve_X.GetLength() * 0.5) for crv in [CURVE_A, CURVE_B, curve_X]]	 
  else: 
    curve_X = circle.ToNurbsCurve()  
    pt_X = curve_X.PointAtLength(curve_X.GetLength() * 0.5)
    param_A = create_param(CURVE_A, pt_X, circle.Radius, param_A)
    param_B = create_param(CURVE_B, pt_X, circle.Radius, param_B)	
    param_X = curve_X.ClosestPoint(pt_X, 0.0)[1]
	
  if param_A is None or param_B is None:
	break
        
  circle = Rhino.Geometry.Circle.TryFitCircleTTT(curve_X, CURVE_A, CURVE_B, param_X, param_A, param_B)
  
  if circle == Rhino.Geometry.Circle.Unset:
    break
    
  #if circle.Radius > scriptcontext.doc.ModelAbsoluteTolerance: 
  CIRCLES.append(circle)
	




    

    
  
 
