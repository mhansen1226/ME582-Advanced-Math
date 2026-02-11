---
geometry: 
  - margin=0.25in
classoption: 
  - twocolumn
header-includes: |
  \DeclareMathOperator{\grad}{\nabla}
  \DeclareMathOperator{\diverg}{\nabla \cdot}
  \DeclareMathOperator{\curl}{\nabla \times}
  \DeclareMathOperator{\laplacian}{\Delta}
  \newcommand{\pder}[2][]{\frac{\partial #1}{\partial #2}}
  \newcommand{\pdder}[2][]{\frac{\partial^2 #1}{\partial #2^2}}
  \newcommand{\parens}[1]{\left( #1 \right)}
  \newcommand{\brackets}[1]{\left[ #1 \right]}
---

# Derivatives

## Gradient
$$
\operatorname{grad} f 
= \grad f 
= \brackets{f_x, f_y, f_z}
$$

## Directional Derivative
$$
D_{\mathbf{a}}f 
= \frac{df}{ds} 
= \frac{\mathbf{a}}{|\mathbf{a}|} \grad f
$$

## Divergence
$$
\operatorname{div} \mathbf{v} 
= \diverg \mathbf{v} 
= \pder[v_1]{x} + \pder[v_2]{y} + \pder[v_3]{z}
$$

$\diverg \mathbf{v} = 0 \rightarrow$ **incompressible**

## Curl
$$
\operatorname{curl} \mathbf{v} 
= \curl \mathbf{v} 
= \begin{vmatrix}
    \mathbf{i} & \mathbf{j} & \mathbf{k} \\
    \pder{x} & \pder{y} & \pder{z} \\
    v_1 & v_2 & v_3
\end{vmatrix}
$$

## Laplacian
$$ 
\laplacian f
= \diverg (\grad f)
= \nabla^2 f
= f_{xx} + f_{yy} + f_{zz}
$$

## Common Equalities

$\grad {fg} 
= f \grad g + g \grad f$

$\grad {\frac{f}{g}} 
= \frac{g \grad f - f \grad g}{g^2}$

$\diverg (f \mathbf{v}) 
= f \diverg \mathbf{v} + \mathbf{v} \cdot \grad f$

$\diverg (f \grad g) 
= f \laplacian g + \grad f \cdot \grad g$

$\laplacian (fg)
= f \laplacian g + 2 \grad f \cdot \grad g + g \laplacian f$

$\curl (f \mathbf{v})
= \grad f \times \mathbf{v} + f (\curl \mathbf{v})$

$\diverg (\mathbf{u} \times \mathbf{v})
= \mathbf{v} \cdot (\curl \mathbf{u}) - \mathbf{u} \cdot (\curl \mathbf{v})$

$\curl (\grad f) = \mathbf{0}$

$\diverg (\curl \mathbf{v}) = 0$

## Normal Vector

**Case $f(x,y,z) =$ const:** $\mathbf{N} = \grad f$

**Case $z = f(x,y)$:** $\mathbf{N} = [f_x, f_y, -1]$

## Tangent Plane

At point $(x_0, y_0, z_0)$, the tangent plane is
$$N_x (x-x_0) + N_y (y-y_0) + N_z (z-z_0) = 0$$

# Line Integrals
Arc Length $ds = |\mathbf{r}'(t)| \ dt$

$$
\begin{aligned}
\int_C \mathbf{F} (\mathbf{r}) \cdot d\mathbf{r} 
&= \int_a^b \mathbf{F} (\mathbf{r}(t)) \cdot \mathbf{r}'(t) \ dt \\
\int_C (F_1 \ dx + F_2 \ dy + F_3 \ dz)
&= \int_a^b (F_1 x' + F_2 y' + F_3 z') \ dt
\end{aligned}
$$

The line integral is **path independent** iff,

1. Field is **conservative**: $\mathbf{F} = \grad f$
2. Value around all closed paths is **zero** 
3. Field is **exact**: $\curl \mathbf{F} = \mathbf{0}$

Note: If $\mathbf{F}$ is defined on a *simply connected domain* (i.e. no holes), then $\mathbf{F}$ is conservative $\iff$ $\mathbf{F}$ is exact

If path independent,
$$
\int_A^B \mathbf{F} \cdot d\mathbf{r}
= \int_A^B \grad f \cdot d\mathbf{r}
= f(B) - f(A)
$$

## Finding $f$ such that $\mathbf{F} = \grad f$

1. Verify the field is exact.
2. Integrate one component of $\mathbf{F}$ wrt the corresponding variable. The result is a fn plus an unknown fn of the other variables. Ex.
$$f = \int F_1 dx + g(y, z)$$
3. Take the partial of the next variable and equate to corresponding component.
4. Rinse & repeat. If functions turn out to be a constant, choose zero.

## Green's Theorem
$$
\begin{aligned}
\iint_{R} \curl \mathbf{F} \cdot \mathbf{k} \ dA
&= \oint_C \mathbf{F} \cdot d\mathbf{r} \\
\iint_{R} \parens{\pder[F_2]{x} - \pder[F_1]{y}} \ dx \ dy
&= \oint_C (F_1 \ dx + F_2 \ dy)
\end{aligned}
$$

## Area Formulas

$\text{Area} = \oint_C x \ dy$

$\text{Area} = -\oint_C y \ dx$

$\text{Area} = \frac{1}{2} \oint_C (x \ dy - y \ dx)$

$\text{Area} = \frac{1}{2} \oint_C r^2 \ d\theta$

## Transforming the Laplacian

$$
\iint_R \laplacian w \ dA 
= \oint_C \grad w \cdot \mathbf{n} \ ds
= \oint_C \pder[w]{n} \ ds
$$

# Surfaces
$$\mathbf{r} = \mathbf{r(u,v)}$$
$$\mathbf{N} = \mathbf{r}_u \times \mathbf{r}_v$$

## Cylinder $x^2 + y^2 = a^2, \quad |z| \leq 1$
$$
\mathbf{r}(z, \theta) = \begin{bmatrix}
	a \cos \theta \\
	a \sin \theta \\
	z
\end{bmatrix}, 
\quad \theta \in [0, 2\pi]
$$

## Sphere $x^2 + y^2 + z^2 = a^2$
$$
\mathbf{r}(\phi, \theta) = \begin{bmatrix}
	a \sin \phi \cos \theta \\
	a \sin \phi \sin \theta \\
	a \cos \phi
\end{bmatrix},
\quad \begin{array}{l}
\phi \in [0, \pi] \\
\theta \in [0, 2\pi]
\end{array}
$$

## Cone $z = \sqrt{x^2 + y^2}$
$$
\mathbf{r}(r, \theta) = \begin{bmatrix}
	r \cos \theta \\
	r \sin \theta \\
	r
\end{bmatrix}, 
\quad \begin{array}{l}
r \in [0, H] \\
\theta \in [0, 2\pi]
\end{array}
$$

## Torus 
With major radius $R$, and minor radius $r$
$$
\mathbf{r}(\phi, \theta) = \begin{bmatrix}
	(R + r \cos \phi) \cos \theta \\
	(R + r \cos \phi) \sin \theta \\
	r \sin \phi
\end{bmatrix}, 
\quad \begin{array}{l}
\phi \in [0, 2\pi] \\
\theta \in [0, 2\pi]
\end{array}
$$

# Surface Integrals
Area element $dA = ||\mathbf{r}_u \times \mathbf{r}_v|| \ du \ dv = ||\mathbf{N}|| \ du \ dv$

## Flux

The amount of fluid passing through a surface $S$ per unit time. $S$ can also be parameterized as $\mathbf{r}(u,v)$ for $(u,v) \in \Omega$.
$$
\text{Flux} = \iint_S \mathbf{F} \cdot \mathbf{n} \ dA = \iint_\Omega \mathbf{F}(\mathbf{r}) \cdot ||\mathbf{N}|| \ du \ dv
$$

## Surface Area
$$
\text{Surface Area} = \iint_\Omega ||\mathbf{N}|| \ du \ dv
$$

## Scalar Surface Integral
$$
\iint_S G \ dA = \iint_\Omega G(\mathbf{r}) ||\mathbf{N}|| \ du \ dv
$$

## Divergence Theorem
Let $V$ be a solid region with boundary $S$ oriented outward. If $\mathbf{F}$ is continuously differentiable,
$$
\iiint_V \diverg \mathbf{F} \ dV = \iint_{S} \mathbf{F} \cdot \mathbf{n} \ dA
$$

## Stokes' Theorem
Let $S$ be an oriented surface with right-hand boundary $C$. If $\mathbf{F}$ is continuously differentiable,
$$
\iint_S \curl \mathbf{F} \cdot \mathbf{n} \ dA = \oint_C \mathbf{F} \cdot d\mathbf{r}
$$

# Triple Integrals

Rectangular: $dV = dx \ dy \ dz$

Cylindrical: $dV = r \ dr \ d\theta \ dz$

Spherical: $dV = \rho^2 \sin \phi \ d\rho \ d\theta \ d\phi$

# Green's Identities

Derived by applying the Divergence Theorem to the vector field $\mathbf{F} = f \grad g$.

## Green's First Identity
$$
\iiint_T \parens{f \laplacian g + \grad f \cdot \grad g} \ dV
= \iint_S f \pder[g]{n} \ dA
$$

## Green's Second Identity
$$
\iiint_T \parens{f \laplacian g - g \laplacian f} \ dV
= \iint_S \parens{f \pder[g]{n} - g \pder[f]{n}} \ dA
$$
