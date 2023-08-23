# GoldenRatio 3D - Version 1.0
[![License](https://img.shields.io/badge/License-GPLv3-orange.svg)](https://github.com/)

**GoldenRatio 3D** is a Python program that beautifully illustrates the golden ratio in a three-dimensional context.

## Authors and Contributors
- **Lev Nagornov** (Maintainer, Author)

For any inquiries and requests, feel free to contact us at lioliovitt@gmail.com.

## Result
Fibonacci figures projected onto the 3D surface of a sphere.

![Animated Image](https://github.com/LIOVITT/GoldenRatio/blob/main/image.gif)

## Mathematical Description
The program generates a sphere in three-dimensional space using a multidimensional list with linear relationships and constraints ranging from 0 to 2π for θ and from 1.1π to π/3 for φ. These constraints shape the structure to represent the golden ratio's aesthetic appeal more effectively.

The coordinates, x, y, and z, are determined by the following equations:
- x = sin(φ) cos(θ)
- y = sin(φ) sin(θ)
- z = cos(φ)

Where φ and θ are within the following ranges:
- θ ∈ [0, 2π]
- φ ∈ [1.1π, π/3]

The radius in this context remains equal to one.

To derive radius and θ angle values, the following formula is utilized:
- r = a * φ^(2θ/π)

Here, φ is the golden ratio and 'a' is an arbitrary positive real constant.

The range limitation for θ from 0 to 2π is due to the measurement system being in radians. The limitation of θ from 1.1π to π/3 is designed to achieve a cup-like structure.

To transform the coordinates according to the enveloping line:
- y_line = sin(φ_line) sin(θ) * r
- z_line = sin(φ_line) cos(θ) * r
- x_line = sqrt(1 - y_line^2 - z_line^2)

The change in coordinates is guided by the angular rotation rule:
- α = (π/6) * i

Since there are 12 spirals, 'i' ranges from 0 to 11. Thus, the new coordinates for each figure are:
- x_line_d = x_line * cos(α) - y_line * sin(α)
- y_line_d = x_line * sin(α) + y_line * cos(α)
- z_line_d = z_line

## Citing the Program
For referencing in publications, please use the following citation:

- **Model Description and First Version of GoldenRatio**<br>
Lev Nagornov. "GoldenRatio 3D: A Python Software for Drawing Lines Based on the Golden Ratio on a 3D Surface." [GitHub Repository](https://github.com/LIOVITT/GoldenRatio)
