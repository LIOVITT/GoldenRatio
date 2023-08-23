GoldenRatio 3D version 1.0
====================
[![License](https://img.shields.io/badge/License-MIT-red.svg)](https://github.com/LIOVITT/GoldenRatio/blob/main/LICENSE)

**GoldenRatio 3D** is a Python program that beautifully illustrates the golden ratio in a three-dimensional context.

Authors and Contributors:
---
- **Lev Nagornov** (Maintainer, Author)

For any inquiries and requests, feel free to contact us at lioliovitt@gmail.com.

Result
---

Fibonacci figures projected onto the 3D surface of a sphere.

![My Image](https://github.com/LIOVITT/GoldenRatio/blob/main/image.gif)


Mathematical Description
---
The program generates a sphere in three-dimensional space using a multidimensional list with linear relationships and constraints ranging from 0 to 2π for θ and from 1.1π to π/3 for φ. These constraints shape the structure to represent the golden ratio's aesthetic appeal more effectively.

The coordinates, $x$, $y$ and $z$ are determined by the following equations:


$x = sin(\phi) cos(\theta),$

$y = sin(\phi) sin(\theta), $

$z = cos(\phi)$

Where φ and θ are within the following ranges:

$\theta \in [0, 2\pi]$

$\phi \in [1.1 \pi,\pi/3]$

The radius in this context remains equal to one.

To derive radius and θ angle values, the following formula is utilized:
$r=a\Phi^{2\theta/\pi}$,

Here, φ is the golden ratio and 'a' is an arbitrary positive real constant.

The range limitation for θ from 0 to 2π is due to the measurement system being in radians. The limitation of θ from 1.1π to π/3 is designed to achieve a cup-like structure.

$\phi_{line} \in [\pi, \pi/2]$

Value for the sphere envelope line


To transform the coordinates according to the enveloping line:

$y_{line} = sin(\phi_{line})sin(\theta)r$

$z_{line} = sin(\phi_{line})cos(\theta)r$

$x_{line} = \sqrt{1-y_{line}^2-z_{line}^2}$


The change in coordinates is guided by the angular rotation rule:

$\alpha = (\pi/6)i$

Since there are 12 spirals, 'i' ranges from 0 to 11. Thus, the new coordinates for each figure are:

$x_{line_{d}} = x_{line}cos(\alpha) - y_{line}sin(\alpha)$

$y_{line_{d}} = x_{line}sin(\alpha) + y_{line}cos(\alpha)$

$z_{line_{d}} = z_{line}$


## Cite program

For publication, please, be kind to use next reference:

- Model description and first version of GoldenRatio

Lev Nagornov,  GoldenRatio 3D: a python software for drawing lines based on the golden ratio on a 3D surface (https://github.com/LIOVITT/GoldenRatio)

