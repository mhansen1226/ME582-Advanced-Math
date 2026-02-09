---
geometry: 
  - margin=1in
header-includes: |
  \usepackage{cancel}
  \usepackage{fancyhdr}
  \pagestyle{fancy}
  \fancyhead[LO,LE]{ME 528 - Spring 2026}
  \fancyhead[CO,CE]{\textbf{Homework 4}}
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

# Problem 10.7.11

Evaluate the surface integral $\iint_S \mathbf{F} \cdot \mathbf{n} \ dA$ by the divergence theorem:

$$\boxed{\iint_S \mathbf{F} \cdot \mathbf{n} \ dA = \iiint_T \diverg \mathbf{F} \ dV}$$

$$\mathbf{F} =  \brackets{e^x, e^y, e^z}, \quad S \text{ the surface of the cube } |x| \leqq 1, \ |y| \leqq 1, \ |z| \leqq 1$$

## Solution

$$
\diverg \mathbf{F} = e^x + e^y + e^z
$$

$$
\begin{aligned}
\iint_S \mathbf{F} \cdot \mathbf{n} \ dA &= \iiint_T \diverg \mathbf{F} \ dV \\
&= \int_{-1}^{1} \int_{-1}^{1} \int_{-1}^{1} (e^x + e^y + e^z) \ dx \ dy \ dz \\
&= \int_{-1}^{1} \int_{-1}^{1} \int_{-1}^{1} e^x \ dx \ dy \ dz 
    + \int_{-1}^{1} \int_{-1}^{1} \int_{-1}^{1} e^y \ dx \ dy \ dz 
    + \int_{-1}^{1} \int_{-1}^{1} \int_{-1}^{1} e^z \ dx \ dy \ dz \\
&= 3 \int_{-1}^{1} \int_{-1}^{1} \int_{-1}^{1} e^x \ dx \ dy \ dz \\
&= 12 \int_{-1}^{1} e^x \ dx \\
&= 12 e^x \Big|_{-1}^{1} \\
&= \boxed{12 (e - e^{-1})}
\end{aligned}
$$

# Problem 10.7.13

Evaluate the surface integral $\iint_S \mathbf{F} \cdot \mathbf{n} \ dA$ by the divergence theorem.

$$\mathbf{F} =  \brackets{\sin y, \cos x, \cos z}, \quad S \text{ the surface of } x^2 + y^2 \leqq 4, \ |z| \leqq 2 \text{ (a cylinder and two disks!)}$$

## Solution

$$
\begin{aligned}
\diverg \mathbf{F} &= 0 + 0 - \sin z \\
&= - \sin z
\end{aligned}
$$

$$
\begin{aligned}
\iint_S \mathbf{F} \cdot \mathbf{n} \ dA &= \iiint_T \diverg \mathbf{F} \ dV \\
&= \int_{-2}^{2} \int_{0}^{2\pi} \int_{0}^{2} (- \sin z) r \ dr \ d\theta \ dz \\
&= \int_{0}^{2} r \ dr
\cdot \int_{0}^{2\pi} \ d\theta
\cdot \int_{-2}^{2} (-\sin z) \ dz \\
&= \brackets{\frac{r^2}{2}}_{0}^{2} 
\cdot (2 \pi)  
\cdot [\cos z]_{-2}^2 \\
&= 4 \pi (\cos(2) - \cos(-2)) \\
&= \boxed{0}
\end{aligned}
$$

# Problem 10.7.17

Evaluate the surface integral $\iint_S \mathbf{F} \cdot \mathbf{n} \ dA$ by the divergence theorem.

$$\mathbf{F} =  \brackets{x^2, y^2, z^2}, \quad S \text{ the surface of the cone } x^2 + y^2 \leqq z^2, \ 0 \leqq z \leqq h$$

## Solution

$$
\diverg \mathbf{F} = 2x + 2y + 2z
$$

In cylindrical coordinates,

