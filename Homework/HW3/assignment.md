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

Evaluate $\int_C \mathbf{F}(\mathbf{r}) \cdot d\mathbf{r}$ counterclockwise around the boundary $C$ of the region $R$ by Green’s theorem, 

$$
\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_R \curl \mathbf{F} \cdot \mathbf{k} \ dA
$$

where

$$
\mathbf{F} = \brackets{
    x^2 e^y, 
    y^2 e^x
}, \qquad
R \text{ the rectangle with vertices (0, 0), (2, 0), (2, 3), (0, 3)}
$$

## Solution.

$$
\begin{aligned}
\oint_C \mathbf{F} \cdot d\mathbf{r} &= \iint_R \curl \mathbf{F} \cdot \mathbf{k} \ dA \\
&= \int_0^3 \int_0^2 \parens{\pder[F_2]{x} - \pder[F_1]{y}} \ dx \ dy \\
&= \int_0^3 \int_0^2 \parens{y^2 e^x - x^2 e^y} \ dx \ dy \\
&= \int_0^3 \brackets{y^2 e^x - \frac{1}{3} x^3 e^y}_{x=0}^{x=2} \ dy \\
&= \int_0^3 \brackets{
    \parens{y^2 e^2 - \frac{1}{3} 2^3 e^y} - \parens{y^2 e^0 - \frac{1}{3} 0^3 e^y}
} \ dy \\
&= \int_0^3 \brackets{
    \parens{y^2 e^2 - \frac{8}{3} e^y} - \parens{y^2}
} \ dy \\
&= \int_0^3 \parens{y^2 (e^2 - 1) - \frac{8}{3} e^y} \ dy \\
&= \frac{1}{3} y^3 (e^2 - 1) - \frac{8}{3} e^y \Big|_0^3 \\
&= \parens{\frac{1}{3} 3^3 (e^2 - 1) - \frac{8}{3} e^3} - \parens{\frac{1}{3} 0^3 (e^2 - 1) - \frac{8}{3} e^0} \\
&= \parens{9 (e^2 - 1) - \frac{8}{3} e^3} - \parens{- \frac{8}{3}} \\
\oint_C \mathbf{F} \cdot d\mathbf{r} &= \boxed{9 (e^2 - 1) - \frac{8}{3} (e^3 - 1)}
\end{aligned}
$$

# Problem 10.4.7.

Evaluate $\int_C \mathbf{F}(\mathbf{r}) \cdot d\mathbf{r}$ counterclockwise around the boundary $C$ of the region $R$ by Green’s theorem, where

$$
\mathbf{F} = \grad \parens{x^3 \cos^2 (xy)}, \qquad
R: 1 \leqq y \leqq 2 - x^2
$$

## Solution.

$$
\begin{aligned}
\oint_C \mathbf{F} \cdot d\mathbf{r} &= \iint_R \curl \mathbf{F} \cdot \mathbf{k} \ dA \\
&= \iint_R \cancelto{0}{\curl \parens{\grad f}} \cdot \mathbf{k} \ dA \\
\oint_C \mathbf{F} \cdot d\mathbf{r} &= \boxed{0}
\end{aligned}
$$

# Problem 10.4.15.

Using the following equation, 

$$
\iint_R \laplacian w \ dA = \oint_C \pder[w]{n} \ ds
$$

Find the value of $\int_C \pder[w]{n} \ ds$ taken counterclockwise over the boundary $C$ of the region $R$.

$$
w = e^x \cos y + xy^3, \qquad
R: 1 \leqq y \leqq 10 - x^2, \quad
x \geqq 0
$$

## Solution.

$$
\begin{aligned}
\laplacian w &= w_{xx} + w_{yy} \\
&= (e^x \cos y) + (-e^x \cos y + 6xy) \\
&= 6xy
\end{aligned}
$$

