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

Ratio Test:
$$
\begin{aligned}
\inflim \abs{\frac{a_{n+1}}{a_n}}
&= \inflim \abs{\frac{(-1)^{n+1} (1 + i)^{2(n+1)}}{(2(n+1))!} \cdot \frac{(2n)!}{(-1)^n (1 + i)^{2n}}} \\
&= \inflim \abs{\frac{-(1 + i)^2}{(2n+2)(2n+1)}} \\
&= 0 < 1, \text{ therefore the series converges}
\end{aligned}
$$

# Problem 15.1.24

Is the series convergent or divergent? Give a reason.

$$\infsum[1] \frac{(3i)^n n!}{n^n}$$

## Solution

Ratio Test:
$$
\begin{aligned}
\inflim \abs{\frac{a_{n+1}}{a_n}}
&= \inflim \abs{\frac{(3i)^{n+1} (n+1)!}{(n+1)^{n+1}} \cdot \frac{n^n}{(3i)^n n!}} \\
&= \inflim \abs{\frac{(3i)^{n+1}}{(3i)^n} \cdot \frac{(n+1)!}{n!} \cdot \frac{n^n}{(n+1)^{n+1}}} \\
&= \inflim \abs{3i \cdot (n+1) \cdot \frac{n^n}{(n+1)^n (n+1)}} \\
&= 3 \inflim \abs{\parens{\frac{n}{n+1}}^n} \\
&= 3 \inflim \abs{\frac{1}{\parens{\frac{n+1}{n}}^n}} \\
&= 3 \inflim \abs{\frac{1}{\parens{1 + \frac{1}{n}}^n}} \\
&= 3 \cdot \frac{1}{e} \\
&= \frac{3}{e} > 1, \text{ therefore the series diverges}
\end{aligned}
$$

# Problem 15.2.7

Find the center and the radius of convergence.

$$\infsum \frac{(-1)^n}{(2n)!} \parens{z - \frac{1}{2}}^{2n}$$

## Solution

$$
\begin{aligned}
R 
&= \inflim \abs{\frac{a_n}{a_{n+1}}} \\
&= \inflim \abs{\frac{(-1)^n}{(2n)!} \cdot \frac{(2n + 2)!}{(-1)^{n+1}}} \\
&= \inflim \abs{(2n + 2) (2n + 1)} \\
&= \infty \\
\end{aligned}
$$

The center of convergence is at $z_0 = \frac{1}{2}$ with radius $R = \infty$.

# Problem 15.2.9

Find the center and the radius of convergence.

$$\infsum \frac{n (n-1)}{3^n} (z - i)^{2n}$$

## Solution

Rearranging the power series to the classic form by substituting $n = 2n$,

$$
\infsum \frac{\frac{n}{2} (\frac{n}{2}-1)}{3^\frac{n}{2}} (z - i)^{n}
= \frac{1}{4} \infsum \frac{n (n-2)}{3^\frac{n}{2}} (z - i)^{n}
$$

$$
\begin{aligned}
R
&= \inflim \abs{\frac{a_n}{a_{n+1}}} \\
&= \inflim \abs{\frac{n (n-2)}{3^\frac{n}{2}} \cdot \frac{3^\frac{n+1}{2}}{(n+1)(n-1)}} \\
&= \sqrt 3 \inflim \abs{\frac{n (n-2)}{(n+1)(n-1)}} \\
&= \sqrt 3 \\
\end{aligned}
$$

The center of convergence is at $z_0 = i$ with radius $R = \sqrt 3$.

# Problem 15.2.13

Find the center and the radius of convergence.

$$\infsum 16^n (z+i)^{4n}$$

## Solution

Rearranging the power series to the classic form by substituting $n = 4n$,

$$\infsum 16^\frac{n}{4} (z+i)^n$$

$$
\begin{aligned}
R
&= \inflim \abs{\frac{a_n}{a_{n+1}}} \\
&= \inflim \abs{\frac{16^\frac{n}{4}}{16^\frac{n+1}{4}}} \\
&= \inflim \abs{16^{-\frac{1}{4}}} \\
&= \frac{1}{2} \\
\end{aligned}
$$

The center of convergence is at $z_0 = -i$ with radius $R = \frac{1}{2}$.

# Problem 15.2.15

Find the center and the radius of convergence.

$$\infsum \frac{(2n)!}{4^n (n!)^2} (z - 2i)^n$$

## Solution

$$
\begin{aligned}
R
&= \inflim \abs{\frac{a_n}{a_{n+1}}} \\
&= \inflim \abs{\frac{(2n)!}{4^n (n!)^2} \cdot \frac{4^{n+1} ((n+1)!)^2}{(2n+2)!}} \\
&= \inflim \abs{4 \cdot \frac{(2n)!}{(2n+2)!} \cdot \frac{((n+1)!)^2}{(n!)^2}} \\
&= \inflim \abs{4 \cdot \frac{1}{(2n+2)(2n+1)} \cdot (n+1)^2} \\
&= \inflim \abs{\frac{2n+2}{2n+1}} \\
&= 1
\end{aligned}
$$

The center of convergence is at $z_0 = 2i$ with radius $R = 1$.

# Problem 15.2.17

Find the center and the radius of convergence.

$$\infsum[1] \frac{2^n}{n (n+1)} z^{2n+1}$$

## Solution

$$
\begin{aligned}
L
&= \inflim \abs{\frac{a_{n+1}}{a_n}} \\
&= \inflim \abs{\frac{2^{n+1}}{(n+1)(n+2)} z^{2n+3} \cdot \frac{n (n+1)}{2^n} z^{-(2n+1)}} \\
&= \inflim \abs{2 z^2 \cdot \frac{n}{n+1}} \\
&= 2\abs{z}^2 \\
\end{aligned}
$$