$$
\diverg \mathbf{F} = 2(r \cos \theta + r \sin \theta + z)
$$

$$
\begin{aligned}
\iint_S \mathbf{F} \cdot \mathbf{n} \ dA &= \iiint_T \diverg \mathbf{F} \ dV \\
&= 2 \int_{0}^{h} \int_{0}^{2\pi} \int_{0}^{z} (r \cos \theta + r \sin \theta + z) r \ dr \ d\theta \ dz \\
&= 2 \int_{0}^{h} \int_{0}^{2\pi} \int_{0}^{z} (r^2 \cos \theta + r^2 \sin \theta + rz \ dr \ d\theta \ dz \\
&= 2 \int_{0}^{h} \int_{0}^{2\pi} \brackets{\frac{r^3}{3} \cos \theta + \frac{r^3}{3} \sin \theta + \frac{r^2}{2}z}_{r=0}^{r=z} \ d\theta \ dz \\
&= 2 \int_{0}^{h} \int_{0}^{2\pi} z^3\parens{\frac{1}{3} \cos \theta + \frac{1}{3} \sin \theta + \frac{1}{2}} \ d\theta \ dz \\
&= 2 \int_{0}^{h} z^3 \ dz \cdot \int_{0}^{2\pi}\parens{\frac{1}{3} \cos \theta + \frac{1}{3} \sin \theta + \frac{1}{2}} \ d\theta \\
&= \frac{1}{2} \brackets{z^4}_{0}^{h} \cdot \brackets{\frac{1}{3} \sin \theta - \frac{1}{3} \cos \theta + \frac{1}{2} \theta}_{0}^{2\pi} \\
&= \boxed{\frac{\pi h^4}{2}} \\
\end{aligned}
$$

# Problem 10.7.22

Given a mass of density 1 in a region $T$ of space, find the moment of intertia about the x-axis,

$$I_x = \iiint_T \parens{y^2 + z^2} \ dV$$

$$T: \text{The paraboloid } y^2 + z^2 \leqq x, \ 0 \leqq x \leqq h$$

## Solution

In cylindrical coordinates along the $x$-axis, the integrand becomes $r^2$ and

$$T: \text{The paraboloid } r^2 \leqq x, \ 0 \leqq x \leqq h$$

$$
\begin{aligned}
I_x &= \iiint_T \parens{y^2 + z^2} \ dV \\
&= \iiint_T \parens{r^2} r \ dr \ d\theta \ dx \\
&= \int_0^h \int_0^{2\pi} \int_0^{\sqrt{x}} \parens{r^2} r \ dr \ d\theta \ dx \\
&= \int_0^h \int_0^{2\pi} \int_0^{\sqrt{x}} \parens{r^3} \ dr \ d\theta \ dx \\
&= \frac{1}{4} \int_0^h \int_0^{2\pi} \parens{x^2} \ d\theta \ dx \\
&= \frac{1}{4} \int_0^h \parens{x^2} \ dx \cdot \int_0^{2\pi} \ d\theta \\
&= \frac{\pi}{6} x^3 \Big|_0^h \\
&= \boxed{\frac{\pi h^3}{6}}
\end{aligned}
$$

# Problem 10.8.1. Harmonic functions. 

---

**Theorem 1. A Basic Property of Harmonic Functions**

Let $f(x, y, z)$ be a harmonic function in some domain $D$ is space. Let $S$ be any piecewise smooth closed orientable surface in $D$ whose entire region it encloses belongs to $D$. Then the integral of the normal derivative of $f$ taken over $S$ is zero.

---

Verify Theorem 1 for $f = 2z^2 - x^2 - y^2$ and $S$ the surface of the box $0 \leqq x \leqq a, \ 0 \leqq y \leqq b, \ 0 \leqq z \leqq c$.

## Solution

$$
\begin{aligned}
\laplacian f &= f_{xx} + f_{yy} + f_{zz} \\
&= (-2) + (-2) + (4) \\
&= 0 
\end{aligned}
$$

$$
\begin{aligned}
\iint_S \pder[f]{n} \ dA &= \iiint_T \cancelto{0}{\laplacian f} \ dV \\
&= \boxed{0}
\end{aligned}
$$

# Problem 10.8.3. Green's First Identity

$$
\boxed{
\iiint_T \parens{f \laplacian g + \grad f \cdot \grad g} \ dV
= \iint_S f \pder[g]{n} \ dA
}
$$

Verify for $f = 4y^2$, $g = x^2$, $S$ the surface of the "unit cube" $0 \leqq x \leqq 1$, $0 \leqq y \leqq 1$, $0 \leqq z \leqq 1$. What are the assumptions of $f$ and $g$? Must $f$ and $g$ be harmonic?

## Solution

$$
\begin{array}{l|cc}
& f & g \\
\hline
& 4y^2 & x^2 \\
\grad & [0, 8y] & [2x, 0] \\
\laplacian & 8 & 2 \\
\end{array}
$$

$$
\begin{aligned}
\iiint_T \parens{f \laplacian g + \grad f \cdot \grad g} \ dV
&= \int_0^1 \int_0^1 \int_0^1 \parens{8y^2} \ dx \ dy \ dz \\
&= \frac{8y^3}{3} \Big|_0^1 \\
&= \boxed{\frac{8}{3}} \\
\end{aligned}
$$

$$
\iint_S f \pder[g]{n} \ dA = \iint_S f \parens{\grad g \cdot \mathbf{n}} \ dA 
$$

Integrating over the cube surface, only the $x=1$ face is non-zero,

$$
\begin{aligned}
\iint_S f \parens{\grad g \cdot \mathbf{n}} \ dA &= \int_0^1 f g_x(x=1) \ dy \\
&= \int_0^1 (4y^2) (2) \ dy \\
&= 8 \int_0^1 y^2 \ dy \\
&= 8 \brackets{\frac{y^3}{3}}_0^1 \\
&= \boxed{\frac{8}{3}} \\
\end{aligned}
$$

The functions do not need to be harmonic, but the divergence theorem assumptions must hold. The functions need to be twice differentiable and $S$ must be piecewise smooth.

# Problem 10.8.5. Green's Second Identity

$$
\boxed{
\iiint_T \parens{f \laplacian g - g \laplacian f} \ dV
= \iint_S \parens{f \pder[g]{n} - g \pder[f]{n}} \ dA
}
$$

Verify for $f = 6y^2$, $g = 2x^2$, $S$ the surface of the "unit cube" $0 \leqq x \leqq 1$, $0 \leqq y \leqq 1$, $0 \leqq z \leqq 1$.

## Solution

$$
\begin{array}{l|cc}
& f & g \\
\hline
& 6y^2 & 2x^2 \\
\grad & [0, 12y] & [4x, 0] \\
\laplacian & 12 & 4 \\
\end{array}
$$

$$
\begin{aligned}
\iiint_T \parens{f \laplacian g - g \laplacian f} \ dV 
&= 24 \int_0^1 \int_0^1 \int_0^1 \parens{y^2 - x^2} \ dx \ dy \ dz \\
&= 24 \parens{\int_0^1 y^2 \ dy - \int_0^1 x^2 \ dx} \cdot \int_0^1 \ dz \\
&= 8 \parens{y^3 \Big|_0^1 - x^3 \Big|_0^1} \\
&= \boxed{0}
\end{aligned}
$$

$$
\iint_S \parens{f \pder[g]{n} - g \pder[f]{n}} \ dA = \iint_S f \parens{\grad g \cdot \mathbf{n}} - g \parens{\grad f \cdot \mathbf{n}}\ dA 
$$

Integrating over the cube surface, only the $x=1$ face (first term) and $y=1$ face (second term) are non-zero,

$$
\begin{aligned}
\iint_S f \parens{\grad g \cdot \mathbf{n}} \ dA &= \int_0^1 f g_x(x=1) \ dy - \int_0^1 g f_y(y=1) \ dx \\
&= \int_0^1 (6y^2) (4) \ dy - \int_0^1 (2x^2) (12) \ dx \\
&= 24 \int_0^1 y^2 \ dy - 24 \int_0^1 x^2 \ dx \\
&= 8 \parens{y^3 \Big|_0^1 - x^3 \Big|_0^1} \\
&= \boxed{0}
\end{aligned}
$$

# Problem 10.8.7

Use the divergence theorem, assuming that the assumptions on $T$ and $S$ are satisfied.

Show that a region $T$ with boundary surface S has the volume

$$
V 
= \iint_S x \ dy \ dz 
= \iint_S y \ dz \ dx
= \iint_S z \ dx \ dy
= \frac{1}{3} \iint_S \parens{x \ dy \ dz + y \ dz \ dx + z \ dx \ dy}
$$

## Solution

Take $\mathbf{F} = [x, 0, 0]$, therefore $\diverg \mathbf{F} = 1$ and

$$
\begin{aligned}
V = \iiint_T \diverg \mathbf{F} \ dV &= \iint_S \mathbf{F} \cdot \mathbf{n} \ dA \\
V &= \iint_S x \ dy \ dz \\
\end{aligned}
$$

Take $\mathbf{F} = [0, y, 0]$, therefore $\diverg \mathbf{F} = 1$ and

$$
\begin{aligned}
V = \iiint_T \diverg \mathbf{F} \ dV &= \iint_S \mathbf{F} \cdot \mathbf{n} \ dA \\
V &= \iint_S y \ dx \ dz \\
\end{aligned}
$$

Take $\mathbf{F} = [0, 0, z]$,

$$
\begin{aligned}
V = \iiint_T \diverg \mathbf{F} \ dV &= \iint_S \mathbf{F} \cdot \mathbf{n} \ dA \\
V &= \iint_S z \ dx \ dy \\
\end{aligned}
$$

Summing the above,

$$
\begin{aligned}
3V &= \iint_S \parens{x \ dy \ dz + y \ dx \ dz + z \ dx \ dy} \\
V &= \frac{1}{3} \iint_S \parens{x \ dy \ dz + y \ dz \ dx + z \ dx \ dy}
\end{aligned}
$$

# Problem 10.9.3

Evaluate the surface integral $\iint_S \parens{\curl \mathbf{F}} \cdot \mathbf{n} \ dA$ directly for the given $\mathbf{F}$ and $S$.

$$\mathbf{F} = [e^{-z}, e^{-z} \cos y, e^{-z} \sin y], \quad S: z = \frac{y^2}{2}, \ -1 \leqq x \leqq 1, \ 0 \leqq y \leqq 1$$

## Solution

$$
\begin{aligned}
\curl \mathbf{F} &= \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\pder{x} & \pder{y} & \pder{z} \\
e^{-z} & e^{-z} \cos y & e^{-z} \sin y
\end{vmatrix} \\
&= \brackets{
    \parens{e^{-z} \cos y + e^{-z} \cos y},
    -\parens{0 + e^{-z}},
    \parens{0 - 0}
} \\
&= \brackets{
    2e^{-z} \cos y,
    -e^{-z},
    0
}
\end{aligned}
$$

$$S: \mathbf{r}(x,y) = [x, y, \frac{y^2}{2}]$$

$$
\begin{aligned}
\mathbf{n} \ dA &= \mathbf{r}_x \times \mathbf{r}_y \ dx \ dy \\
&= \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
1 & 0 & 0 \\
0 & 1 & y
\end{vmatrix} \ dx \ dy \\
&= [0, -y, 1] \ dx \ dy
\end{aligned}
$$

$$
\begin{aligned}
\iint_S \parens{\curl \mathbf{F}} \cdot \mathbf{n} \ dA 
&= \iint_S \brackets{
    2e^{-z} \cos y,
    -e^{-z},
    0
} \cdot [0, -y, 1] \ dx \ dy \\
&= \iint_S \parens{ye^{-z} + 0} \ dx \ dy \\
&= \int_{-1}^{1} \ dx \cdot \int_{0}^{1} ye^{-\frac{y^2}{2}} \ dy \\
&= 2 \int_{0}^{1} ye^{-\frac{y^2}{2}} \ dy \\
&= -2 e^{-\frac{y^2}{2}} \Big|_{0}^{1} \\
&= \boxed{2(1 - e^{-\frac{1}{2}})}
\end{aligned}
$$

# Problem 10.9.5

Evaluate the surface integral $\iint_S \parens{\curl \mathbf{F}} \cdot \mathbf{n} \ dA$ directly for the given $\mathbf{F}$ and $S$.

$$
\mathbf{F} = [z^2, \frac{3}{2}x, 0], 
\quad S: 0 \leqq x \leqq a, \ 0 \leqq y \leqq a, \ z = 1
$$

## Solution

$$
\begin{aligned}
\curl \mathbf{F} &= \begin{vmatrix}
\mathbf{i} & \mathbf{j} & \mathbf{k} \\
\pder{x} & \pder{y} & \pder{z} \\
z^2 & \frac{3}{2}x & 0
\end{vmatrix} \\
&= \brackets{
    \parens{0 - 0},
    -\parens{0 - 2z},
    \parens{\frac{3}{2} - 0}
} \\
&= \brackets{
    0,
    2z,
    \frac{3}{2}
}
\end{aligned}
$$

The surface is a flat plane and therefore $\mathbf{n} \ dA = [0, 0, 1] \ dx \ dy$.

$$
\begin{aligned}
\iint_S \parens{\curl \mathbf{F}} \cdot \mathbf{n} \ dA 
&= \iint_S \brackets{
    0,
    2z,
    \frac{3}{2}
} \cdot [0, 0, 1] \ dx \ dy \\
&= \iint_S \frac{3}{2} \ dx \ dy \\
&= \frac{3}{2} \int_{0}^{a} \ dx \cdot \int_{0}^{a} \ dy \\
&= \boxed{\frac{3a^2}{2}}
\end{aligned}
$$

# Problem 10.9.13

Calculate $\oint_C \mathbf{F} \cdot \mathbf{r}'(s) \ ds$ by Stokes’s theorem,

$$
\boxed{
\iint_S \parens{\curl \mathbf{F}} \cdot \mathbf{n} \ dA
= \oint_C \mathbf{F} \cdot \mathbf{r}'(s) \ ds
}
$$

for the given $\mathbf{F}$ and $C$. Assume the Cartesian coordinates to be right-handed and the $z$-component of the surface normal to be nonnegative.

$$
\mathbf{F} = [-5y, 4x, z], \quad C \text{ the circle } x^2 + y^2 = 16, \ z = 4
$$

## Solution

# Problem 10.9.15

Calculate $\oint_C \mathbf{F} \cdot \mathbf{r}'(s) \ ds$ by Stokes’s theorem for the given $\mathbf{F}$ and $C$. Assume the Cartesian coordinates to be right-handed and the $z$-component of the surface normal to be nonnegative.

$$
\mathbf{F} = [z^3, x^3, y^3], \text{ around the triangle with vertices } (0,0,0), \ (1,0,0), \ (1,1,0)
$$

## Solution

# Problem 10.9.19

Calculate $\oint_C \mathbf{F} \cdot \mathbf{r}'(s) \ ds$ by Stokes’s theorem for the given $\mathbf{F}$ and $C$. Assume the Cartesian coordinates to be right-handed and the $z$-component of the surface normal to be nonnegative.

$$
\mathbf{F} = [z, e^z, 0], \quad C \text{ the boundary curve of the portion of the cone } z = \sqrt{x^2 + y^2}, \ x \geqq 0, \ y \geqq 0, 0 \leqq z \leqq 1
$$

## Solution
