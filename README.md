![the legend of math logo](assets/legendofmath.svg)

# Link to editor

[./editor/editor.html](./editor/editor.html)

# Basics

A **dungeon graph** is a graph $G$ (multigraph, loops allowed)
which has an **item set** $I=I_e\cup I_p$ partitioned into
**exhaustible** ($I_e$) and **permanent** ($I_p$) items, a
**treasure map** $T_G:V(G)\to \omega^I$, a **barrier map**
$B_G:E(G)\to \omega^I$, and a **starting vertex** $s_G\in V(G)$.

A **move** in a dungeon graph $G$ is
an edge $p=\{s_G,v\}$ satisfying
$$T_G(s_G)(i)\geq B_G(p)(i)$$
for all $i\in I$. Each move defines a new dungeon graph $G/p$
contracting the edge $p$ to its starting vertex $s_{G/p}$,
such that
$$B_{G/p}(e)=B_G(e), T_{G/p}(w)=T_G(w)$$
for all $e\in E(G/p), w\in V(G/p)\setminus\{s_{G/p}\}$,
$$T_{G/p}(s_{G/p})(i)=T_G(s_G)(i)+T_G(v)(i)$$ 
for $i\in I_p$, and
$$T_{G/p}(s_{G/p})(i)=T_G(s_G)(i)+T_G(v)(i)-B_G(e)(i)$$
for $i\in I_e$.

For a sequence of edges
$d=\langle e_0,e_1,\dots,e_{n-1}\rangle$, let
$d\upharpoonright m=\langle e_0,e_1,\dots,e_{m-1}\rangle$
restrict $d$ to its first $m$ edges, and let
$G/(d\upharpoonright m)=G/e_0\cdots e_{m-1}$.
Then $d$ is a **dive** provided each
$e_m$ is a move from $G/(d\upharpoonright m)$ to
$G/(d\upharpoonright m+1)$.

A dungeon graph $G$ is **solvable** if there exists a
**complete dive** using every edge of $G$.

A dungeon graph is **strongly solvable** provided every dive
can be extended to a complete dive.

## Proposition

Strongly solvable dungeon graphs are solvable.

## Proposition

Suppose $e\in E(G)$ with $B_G(e)(i)=0$ for all $i\in I$.
Then $G$ is [strongly] solvable if and only if $G/e$ is.

## Proposition

A dungeon graph is strongly solvable if and only if
every incomplete dive can be extended by an edge.

## Proposition

Given a dive $d=\{e_0,\cdots,e_{n-1}\}$ with
$e_m=\{v_m,v_{m+1}\}$,
$$T_{G/d}(s_{G/d})(i)=\sum_{m=0}^{|d|}
T_{G}(v_m)(i)$$
for $i\in I_p$, and
$$T_{G/d}(s_{G/d})(i)=\sum_{m=0}^{|d|}
T_{G}(v_m)(i)-
\sum_{m=0}^{|d|-1} B_{G}(e_m)(i)$$
for $i\in I_e$.

# Tunnel Graphs

A **key-lock graph** $G$ is a dungeon graph such that
$I_p=\{\}$, $I_e=\{k\}$, 
and $B_{G}(e)(k)=1$ for all $e\in E(G)$.

Let $P_N$ denote the path with $N+1$ vertices
$V(P_N)=\{v_n:n\leq N\}$
and $N$ edges $E(P_N)=\{e_n:n<N\}$ where
$e_n=\{v_n,v_{n+1}\}$.
A **tunnel graph** $G$ of length $N$ is the path $P_N$ considered as a key-lock graph with $s=v_0$.

We say a tunnel graph $G$ of length $N$
is **well-keyed** provided
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
necessarily, since $e_m$ is the only edge adjacent to
the starting vertex of $G/(d\upharpoonright m)$.

Let $0\leq n<N$, and note
$$T_{G/(d\upharpoonright n)}(s_{G/(d\upharpoonright n)})(k)\geq
B_{G/(d\upharpoonright n)}(e_n)(k)=1.$$

We may also note by the earlier proposition that
$$T_{G/(d\upharpoonright n)}(s_{G/(d\upharpoonright n)})(k)=
\sum_{m=0}^{n}T_G(v_m)(k)-\sum_{m=0}^{n-1}B_G(e_m)(k)$$
$$=
\left(\sum_{m=0}^nT_G(v_m)(k)\right)-n.$$
It follows that
$$
\left(\sum_{m=0}^nT_G(v_m)(k)\right) -n \geq 1
$$
$$
\Rightarrow
\sum_{m=0}^nT_G(v_m)(k) \geq n+1
$$
for all $0\leq n<N$, showing $G$ is well-keyed.

&nbsp;

