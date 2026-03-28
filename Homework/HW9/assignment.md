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
---

# Problem 15.4.3

Find the Maclaurin series and its radius of convergence.

$$\sin 2 z^2$$

## Solution



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



\newpage
# Problem 15.4.19

Find the Taylor series with center $z_0$ and its radius of convergence.

$$
\frac{1}{1-z}, \quad z_0 = i
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
