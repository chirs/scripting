import math
import random

import rhinoscriptsyntax as rs
import Rhino.Geometry as rg


if seed is not None:
	random.seed(seed)

start = rg.Point3d(0,0,0)

points = [start]
curve_list = []
thicknesses = []

def point_from_vector(start, direction, scale):
	x, y = [scale * op(direction) for op in (math.sin, math.cos)]
	return rs.PointAdd(start, rg.Point3d(x, y, 0))
	
	
def split_thickness(t):
	return [t / 2.0, t / 2.0]
	

def scale_vector(v, scale):
	return [scale * e for e in v] 

def get_new_point(p):
	radians = (2 * math.pi) * degrees / 360.0
	print(degrees)
	print(radians)
	direction = random.uniform(-1/2.0 * radians, radians / 2.0)
	np = point_from_vector(p, direction, stride)
	return np
	
	


def loop(steps, parent, thickness):
	print("loop")
	
	if steps == 0:
		return
		
	else:
		new_point = get_new_point(parent)
		
		c = rs.AddCurve([parent, new_point])
		curve_list.append(c)
		thicknesses.append(thickness)
		points.append(new_point)
		

		if random.random() < split:
			t1, t2 = split_thickness(thickness)
			loop(steps - 1, new_point, t1)
			loop(steps - 1, rg.Point3d(new_point), t2)
		else:
			loop(steps - 1, new_point, thickness)
		
loop(xsteps, start, 1.0)
