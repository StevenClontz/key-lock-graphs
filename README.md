![the legend of math logo](assets/legendofmath.svg)

# Link to editor

[./editor/editor.html](./editor/editor.html)

# Basics

A **dungeon graph** is a graph $G$ (multigraph, loops allowed)
which has an **item set** $I=I_e\cup I_p$ partitioned into
**exhaustible** ($I_e$) and **permanent** ($I_p$) items, a
**treasure map** $T_G:V(G)\to \omega^I$, a **barrier map**
$B_G:E(G)\to \omega^I$, and a **starting vertex** $s\in V(G)$.

A **move** in a dungeon graph $G$ is
an edge $p$ between the starting vertex $s$ and some
vertex $v$ satisfying
$$T_G(s)(i)\geq B_G(p)(i)$$
for all $i\in I$. Each move defines a new dungeon graph $G/p$
contracting the edge $p$, such that
$$B_{G/p}(e)=B_G(e)$$
for all $e\in E(G/p)$,
$$T_{G/p}(s)(i)=T_G(s)(i)+T_G(v)(i)$$ 
for $i\in I_p$, and
$$T_{G/p}(s)(i)=T_G(s)(i)+T_G(v)(i)-B_G(e)(i)$$
for $i\in I_e$.

Let $G/e_0\cdots e_n$ denote $((G/e_0)/\cdots)/e_n$.

A **dive** is a sequence of edges
$\langle e_0,e_1,\dots,e_{n-1}\rangle$ 
such that each
$e_m$ is a legal move from $G/e_0 \cdots e_{m-1}$ to
$G/e_0 \cdots e_m$.

A dungeon graph $G$ is **solvable** if there exists a
**complete dive** using every edge of $G$.

A dungeon graph is **strongly solvable** provided every dive
can be extended to a complete dive.

## Proposition

Strongly solvable dungeon graphs are solvable.

## Proposition

Suppose $e\in E(G)$ with $B_G(e)(i)=0$ for all $i\in I$.
Then $G$ is [strongly] solvable if and only if $G/e$ is.

# Tunnel Graphs

Let $P_N$ denote the path with $N+1$ vertices
$V(P_N)=\{v_n:n\leq N\}$
and $N$ edges $E(P_N)=\{e_n:n<N\}$ where
$e_n=\{v_n,v_{n+1}\}$.

A **tunnel graph** $G$ of length $N$ is the path $P_N$ considered as a
dungeon graph, with $s=v_0$, $I_p=\{\}$, $I_e=\{k\}$,
and $B_{P_N}(e)(k)=1$.

We say a tunnel graph is **well-keyed** provided
$$
\sum_{m=0}^{n} T_{G}(v_m)(k) \geq {n + 1}
$$
for all $0\leq n<N$.

## Theorem

A tunnel graph $G$ is strongly solvable if and only if 
it is solvable if and only if
it is well-keyed.

### Proof

Let $G$ of length $N$ be solvable; we will prove it is well-keyed.
So let $d$ be a complete dive, and note $d=\langle e_0,\dots,e_N\rangle$
necessarily, since $e_m$ is the only edge adjacent to $s$ in
$G/e_0\cdots e_{m-1}$.

Let $0\leq m<N$. 
$$T_{G/p}(s)(i)=T_G(s)(i)+T_G(v)(i)-B_G(e)(i)$$

<!-- Note that if $N=0$, it is well-keyed vacuously.

So suppose the inequality holds for $N$;
we will show it holds for $N+1$.
So given a complete dive $d$ of $P_{N+1}$, note that it must be
$d=\langle e_0,\cdots,e_n\rangle$ with $e_m=\{v_m,v_{m+1}\}$.
We see immediately that $\langle e_0,\cdots, e_{n-1}\rangle$ is a
complete dive of $P_N$, showing it is solvable, and therefore
$$
\sum_{m=0}^{n} T(v_m)(k) \geq {n + 1}
$$
for all $0\leq n<N$.
It remains to be shown that
$$
\sum_{n=0}^{N} k(R_n) \geq N + 1.
$$

But we have that $d$ is a complete dive, and if we let $W''$ be the
initial subwalk of $W$ removing all vertices following the first vertex of $R_{N+1}$,
we must have $k(W'')\geq l(W'')$. Thus we may conclude
$$
\sum_{n=0}^{N} k(R_n) \geq
k(W'') \geq
l(W'') =
N+1.
$$

&nbsp;

So finally, assume $G$ is a well-keyed tunnel graph;
we will show that it satisfies $SK_2$. To do this, let $W$ be a partial
admissible walk; we will show that it can be extended to use one more
lock edge.

If $G$ has $N$ locks and $N+1$ regions, then $W$ uses $M$ lock edges for
some $M<N$; in particular, it must use the lock edges $L_0,\dots,L_{M-1}$.
It follows that it includes vertices in regions $R_m$ for all
$0\leq m\leq M$. Thus it may be extended to an admissible walk $W'$ that
includes all vertices in those regions.

Since the graph is well-keyed, there exist at least $M+1$ keys in these
regions. Thus $W'$ may be extended to an admissible walk that uses $L_M$.
$\square$ -->


# Old Key-Lock Graph Jupyter Notebooks

1. [Basics](notebooks/basics.ipynb)
2. [Tunnel Graphs](notebooks/tunnel.ipynb)
3. [Greedy Walks](notebooks/greedy.ipynb)
4. [Gluing](notebooks/gluing.ipynb)
5. [Adding Edges](notebooks/addedge.ipynb)