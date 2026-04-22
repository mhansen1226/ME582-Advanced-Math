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
  \fancyhead[CO,CE]{\textbf{Homework 12}}
  \fancyhead[RO,RE]{M. Hansen}
  \fancyfoot[CO,CE]{\thepage}
  
  \DeclareMathOperator{\grad}{\nabla}
  \DeclareMathOperator{\diverg}{\nabla \cdot}
  \DeclareMathOperator{\curl}{\nabla \times}
  \DeclareMathOperator{\laplacian}{\Delta}
  \DeclareMathOperator{\Ln}{\operatorname{Ln}}
  \DeclareMathOperator{\Arg}{\operatorname{Arg}}
  \DeclareMathOperator*{\Res}{Res}
  \renewcommand{\Re}{\operatorname{Re}}
  \renewcommand{\Im}{\operatorname{Im}}
  \newcommand{\pder}[2][]{\frac{\partial #1}{\partial #2}}
  \newcommand{\pdder}[2][]{\frac{\partial^2 #1}{\partial #2^2}}
  \newcommand{\parens}[1]{\left( #1 \right)}
  \newcommand{\brackets}[1]{\left[ #1 \right]}
  \newcommand{\braces}[1]{\left\{ #1 \right\}}
  \newcommand{\abs}[1]{\left| #1 \right|}
  \newcommand{\mat}[1]{\mathbf{#1}}
  \renewcommand{\vec}[1]{\mathbf{#1}}
  \newcommand{\infsum}[1][0]{\sum_{n=#1}^\infty}
  \newcommand{\inflim}{\lim_{n \to \infty}}
  \newcommand{\infint}{\int_{-\infty}^{\infty}}
  \newcommand{\pv}{\text{pr. v. }}
---

# Problem 17.1.11

Sketch or graph the given region and its image under the given mapping.

$$
\abs{z} \leqq \frac{1}{2}, \quad
-\frac{\pi}{8} < \Arg z < \frac{\pi}{8}, \quad
w = z^2
$$

## Solution

$$
z = r e^{i \theta}
$$

$$
\begin{aligned}
w &= R e^{i \phi} \\
z^2 &= r^2 e ^{2 i \theta}
\end{aligned}
$$

$$
R = r^2 = \frac{1}{4}
$$

$$
\phi = 2 \theta \implies -\frac{\pi}{4} < \Arg w < \frac{\pi}{4}
$$

![](images/17.1.11.svg)

\newpage
# Problem 17.1.13

Sketch or graph the given region and its image under the given mapping.

$$
2 \leqq \Im z \leqq 5, \quad
w = iz
$$

## Solution

The region is an infinite strip bounded by $z_1 = 2i$ and $z_2 = 5i$, mapping to $w = iz$ gives another infinite strip bounded by

$$
w_1 = i z_1 = -2
$$

$$
w_2 = i z_2 = -5
$$

![](images/17.1.13.svg)

\newpage
# Problem 17.1.15

Sketch or graph the given region and its image under the given mapping.

$$
\abs{z - \frac{1}{2}} \leqq \frac{1}{2}, \quad
w = \frac{1}{z}
$$

## Solution

The boundary of the region $z = x + iy$ has the equation

$$
\begin{aligned}
\parens{x - \frac{1}{2}}^2 + y^2 &= \parens{\frac{1}{2}}^2 \\
x^2 - x + \frac{1}{4} + y^2 &= \frac{1}{4} \\
x^2 - x + y^2 &= 0 \\
x^2 + y^2 &= x \implies \abs{z}^2 = \Re z
\end{aligned}
$$

Applying this relation to $w = u + iv = \frac{1}{z}$ we can find the boundary of the mapping.

$$
\begin{aligned}
\abs{\frac{1}{w}}^2 = \Re \frac{1}{w} \\
\frac{1}{\abs{w}^2} = \Re \frac{1}{u + iv} \\
\frac{1}{\abs{w}^2} = \Re \frac{u - iv}{u^2 + v^2} \\
\frac{1}{\abs{w}^2} = \frac{u}{\abs{w}^2} \\
u = 1 \\
\end{aligned}
$$

This is a vertical line. Since $z_c = \frac{1}{2}$ is within the original region, then $w_c = \frac{1}{z_c} = 2$ which is on the right side of the boundary and therefore the mapped region is the half plane on the positive side of $u=1$

![](images/17.1.15.svg)

\newpage
# Problem 17.1.17

Sketch or graph the given region and its image under the given mapping.

$$
\Ln 2 \leqq x \leqq \Ln 4, \quad
w = e^z
$$

## Solution

The region is an infinite vertical strip bounded by $z_1 = \Ln 2$ and $z_2 = \Ln 4$,

$$
\abs{w_1} = \abs{e^{z_1}} = \abs{e^{\Ln 2}} = 2
$$

$$
\abs{w_2} = \abs{e^{z_2}} = \abs{e^{\Ln 4}} = 4
$$

The new boundary is two concentric circles.

![](images/17.1.17.svg)

\newpage
# Problem 17.1.19

Sketch or graph the given region and its image under the given mapping.

$$
1 < \abs{z} < 4, \quad
\frac{\pi}{4} < \theta \leqq \frac{3\pi}{4}, \quad
w = \Ln z
$$

## Solution

The region is bounded by 4 borders that can be described in the form $z = r e^{i \theta}$. 

Mapping to 
$$
\begin{aligned}
w 
&= \Ln z \\
&= \ln \abs{z} + i \Arg z \\
&= \ln r + i \theta \\
&= u + i v
\end{aligned}
$$

$$
u = r 
\implies \ln 1 < u < \ln 4
$$

$$
v = \theta
\implies \frac{\pi}{4} < v \leqq \frac{3\pi}{4}
$$

![](images/17.1.19.svg)

\newpage
# Problem 17.2.7

Find the inverse $z = z(w)$ Check by solving $z(w)$ for $w$.

$$
w = \frac{i}{2z - 1}
$$

## Solution

$$
\begin{aligned}
w &= \frac{i}{2z - 1} \\
2z - 1 &= \frac{i}{w} \\
z &= \frac{i}{2w} + \frac{1}{2} \\
\end{aligned}
$$

$$
\boxed{z(w) = \frac{i}{2w} + \frac{1}{2}}
$$

\newpage
# Problem 17.2.13

Find the fixed points.

$$
w = 16 z^5
$$

## Solution

$$
\begin{aligned}
f(z) &= z \\
w = 16 z^5 &= z \\
16 z^5 - z &= 0 \\
z \parens{16 z^4 - 1} &= 0
&\implies \boxed{z = 0, \ \pm \frac{1}{2}, \ \pm \frac{1}{2} i}
\end{aligned}
$$

\newpage
# Problem 17.2.15

Find the fixed points.

$$
w = \frac{iz + 4}{2z - 5i}
$$

## Solution

$$
\begin{aligned}
f(z) &= z \\
w = \frac{iz + 4}{2z - 5i} &= z \\
iz + 4 &= 2z^2 - 5iz \\
0 &= 2z^2 - 6iz - 4 \\
0 &= z^2 - 3iz - 2
&\implies \boxed{z = \frac{3i \pm i}{2} = i, 2i} \\
\end{aligned}
$$

\newpage
# Problem 17.2.19

Find all Linear Fractional Transformations (LFTs) with fixed point(s).

$$
z = \pm i
$$

## Solution

$$
w = \frac{az + b}{cz + d}
$$

$$
w = z \implies cz^2 - (a - d)z - b = 0
$$

$$
z = i: \quad ci^2 - (a - d)i - b = -(c + b) - (a - d)i = 0
$$

$$
z = -i: \quad c(-i)^2 - (a - d)(-i) - b = -(c + b) + (a - d)i = 0
$$

From the real parts: $c = -b$

From the imaginary parts: $a = d$

$$
\boxed{w = \frac{az + b}{a - bz}, \quad \forall a, b \in \mathbb{C}}
$$

\newpage
# Problem 17.3.9

Find the LFTs that maps the given three points onto the three given points in the respective order.

$$
1, \ i, \ -1 \text{ onto } i, \ -1, \ -i
$$

## Solution

$$
\begin{aligned}
\frac{w - w_1}{w - w_3} \cdot \frac{w_2 - w_3}{w_2 - w_1}
&= \frac{z - z_1}{z - z_3} \cdot \frac{z_2 - z_3}{z_2 - z_1} \\
\frac{w - i}{w - (-i)} \cdot \frac{(-1) - (-i)}{(-1) - i}
&= \frac{z - 1}{z - (-1)} \cdot \frac{i - (-1)}{i - 1} \\
\frac{w - i}{w + i} \cdot \frac{1 - i}{1 + i}
&= \frac{z - 1}{z + 1} \cdot \frac{i + 1}{i - 1} \\
\end{aligned}
$$

$$
\frac{1 - i}{1 + i} 
= \frac{(1 - i)^2}{1^2 + i^2}
= \frac{-2i}{2}
= -i
$$

$$
\frac{i + 1}{i - 1}
= \frac{(i + 1)^2}{i^2 - 1^2}
= \frac{2i}{-2}
= -i
$$

$$
\begin{aligned}
\frac{w - i}{w + i} &= \frac{z - 1}{z + 1} \\
(w - i)(z + 1) &= (z - 1)(w + i) \\
wz + w - iz - i &= zw + iz - w - i \\
2w &= 2iz \\
w &= iz \\
\end{aligned}
$$

$$
\boxed{w = iz}
$$

\newpage
# Problem 17.3.11

Find the LFT that maps the given three points onto the three given points in the respective order.

$$
-1, \ 0, \ 1 \text{ onto } -i, \ -1, \ i
$$

## Solution

$$
\begin{aligned}
\frac{w - w_1}{w - w_3} \cdot \frac{w_2 - w_3}{w_2 - w_1}
&= \frac{z - z_1}{z - z_3} \cdot \frac{z_2 - z_3}{z_2 - z_1} \\
\frac{w - (-i)}{w - i} \cdot \frac{(-1) - i}{(-1) - (-i)}
&= \frac{z - (-1)}{z - 1} \cdot \frac{0 - 1}{0 - (-1)} \\
\frac{w + i}{w - i} \cdot \frac{-1 - i}{-1 + i}
&= \frac{z + 1}{z - 1} \cdot \frac{1}{-1} \\
\end{aligned}
$$

$$
\frac{-1 - i}{-1 + i}
= \frac{(-1 - i)^2}{(-1)^2 + i^2}
= \frac{2i}{2}
= i
$$

$$
\begin{aligned}
\frac{w + i}{w - i} \cdot i &= \frac{z + 1}{1 - z} \\
(w + i)(1 - z) \cdot i &= (z + 1)(w - i) \\
(w - wz + i - iz) \cdot i &= zw - iz + w - i \\
iw - iwz - 1 + z &= zw - iz + w - i \\
iw - iwz - w - zw &= - iz - i + 1 - z \\
w (i - iz - 1 - z) &= - iz - i + 1 - z \\
w &= \frac{-iz - i + 1 - z}{i - iz - 1 - z} \\
\end{aligned}
$$

$$
\boxed{w = \frac{-(1 + i) z + (1 - i)}{-(1 + i) z + (i - 1)}}
$$

\newpage
# Problem 17.4.1

Find the image of $x = c = \text{const}$, $-\pi < y \leqq \pi$, under $w = e^z$.

## Solution

$$
z = x + iy = c + iy
$$

$$
w = e^c e^{iy}
$$

![](images/17.4.1.svg)

\newpage
# Problem 17.4.3

Find and sketch the image of the given region under $w = e^z$.

$$
-\frac{1}{2} \leqq x \leqq \frac{1}{2}, \quad
-\pi \leqq y \leqq \pi
$$

## Solution

$$
z = x + iy
$$

$$
w = e^x e^{iy}
$$

![](images/17.4.3.svg)

\newpage
# Problem 17.4.5

Find and sketch the image of the given region under $w = e^z$.

$$
-\infty \leqq x \leqq \infty, \quad
0 \leqq y \leqq 2\pi
$$

## Solution

The initial region is an infinite strip between $0 \leqq y \leqq 2\pi$,
$$
z = x + iy
$$

The image fills the entire plane except at the center,
$$
w = e^x e^{iy}
$$

![](images/17.4.5.svg)

\newpage
# Problem 17.4.7

Find and sketch the image of the given region under $w = e^z$.

$$
0 < x < 1, \quad
0 < y < \pi
$$

## Solution



\newpage
# Problem 17.4.11

Find and sketch or graph the image of the given region under $w = \sin z$.

$$
0 < x < \frac{\pi}{2}, \quad
0 < y < 2
$$

## Solution



\newpage
# Problem 17.4.13

Find and sketch or graph the image of the given region under $w = \sin z$.

$$
0 < x < 2\pi, \quad
1 < y < 3
$$

## Solution



\newpage
# Problem 17.4.19

Find the images of the lines mapping $x = c = \text{const}$ under the mapping $w = \cos z$.

## Solution



\newpage
# Problem 17.4.21

Find and sketch or graph the image of the given region under the mapping $w = \cos z$ directly from **Problem 17.4.11**.

$$
0 < x < \frac{\pi}{2}, \quad
0 < y < 2
$$

## Solution