Now assume $G$ is well-keyed, and let $d$ be an
incomplete dive. Necessarily, $d=\langle e_0,\cdots e_{n-1}\rangle$ for some $n\leq N$. Note that
$$T_{G/d}(s_{G/d})(k)=
\sum_{m=0}^{n}T_G(v_m)(k)-\sum_{m=0}^{n-1}B_G(e_m)(k)$$
$$=
\left(\sum_{m=0}^nT_G(v_m)(k)\right)-n.$$
and by the assumption of well-keyed,
$$T_{G/d}(s_{G/d})(k)\geq
\left(n+1\right) -n = 1 = B_{G/d}(e_n)(k).
$$
It follows that $d$ may be extended by $e_n$,
and thus $G$ is strongly solvable.

# Gluing

Let $G_1,G_2$ be disjoint dungeon graphs with
$g_1\in V(G_1),g_2\in V_{G_2}$.
These graphs may be **glued** together
as $G=(G_1\cup G_2)/\{g_1,g_2\}$ by
identifying $g_1$ with $g_2$ as $g$, where $s_G=s_{G_1}$
and $T_G(g)=T_{G_1}(g_1)+T_{G_2}(g_2)$.

## Theroem

Let $G_1,G_2$ be disjoint [strongly]
solvable dungeon graphs with $g\in G_1$.
Then $(G_1\cup G_2)/\{g,s_{G_2}\}$ is [strongly]
solvable.

### Proof

First let $d_1,d_2$ be complete dives for $G_1,G_2$
respectively. Then $d_1d_2$ is a complete dive for
$(G_1\cup G_2)/\{g,s_{G_2}\}$.

Now assume $G_1,G_2$ are strongly solvable, and consider
an incomplete dive $d$ of $(G_1\cup G_2)/\{g,s_{G_2}\}$.
Suppose it cannot be extended by an edge in $G_1$.

If the
restriction $d_{G_1}$ of $d$ to edges in $G_1$ is complete,
then it follows that the restriction $d_{G_2}$ of $d$
to edges in $G_2$ is an incomplete dive in $G_2$, and thus
can be extended by some $e\in E(G_2)$. It follows that
$d$ can be extended by $e$ as well.

Otherwise, $d_{G_1}$ can be extended by an edge $e\in E(G_1)$
as a dive in $G_1$. Since this edge cannot extend $d$ in $G$,
it must be that while
$$T_{G_1/d_1}(s_{G_1/d_1})(i)\geq B_{G_1/d_1}(e)(i)=B_G(e)(i)$$
for all $i\in I$,
$$T_{G/d}(s_{G/d})(i)< B_{G/d}(e)(i)=B_G(e)(i)$$
for some $i\in I$. Now if $i\in I_p$ was
permanent, we'd have that
$$B_G(e)(i)>T_{G/d}(s_{G/d})\geq T_{G_1/d_1}(s_{G_1/d_1})
\geq B_G(e)(i),$$
a contradiction.

So we have $i\in I_e$ exhaustible and
$T_{G/d}(s_{G/d})< T_{G_1/d_1}(s_{G_1/d_1})$.
We recall that, denoting $d=\langle e_0,\dots,e_{|d|-1}\rangle$
with $e_m=\{v_m,v_{m+1}\}$
and $d_1=\langle e_0',\dots,e_{|d_1|-1}'\rangle$
with $e_m'=\{v_m',v_{m+1}'\}$,
$$T_{G/d}(s_{G/d})(i)=\sum_{m=0}^{|d|}
T_{G}(v_m)(i)-
\sum_{m=0}^{|d|-1} B_{G}(e_m)(i)$$
and
$$T_{G_1/d_1}(s_{G_1/d_1})(i)=\sum_{m=0}^{|d_1|}
T_{G_1}(v_m')(i)-
\sum_{m=0}^{|d_1|-1} B_{G_1}(e_m')(i).$$

It's immediate that
$\sum_{m=0}^{|d|}T_{G}(v_m)(i)\geq
\sum_{m=0}^{|d_1|}T_{G_1}(v_m')(i)$ since
$\{v_m:0\leq m<|d|\}\supseteq\{v_m':0\leq m<|d_1|\}$.
Therefore we must have
$$\sum_{m=0}^{|d|-1} B_{G}(e_m)(i)>
\sum_{m=0}^{|d_1|-1} B_{G_1}(e_m')(i).$$

In particular, we have,
denoting $d_2=\langle e_0'',\cdots,e_{|d_2|-1}''\rangle$,
$$\sum_{m=0}^{|d_2|-1} B_{G_2}(e_m'')(i)> 0.$$

(TODO, finish)

# Old Key-Lock Graph Jupyter Notebooks

1. [Basics](notebooks/basics.ipynb)
2. [Tunnel Graphs](notebooks/tunnel.ipynb)
3. [Greedy Walks](notebooks/greedy.ipynb)
4. [Gluing](notebooks/gluing.ipynb)
5. [Adding Edges](notebooks/addedge.ipynb)