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
  \fancyhead[CO,CE]{\textbf{Homework 10}}
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
  \newcommand{\abs}[1]{\left| #1 \right|}
  \newcommand{\mat}[1]{\mathbf{#1}}
  \renewcommand{\vec}[1]{\mathbf{#1}}
  \newcommand{\infsum}[1][0]{\sum_{n=#1}^\infty}
  \newcommand{\inflim}{\lim_{n \to \infty}}
---
# Problem 16.1.1

Expand the function in a Laurent series that converges for $0 < \abs{z} < R$ and determine the precise region of convergence.

$$
\frac{\cos z}{z^4}
$$

## Solution

The Taylor series for $\cos z$ is,

$$
\cos z = \infsum \frac{(-1)^n}{(2n)!} z^{2n},
$$

Dividing by $z^4$,

$$
\boxed{\frac{\cos z}{z^4} 
= \infsum \frac{(-1)^n}{(2n)!} z^{2n-4}}
$$

The Taylor series for $\cos z$ converges with $R=\infty$, so the Laurent series converges for every $z\neq 0$, or $0 < \abs{z} < \infty$.

\newpage
# Problem 16.1.3

Expand the function in a Laurent series that converges for $0 < \abs{z} < R$ and determine the precise region of convergence.

$$
\frac{\exp z^2}{z^3}
$$

## Solution

The Taylor series for $\exp z^2$ is,

$$
\exp z^2 = \infsum \frac{z^{2n}}{n!}
$$

Dividing by $z^3$,

$$
\boxed{\frac{\exp z^2}{z^3} = \infsum \frac{z^{2n-3}}{n!}}
$$

The Taylor series for $\exp z^2$ converges with $R=\infty$, so the Laurent series converges for every $z\neq 0$, or $0 < \abs{z} < \infty$.

\newpage
# Problem 16.1.5

Expand the function in a Laurent series that converges for $0 < \abs{z} < R$ and determine the precise region of convergence.

$$
\frac{1}{z^2 - z^3}
$$

## Solution

$$
\frac{1}{z^2 - z^3} = \frac{1}{z^2} \frac{1}{1 - z}
$$

The Taylor series for the geometric series $\frac{1}{1 - z}$ is,

$$
\frac{1}{1 - z} = \infsum z^n
$$

Dividing by $z^2$,

$$
\boxed{\frac{1}{z^2 - z^3} = \infsum z^{n-2}}
$$

The Taylor series for $\frac{1}{1 - z}$ converges on $\abs{z} < 1$, so the Laurent series converges on $0 < \abs{z} < 1$.

\newpage
# Problem 16.1.8

Expand the function in a Laurent series that converges for $0 < \abs{z} < R$ and determine the precise region of convergence.

$$
\frac{e^z}{z^2 - z^3}
$$

## Solution

The Taylor series for $e^z$ is,

$$
e^z = \infsum \frac{z^n}{n!}
$$

Multiplying by the series from **16.1.5**,

$$
\frac{e^z}{z^2 - z^3} = \infsum \frac{z^{2n-2}}{n!}
$$

The Taylor series for $e^z$ converges everywhere. As in **16.1.5**, the Laurent series converges on $0 < \abs{z} < 1$.

\newpage
# Problem 16.1.13

Find the Laurent series that converges for $0 < \abs{z - i} < R$ and determine the precise region of convergence.

$$
\frac{1}{z^3 \parens{z - i}^2}
$$

## Solution

Substituting $w = z - i$,

$$
\begin{aligned}
\frac{1}{z^3 \parens{z - i}^2}
&= \frac{1}{w^2} \cdot \frac{1}{\parens{i + w}^3} \\
&= \frac{1}{w^2} \cdot \frac{1}{i^3 \parens{1 + \frac{w}{i}}^3} \\
&= \frac{1}{w^2} \cdot \frac{1}{-i \parens{1 - iw}^3} \\
&= \frac{i}{w^2} \cdot \frac{1}{\parens{1 - iw}^3} \\
\end{aligned}
$$

The Taylor series of $\frac{1}{\parens{1 - iw}^3}$ is 

$$
\begin{aligned}
\parens{1 + z}^{-m} &= \infsum \begin{pmatrix} -m \\ n \end{pmatrix} z^n \\
\parens{1 - iw}^{-3} &= \infsum \begin{pmatrix} -3 \\ n \end{pmatrix} (-iw)^n \\
\end{aligned}
$$

Multiplying by $\frac{i}{w^2}$,

$$
\frac{i}{w^2 \parens{1 - iw}^3} 
= \infsum \begin{pmatrix} -3 \\ n \end{pmatrix} -i^{n+1} w^{n-2}
$$

Substituting $z = w + i$,

$$
\boxed{
\frac{1}{z^3 \parens{z - i}^2}
= \infsum \begin{pmatrix} -3 \\ n \end{pmatrix} -i^{n+1} {z-i}^{n-2}
}
$$

The Laurent series converges on $0 < \abs{z - i} < 1$.

\newpage
# Problem 16.1.22

Find all Taylor and Laurent series with center $z_0 = i$. Determine the precise regions of convergence.

$$
\frac{1}{z^2}
$$

## Solution

$\frac{1}{z^2}$ is singular at $z = 0$, therefore a Taylor series can be defined on $\abs{z-i} < 1$ and a Laurent series can be defined on $\abs{z-i} > 1$ 

### Taylor Series

Substituting $w = z - i$,

$$
\frac{1}{z^2} 
= \frac{1}{(i + w)^2} \\
= \frac{1}{i^2 (1 - iw)^2} \\
= \frac{-1}{(1 - iw)^2} \\
$$

The Taylors series of $-(1 - iw)^{-2}$ is

$$
\begin{aligned}
\parens{1 + z}^{-m} &= \infsum \begin{pmatrix} -m \\ n \end{pmatrix} z^n \\
-\parens{1 - iw}^{-2} &= -\infsum \begin{pmatrix} -2 \\ n \end{pmatrix} (-iw)^n \\
\end{aligned}
$$

Substituting $z = w + i$,

$$
\boxed{\frac{1}{z^2} = -\infsum \begin{pmatrix} -2 \\ n \end{pmatrix} (-i)^n (z-i)^n}
$$

### Laurent Series

Substituting $w = z - i$ and rearranging for the Laurent series,

$$
\frac{1}{z^2}
= \frac{1}{(w + i)^2} \\
= \frac{1}{w^2 (1 + \frac{i}{w})^2} \\
= \frac{1}{w^2} \cdot \frac{1}{(1 + \frac{i}{w})^2} \\
$$

The Taylor series of $(1 + \frac{i}{w})^{-2}$

$$
\begin{aligned}
\parens{1 + z}^{-m} &= \infsum \begin{pmatrix} -m \\ n \end{pmatrix} z^n \\
\parens{1 - iw}^{-2} &= \infsum \begin{pmatrix} -2 \\ n \end{pmatrix} \parens{\frac{i}{w}}^n \\
\end{aligned}
$$

Dividing by $w^2$,

$$
\frac{1}{w^2 (w + i)^2}
= \infsum \begin{pmatrix} -2 \\ n \end{pmatrix} \frac{i^n}{w^{n+2}}
$$

Substituting $z = w + i$,

$$
\boxed{
\frac{1}{z^2} 
\infsum \begin{pmatrix} -2 \\ n \end{pmatrix} \frac{i^n}{\parens{z - i}^{n+2}}
}
$$

\newpage
# Problem 16.1.23

Find all Taylor and Laurent series with center $z_0 = 0$. Determine the precise regions of convergence.

$$
\frac{z^8}{1 - z^4}
$$

## Solution

$\frac{z^8}{1 - z^4}$ is singular at $z = \pm 1, \pm i$, therefore a Taylor series can be defined on $\abs{z} < 1$ and a Laurent series can be defined on $\abs{z} > 1$ 

### Taylor Series

$$
\frac{1}{1 - z^4}
= \infsum z^{4n}
$$

$$
\boxed{
\frac{z^8}{1 - z^4}
= \infsum z^{4n + 8}
}
$$

### Laurent Series

$$
\frac{1}{1 - z^4} = \frac{-z^4}{1 - z^{-4}} = -z^4 \infsum z^{-4n}
$$

$$
\boxed{
\frac{z^8}{1 - z^4}
= \infsum z^{4-4n}
}
$$

\newpage
# Problem 16.2.1

Determine the location and order of the zeros.

$$
\sin^4 \frac{1}{2} z
$$

## Solution

$$
\begin{aligned}
&\sin^4 \frac{1}{2} z = 0 \\
&\implies
\sin \frac{1}{2} z = 0 \\
&\implies 
\frac{1}{2} z = n \pi \\
&\implies
\boxed{z = 2 n \pi, \quad n \in \mathbb{Z} \text{ with order 4}}
\end{aligned}
$$

\newpage
# Problem 16.2.3

Determine the location and order of the zeros.

$$
(z + 81 i)^4
$$

## Solution

$$
\begin{aligned}
&(z + 81 i)^4 = 0 \\
&\implies
z + 81 i = 0 \\
&\implies 
\boxed{z = -81 i \text{ with order 4}}
\end{aligned}
$$

\newpage
# Problem 16.2.5

Determine the location and order of the zeros.

$$
z^{-2} \sin^2 \pi z
$$

## Solution

$$
\begin{aligned}
&z^{-2} \sin^2 \pi z = 0 \\
&\implies
\sin^2 \pi z = 0 \\
&\implies 
z = n, \quad n \in \mathbb{Z}  
\end{aligned}
$$

$$
\sin^2 \pi z 
= \parens{\infsum (-1)^n \frac{z^{2n+1}}{(2n+1)!}}^2 
= (\pi z)^2 + \cdots \text{ (higher order powers of z)}
$$

$$
z^{-2} \sin^2 \pi z
= \pi^2 + \cdots \text{ (higher order powers of z)}
$$

Therefore $z = 0$ is a removable singularity and the zeros are

$$
\boxed{z = \pm n, \quad n \in \mathbb{Z}^+ \text{ with order 2}}
$$

\newpage
# Problem 16.2.7

Determine the location and order of the zeros.

$$
z^4 + (1 - 8i) z^2 - 8i
$$

## Solution

$$
\begin{aligned}
z^4 + (1 - 8i) z^2 - 8i
&= z^4 + z^2 - 8i z^2 - 8i \\
&= z^2(z^2 + 1) - 8i (z^2 + 1) \\
&= (z^2 - 8i) (z^2 + 1) \\
\end{aligned}
$$

$$
z^2 = 8i \implies \boxed{z = \pm \sqrt{8i} \text{ with order 1}}
$$

$$
z^2 = -1 \implies \boxed{z = \pm i \text{ with order 1}}
$$

\newpage
# Problem 16.2.9

Determine the location and order of the zeros.

$$
\sin 2z \cos 2z
$$

## Solution

$$
\sin 2z \cos 2z = \frac{1}{2} \sin 4z = 0
\implies \boxed{z = \frac{n \pi}{4}, \quad n \in \mathbb{Z}}
$$

$$
f'(z) = 2 \cos 4z 
\qquad f'\parens{\frac{n \pi}{4}} = 2 (-1)^n \neq 0
$$

Therefore the zeros are all simple zeros

\newpage
# Problem 16.2.13

Determine the location of the singularities, including those at infinity. For poles also state the order. Give reasons.

$$
\frac{1}{\parens{z + 2i}^2} - \frac{z}{z - i} + \frac{z + 1}{\parens{z - i}^2}
$$

## Solution

Poles with order 2: 

$$
\parens{z + 2i}^2
\implies
\boxed{z = -2i}
$$

$$
\parens{z - i}^2
\implies
\boxed{z = i}
$$

Looking at $\infty$,

$$
\begin{aligned}
f(z) = f(1/w) 
&= \frac{1}{\parens{\frac{1}{w} + 2i}^2} 
    - \frac{\frac{1}{w}}{\frac{1}{w} - i} 
    + \frac{\frac{1}{w} + 1}{\parens{\frac{1}{w} - i}^2} \\
&= \frac{w^2}{\parens{1 + 2iw}^2} 
    - \frac{1}{1 - iw} 
    + \frac{w (1 + w)}{\parens{1 - iw}^2} \\
\end{aligned}
$$

As $z \to \infty$ or $w \to 0$,

$$
f \to 0 - 1 + 0 = -1
$$

Therefore the function is bounded at $\infty$.

\newpage
# Problem 16.2.15

Determine the location of the singularities, including those at infinity. For poles also state the order. Give reasons.

$$
z \exp \parens{\frac{1}{\parens{z - 1 - i}^2}}
$$

## Solution

Essential singularity: 

$$
\parens{z - 1 - i}^2
\implies
\boxed{z = 1 + i}
$$

Looking at $\infty$,

$$
\begin{aligned}
f(z) = f(1/w) 
&= \frac{1}{w} \exp \parens{\frac{1}{\parens{\frac{1}{w} - 1 - i}^2}} \\
&= \frac{1}{w} \exp \parens{\frac{w^2}{\parens{1 - w - iw}^2}} \\
\end{aligned}
$$

As $z \to \infty$ or $w \to 0$ there is a simple pole.

\newpage
# Problem 16.2.17

Determine the location of the singularities, including those at infinity. For poles also state the order. Give reasons.

$$
\cot^4 z
$$

## Solution

\newpage
# Problem 16.2.19

Determine the location of the singularities, including those at infinity. For poles also state the order. Give reasons.

$$
\frac{1}{e^z - e^{2z}}
$$

## Solution

\newpage
# Problem 16.2.21

Determine the location of the singularities, including those at infinity. For poles also state the order. Give reasons.

$$
\frac{e^{\frac{1}{z-1}}}{e^z - 1}
$$

## Solution

\newpage
# Problem 16.3.3

Find all the singularities in the finite plane and the corresponding residues.

$$
\frac{\sin 2z}{z^6}
$$

## Solution

\newpage
# Problem 16.3.5

Find all the singularities in the finite plane and the corresponding residues.

$$
\frac{8}{1 + z^2}
$$

## Solution

\newpage
# Problem 16.3.7

Find all the singularities in the finite plane and the corresponding residues.

$$
\cot \pi z
$$

## Solution

\newpage
# Problem 16.3.9

Find all the singularities in the finite plane and the corresponding residues.

$$
\frac{1}{1 - e^z}
$$

## Solution

\newpage
# Problem 16.3.11

Find all the singularities in the finite plane and the corresponding residues.

$$
\frac{e^z}{\parens{z - \pi i}^3}
$$

## Solution
