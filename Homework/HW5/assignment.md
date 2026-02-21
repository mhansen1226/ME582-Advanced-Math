---
geometry: 
  - margin=1in
header-includes: |
  \usepackage{cancel}
  \usepackage{fancyhdr}
  \pagestyle{fancy}
  \fancyhead[LO,LE]{MA 528 - Spring 2026}
  \fancyhead[CO,CE]{\textbf{Homework 5}}
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
  \newcommand{\mat}[1]{\mathbf{#1}}
  \renewcommand{\vec}[1]{\mathbf{#1}}
  \renewcommand{\Im}{\operatorname{Im}}
  \renewcommand{\Re}{\operatorname{Re}}
---

# Problem 13.3.1

Determine and sketch or graph the sets in the complex plane given by

$$|z + 1 - 5i| \leqq \frac{3}{2}$$

## Solution

$$|z - (-1 + 5i)| \leqq \frac{3}{2}$$

This is a closed disc centered at $(-1 + 5i)$ with radius $1.5$

![](images/13.3.1.svg){width=2.5in}

# Problem 13.3.3

Determine and sketch or graph the sets in the complex plane given by

$$\pi < |z - 4 + 2i| < 3\pi$$

## Solution

$$\pi < |z - (4 - 2i)| < 3\pi$$
This is an open disc centered at $(4 - 2i)$ with outer radius $3\pi$, and inner radius $\pi$

![](images/13.3.3.svg){width=2.5in}

# Problem 13.3.5

Determine and sketch or graph the sets in the complex plane given by

$$|\arg z| < \frac{1}{4}\pi$$

## Solution

$$-\frac{1}{4}\pi < \arg z < \frac{1}{4}\pi$$

This is a wedge from $-\frac{1}{4}\pi$ to $\frac{1}{4}\pi$. There is no bound to the radius of the wedge.

![](images/13.3.5.svg){width=2.5in}

# Problem 13.3.7

Determine and sketch or graph the sets in the complex plane given by

$$\Re z \geqq -1$$

## Solution

This covers the right half of plane bounded at the left by $x=-1$.

![](images/13.3.7.svg){width=2.5in}

# Problem 13.3.11

Find $\Re f$, and $\Im f$ and their values at the given point $z$.

$$f(z) = \frac{1}{1-z} \text{ at } 1 - i$$

## Solution

$z = x+iy$

$$
\begin{aligned}
f(z)
&= \frac{1}{1 - (x+iy)} \\
&= \frac{1}{(1-x) - iy} \\
&= \frac{1}{(1-x) - iy} \cdot \frac{(1-x) + iy}{(1-x) + iy} \\
&= \frac{(1-x) + iy}{(1-x)^2 + y^2} \\
\end{aligned}
$$

$$
\boxed{\Re f(z) = \frac{1-x}{(1-x)^2 + y^2}}
\quad
\boxed{\Im f(z) = \frac{y}{(1-x)^2 + y^2}}
$$

$$
\boxed{\Re f(1 - i) = 0}
\quad
\boxed{\Im f(1 - i) = -1}
$$

# Problem 13.3.23

Find the value of the derivative of

$$\frac{z^3}{(z + 1)^3} \text{ at } i$$

## Solution

# Problem 13.4.3

Is $f$ analytic?

$$f(z) = e^{-2x} (\cos 2y - i \sin 2y)$$

## Solution

# Problem 13.4.5

Is $f$ analytic?

$$f(z) = \Re (z^2) - i \Im (z^2)$$

## Solution

# Problem 13.4.7

Is $f$ analytic?

$$f(z) = \frac{i}{z^8}$$

## Solution

# Problem 13.4.13

Is the function harmonic? If yes, find a corresponding analytic function $f(z) = u(x, y) + iv(x, y)$.

$$u = xy$$

## Solution

# Problem 13.4.17

Is the function harmonic? If yes, find a corresponding analytic function $f(z) = u(x, y) + iv(x, y)$.

$$v = (2x + 1)y$$

## Solution

# Problem 13.4.23

Determine $a$ and $b$ so that the given function is harmonic and find a harmonic conjugate.

$$u = \cosh ax \cos y$$

## Solution

# Problem 13.5.3

Find $e^z$ in the form $u + iv$ and $|e^z|$ if

$$z = 2 \pi i (1 + i)$$

## Solution

# Problem 13.5.9

Write in exponential form

$$4 + 3i$$

## Solution

# Problem 13.5.15

Fine $\Re$ and $\Im$ of

$$\exp (z^2)$$

## Solution

# Problem 13.5.17

Fine $\Re$ and $\Im$ of

$$\exp (z^3)$$

## Solution

# Problem 13.5.19

Find all solutions and graph some of them in the complex plane.

$$e^z = 1$$

## Solution
