# Farsight

## Introduction

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
    nothing more than a view angle. 
  * We need a metric do calculate ***distance*** between two points &#8594; euclidean distance
  * We need a way to determine ***line of sight***, as in "all points between two given points"

## 2. Step:

Make it realistic. The earth isn't flat. When does it begin to curve?

* The curvature of the earth takes away from the height of distant points.  
  `distance of point x - earth_curvature_factor = new distance of point x`  
  Curvature factor is dependent on distance between points.

## 3. Step:

Make it work on a map.
