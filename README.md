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
  * A point "a" needs a ***visibility height*** in each direction. Points above that height
    are visible, everything below is not. This visibilty height depends on the closest and
    highest point "b" and the distance between points on the map. Visibility height is
    nothing more than a ***view angle***. This view angle is different for every direction 
    you might look in. 
  * We need a metric do calculate ***distance*** between two points &#8594; euclidean distance.
  * We need a way to determine ***line of sight***, as in "all points between two given points". 
    View angle is dependent on this variable as we have one view angle for every direction.
    [Bresenham Algorithm](https://en.wikipedia.org/wiki/Bresenham%27s_line_algorithm) should
    be quite useful to achieve this.

  **&#8658;** To check whether you see point b from point a requires:
  * Map of all points, point a, point b, view angle, line of sight, distance
  * Idea:  
  Starting from point a, in loops around it, for each point check visibility. 
  Update the view angle at each point. Further out, visibilty depends on the view angle
  of the last point in the line of sight. View angle may only ever go up or down in a
  line of sight but not both! As a result every point needs a way to save its view angle.

## 2. Step:

Make it realistic. The earth isn't flat. When does it begin to curve?

* The curvature of the earth takes away from the height of distant points.  
  `distance of point x - earth_curvature_factor = new distance of point x`  
  Curvature factor is dependent on distance between points.
* Human height provides and additional ~1.8 meter.

## 3. Step:

Make it work on a real map.
