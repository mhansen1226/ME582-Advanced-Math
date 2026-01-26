---
geometry: 
  - margin=1in
header-includes: |
  \usepackage{cancel}
  \usepackage{fancyhdr}
  \pagestyle{fancy}
  \fancyhead[LO,LE]{ME 528 - Spring 2026}
  \fancyhead[CO,CE]{\textbf{Homework 3}}
  \fancyhead[RO,RE]{M. Hansen}
  \fancyfoot[CO,CE]{\thepage}
  
  \DeclareMathOperator{\grad}{\nabla}
  \DeclareMathOperator{\diverg}{\nabla \cdot}
  \DeclareMathOperator{\curl}{\nabla \times}
  \DeclareMathOperator{\laplacian}{\Delta}
  \newcommand{\pder}[2][]{\frac{\partial #1}{\partial #2}}
  \newcommand{\pdder}[2][]{\frac{\partial^2 #1}{\partial #2^2}}
  \newcommand{\parens}[1]{\left( #1 \right)}
  \newcommand{\brackets}[1]{\left[ #1 \right]}
---
# Problem 10.4.3.

Evaluate $\int_C \mathbf{F}(\mathbf{r}) \cdot d\mathbf{r}$ counterclockwise around the boundary $C$ of the region $R$ by Green’s theorem, where

$$
\mathbf{F} = \brackets{
    x^2 e^y, 
    y^2 e^x
}, \qquad
R \text{ the rectangle with vertices (0, 0), (2, 0), (2, 3), (0, 3)}
$$

## Solution.

# Problem 10.4.7.

Evaluate $\int_C \mathbf{F}(\mathbf{r}) \cdot d\mathbf{r}$ counterclockwise around the boundary $C$ of the region $R$ by Green’s theorem, where

$$
\mathbf{F} = \grad \parens{x^3 \cos^2 (xy)}, \qquad
R: 1 \leqq y \leqq 2 - x^2
$$

## Solution.

# Problem 10.4.15.

Using the following equation, 

$$
\iint_R \laplacian w \ dx \ dy = \oint_C \pder[w]{n} ds
$$

Find the value of $\int_C \pder[w]{n} \ ds$ taken counterclockwise over the boundary $C$ of the region $R$.

$$
w = e^x \cos y + xy^3, \qquad
R: 1 \leqq y \leqq 10 - x^2, \quad
x \geqq 0
$$

## Solution.

# Problem 10.4.16.

Using the following equation, 

$$
\iint_R \laplacian w \ dx \ dy = \oint_C \pder[w]{n} \ ds
$$

find the value of $\int_C \pder[w]{n} \ ds$ taken counterclockwise over the boundary $C$ of the region $R$.

$$
W = x^2 + y^2, \qquad 
C: x^2 + y^2 = 4
$$

Confirm the answer by direct integration.

## Solution.

# Problem 10.4.19.

Show that $w = e^x \sin y$ satisfies Laplace's equation $\laplacian w = 0$ and, using the following equation, 

$$
\iint_R \brackets{
    \parens{\pder[w]{x}}^2 + \parens{\pder[w]{y}}^2
} \ dx \ dy = \oint_C w \parens{\pder[w]{n}} \ ds
$$

integrate $w \parens{\pder[w]{n}}$ counter-clockwise around the boundary curve $C$ of the rectangle $0 \leqq x \leqq 2$, $0 \leqq y \leqq 5$.

## Solution.

# Problem 10.5.2.

Derive a parametric representation, $z = f(x, y)$ or $g(x, y, z) = 0$, by finding the **parameter curves** (curves $u =$ const and $v =$ const) of the surface and a normal vector $\mathbf{N} = \mathbf{r}_u \times \mathbf{r}_v$ of the surface.

$$xy\text{-plane in polar coordinates } \mathbf{r}(u, v) = [u \cos v, u \sin v], \quad (\text{thus } u = r, v = \theta)$$

## Solution.

# Problem 10.5.3.

Derive a parametric representation by finding the parameter curves of the surface and a normal vector of the surface.

$$\text{Cone } \mathbf{r}(u, v) = [u \cos v, u \sin v, cu]$$

## Solution.

# Problem 10.5.5.

Derive a parametric representation by finding the parameter curves of the surface and a normal vector of the surface.

$$\text{Paraboloid of revolution } \mathbf{r}(u, v) = [u \cos v, u \sin v, u^2]$$

## Solution.

# Problem 10.5.7.

Derive a parametric representation by finding the parameter curves of the surface and a normal vector of the surface.

$$\text{Ellipsoid } \mathbf{r}(u, v) = [a \cos v \cos u, b \cos v \sin u, c \sin v]$$

## Solution.

# Problem 10.5.14.

Find a normal vector. Sketch the surface and parameter curves.

$$\text{Plane } 4x + 3y + 2z = 12$$

## Solution.

# Problem 10.5.15.

Find a normal vector. Sketch the surface and parameter curves.

$$\text{Cylinder of revolution } (x - 2)^2 + (y + 1)^2 = 25$$

## Solution.

# Problem 10.5.18.

Find a normal vector. Sketch the surface and parameter curves.

$$\text{Elliptic cone } z = \sqrt{x^2 + 4y^2}$$

## Solution.

# Problem 10.6.3.

Evaluate the flux integral, $\int_S \mathbf{F} \cdot \mathbf{n} \ dA$, for the given data. Describe the kind of surface.

$$
\mathbf{F} = [0, x, 0], \qquad
S: x^2 + y^2 + z^2 = 1, \quad
x, y, z \geqq 0
$$

## Solution.

# Problem 10.6.5.

Evaluate the flux integral for the given data. Describe the kind of surface.

$$
\mathbf{F} = [x, y, z], \qquad
S: \mathbf{r} = [u \cos v, u \sin v, u^2], \quad
0 \leqq u \leqq 4, \quad
-\pi \leqq v \leqq \pi
$$

## Solution.

# Problem 10.6.7.

Evaluate the flux integral for the given data. Describe the kind of surface.

$$
\mathbf{F} = [0, \sin y, \cos z], \qquad
S \text{ the cylinder } x = y^2, 
\text { where } 0 \leqq y \leqq \frac{\pi}{4}, \quad
0 \leqq z \leqq y
$$

## Solution.

# Problem 10.6.13.

Evaluate the surface integral, $\iint_S G (\mathbf{r}) \ dA$, for the following data. Indicate the kind of surface.

$$
G = x + y + z, \qquad
z = x + 2y, \quad
0 \leqq x \leqq \pi, \quad
0 \leqq y \leqq x
$$

## Solution.

# Problem 10.6.15.

Evaluate the surface integral for the following data. Indicate the kind of surface.

$$
G = (1 + 9xz)^{3/2}, \qquad
S: \mathbf{r} = [u, v, u^3],
0 \leqq u \leqq 1, \quad
-2 \leqq v \leqq 2
$$

## Solution.
