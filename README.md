GoldenRatio 3D version 1.0
====================
[![License](https://img.shields.io/badge/License-GPLv3-orange.svg)](https://github.com/)

**GoldenRatio 3D** is a python program for . 

Authors and contributor list:
---
_**Lev Nagornov**_ (Maintainer, Author)

All questions and requests can be sent to lioliovitt@gmail.com  

Description
---
First, programmatically creates a sphere in three-dimensional space, for this we set a multidimensional list with a linear
relationship and constraints from 0 to 2 pi and from 1.1 pi to pi divided by three, all this is needed to create the shape
of the cup, for a better representation of the beauty of the golden ratio.

x, y and z are given by the following formulas:

x = np.sin(phi) * np.cos(theta)
y = np.sin(phi) * np.sin(theta)
z = np.cos(phi)

whrere phi and theta are given by the following:

$theta, phi = 0:2*np.pi:100j,np.pi*1.1:np.pi/3:100j$

$p_u = i^4$

## Cite program

For publication, please, be kind to use next reference:

- Model description and first version of GoldenRatio

Lev Nagornov,  GoldenRatio 3D: a python software for drawing lines based on golden ratio on a 3D surface (https://github.com/LIOVITT/GoldenRatio)