$$
\begin{aligned}
L &< 1 \\
2\abs{z}^2 &< 1 \\
\abs{z}^2 &< \frac{1}{2} \\
\abs{z} &< \frac{1}{\sqrt 2} \\
\end{aligned}
$$

The center of convergence is at $z_0 = 0$ with radius $R = \frac{1}{\sqrt 2}$.

# Problem 15.3.5

Find the radius of convergence in two ways: 

(a) Directly by the Cauchy–Hadamard formula in Sec. 15.2 
(b) From a series of simpler terms by using Theorem 3 or Theorem 4

$$\infsum[2] \frac{n (n-1)}{2^n} (z - 2i)^n$$

## Solution

### Cauchy-Hadamard

$$
\begin{aligned}
R
&= \inflim \abs{\frac{a_n}{a_{n+1}}} \\
&= \inflim \abs{\frac{n (n-1)}{2^n} \cdot \frac{2^{n+1}}{(n+1) n}} \\
&= 2 \cdot \inflim \abs{\frac{n-1}{n+1}} \\
&= 2 \\
\end{aligned}
$$

### Theorem 3: Differentiation

$$
f(z) = \infsum \parens{\frac{z - 2i}{2}}^n = \infsum \frac{1}{2^n} (z - 2i)^n
$$

The geometric series $f(z)$ converges if 

$$
\frac{z - 2i}{2} < 1 \implies R = 2
$$

Differentiating,

$$
\begin{aligned}
f'(z) &= \infsum[1] \frac{n}{2^n} (z - 2i)^{n-1} \\
f''(z) &= \infsum[2] \frac{n (n-1)}{2^n} (z - 2i)^{n-2} \\
\end{aligned}
$$

The original series is equivalent to $f''(z) (z - 2i)^2$ and therefore also converges with $R = 2$

# Problem 15.3.7

Find the radius of convergence in two ways: 

(a) Directly by the Cauchy–Hadamard formula in Sec. 15.2 
(b) From a series of simpler terms by using Theorem 3 or Theorem 4

$$\infsum[1] \frac{n}{3^n} (z + 2i)^{2n}$$

## Solution

### Cauchy-Hadamard

$$
\begin{aligned}
L
&= \inflim \abs{\frac{a_{n+1}}{a_n}} \\
&= \inflim \abs{\frac{3^{n+1}}{n+1} (z + 2i)^{2n+2} \cdot \frac{n}{3^n} (z + 2i)^{-2n}} \\
&= \frac{1}{3} \cdot \inflim \abs{(z + 2i)^2 \cdot \frac{n+1}{n}} \\
&= \frac{1}{3} \abs{z + 2i}^2
\end{aligned}
$$

$$
\begin{aligned}
\frac{1}{3} \abs{z + 2i}^2 &< 1 \\
\abs{z + 2i}^2 &< 3 \\
\abs{z + 2i} &< \sqrt 3 \\
\end{aligned}
$$

Therefore $R = \sqrt 3$

### Theorem 3: Differentiation

$$
f(z) = \infsum \parens{\frac{(z + 2i)^2}{3}}^n = \infsum \frac{1}{3^n} (z + 2i)^{2n}
$$

The geometric series $f(z)$ converges if 

$$
\frac{(z + 2i)^2}{3} < 1 \implies R = \sqrt 3
$$

Differentiating,

$$
\begin{aligned}
f'(z) &= \infsum[1] \frac{2n}{3^n} (z + 2i)^{2n-1} \\
\end{aligned}
$$

The original series is equivalent to $\frac{1}{2} (z + 2i) f'(z)$ and therefore also converges with $R = \sqrt 3$


# Problem 15.3.9

Find the radius of convergence in two ways: 

(a) Directly by the Cauchy–Hadamard formula in Sec. 15.2 
(b) From a series of simpler terms by using Theorem 3 or Theorem 4

$$\infsum[1] \frac{(-2)^n}{n (n+1) (n+2)} z^{2n}$$

## Solution

### Cauchy-Hadamard

$$
\begin{aligned}
L
&= \inflim \abs{\frac{a_{n+1}}{a_n}} \\
&= \inflim \abs{\frac{(-2)^{n+1}}{(n+1) (n+2) (n+3)} z^{2n+2} \cdot \frac{n (n+1) (n+2)}{(-2)^n} z^{-2n}} \\
&= 2 \abs{z}^2 \cdot \inflim \abs{\frac{n (n+1) (n+2)}{(n+1) (n+2) (n+3)}} \\
&= 2 \abs{z}^2 \\
\end{aligned}
$$

$$
\begin{aligned}
L &< 1 \\
2 \abs{z}^2 &< 1 \\
\abs{z}^2 &< \frac{1}{2} \\
\abs{z} &< \frac{1}{\sqrt 2} \\
\end{aligned}
$$

Therefore $R = \frac{1}{\sqrt 2}$

### Theorem 4: Integration

$$
f(z) = \infsum \parens{-2 z^{2}}^n
$$

The geometric series $f(z)$ converges if 

$$
\abs{-2 z^{2}} < 1 \implies R = \frac{1}{\sqrt 2}
$$

Integrating 3 times introduces the factors $\frac{1}{n+1}$, $\frac{1}{n+2}$, and $\frac{1}{n+3}$ which is similar to the original series and it therefore also converges with $R = \frac{1}{\sqrt 2}$

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
