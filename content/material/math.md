---
jupytext:
  formats: ipynb,md
  text_representation:
    extension: .md
    format_name: myst
    format_version: '0.12'
---

# Mathematical Refresher

Before starting the INF1220 course, it is useful to recall some mathematical notions that will be used throughout the course.  
This document does **not** replace a mathematics course; it only recalls notions assumed to be known.

---

## Table of Contents

1. Propositions, Sets, Relations, and Numbers  
2. Variables and Elementary Numerical Functions  
3. Random Variable and Function of a Random Variable  
4. Appendix

---

## 1. Propositions, Sets, Relations, and Numbers

### 1.1 Propositions

A **proposition** is a sentence that can be either *true* or *false*.

Examples:
- “2 is an even number.” (true)
- “3 is divisible by 2.” (false)

Logical symbols are used to combine propositions.

#### Table 1 – Logical connectives

| p | q | ¬p | p ∨ q | p ⊕ q | p ∧ q | p ⇒ q | p ⇔ q |
|---|---|----|--------|--------|--------|--------|--------|
| T | T | F | T | F | T | T | T |
| T | F | F | T | T | F | F | F |
| F | T | T | T | T | F | T | F |
| F | F | T | F | F | F | T | T |

Meanings:
- ¬p means “not p”.
- p ∨ q means “p or q”.
- p ⊕ q means “p or q, but not both”.
- p ∧ q means “p and q”.
- p ⇒ q means “if p then q”.
- p ⇔ q means “p if and only if q”.

---

### 1.2 Sets

A **set** is a collection of distinct objects.

If an object \( o \) belongs to a set \( E \), we write:
\[
o \in E
\]

Otherwise:
\[
o \notin E
\]

A set can be defined:
- by listing its elements:  
  \[
  E = \{o_1, o_2, o_3\}
  \]
- by describing a property satisfied by its elements:  
  \[
  T = \{ o \mid o \text{ is registered in INF1220 on March 1, 2021} \}
  \]

The empty set is written \( \emptyset \).

---

#### Operations on sets

Let \( A \) and \( B \) be two sets.

- **Intersection**:
\[
A \cap B = \{ x \mid x \in A \text{ and } x \in B \}
\]

- **Union**:
\[
A \cup B = \{ x \mid x \in A \text{ or } x \in B \}
\]

- **Difference**:
\[
A \setminus B = \{ x \mid x \in A \text{ and } x \notin B \}
\]

- **Cartesian product**:
\[
A \times B = \{ (a,b) \mid a \in A, b \in B \}
\]

---

### 1.3 Binary Relations

A **binary relation** \( R \) between sets \( A \) and \( B \) is a subset of \( A \times B \).

If \( (a,b) \in R \), we write:
\[
aRb
\]

#### Properties of relations

Let \( R \) be a relation on a set \( A \).

- Reflexive:  
  \[
  \forall a \in A,\ aRa
  \]

- Symmetric:  
  \[
  aRb \Rightarrow bRa
  \]

- Transitive:  
  \[
  aRb \land bRc \Rightarrow aRc
  \]

- Antisymmetric:  
  \[
  aRb \land bRa \Rightarrow a=b
  \]

An **equivalence relation** is reflexive, symmetric, and transitive.

A **partial order** is reflexive, antisymmetric, and transitive.

A **total order** is a partial order such that any two elements are comparable.

---

### 1.4 The Set of Natural Numbers and Other Number Sets

The set of natural numbers is:
\[
\mathbb{N} = \{0,1,2,3,\dots\}
\]

Other number sets:
\[
\mathbb{N} \subset \mathbb{Z} \subset \mathbb{D} \subset \mathbb{Q} \subset \mathbb{R}
\]

Where:
- \( \mathbb{Z} \): integers
- \( \mathbb{D} \): decimal numbers
- \( \mathbb{Q} \): rational numbers
- \( \mathbb{R} \): real numbers

---

#### Euclidean division

Let \( a \) and \( b \) be integers, with \( b \neq 0 \).  
There exist unique integers \( q \) and \( r \) such that:
\[
a = bq + r \quad \text{with} \quad 0 \le r < |b|
\]

---

#### Even and odd numbers

An integer is **even** if it is divisible by 2.  
Otherwise, it is **odd**.

---

#### Prime numbers

