# Foundations of Computational Data Analysis 

Course Work - https://drive.google.com/drive/folders/1BZ2FJMHQ9DfdgRkgVQoOZgqmaoc6gqRv?usp=sharing


A week-by-week record of the topics covered in this course. This repository documents
**what the course covered and what I studied**

The course is split roughly in half: five weeks of probability and mathematical
statistics, followed by four weeks of linear algebra, converging on the matrix
techniques that underpin modern data analysis.

---

## Texts

| Key | Reference |
|-----|-----------|
| **[LM]** | *An Introduction to Mathematical Statistics and Its Applications*, 6th ed. — Larsen & Marx |
| **[Lay]** | *Linear Algebra and Its Applications*, 5th ed. — Lay, Lay & McDonald |
| **[TS]** | *Think Stats: Exploratory Data Analysis in Python* — Downey |

---

## Part I — Probability & Mathematical Statistics

### Week 1 (Mar 23) — Probability and Random Variables
**Reading:** LM 1.1–3.8

Sample spaces, axioms of probability, and the distinction between disjoint and
independent events. Conditional probability and Bayes' theorem, including the
posterior-updating problems that motivate later inference. Combinatorics and counting
as the backbone of discrete probability. Discrete random variables: pmfs and cdfs,
expectation and variance, and the standard families — binomial, geometric,
hypergeometric, Poisson. Transition into continuous random variables and density
functions, joint and marginal densities, and independence of random variables.

### Week 2 (Mar 30) — Conditional Densities, MGFs, Special Distributions
**Reading:** LM 3.9, 3.11–3.12, 4.1–4.3 · *Quiz 1*

Transformations of random variables and deriving the density of a function of one or
more variables from first principles. Order statistics. Expected values of functions of
random variables, including geometric-mean style computations. Moment-generating
functions and their use in identifying distributions and recovering moments. Joint
densities, conditional densities, and conditional expectation. The special continuous
distributions: normal, gamma, exponential, and the Poisson/exponential relationship.

### Week 3 (Apr 6) — Central Limit Theorem and Estimation
**Reading:** LM 4.A.2, 5.1–5.4, 5.8 · TS Ch. 8

The Central Limit Theorem and normal approximation. Point estimation: the method of
maximum likelihood and the method of moments, and how the two diverge. Properties of
estimators — unbiasedness, efficiency, consistency, and sufficiency. Interval
estimation and confidence intervals. Bayesian estimation, conjugate priors, and
posterior distributions, including work with the scaled inverse chi-squared family.
Downey's chapter supplies the computational counterpart: estimation by simulation,
sampling distributions, and standard error.

### Week 4 (Apr 13) — Hypothesis Testing
**Reading:** LM 6.1–6.5 · TS Ch. 9 · *Quiz 2*

The structure of a hypothesis test: null and alternative hypotheses, test statistics,
critical regions, and significance levels. One-sided versus two-sided alternatives.
Type I and Type II errors, power, and power curves. The Neyman–Pearson paradigm and its
deliberate asymmetry in prioritizing control of Type I error — including a critical
look at when that asymmetry is the wrong default. Likelihood ratios as the organizing
idea behind test construction, and the Bayesian framing via prior and posterior
probabilities on hypotheses. Computational work in Python on resampling-based testing
and p-values.

---

## Part II — Linear Algebra

### Week 5 (Apr 20) — Systems of Linear Equations
**Reading:** Lay 1.1–1.5 · *Midterm*

Systems of linear equations, augmented matrices, and row reduction to echelon and
reduced echelon form. Pivot positions, basic and free variables, and the conditions
governing existence and uniqueness of solutions. Vector equations, linear combinations,
and span. The matrix equation **Ax** = **b** and the equivalence of its several
formulations. Homogeneous systems, the structure of their solution sets, and solutions
in parametric vector form.

### Week 6 (Apr 27) — Matrix Algebra
**Reading:** Lay 1.7–1.9, 2.1–2.3, 2.8–2.9

Linear independence and its characterization through pivot columns. Linear
transformations, their matrix representations, and the geometry of standard
transformations; one-to-one and onto maps. Matrix operations, the transpose, and matrix
inverses. Elementary matrices and the interpretation of row reduction as left
multiplication by a nonsingular matrix. The Invertible Matrix Theorem as the hub
connecting these ideas. Subspaces of R^n, column space and null space, bases, dimension,
and rank.

### Week 7 (May 4) — Determinants, Eigenvalues, Diagonalization
**Reading:** Lay 5.1–5.3 (with Ch. 3 on determinants)

Determinants via cofactor expansion and via row reduction, and their behavior under
elementary operations. Eigenvalues, eigenvectors, and eigenspaces. The characteristic
polynomial and characteristic equation; algebraic versus geometric multiplicity.
Relationships among the spectra of related matrices — that A and Aᵀ share a
characteristic polynomial but not eigenvectors, that eigenpairs of A invert to
eigenpairs of A⁻¹, and that eigenvalues are not additive or multiplicative across
matrices. Similarity and diagonalization, and the conditions under which a matrix is
diagonalizable.

### Week 8 (May 11) — Orthogonality and Quadratic Forms
**Reading:** Lay 6.1–6.2, 7.1–7.3 · *Quiz 3*

Inner products, vector norms, and orthogonality. Orthogonal complements and the
relationship between the row space and null space. Orthogonal sets, orthonormal bases,
and orthogonal matrices — including the result that an orthogonal matrix has
determinant ±1, and its geometric reading: +1 for rotations, −1 for reflections.
Explicit derivation of rotation and reflection matrices. Symmetric matrices and the
Spectral Theorem, orthogonal diagonalization, and quadratic forms with their
classification as positive definite, negative definite, or indefinite. Constrained
optimization of quadratic forms.

### Week 9 (May 18) — Final Examination

### Week 10 (May 26, optional) — SVD and PCA
**Reading:** Lay 7.4–7.5

Singular value decomposition: singular values, the geometry of the decomposition, and
the four fundamental subspaces. Low-rank approximation. Principal component analysis
as an application of the spectral decomposition of a covariance matrix, and its use in
dimensionality reduction.

---

## Assignment Sequence

The course ran eight problem sets, each due at the start of the following week and
tracking that week's material:

| # | Topic |
|---|-------|
| 1 | Random variables |
| 2 | Conditional densities, MGFs, special distributions |
| 3 | Estimation |
| 4 | Hypothesis testing (incl. a likelihood-ratio notebook) |
| 5 | Linear equations |
| 6 | Matrix inverses and subspaces |
| 7 | Determinants and eigenvectors |
| 8 | Orthogonality and quadratic forms |


