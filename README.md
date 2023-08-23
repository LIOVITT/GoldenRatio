GoldenRatio 3D version 1.0
====================
[![License](https://img.shields.io/badge/License-GPLv3-orange.svg)](https://github.com/)

**GoldenRatio 3D** is a python program for the representation of the beauty of the golden ratio in 3D. 

Authors and contributor list:
---
_**Lev Nagornov**_ (Maintainer, Author)

All questions and requests can be sent to lioliovitt@gmail.com  

Description
---
First, the program creates a sphere in three-dimensional space, for this we set a multidimensional list with a linear
relationship and constraints from 0 to 2 $\pi$ and from 1.1 $\pi$ to $\pi$ divided by three, all this is needed to create the shape
of the cup, for a better representation of the beauty of the golden ratio.

$x$, $y$ and $z$ are given by the following formulas:

$`
x = sin(\phi) cos(\theta),
`$
$`
y = sin(\phi) sin(\theta),
`$
$`
z = cos(\phi)
`$

where phi and theta are given by the following:

$\theta = [0, 2\pi]$

$\phi = [1.1 \pi,\pi/3]$
radius in this case will be equal to one.

limitation of the list from 0 to two pi is made due to the fact that the measurement system is made in radians,
and also limitation of theta from 1.1 pi to pi/3 is obtained to create a cup effect.

To make radius and theta angle values need to use this formulas

$`r=a\phi^{2\teta/\pi}`$

where $\phi$ is golden ration, and $a$ is arbitrary positive real constant


linetheta = np.linspace(0, pi, n+1)
linephi = np.linspace(pi, pi/2, n+1)

Values for the sphere envelope line


Change coordinates due to line

$`
line_y = sin(linephi)sin(teta)r, 
`$
$`
line_z = sin(linephi)cos(teta)r, 
`$

$`
line_x = \sqrt{1-line_y^2-line_z^2}
`$


Changes x, y, and z values to sphere coordinates

$`
alpha_0 = (pi/(n_d/2))i 
`$
where $`n_d`$ is 12 - values of spirals

$`
line{x_d} = cos(alpha_0)line_x - sin(alpha_0)line_y, 
`$

$`
line{y_d} = sin(alpha_0)line_x + cos(alpha_0)line_y, 
`$

$`
line{z_d} = line_z
`$


## Cite program

For publication, please, be kind to use next reference:

- Model description and first version of GoldenRatio

Lev Nagornov,  GoldenRatio 3D: a python software for drawing lines based on the golden ratio on a 3D surface (https://github.com/LIOVITT/GoldenRatio)

