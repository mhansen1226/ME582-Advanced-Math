---
geometry: 
  - margin=1in
header-includes: |
  \usepackage{float}
  \floatplacement{figure}{H}
  \usepackage{cancel}
  \usepackage{fancyhdr}
  \pagestyle{fancy}
  \fancyhead[LO,LE]{MA 528 - Spring 2026}
  \fancyhead[CO,CE]{\textbf{Homework 6}}
  \fancyhead[RO,RE]{M. Hansen}
  \fancyfoot[CO,CE]{\thepage}
  
  \DeclareMathOperator{\grad}{\nabla}
  \DeclareMathOperator{\diverg}{\nabla \cdot}
  \DeclareMathOperator{\curl}{\nabla \times}
  \DeclareMathOperator{\laplacian}{\Delta}
  \DeclareMathOperator{\Ln}{\operatorname{Ln}}
  \DeclareMathOperator{\Arg}{\operatorname{Arg}}
  \renewcommand{\Re}{\operatorname{Re}}
  \renewcommand{\Im}{\operatorname{Im}}
  \newcommand{\pder}[2][]{\frac{\partial #1}{\partial #2}}
  \newcommand{\pdder}[2][]{\frac{\partial^2 #1}{\partial #2^2}}
  \newcommand{\parens}[1]{\left( #1 \right)}
  \newcommand{\brackets}[1]{\left[ #1 \right]}
  \newcommand{\mat}[1]{\mathbf{#1}}
  \renewcommand{\vec}[1]{\mathbf{#1}}
---

# Problem 13.6.1

Show that

a) $\sinh z = \sinh x \cos y + i \cosh x \sin y$

b) $\cosh z = \cosh x \cos y + i \sinh x \sin y$

## Solution

### a)

$$
\begin{aligned}
\sinh z &= \frac{1}{2} (e^{z} - e^{-z}) \\
&= \frac{1}{2} (e^{x+iy} - e^{-x-iy}) \\
&= \frac{1}{2} (e^x e^{iy} - e^{-x} e^{-iy}) \\
&= \frac{1}{2} (e^x (\cos y + i \sin y) - e^{-x} (\cos y - i \sin y)) \\
&= \frac{1}{2} (e^x \cos y + i e^x \sin y - e^{-x} \cos y + i e^{-x} \sin y) \\
&= \frac{1}{2} ((e^x - e^{-x}) \cos y + i (e^x + e^{-x}) \sin y) \\
&= \boxed{\sinh x \cos y + i \cosh x \sin y}
\end{aligned}
$$

### b)

$$
\begin{aligned}
\cosh z &= \frac{1}{2} (e^{z} + e^{-z}) \\
&= \frac{1}{2} (e^{x+iy} + e^{-x-iy}) \\
&= \frac{1}{2} (e^x e^{iy} + e^{-x} e^{-iy}) \\
&= \frac{1}{2} (e^x (\cos y + i \sin y) + e^{-x} (\cos y - i \sin y)) \\
&= \frac{1}{2} (e^x \cos y + i e^x \sin y + e^{-x} \cos y - i e^{-x} \sin y) \\
&= \frac{1}{2} ((e^x + e^{-x}) \cos y + i (e^x - e^{-x}) \sin y) \\
&= \boxed{\cosh x \cos y + i \sinh x \sin y}
\end{aligned}
$$

# Problem 13.6.3

Show that

a) $\cosh^2 z - \sinh^2 z = 1$

b) $\cosh^2 z + \sinh^2 z = \cosh 2z$

## Solution

### a)

$$
\begin{aligned}
\cosh^2 z - \sinh^2 z &= \frac{1}{4} (e^{z} + e^{-z})^2 - \frac{1}{4} (e^{z} - e^{-z})^2 \\
&= \frac{1}{4} \brackets{
    \parens{e^{2z} + 2 + e^{-2z}} 
    - \parens{e^{2z} - 2 + e^{-2z}}
} \\
&= \boxed{1}
\end{aligned}
$$

### b)

$$
\begin{aligned}
\cosh^2 z + \sinh^2 z &=  \frac{1}{4} (e^{z} + e^{-z})^2 + \frac{1}{4} (e^{z} - e^{-z})^2 \\
&= \frac{1}{4} \brackets{
    \parens{e^{2z} + 2 + e^{-2z}} 
    + \parens{e^{2z} - 2 + e^{-2z}}
} \\
&= \frac{1}{4} (2e^{2z} + 2e^{-2z}) \\
&= \frac{1}{2} (e^{2z} + e^{-2z}) \\
&= \boxed{\cosh 2z}
\end{aligned}
$$

# Problem 13.6.7

Find, in the form $u + iv$

a) $\cos i$

b) $\sin i$

## Solution

### a)

$$
\cos i = \boxed{\cosh 1}
$$

### b)

$$
\sin i = \boxed{i \sinh 1}
$$

# Problem 13.6.13

Using the definitions, prove

a) $\cos z$ is even, $\cos(-z) = \cos z$

b) $\sin z$ is odd, $\sin(-z) = -\sin z$

## Solution

### a)

$$
\begin{aligned}
\cos(-z) &= \frac{1}{2} \parens{e^{i \cdot (-z)} + e^{-i \cdot (-z)}} \\
&= \frac{1}{2} \parens{e^{-iz} + e^{iz}} \\
&= \boxed{\cos z}
\end{aligned}
$$

### b)

$$
\begin{aligned}
\sin(-z) &= \frac{1}{2i} \parens{e^{i \cdot (-z)} - e^{-i \cdot (-z)}} \\
&= \frac{1}{2i} \parens{e^{-iz} - e^{iz}} \\
&= \boxed{-\sin z}
\end{aligned}
$$

# Problem 13.6.16

Find all solutions

$$\sin z = 100$$

## Solution

$$
\sin z = \frac{1}{2i} \parens{e^{iz} - e^{-iz}} = 100
$$

Let $w = e^{iz}$. Then $w - w^{-1} = 100i$

$$
w^2 - 200iw - 1 = 0 \quad \implies \quad w = i(100 \pm \sqrt{9999})
$$

Thus $e^{iz} = i(100 \pm \sqrt{9999})$, so

$$
\begin{aligned}
iz &= \ln(i(100 \pm \sqrt{9999})) \\
&= \ln|i(100 \pm \sqrt{9999})| + i \Arg(i(100 \pm \sqrt{9999})) + i 2 \pi n \\
&= \ln(100 \pm \sqrt{9999}) + i \frac{\pi}{2} + i 2 \pi n \\
&= \pm \ln(100 + \sqrt{9999}) + i \pi \parens{2 n + \frac{1}{2}}\\
\end{aligned}
$$

Dividing by $i$,

$$
\boxed{
z =  \pi \parens{2 n + \frac{1}{2}} \pm \ln(100 + \sqrt{9999}) \quad n \in \mathbb{Z}
}
$$

# Problem 13.7.5

Find

$$\Ln (-11)$$

## Solution

$$
\begin{aligned}
\Ln (-11) &= \ln|-11| + i \Arg(-11) \\
= \boxed{\ln 11 + i \pi}
\end{aligned}
$$

# Problem 13.7.7

Find

$$\Ln (4 - 4i)$$

## Solution

$$
\begin{aligned}
\Ln (4 - 4i) &= \ln|4 - 4i| + i \Arg(4 - 4i) \\
&= \ln \sqrt{4^2 + 4^2} + i \tan^{-1} \parens{\frac{-4}{4}} \\
&= \ln \sqrt{32} + i \tan^{-1} (-1) \\
&= \boxed{\frac{1}{2} \ln 32 - i\frac{\pi}{4}}
\end{aligned}
$$

# Problem 13.7.8

Find

$$\Ln (1 \pm i)$$

## Solution

$$
\begin{aligned}
\Ln (1 \pm i) &= \ln|1 \pm i| + i \Arg(1 \pm i) \\
&= \ln \sqrt{2} + i \tan^{-1} \parens{\frac{\pm 1}{1}} \\
&= \ln \sqrt{2} + i \tan^{-1} (\pm 1) \\
&= \boxed{\frac{1}{2} \ln 2 \pm i \frac{\pi}{4}} \\
\end{aligned}
$$

# Problem 13.7.15

Find all values and graph some in the complex plane

$$\ln (e^i)$$

## Solution

$$
\begin{aligned}
\ln (e^i) &= \ln |e^i| + i \Arg (e^i) + i 2 \pi n \\
&= \ln 1 + i + i 2 \pi n \\
&= \boxed{i (1 + 2 \pi n) \quad n \in \mathbb{Z}}
\end{aligned}
$$

![Solutions of $\ln (e^i)$](images/13.7.15.svg){width=3.5in}

# Problem 13.7.19

Solve for $z$

$$\ln z = 4 - 3i$$

## Solution

# Problem 13.7.23

Find the principal value.

$$(1 + i)^{1-i}$$

## Solution

# Problem 14.1.1

Find and sketch the path

$$z(t) = (1 + \frac{1}{2}i)t \quad (2 \leqq t \leqq 5)$$

## Solution

# Problem 14.1.11

Find a parametric representation and sketch the path

$$\text{Segment from } (-1, 1) \text{ to } (1, 3)$$

## Solution

# Problem 14.1.19

Find a parametric representation and sketch the path

$$\text{Parabola } y = 1 - \frac{1}{4} x^2 \quad (-2 \leq x \leq 2)$$

## Solution

# Problem 14.1.21

Integrate by the first method or state why it does not apply and use the second method. Show the details.

$$\int_C \Re z \ dz, \quad \text{C the shortest path from } 1 + i \text{ to } 3 + 3i$$

## Solution

# Problem 14.1.25

$$\int_C z \exp(z^2) \ dz, \quad \text{C from } 1 \text{ along the axes to } i$$

## Solution

# Problem 14.1.29

$$\int_C \Im z^2 \ dz \quad \text{counterclockwise around the triangle with vertices } 0, \ 1, \ i$$

## Solution
