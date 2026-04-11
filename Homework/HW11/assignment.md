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
  \fancyhead[CO,CE]{\textbf{Homework 11}}
  \fancyhead[RO,RE]{M. Hansen}
  \fancyfoot[CO,CE]{\thepage}
  
  \DeclareMathOperator{\grad}{\nabla}
  \DeclareMathOperator{\diverg}{\nabla \cdot}
  \DeclareMathOperator{\curl}{\nabla \times}
  \DeclareMathOperator{\laplacian}{\Delta}
  \DeclareMathOperator{\Ln}{\operatorname{Ln}}
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
---

# Problem 16.3.15

Evaluate counterclockwise.

$$
\oint_C \tan 2 \pi z \ dz, 
\quad C:\abs{z - 0.2} = 0.2
$$

## Solution

The function $f(z) = \tan 2 \pi z = \frac{\sin 2 \pi z}{\cos 2 \pi z}$ has simple poles at

$$
\cos 2 \pi z = 0
\implies 2 \pi z = \frac{\pi}{2} + n\pi
\implies z = \frac{1}{4} + \frac{n}{4}, \ n \in \mathbb{Z}
$$

Only $z_0 = \frac{1}{4}$ lies in $C$,

$$
\Res_{z = z_0} f(z) = \frac{\sin 2 \pi z}{-2 \pi\sin 2 \pi z} = -\frac{1}{2 \pi}
$$

The integral is then in the form, $$\oint_C f(z) \ dz = 2 \pi i \Res_{z = z_0} f(z)$$

$$
\oint_C \tan 2 \pi z \ dz 
= 2 \pi i \Res_{z = \frac{1}{4}} f(z)
= \boxed{-i} 
$$

\newpage
# Problem 16.3.17

Evaluate counterclockwise.

$$
\oint_C \frac{e^z}{\cos z} \ dz, 
\quad C:\abs{z - \frac{\pi i}{2}} = 4.5
$$

## Solution



\newpage
# Problem 16.3.19

Evaluate counterclockwise.

$$
\oint_C \frac{\sinh z}{2z - i} \ dz, 
\quad C:\abs{z - 2i} = 2
$$

## Solution



\newpage
# Problem 16.3.21

Evaluate counterclockwise.

$$
\oint_C \frac{\cos \pi z}{z^5} \ dz, 
\quad C:\abs{z} = \frac{1}{2}
$$

## Solution



\newpage
# Problem 16.4.1

Evaluate.

$$
\int_0^\pi \frac{2}{k - \cos \theta} \ d\theta
$$

## Solution



\newpage
# Problem 16.4.7

Evaluate.

$$
\int_0^{2\pi} \frac{a}{a - \sin \theta} \ d\theta
$$

## Solution



\newpage
# Problem 16.4.9

Evaluate.

$$
\int_0^{2\pi} \frac{\cos \theta}{13 - 12 \cos 2\theta} \ d\theta
$$

## Solution



\newpage
# Problem 16.4.11

Evaluate.

$$
\infint \frac{1}{\parens{1 + x^2}^2} \ dx
$$

## Solution



\newpage
# Problem 16.4.15

Evaluate.

$$
\infint \frac{x^2}{x^6 + 1} \ dx
$$

## Solution



\newpage
# Problem 16.4.17

Evaluate.

$$
\infint \frac{\sin 3x}{x^4 + 1} \ dx
$$

## Solution



\newpage
# Problem 16.4.19

Evaluate.

$$
\infint \frac{1}{x^4 - 1} \ dx
$$

## Solution



\newpage
# Problem 16.4.21

Evaluate.

$$
\infint \frac{\sin x}{\parens{x - 1} \parens{x^2 + 4}} \ dx
$$

## Solution



\newpage
# Problem 16.4.25

Find the Cauchy principal value.

$$
\infint \frac{x+5}{x^3 - x} \ dx
$$