$$
\begin{aligned}
\oint_C \pder[w]{n} \ ds &= \iint_R \laplacian w \ dA \\
&= \int_0^{3} \int_1^{10 - x^2} 6xy \ dy \ dx \\
&= \int_0^{3} \brackets{3xy^2}_{y=1}^{y=10 - x^2} \ dx \\
&= \int_0^{3} \parens{3x(10 - x^2)^2 - 3x} \ dx \\
&= \int_0^{3} \parens{3x(100 - 20x^2 + x^4) - 3x} \ dx \\
&= \int_0^{3} \parens{297x - 60x^3 + 3x^5} \ dx \\
&= \frac{297}{2}x^2 - 15x^4 + \frac{1}{2}x^6 \Big|_0^{3} \\
&= 1336.5 - 1215 + 364.5 \\
&= \boxed{486}
\end{aligned}
$$

# Problem 10.4.16.

Using the following equation, 

$$
\iint_R \laplacian w \ dx \ dy = \oint_C \pder[w]{n} \ ds
$$

find the value of $\int_C \pder[w]{n} \ ds$ taken counterclockwise over the boundary $C$ of the region $R$.

$$
w = x^2 + y^2, \qquad 
C: x^2 + y^2 = 4
$$

## Solution.

$$
\begin{aligned}
\laplacian w &= w_{xx} + w_{yy} \\
&= (2) + (2) \\
&= 4
\end{aligned}
$$

$$
\begin{aligned}
\oint_C \pder[w]{n} \ ds &= \iint_R \laplacian w \ dA \\
&= 4 \iint_R \ dA \\
&= 4 \cdot \text{Area}(R) \\
&= 4 \cdot \pi \cdot 2^2 \\
&= \boxed{16\pi}
\end{aligned}
$$

## Confirm the answer by direct integration.

$$
C \implies \mathbf{r}(t) = [2 \cos t, 2 \sin t], \quad t \in [0, 2 \pi]
$$

The arc length of $C$ is,

$$
\begin{aligned}
ds 
&= |\mathbf{r}'(t)| \ dt \\
&= \sqrt{(-2 \sin t)^2 + (2 \cos t)^2} \ dt \\
&= 2 \ dt
\end{aligned}
$$

The normal vector is,

$$
\begin{aligned}
\mathbf{n} &= \frac{\grad{x^2 + y^2}}{|\grad{x^2 + y^2}|} \\
&= \frac{[2x, 2y]}{\sqrt{(2x)^2 + (2y)^2}} \\
&= \frac{[x, y]}{\sqrt{x^2 + y^2}}
\end{aligned}
$$

On $C$, $r=2$,

$$
\mathbf{n} = \frac{[x, y]}{2}
$$

The integral of the normal derivative is then,

$$
\begin{aligned}
\oint_C \pder[w]{n} \ ds 
&= \oint_C \grad w \cdot \mathbf{n} \ ds \\
&= \frac{1}{2} \oint_C [2x, 2y] \cdot [x, y] \ ds \\
&= \frac{1}{2} \oint_C 2x^2 + 2y^2 \ ds \\
&= \oint_C x^2 + y^2 \ ds \\
\end{aligned}
$$

On $C$, $x^2 + y^2 = 4$, and $ds=2 \ dt$ where $t \in [0, 2\pi]$,

$$
\begin{aligned}
\oint_C x^2 + y^2 \ ds &= 8 \int_0^{2\pi} \ dt \\
&= 8 \cdot 2\pi \\
&= \boxed{16\pi}
\end{aligned}
$$

# Problem 10.4.19.

Show that $w = e^x \sin y$ satisfies Laplace's equation $\laplacian w = 0$ and, using the following equation, 

$$
\iint_R \brackets{
    \parens{\pder[w]{x}}^2 + \parens{\pder[w]{y}}^2
} \ dx \ dy = \oint_C w \parens{\pder[w]{n}} \ ds
$$

integrate $w \parens{\pder[w]{n}}$ counter-clockwise around the boundary curve $C$ of the rectangle $0 \leqq x \leqq 2$, $0 \leqq y \leqq 5$.

## Solution.

$$
\grad w = [e^x \sin y, e^x \cos y]
$$

$$
\begin{aligned}
\laplacian w &= (e^x \sin y) + (-e^x \sin y) \\
&= \boxed{0}
\end{aligned}
$$

