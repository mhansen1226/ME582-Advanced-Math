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
  \fancyhead[CO,CE]{\textbf{Homework 9}}
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

# Problem 15.4.3

Find the Maclaurin series and its radius of convergence.

$$\sin 2 z^2$$

## Solution

$$
\sin (w) = \infsum[1] (-1)^n \frac{w^{2n+1}}{(2n+1)!}
$$

$$
\sin 2 z^2
= \infsum[1] (-1)^n \frac{(2 z^2)^{2n+1}}{(2n+1)!}
= \boxed{\infsum[1] (-1)^n \frac{2^{2n+1} z^{4n+2}}{(2n+1)!}}
$$

$$
\begin{aligned}
L
&= \inflim \abs{\frac{(-1)^{n+1}}{(-1)^n} \cdot \frac{2^{2n+3}}{2^{2n+1}} \cdot \frac{(2n+1)!}{(2n+3)!}} \\
&= \inflim \abs{-1 \cdot 4 \cdot \frac{1}{(2n+3)(2n+2)}} \\
&= 0 \\
\therefore R &= \boxed{\infty}
\end{aligned}
$$

\newpage
# Problem 15.4.16. Inverse sine. 

Developing $1 / \sqrt{1 - z^2}$ and integrating, show that

$$
\sin^{-1} z 
= z 
    + \parens{\frac{1}{2}} \frac{z^3}{3}
    + \parens{\frac{1 \cdot 3}{2 \cdot 4}} \frac{z^5}{5}
    + \parens{\frac{1 \cdot 3 \cdot 5}{2 \cdot 4 \cdot 6}} \frac{z^7}{7}
    + \cdots (\abs{z} < 1)
$$

## Solution

$$f(z) = \sin^{-1} z$$

$$f'(z) = \parens{1 - z^2}^{-1/2}$$

$$
\parens{1 + w}^{-m}
= \infsum \begin{pmatrix} -m \\ n \end{pmatrix} w^n
= 1 - m w
    + \frac{m (m+1)}{2!} w^2 
    - \frac{m (m+1) (m+2)}{3!} w^3 
    + \cdots
$$

$$
\begin{aligned}
f'(z)
&= \infsum \begin{pmatrix} \frac{1}{2} \\ n \end{pmatrix} \parens{-z^2}^n \\
&= 1 - \frac{1}{2} \parens{-z^2} 
    + \frac{\frac{1}{2} (\frac{1}{2}+1)}{2!} \parens{-z^2}^2 
    - \frac{\frac{1}{2} (\frac{1}{2}+1) (\frac{1}{2}+2)}{3!} \parens{-z^2}^3 
    + \cdots \\
&= 1 + \frac{1}{2} z^2
    + \frac{\frac{1}{2} (\frac{3}{2})}{2} z^4
    + \frac{\frac{1}{2} (\frac{3}{2}) (\frac{5}{2})}{6} z^6
    + \cdots \\
&= 1 
    + \parens{\frac{1}{2}} z^2
    + \parens{\frac{1 \cdot 3}{2 \cdot 4}} z^4
    + \parens{\frac{1 \cdot 3 \cdot 5}{2 \cdot 4 \cdot 6}} z^6
    + \cdots
\end{aligned}
$$

Integrating termwise

$$
f(z)
= z 
    + \parens{\frac{1}{2}} \frac{z^3}{3}
    + \parens{\frac{1 \cdot 3}{2 \cdot 4}} \frac{z^5}{5}
    + \parens{\frac{1 \cdot 3 \cdot 5}{2 \cdot 4 \cdot 6}} \frac{z^7}{7}
    + \cdots
$$

This converges on $\abs{z} < 1$ due to the geometric series $f'$

\newpage
# Problem 15.4.19

Find the Taylor series with center $z_0 = i$ and its radius of convergence.

$$
\frac{1}{1-z}
$$

## Solution



\newpage
# Problem 15.4.21

Find the Taylor series with center $z_0$ and its radius of convergence.

$$
\sin z, \quad z_0 = \frac{\pi}{2}
$$

## Solution



\newpage
# Problem 15.4.23

$$
\frac{1}{(z + i)^2}, \quad z_0 = i
$$

## Solution
