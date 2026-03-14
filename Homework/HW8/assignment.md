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
  \newcommand{\abs}[1]{\left| #1 \right|}
  \newcommand{\mat}[1]{\mathbf{#1}}
  \renewcommand{\vec}[1]{\mathbf{#1}}
  \newcommand{\infsum}[1][0]{\sum_{n=#1}^\infty}
  \newcommand{\inflim}{\lim_{n \to \infty}}
---

# Problem 15.1.16

Is the series convergent or divergent? Give a reason.

$$\infsum \frac{(20 + 30i)^n}{n!}$$

## Solution

Ratio Test:
$$
\begin{aligned}
\inflim \abs{\frac{a_{n+1}}{a_n}}
&= \inflim \abs{\frac{(20 + 30i)^{n+1}}{(n+1)!} \cdot \frac{n!}{(20 + 30i)^n}} \\
&= \inflim \abs{\frac{20 + 30i}{n+1}} \\
&= \inflim \frac{\sqrt{1300}}{n+1} \\
&= 0 < 1, \text{ therefore the series converges}
\end{aligned}
$$

# Problem 15.1.17

Is the series convergent or divergent? Give a reason.

$$\infsum[2] \frac{(-i)^n}{\ln n}$$

## Solution

The numerator is bounded cyclically so only the denominator affects the series convergence. 

$$
\begin{aligned}
\frac{1}{\ln n} &> \frac{1}{n} \ \forall n \in \mathbb{Z} \ge 2
\end{aligned}
$$

Therefore, the series diverges by direct comparison to the divergent harmonic series.

# Problem 15.1.18

Is the series convergent or divergent? Give a reason.

$$\infsum[1] n^2 \parens{\frac{i}{4}}^n$$

## Solution

Ratio Test:
$$
\begin{aligned}
\inflim \abs{\frac{a_{n+1}}{a_n}}
&= \inflim \abs{\frac{(n+1)^2 \parens{\frac{i}{4}}^{n+1}}{n^2 \parens{\frac{i}{4}}^n}} \\
&= \inflim \abs{\frac{(n+1)^2}{n^2} \cdot \frac{i}{4}} \\
&= \frac{1}{4} \cdot \inflim \frac{(n+1)^2}{n^2} \\
&= \frac{1}{4} \cdot 1 \\
&= \frac{1}{4} < 1, \text{ therefore the series converges}
\end{aligned}
$$

# Problem 15.1.19

Is the series convergent or divergent? Give a reason.

$$\infsum \frac{i^n}{n^2 - i}$$

## Solution

$$\abs{a_n} = \abs{\frac{i^n}{n^2 - i}} = \frac{1}{\sqrt{n^4 + 1}}$$

$$\abs{a_n} < \frac{1}{n^2} \ \forall n \in \mathbb{Z} > 0$$

Therefore, the series converges by direct comparison to the convergent p-series $\infsum \frac{1}{n^2}$.

# Problem 15.1.20

Is the series convergent or divergent? Give a reason.

$$\infsum \frac{n + i}{3n^2 + 2i}$$

## Solution

The real part diverges due to the harmonic series and therefore the series diverges.

$$\infsum \frac{n}{3n^2} = \frac{1}{3} \infsum \frac{1}{n}$$

# Problem 15.1.21

Is the series convergent or divergent? Give a reason.

$$\infsum \frac{(\pi + \pi i)^{2n + 1}}{(2n + 1)!}$$

## Solution

Ratio Test:
$$
\begin{aligned}
\inflim \abs{\frac{a_{n+1}}{a_n}}
&= \inflim \abs{\frac{(\pi + \pi i)^{2n + 3}}{(2n + 3)!} \cdot \frac{(2n + 1)!}{(\pi + \pi i)^{2n + 1}}} \\
&= \inflim \abs{\frac{(\pi + \pi i)^2}{(2n + 3)(2n + 2)}} \\
&= 0 < 1, \text{ therefore the series converges}
\end{aligned}
$$

# Problem 15.1.22

Is the series convergent or divergent? Give a reason.

$$\infsum[1] \frac{1}{\sqrt n}$$

## Solution

$$\frac{1}{\sqrt n} > \frac{1}{n} \ \forall n \in \mathbb{Z} > 1$$

Therefore, the series diverges by direct comparison with the harmonic series.

# Problem 15.1.23

Is the series convergent or divergent? Give a reason.

$$\infsum \frac{(-1)^n (1 + i)^{2n}}{(2n)!}$$

## Solution

# Problem 15.1.24

Is the series convergent or divergent? Give a reason.

$$\infsum[1] \frac{(3i)^n n!}{n^n}$$

## Solution

# Problem 15.2.7

Find the center and the radius of convergence.

$$\infsum \frac{(-1)^n}{(2n)!} \parens{z - \frac{1}{2}}^{2n}$$

## Solution

# Problem 15.2.9

Find the center and the radius of convergence.

$$\infsum \frac{n (n-1)}{3^n} (z - i)^{2n}$$

## Solution

# Problem 15.2.13

Find the center and the radius of convergence.

$$\infsum 16^n (z+i)^{4n}$$

## Solution

# Problem 15.2.15

Find the center and the radius of convergence.

$$\infsum \frac{(2n)!}{4^n (n!)^2} (z - 2i)^n$$

## Solution

# Problem 15.2.17

Find the center and the radius of convergence.

$$\infsum[1] \frac{2^n}{n (n+1)} z^{2n+1}$$

## Solution

# Problem 15.3.5

Find the radius of convergence in two ways: 

(a) Directly by the Cauchy–Hadamard formula in Sec. 15.2 
(b) From a series of simpler terms by using Theorem 3 or Theorem 4

$$\infsum[2] \frac{n (n-1)}{2^n} (z - 2i)^n$$

## Solution

# Problem 15.3.7

Find the radius of convergence in two ways: 

(a) Directly by the Cauchy–Hadamard formula in Sec. 15.2 
(b) From a series of simpler terms by using Theorem 3 or Theorem 4

$$\infsum[1] \frac{n}{3^n} (z + 2i)^{2n}$$


## Solution

# Problem 15.3.9

Find the radius of convergence in two ways: 

(a) Directly by the Cauchy–Hadamard formula in Sec. 15.2 
(b) From a series of simpler terms by using Theorem 3 or Theorem 4

$$\infsum[1] \frac{(-2)^n)}{n (n+1) (n+2)} z^{2n}$$

## Solution

# Problem 15.3.11

Find the radius of convergence in two ways: 

(a) Directly by the Cauchy–Hadamard formula in Sec. 15.2 
(b) From a series of simpler terms by using Theorem 3 or Theorem 4

$$\infsum[1] \frac{3^n n (n+1)}{7^n} (z + 2)^{2n}$$

## Solution

# Problem 15.3.13

Find the radius of convergence in two ways: 

(a) Directly by the Cauchy–Hadamard formula in Sec. 15.2 
(b) From a series of simpler terms by using Theorem 3 or Theorem 4

$$
\infsum \brackets{\begin{pmatrix}
    n+k \\ k
\end{pmatrix}}^{-1} z^{n+k}
$$

## Solution
