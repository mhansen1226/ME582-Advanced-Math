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

# Problem 10.7.17

Evaluate the surface integral $\iint_S \mathbf{F} \cdot \mathbf{n} \ dA$ by the divergence theorem.

$$\mathbf{F} =  \brackets{x^2, y^2, z^2}, \quad S \text{ the surface of the cone } x^2 + y^2 \leqq z^2, \ 0 \leqq z \leqq h$$

## Solution

# Problem 10.7.22

Given a mass of density 1 in a region $T$ of space, find the moment of intertia about the x-axis,

$$I_x = \iiint_T \parens{y^2 + z^2} \ dV$$

$$T: \text{The paraboloid } y^2 + z^2 \leqq x, \ 0 \leqq x \leqq h$$

## Solution

# Problem 10.8.1. Harmonic functions. 

Verify Theorem 1 for $f = 2z^2 - x^2 - y^2$ and $S$ the surface of the box $0 \leqq x \leqq a, \ 0 \leqq y \leqq b, \ 0 \leqq z \leqq c$.

---

**Theorem 1. A Basic Property of Harmonic Functions**

Let $f(x, y, z)$ be a harmonic function in some domain $D$ is space. Let $S$ be any piecewise smooth closed orientable surface in $D$ whose entire region it encloses belongs to $D$. Then the integral of the normal derivative of $f$ taken over $S$ is zero.

---

## Solution

# Problem 10.8.3. Green's First Identity

$$
\boxed{
\iiint_T \parens{f \laplacian g + \grad f \cdot \grad g} \ dV
= \iint_S f \pder[g]{n} \ dA
}
$$

Verify for $f = 4y^2$, $g = x^2$, $S$ the surface of the "unit cube" $0 \leqq x \leqq 1$, $0 \leqq y \leqq 1$, $0 \leqq z \leqq 1$. What are the assumptions of $f$ and $g$? Must $f$ and $g$ be harmonic?

## Solution

# Problem 10.8.5. Green's Second Identity

$$
\boxed{
\iiint_T \parens{f \laplacian g - g \laplacian f} \ dV
= \iint_S \parens{f \pder[g]{n} - g \pder[f]{n}} \ dA
}
$$

Verify for $f = 6y^2$, $g = 2x^2$, $S$ the surface of the "unit cube" $0 \leqq x \leqq 1$, $0 \leqq y \leqq 1$, $0 \leqq z \leqq 1$.

## Solution

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

# Problem 10.9.3

Evaluate the surface integral $\iint_S \parens{\curl \mathbf{F}} \cdot \mathbf{n} \ dA$ for the given $\mathbf{F}$ and $S$.

$$\mathbf{F} = [e^{-z}, e^{-z} \cos y, e^{-z} \sin y], \quad S: z = \frac{y^2}{2}, \ -1 \leqq x \leqq 1, \ 0 \leqq y \leqq 1$$

## Solution

# Problem 10.9.5

Evaluate the surface integral $\iint_S \parens{\curl \mathbf{F}} \cdot \mathbf{n} \ dA$ for the given $\mathbf{F}$ and $S$.

$$
\mathbf{F} = [z^2, \frac{3}{2}x, 0], 
\quad S: 0 \leqq x \leqq a, \ 0 \leqq y \leqq a, \ z = 1
$$

## Solution

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