$$
\begin{aligned}
\oint_C w \parens{\pder[w]{n}} \ ds
&= \iint_R \brackets{
    \parens{\pder[w]{x}}^2 + \parens{\pder[w]{y}}^2
} \ dx \ dy \\
&= \iint_R \parens{e^x \sin y}^2 + \parens{e^x \cos y}^2 \ dx \ dy \\
&= \iint_R \parens{e^2x [\sin^2 y + \cos^2 y} \ dx \ dy \\
&= \iint_R \parens{e^2x} \ dx \ dy \\
&= \int_0^5 \int_0^2 \parens{e^2x} \ dx \ dy \\
&= \frac{1}{2} \int_0^5 \brackets{e^2x}_0^2 \ dy \\
&= \frac{1}{2} (e^4 - 1) \int_0^5 \ dy \\
&= \frac{1}{2} (e^4 - 1) \cdot 5 \\
&= \boxed{\frac{5}{2} (e^4 - 1)}
\end{aligned}
$$

# Problem 10.5.2.

Derive a parametric representation, $z = f(x, y)$ or $g(x, y, z) = 0$, by finding the **parameter curves** (curves $u =$ const and $v =$ const) of the surface and a normal vector $\mathbf{N} = \mathbf{r}_u \times \mathbf{r}_v$ of the surface.

$$xy\text{-plane in polar coordinates } \mathbf{r}(u, v) = [u \cos v, u \sin v], \quad (\text{thus } u = r, v = \theta)$$

## Solution.

$$\boxed{z = 0}$$

The parameter curves are,

- $u =$ const $\rightarrow$ concentric circles

- $v =$ const $\rightarrow$ radial straight lines

$$
\begin{aligned}
\mathbf{r}_u &= [\cos v, \sin v] \\
\mathbf{r}_v &= [-u \sin v, u \cos v]
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{N} &= \mathbf{r}_u \times \mathbf{r}_v \\
&= \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\cos v & \sin v & 0 \\
-u \sin v & u \cos v & 0
\end{vmatrix} \\
&= \parens{\cos v \cdot u \cos v - \sin v \cdot (-u \sin v)} \mathbf{k} \\
&= (u \cos^2 v + u \sin^2 v) \mathbf{k} \\
&= u \mathbf{k} \\
\mathbf{N} &= \boxed{[0, 0, u]}
\end{aligned}
$$

# Problem 10.5.3.

Derive a parametric representation by finding the parameter curves of the surface and a normal vector of the surface.

$$\text{Cone } \mathbf{r}(u, v) = [u \cos v, u \sin v, cu]$$

## Solution.

$$
\begin{aligned}
x &= u \cos v \\
y &= u \sin v \\
z &= cu
\end{aligned}
$$

$$
\begin{aligned}
x^2 + y^2 + z^2 &= u^2 (\cos^2 v + \sin^2 v + c^2) \\
x^2 + y^2 + z^2 &= u^2 (1 + c^2) \\
\end{aligned}
$$

But $u = \frac{z}{c}$,

$$
\begin{aligned}
x^2 + y^2 + z^2 &= \frac{z^2}{c^2} (1 + c^2) \\
x^2 + y^2 + \cancel{z^2} &= \frac{z^2}{c^2} + \cancel{z^2} \\
\end{aligned}
$$

$$\boxed{z = c \sqrt{x^2 + y^2}}$$

The parameter curves are,

- $u =$ const $\rightarrow$ concentric circles

- $v =$ const $\rightarrow$ straight lines through the origin

$$
\begin{aligned}
\mathbf{r}_u &= [\cos v, \sin v, c] \\
\mathbf{r}_v &= [-u \sin v, u \cos v, 0]
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{N} &= \mathbf{r}_u \times \mathbf{r}_v \\
&= \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\cos v & \sin v & c \\
-u \sin v & u \cos v & 0
\end{vmatrix} \\
&= \brackets{
    (0 - cu \cos v), 
    -(0 + cu \sin v),
    (u \cos^2 v + u \sin^2 v)
} \\
&= \brackets{
    -cu \cos v, 
    -cu \sin v,
    u
} \\
&= \boxed{u [-c \cos v, -c \sin v, 1]}
\end{aligned}
$$

# Problem 10.5.5.

Derive a parametric representation by finding the parameter curves of the surface and a normal vector of the surface.

$$\text{Paraboloid of revolution } \mathbf{r}(u, v) = [u \cos v, u \sin v, u^2]$$

## Solution.

$$
\begin{aligned}
x &= u \cos v \\
y &= u \sin v \\
z &= u^2
\end{aligned}
$$

$$
\begin{aligned}
x^2 + y^2 + z &= u^2 \cos^2 v + u^2 \sin^2 v + u^2 \\
&= u^2 (\cos^2 v + \sin^2 v + 1) \\
&= u^2 (1 + 1) \\
&= 2u^2
\end{aligned}
$$

But $u^2 = z$,

$$x^2 + y^2 + z = 2z$$

$$\boxed{z = x^2 + y^2}$$

The parameter curves are,

- $u =$ const $\rightarrow$ concentric circles at a given height

- $v =$ const $\rightarrow$ parabolas with vertex at the origin

$$
\begin{aligned}
\mathbf{r}_u &= [\cos v, \sin v, 2u] \\
\mathbf{r}_v &= [-u \sin v, u \cos v, 0]
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{N} &= \mathbf{r}_u \times \mathbf{r}_v \\
&= \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\cos v & \sin v & 2u \\
-u \sin v & u \cos v & 0
\end{vmatrix} \\
&= \brackets{
    (0 - 2u^2 \cos v), 
    -(0 + 2u^2 \sin v),
    (u \cos^2 v + u \sin^2 v)
} \\
&= \boxed{\brackets{
    -2u^2 \cos v, 
    -2u^2 \sin v,
    u
}} \\
\end{aligned}
$$

# Problem 10.5.7.

Derive a parametric representation by finding the parameter curves of the surface and a normal vector of the surface.

$$\text{Ellipsoid } \mathbf{r}(u, v) = [a \cos v \cos u, b \cos v \sin u, c \sin v]$$

## Solution.

$$
\begin{aligned}
x &= a \cos v \cos u \\
y &= b \cos v \sin u \\
z &= c \sin v
\end{aligned}
$$

$$
\begin{aligned}
\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} &= \cos^2 v \cos^2 u + \cos^2 v \sin^2 u + \sin^2 v \\
&= (\cos^2 u + \sin^2 u) \cos^2 v + \sin^2 v \\
&= \cos^2 v + \sin^2 v \\
&= 1 \\
\end{aligned}
$$

