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
  \fancyhead[CO,CE]{\textbf{Homework 7}}
  \fancyhead[RO,RE]{M. Hansen}
  \fancyfoot[CO,CE]{\thepage}
  
  \DeclareMathOperator{\grad}{\nabla}
  \DeclareMathOperator{\diverg}{\nabla \cdot}
  \DeclareMathOperator{\curl}{\nabla \times}
  \DeclareMathOperator{\laplacian}{\Delta}
  \DeclareMathOperator{\Ln}{\operatorname{Ln}}
  \renewcommand{\Re}{\operatorname{Re}}
  \renewcommand{\Im}{\operatorname{Im}}
  \newcommand{\pder}[2][]{\frac{\partial #1}{\partial #2}}
  \newcommand{\pdder}[2][]{\frac{\partial^2 #1}{\partial #2^2}}
  \newcommand{\parens}[1]{\left( #1 \right)}
  \newcommand{\brackets}[1]{\left[ #1 \right]}
  \newcommand{\mat}[1]{\mathbf{#1}}
  \renewcommand{\vec}[1]{\mathbf{#1}}
---

# Problem 14.2.9

Integrate $f(z)$ counterclockwise around the unit circle. Indicate whether Cauchy’s integral theorem applies. Show the details.

$$f(z) = \exp(-z^2)$$

## Solution

$f$ is entire since $f'$ is defined everywhere, therefore by Cauchy’s integral theorem

$$
\boxed{\oint_C f(z) \ dz = 0}
$$

# Problem 14.2.11

Integrate $f(z)$ counterclockwise around the unit circle. Indicate whether Cauchy’s integral theorem applies. Show the details.

$$f(z) = \frac{1}{2z-1}$$

## Solution

$f'$ is not defined at $z = \frac{1}{2}$ and therefore Cauchy’s integral theorem does not apply.

$C: z = e^{it}, dz = ie^{it} \ dt, \quad t \in [0, 2\pi]$

$$
\begin{aligned}
\oint_C f(z) \ dz 
&= \oint_C f(z(t)) \dot z(t) \ dt \\
&= \oint_0^{2\pi} \frac{ie^{it}}{2e^{it}-1} \ dt
\end{aligned}
$$

$u = 2e^{it}-1, \ du = 2ie^{it}, \ C'$ is the circle centered at $-1$ with radius $2$

$$
\begin{aligned}
\oint_0^{2\pi} \frac{ie^{it}}{2e^{it}-1} \ dt 
&= \frac{1}{2} \oint_{C'} \frac{1}{u} \ du \\
&= \frac{1}{2} \ln u \Big|_{C'} \\
&= \frac{1}{2} \brackets{\ln |u| + i \arg(u)}_{t=0}^{t=2 \pi} \\
&= \boxed{\pi i}
\end{aligned}
$$

# Problem 14.2.13

Integrate $f(z)$ counterclockwise around the unit circle. Indicate whether Cauchy’s integral theorem applies. Show the details.

$$f(z) = \frac{1}{z^4-1.1}$$

## Solution

$f'$ is not defined at $z = \sqrt[4]{1.1} \approx 1.02$, however this is outside the unit circle and therefore Cauchy’s integral theorem applies.

$$
\boxed{\oint_C f(z) \ dz = 0}
$$

# Problem 14.2.18

Integrate $f(z)$ counterclockwise around the unit circle. Indicate whether Cauchy’s integral theorem applies. Show the details.

$$f(z) = \frac{1}{4z-3}$$

## Solution

$f'$ is not defined at $z = \frac{3}{4}$ and therefore Cauchy’s integral theorem does not apply.

$C: z = e^{it}, dz = ie^{it} \ dt, \quad t \in [0, 2\pi]$

$$
\begin{aligned}
\oint_C f(z) \ dz 
&= \oint_C f(z(t)) \dot z(t) \ dt \\
&= \oint_0^{2\pi} \frac{ie^{it}}{4e^{it}-3} \ dt
\end{aligned}
$$

$u = 4e^{it}-3, \ du = 4ie^{it}, \ C'$ is the circle centered at $-3$ with radius $4$

$$
\begin{aligned}
\oint_0^{2\pi} \frac{ie^{it}}{4e^{it}-3} \ dt 
&= \frac{1}{4} \oint_{C'} \frac{1}{u} \ du \\
&= \frac{1}{4} \ln u \Big|_{C'} \\
&= \frac{1}{4} \brackets{\ln |u| + i \arg(u)}_{t=0}^{t=2 \pi} \\
&= \boxed{\frac{\pi i}{2}}
\end{aligned}
$$

# Problem 14.2.22

Evaluate the integral. Does Cauchy’s theorem apply? Show details.

$$\oint_C \Re z \ dz$$

![C](images/C-14.2.22.png){width=2in}

## Solution

$$f(z) = \Re z = u(x,y) + i v(x,y)$$

$$
\begin{aligned}
u &= x \\
u_x &= 1 \\
u_y &= 0
\end{aligned}
\quad
\begin{aligned}
v &= 0 \\
v_x &= 0 \\
v_y &= 0
\end{aligned}
$$

$u_x \neq v_y$ therefore $f$ is not analytic and Cauchy’s theorem does not apply.

$C_1: z = e^{it}, dz = ie^{it} \ dt, \ \Re z = \cos t, \quad t \in [0, \pi]$
$C_2: z = t, dz = dt, \ \Re z = t, \quad t \in [-1, 1]$

$$
\begin{aligned}
\oint_C f(z) \ dz 
&= \oint_C f(z(t)) \dot z(t) \ dt \\
&= \int_0^\pi \cos t ie^{it} \ dt 
    + \int_{-1}^{1} t \ dt \\
&= \int_0^\pi \cos t i(\cos t + i \sin t) \ dt 
    + \int_{-1}^{1} t \ dt \\
&= i\int_0^\pi \cos^2 t \ dt 
    - \int_0^\pi \cos t \sin t \ dt 
    + \int_{-1}^{1} t \ dt \\
&= \frac{i}{2} \int_0^\pi 1 + \cos 2t \ dt 
    - \frac{1}{2} \int_0^\pi \sin 2t \ dt 
    + \int_{-1}^{1} t \ dt \\
&= \frac{i}{2} \brackets{t + \frac{\sin 2t}{2}}_0^\pi 
    + \frac{1}{4} \brackets{\cos 2t}_0^\pi 
    + \frac{1}{2} \brackets{t^2}_{-1}^{1} \\
&= \frac{i}{2} \brackets{\pi}
    + \frac{1}{4} \brackets{0}
    + \frac{1}{2} \brackets{0} \\
&= \boxed{\frac{\pi i}{2}}
\end{aligned}
$$

# Problem 14.2.24

Evaluate the integral. Does Cauchy’s theorem apply? Show details. *(Use partial fraction)*

$$\oint_C \Re z \ dz$$

![C](images/C-14.2.24.png){width=2in}

## Solution

# Problem 14.3.3

Integrate by Cauchy's formula counterclockwise around the circle.

$$\frac{z^2}{z^2 - 1}, \qquad |z + i| = 1.4$$

## Solution

# Problem 14.3.11

Integrate counterclockwise.

$$
\oint_C \frac{dz}{z^2 + 4}, \quad C: 4x^2 + (y-2)^2 = 4
$$

## Solution

# Problem 14.3.13

Integrate counterclockwise.

$$
\oint_C \frac{z + 2}{z - 2} \ dz, \quad C: |z - 1| = 2
$$

## Solution

# Problem 14.3.15 

Integrate counterclockwise. *(compute it for two squares: one with vertices $\pm 2, \pm 2i$; the other one with vertices $\pm 4, \pm 4i$)*

$$
\oint_C \frac{\cosh \parens{z^2 - \pi i}}{z - \pi i} \ dz, \quad C \text{ the boundary of the square with vertices } \pm 2, \pm 2, \pm 4i
$$

## Solution

# Problem 14.4.1

Integrate counterclockwise around the unit circle.

$$
\oint_C \frac{\sin z}{z^4} \ dz
$$

## Solution

# Problem 14.4.3

Integrate counterclockwise around the unit circle.

$$
\oint_C \frac{e^z}{z^n} \ dz, \quad n = 1, 2, \cdots
$$

## Solution

# Problem 14.4.6

Integrate counterclockwise around the unit circle.

$$
\oint_C \frac{dz}{(z - 2i)^2(z - i/2)^2}
$$

## Solution

# Problem 14.4.11

Integrate. Show the details. *Hint.* Begin by sketching the contour. Why?

$$
\oint_C \frac{(1 + z) \sin z}{(2z - 1)^2} \ dz, \quad C: |z - i| = 2 \text{ counterclockwise}
$$

## Solution