A natural number greater than 1 is **prime** if it has exactly two divisors in \( \mathbb{N} \): 1 and itself.

---

## 2. Variables and Elementary Numerical Functions

### 2.1 The Notion of a Variable

A **variable** is a symbol representing an element of a set.

A **function** from a set \( E \) to a set \( F \) associates each element of \( E \) with exactly one element of \( F \):
\[
f : E \rightarrow F
\]

Example:
\[
f(t) = at + b
\]

---

### 2.2 Usual Elementary Numerical Functions

#### Power function

\[
f_a(x) = x^a
\]

Property:
\[
x^{a+b} = x^a x^b
\]

---

#### Exponential function

\[
f(x) = e^x
\]

Property:
\[
e^{x+y} = e^x e^y
\]

---

#### Logarithmic function

\[
f(x) = \ln(x)
\]

Properties:
\[
\ln(xy) = \ln(x) + \ln(y)
\]

---

### 2.3 Real Sequences and Series

A **real sequence** is a function:
\[
u : \mathbb{N} \rightarrow \mathbb{R}
\]

It is written \( (u_n) \).

A **series** is the sum:
\[
\sum_{k=0}^{n} u_k
\]

Example:
\[
\sum_{k=1}^{n} \frac{1}{k}
\]

---

### 2.4 Real Matrices

A real matrix with \( m \) rows and \( n \) columns is written:

\[
A =
\begin{pmatrix}
a_{11} & a_{12} & \cdots & a_{1n} \\
a_{21} & a_{22} & \cdots & a_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & \cdots & a_{mn}
\end{pmatrix}
\]

Operations:
- Addition: \( (A+B)_{ij} = a_{ij} + b_{ij} \)
- Multiplication:
\[
(AB)_{ij} = \sum_{k=1}^{n} a_{ik} b_{kj}
\]
- Transpose:
\[
(A^\top)_{ij} = a_{ji}
\]

---

## 3. Random Variable and Function of a Random Variable

### 3.1 Random Variable

A **random variable** is a function defined on a sample space \( \Omega \) that assigns a real number to each outcome.

If it takes a finite number of values, it is called a **discrete random variable**.

---

### Probability Law

A probability law associates to each possible value \( x_i \) a probability \( p_i \) such that:
- \( p_i \ge 0 \)
- \( \sum p_i = 1 \)

Example:

| Number of flowers | 0 | 1 | 2 | 3 | 4 |
|------------------|---|---|---|---|---|
| Probability | 1/8 | 1/8 | 3/8 | 1/8 | 1/8 |

---

### Cumulative Distribution Function

\[
F(x) = \sum_{x_i \le x} p(X = x_i)
\]

---

### Common Discrete Laws

- **Uniform distribution** on \( \{1,\dots,n\} \):
\[
p(X=x) = \frac{1}{n}
\]

- **Bernoulli distribution** with parameter \( p \):
\[
p(X=x) = p^x(1-p)^{1-x}
\]

---

## 4. Appendix

### Table 5 – Common abbreviations and symbols

| Symbol | Meaning | Example |
|------|--------|---------|
| ssi | If and only if | An integer is even iff its last digit is even. |
| \( \sum \) | Summation | \( \sum_{i=1}^{n} i \) |
| \( \le \) | Less than or equal | \( 1 \le 2 \) |
| \( \ge \) | Greater than or equal | \( 2 \ge 1 \) |
| \( < \) | Strictly less than | \( 1 < 2 \) |
| \( > \) | Strictly greater than | \( 2 > 1 \) |
| \( \forall \) | For all | \( \forall a \in \mathbb{N}, a \ge 0 \) |
| \( \exists \) | There exists | \( \exists a \neq 0 \) |
| \( \in \) | Belongs to | \( 2 \in \mathbb{N} \) |
| \( \notin \) | Does not belong | \( -1 \notin \mathbb{N} \) |
| \( \subseteq \) | Included or equal | \( A \subseteq A \cup B \) |
| \( \subset \) | Strictly included | \( \mathbb{N} \subset \mathbb{Z} \) |
| \( \Rightarrow \) | Implies | \( p \Rightarrow q \) |
| \( \|a\| \) | Absolute value | \( \|a\| = a \) if \( a \ge 0 \), otherwise \( -a \) |

---