$$\boxed{\frac{x^2}{a^2} + \frac{y^2}{b^2} + \frac{z^2}{c^2} = 1}$$

The parameter curves are,

- $u =$ const $\rightarrow$ elipses

- $v =$ const $\rightarrow$ elipses

$$
\begin{aligned}
\mathbf{r}_u &= [-a \cos v \sin u, b \cos v \cos u, 0] \\
\mathbf{r}_v &= [-a \sin v \cos u, -b \sin v \sin u, c \cos v]
\end{aligned}
$$

$$
\begin{aligned}
\mathbf{N} &= \mathbf{r}_u \times \mathbf{r}_v \\
&= \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
-a \cos v \sin u & b \cos v \cos u & 0 \\
-a \sin v \cos u & -b \sin v \sin u & c \cos v
\end{vmatrix} \\
&= \brackets{
    (b c \cos^2 v \cos u - 0),
    -(-a c \cos^2 v \sin u - 0),
    (a b \cos v \sin v \sin^2 u + a b \cos v \sin v \cos^2 u)
} \\
&= \brackets{
    (b c \cos^2 v \cos u),
    (a c \cos^2 v \sin u),
    (a b \cos v \sin v (\sin^2 u + \cos^2 u))
} \\
&= \boxed{\brackets{
    (b c \cos^2 v \cos u),
    (a c \cos^2 v \sin u),
    (a b \cos v \sin v)
}} \\
\end{aligned}
$$

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
