---
geometry: 
  - margin=1in
header-includes: |
  \usepackage{fancyhdr}
  \pagestyle{fancy}
  \fancyhead[LO,LE]{ME 528}
  \fancyhead[CO,CE]{\textbf{Homework 2}}
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

# Problem 10.2.3.
Show that the form under the integral sign is exact in the plane and evaluate the integral. Show the details of your work.

$$\int_{(\pi / 2, \pi)}^{(\pi, 0)} \parens{\frac{1}{2} \cos \frac{1}{2} x \cos 2y \ dx -2 \sin \frac{1}{2} x \sin 2y \ dy}$$

## Solution.

The form is exact iff $\curl \mathbf{F} = \mathbf{0}$, where $\mathbf{F} = \brackets{\frac{1}{2} \cos \frac{1}{2} x \cos 2y, -2 \sin \frac{1}{2} x \sin 2y}$. For 2D $\mathbf{F}$,

$$
\begin{aligned}
\curl \mathbf{F} &= F_y - F_x \\
&= \parens{-2 \sin \frac{1}{2} x \sin 2y} - \parens{\frac{1}{2} \cos \frac{1}{2} x \cos 2y} \\
&= 0
\end{aligned}
$$

Therefore the form is **exact**. The integral then takes the form,

$$\int_A^B \mathbf{F} \cdot d\mathbf{r} = \int_A^B df = f(B) - f(A)$$

$$
f 
= \int F_1 dx 
= \int \frac{1}{2} \cos \frac{1}{2} x \cos 2y \ dx 
= \sin \frac{1}{2} x \cos 2y + g(x)
$$

$$
f_y 
= -2 \sin \frac{1}{2} x \sin 2y + g_y 
= F_2 
= -2 \sin \frac{1}{2} x \sin 2y, 
\quad g_y = 0, 
\quad g = 0
$$

$$f = \sin \frac{1}{2} x \cos 2y$$

$$\int_{(\pi / 2, \pi)}^{(\pi, 0)} df = f(\pi, 0) - f(\pi / 2, \pi) = \boxed{1 - \frac{\sqrt 2}{2}}$$

# Problem 10.2.5.
Show that the form under the integral sign is exact in space and evaluate the integral. Show the details of your work.

$$\int_{(0,0, \pi)}^{(2,1 / 2, \pi / 2)} e^{x y} (y \sin z \ dx + x \sin z \ dy + \cos z \ dz)$$

## Solution.

The form is exact iff $\curl \mathbf{F} = \mathbf{0}$, where $\mathbf{F} = e^{x y} \brackets{y \sin z, x \sin z, \cos z}$.

$$
\begin{aligned}
\curl \mathbf{F} &= \left| \begin{matrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\pder{x} & \pder{y} & \pder{z} \\
F_1 & F_2 & F_3
\end{matrix} \right| \\
&= \begin{bmatrix}
    (F_3)_y - (F_2)_z \\
    (F_1)_z - (F_3)_x \\
    (F_2)_x - (F_1)_y
\end{bmatrix} 
= \begin{bmatrix}
    \parens{x e^{x y} \cos z}  - \parens{x e^{x y} \cos z} \\
    \parens{y e^{x y} \cos z}  - \parens{y e^{x y} \cos z} \\
    \parens{xy e^{x y} \sin z + e^{x y} \sin z}  - \parens{xy e^{x y} \sin z + e^{x y} \sin z}
\end{bmatrix} 
= \mathbf{0}
\end{aligned}
$$

Therefore the form is **exact**. The integral then takes the form,

$$\int_A^B \mathbf{F} \cdot d\mathbf{r} = \int_A^B df = f(B) - f(A)$$

$$f = \int F_1 dx = \int e^{x y} y \sin z \ dx = e^{x y} \sin z + g(y, z)$$

$$
f_y 
= x e^{x y} \sin z + g_y 
= F_2 
= x e^{x y} \sin z, 
\quad g_y = 0, 
\quad g = h(z)
$$

$$
f_z 
= e^{x y} \cos z + h'(z) 
= F_3 
= e^{x y} \cos z, 
\quad h'(z) = 0, 
\quad h(z) = 0
$$

$$f = e^{x y} \sin z$$

$$
\int_{(0,0, \pi)}^{(2,1 / 2, \pi / 2)} df 
= f(2,1 / 2, \pi / 2) - f(0,0, \pi) 
= e \sin (\pi / 2) - e^{0} \sin (\pi)
= \boxed{e}
$$

# Problem 10.2.13.
Check, and if independent, integrate from $(0, 0, 0)$ to $(a, b, c)$.

$$2e^{x^2} (x \cos 2y \ dx - \sin 2y \ dy)$$

## Solution.

# Problem 10.2.16.
Check, and if independent, integrate from $(0, 0, 0)$ to $(a, b, c)$.

$$e^y \ dx + (x e^y - e^z) \ dy - y e^z \ dz$$

## Solution.

# Problem 10.3.5.
Describe the region of integration and evaluate.

$$\int_0^1 \int_{x^2}^x \parens{1 - 2xy} \ dy \ dx$$

## Solution.

# Problem 10.3.10.
Find the volume of the first octant region bounded by the coordinate planes and the surfaces $y = 1 - x^2$ and $z = 1 - x^2$. Sketch it.

## Solution.

# Problem 10.3.12.
Find the center of gravity $\parens{\bar x, \bar y}$ of a mass of density $f(x, y) = 1$ in the given region $R$.

![](images/region_10.3.12.png){width=2in}\ 

## Solution.

# Problem 10.3.17.
Find $I_x$, $I_y$, $I_0$ of a mass of density $f(x, y) = 1$ in the region $R$.

![](images/region_10.3.13.png){width=2in}\ 

## Solution.
