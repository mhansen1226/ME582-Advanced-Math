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
  \fancyhead[CO,CE]{\textbf{Homework 8}}
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

# Problem 15.1.16

Is the series convergent or divergent? Give a reason.

$$\sum_{n=0}^\infty \frac{(20 + 30i)^n}{n!}$$

# Problem 15.1.17

Is the series convergent or divergent? Give a reason.

$$\sum_{n=2}^\infty \frac{(-i)^n}{\ln n}$$

# Problem 15.1.18

Is the series convergent or divergent? Give a reason.

$$\sum_{n=1}^\infty n^2 \parens{\frac{i}{4}}^n$$

# Problem 15.1.19

Is the series convergent or divergent? Give a reason.

$$\sum_{n=0}^\infty \frac{i^n}{n^2 - i}$$

# Problem 15.1.20

Is the series convergent or divergent? Give a reason.

$$\sum_{n=0}^\infty \frac{n + i}{3n^2 + 2i}$$

# Problem 15.1.21

Is the series convergent or divergent? Give a reason.

$$\sum_{n=0}^\infty \frac{(\pi + \pi i)^{2n + 1}}{(2n + 1)!}$$

# Problem 15.1.22

Is the series convergent or divergent? Give a reason.

$$\sum_{n=1}^\infty \frac{1}{\sqrt n}$$

# Problem 15.1.23

Is the series convergent or divergent? Give a reason.

$$\sum_{n=0}^\infty \frac{(-1)^n (1 + i)^{2n}}{(2n)!}$$

# Problem 15.1.24

Is the series convergent or divergent? Give a reason.

$$\sum_{n=1}^\infty \frac{(3i)^n n!}{n^n}$$

# Problem 15.2.7

Find the center and the radius of convergence.

$$\sum_{n=0}^\infty \frac{(-1)^n}{(2n)!} \parens{z - \frac{1}{2}}^{2n}$$

# Problem 15.2.9

Find the center and the radius of convergence.

$$\sum_{n=0}^\infty \frac{n (n-1)}{3^n} (z - i)^{2n}$$

# Problem 15.2.13

Find the center and the radius of convergence.

$$\sum_{n=0}^\infty 16^n (z+i)^{4n}$$

# Problem 15.2.15

Find the center and the radius of convergence.

$$\sum_{n=0}^\infty \frac{(2n)!}{4^n (n!)^2} (z - 2i)^n$$

# Problem 15.2.17

Find the center and the radius of convergence.

$$\sum_{n=1}^\infty \frac{2^n}{n (n+1)} z^{2n+1}$$

# Problem 15.3.5

Find the radius of convergence in two ways: 

(a) Directly by the Cauchy–Hadamard formula in Sec. 15.2 
(b) From a series of simpler terms by using Theorem 3 or Theorem 4

$$\sum_{n=2}^\infty \frac{n (n-1)}{2^n} (z - 2i)^n$$

# Problem 15.3.7

Find the radius of convergence in two ways: 

(a) Directly by the Cauchy–Hadamard formula in Sec. 15.2 
(b) From a series of simpler terms by using Theorem 3 or Theorem 4

$$\sum_{n=1}^\infty \frac{n}{3^n} (z + 2i)^{2n}$$


# Problem 15.3.9

Find the radius of convergence in two ways: 

(a) Directly by the Cauchy–Hadamard formula in Sec. 15.2 
(b) From a series of simpler terms by using Theorem 3 or Theorem 4

$$\sum_{n=1}^\infty \frac{(-2)^n)}{n (n+1) (n+2)} z^{2n}$$

# Problem 15.3.11

Find the radius of convergence in two ways: 

(a) Directly by the Cauchy–Hadamard formula in Sec. 15.2 
(b) From a series of simpler terms by using Theorem 3 or Theorem 4

$$\sum_{n=1}^\infty \frac{3^n n (n+1)}{7^n} (z + 2)^{2n}$$

# Problem 15.3.13

Find the radius of convergence in two ways: 

(a) Directly by the Cauchy–Hadamard formula in Sec. 15.2 
(b) From a series of simpler terms by using Theorem 3 or Theorem 4

$$
\sum_{n=0}^\infty \brackets{\begin{pmatrix}
    n+k \\ k
\end{pmatrix}}^{-1} z^{n+k}
$$
