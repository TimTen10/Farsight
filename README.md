# Farsight

## Introduction

Have you ever wondered how far you can see from home or your favorite hill?  
This project aims to answer that question.

## 1. Step:

* How far can you see?
  * How to go about checking neighboring numbers?
  * Where are points that you can't see above?
  * Make sure you can't see around corners.
* Distance between single points of height.
  * How does sight change with shorter/longer distance between points?
* Make it work with simple numbers.
* Visualize the array (using seaborn or the like)

### Concepts:

* Visibility: 
  
  Which points are still visible? Depends on every single point between "a" and "b".
  E.g. high mountains far in the back are still visible over a 20-meter hill, while
  a valley behind said hill is not visible anymore. This leads to the following idea(s):
  * A point "a" needs a ***view angle*** in each direction. Depending on what that angle currently
    is, a point b might or might not be visible. View angle depends on current view angle, 
    the highest obstacle in line of sight, distance between points on the map and distance
    between a and b.
  * We need a metric do calculate ***distance*** between two points &#8594; euclidean distance.
  * We need a way to determine ***line of sight***, as in "all points between two given points". 
    View angle is dependent on this variable as we have one view angle for every direction.
    [Bresenham Algorithm](https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm) should
    be quite useful to achieve this.  
    &#8594; Calculating a path starting from the view point to every point at the outer edge
    of the map gives us a path to every point of the whole map.

&#8658; To check whether you see point b from point a requires:
* Map of all points, point a, point b, view angle, line of sight, distance
* Idea:  
Starting from point a, in loops around it, for each point check visibility. 
Update the view angle at each point. Further out, visibilty depends on the view angle
of the last point in the line of sight. The view angle can not get smaller!
As a result every point needs a way to save its view angle.
Output should be an array of the same size as the input map with 0 or 1 depending on whether
the point is visible or not.
* Implementation:
For every point we only need to save the preceding point in the Bresenham path and check against
that point whether, with the given distance between points (later on including curvature) and
given view angle, the point is visible. All in all every single point holds: height, (view) angle,
preceding point in Bresenham path, visibility, distance to view point (needed?)

## 2. Step:

Make it realistic. The earth isn't flat. When does it begin to curve?

* The curvature of the earth takes away from the height of distant points.  
  `distance of point x - earth_curvature_factor = new distance of point x`  
  Curvature factor is dependent on distance between points. See [here](https://earthcurvature.com/)
  for additional information.
* Human height provides and additional ~1.8 meter.

## 3. Step:

Make it work on a real map.
