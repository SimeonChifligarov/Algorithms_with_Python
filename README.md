# Algorithms with Python

### Recursion, Searching & Sorting, Graph Algorithms, Shortest Paths, Minimum Spanning Trees & Dynamic Programming

[![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Algorithms](https://img.shields.io/badge/Focus-Algorithms%20%26%20Problem%20Solving-blueviolet)](#topics-covered)
[![Educational](https://img.shields.io/badge/Purpose-Education-orange)](#educational-scope)

A structured collection of **Python implementations, algorithmic exercises, graph problems, dynamic programming challenges, and exam solutions** created while studying fundamental algorithms and problem-solving techniques.

The repository is based on material studied during the **SoftUni Algorithms with Python course — July 2022** and was inspired by **Atanas Atanasov**.

---

> [!IMPORTANT]
> This is an **independent educational repository** containing personal implementations and solutions created during the learning process.
>
> It is not an official SoftUni repository, is not affiliated with or endorsed by SoftUni, and should not be considered a replacement for the original course materials.

## Table of Contents

- [Overview](#overview)
- [Topics Covered](#topics-covered)
- [Learning Objectives](#learning-objectives)
- [Repository Structure](#repository-structure)
- [Algorithm Overview](#algorithm-overview)
- [Problem Highlights](#problem-highlights)
- [Labs, Exercises and Exams](#labs-exercises-and-exams)
- [Getting Started](#getting-started)
- [Running the Solutions](#running-the-solutions)
- [Recommended Learning Path](#recommended-learning-path)
- [Algorithmic Complexity](#algorithmic-complexity)
- [Educational Scope](#educational-scope)
- [Contributing](#contributing)
- [Course Attribution and Disclaimer](#course-attribution-and-disclaimer)
- [License](#license)
- [Author](#author)

---

## Overview

This repository documents my work through a practical algorithms curriculum implemented entirely in **Python**.

The material progresses from fundamental recursion and searching techniques to more advanced topics such as graph traversal, shortest-path algorithms, minimum spanning trees, and dynamic programming.

The repository contains:

- Recursive and iterative problem-solving examples
- Backtracking problems
- Binary search
- Elementary and divide-and-conquer sorting algorithms
- Breadth-First Search and Depth-First Search
- Connected-component discovery
- Cycle detection and graph modification problems
- Topological sorting
- Shortest-path algorithms
- Minimum spanning tree algorithms
- Dynamic programming problems
- Sequence optimization problems
- Exam-preparation problems
- Solutions from a timed practical exam
- Separate laboratory and exercise implementations where applicable

The primary goal is not simply to collect solutions, but to practice **recognizing algorithmic patterns, selecting appropriate techniques, reasoning about complexity, and translating an algorithm into clear Python code**.

---

## Topics Covered

### Recursion

The repository begins with the fundamentals of recursive problem solving:

- Recursive function design
- Base cases
- Recursive decomposition
- Call-stack reasoning
- Recursion versus iteration
- Recursive array processing
- Factorial calculation
- Recursive drawing
- Fibonacci sequences

Representative problems include:

- Recursive Array Sum
- Recursive Factorial
- Recursive Drawing
- Recursive Fibonacci

---

### Backtracking

Backtracking extends recursion by exploring candidate solutions and abandoning branches that cannot lead to a valid result.

Topics and problems include:

- Generating binary vectors
- Exploring paths in a labyrinth
- Eight Queens
- Nested-loop generation
- Connected areas in matrices
- Word construction problems

Representative problems:

- `Generating 0/1 Vectors`
- `Paths in Labyrinth`
- `8 Queens Puzzle`
- `Nested Loops`
- `Connected Areas in Matrix`
- `Word Cruncher`

These problems help develop an understanding of:

- State-space exploration
- Recursive branching
- Undoing decisions
- Constraint satisfaction
- Exhaustive search

---

### Searching Algorithms

Searching is one of the most fundamental operations in computer science.

The repository covers:

- Linear-search concepts
- Binary Search

#### Binary Search

Binary search repeatedly divides an ordered search space in half.

Typical time complexity:

```text
O(log n)
```

The implementation demonstrates how exploiting sorted data can dramatically reduce the number of comparisons required compared with a linear scan.

---

### Sorting Algorithms

Several fundamental sorting algorithms are implemented and compared.

#### Selection Sort

Repeatedly selects the smallest remaining element and moves it into its correct position.

Typical complexity:

```text
Time:  O(n²)
Space: O(1)
```

#### Bubble Sort

Repeatedly compares adjacent elements and swaps them when they are out of order.

Typical complexity:

```text
Average/Worst Time: O(n²)
Space:              O(1)
```

#### Insertion Sort

Builds a sorted portion of the collection by inserting each new element into its appropriate position.

Typical complexity:

```text
Average/Worst Time: O(n²)
Best Time:          O(n)
Space:              O(1)
```

#### QuickSort

A divide-and-conquer sorting algorithm based on partitioning elements around a pivot.

Typical complexity:

```text
Average: O(n log n)
Worst:   O(n²)
```

#### Merge Sort

Recursively divides a collection and merges the sorted subcollections.

Typical complexity:

```text
Time:  O(n log n)
Space: O(n)
```

---

### Graph Theory

A significant portion of the repository focuses on graph algorithms.

Concepts include:

- Vertices and edges
- Directed and undirected graphs
- Adjacency representations
- Graph traversal
- Connected components
- Reachability
- Cycles
- Directed acyclic graphs
- Topological ordering

---

### Breadth-First Search

Breadth-First Search explores a graph level by level.

It is particularly useful for:

- Traversing unweighted graphs
- Discovering connected components
- Finding minimum-edge paths
- Exploring nodes by distance from a starting vertex

Typical complexity with an adjacency-list representation:

```text
O(V + E)
```

where:

- `V` = number of vertices
- `E` = number of edges

---

### Depth-First Search

Depth-First Search explores one branch as deeply as possible before backtracking.

Typical applications include:

- Graph traversal
- Connected components
- Cycle detection
- Topological sorting
- Dependency analysis

Typical complexity:

```text
O(V + E)
```

---

### Topological Sorting

Topological sorting creates a linear ordering of vertices in a **directed acyclic graph (DAG)** such that dependencies appear before the vertices that depend on them.

The repository includes practical work with:

- Dependency graphs
- DAGs
- Ordering constraints
- Cycle-related graph problems

---

### Shortest Paths

The repository explores multiple shortest-path strategies because no single algorithm is appropriate for every graph.

Covered techniques include:

#### Shortest Path in an Unweighted Graph

For an unweighted graph, Breadth-First Search can be used to find a shortest path measured by number of edges.

#### Dijkstra's Algorithm

Used for shortest-path problems involving graphs with non-negative edge weights.

Core ideas include:

- Distance relaxation
- Greedy vertex selection
- Maintaining tentative shortest distances

#### Bellman-Ford Algorithm

A shortest-path algorithm capable of working with negative edge weights and detecting situations involving negative cycles.

Core ideas include:

- Repeated edge relaxation
- Distance propagation
- Negative-cycle reasoning

---

### Minimum Spanning Trees

A **Minimum Spanning Tree (MST)** connects all vertices of a weighted undirected graph while minimizing the total edge weight.

The repository includes two classic MST algorithms.

#### Kruskal's Algorithm

Builds the spanning tree by processing edges from lowest to highest weight while preventing cycles.

Important concepts:

- Greedy selection
- Edge ordering
- Connected components
- Cycle prevention

#### Prim's Algorithm

Builds a spanning tree by repeatedly expanding from the already-connected portion of the graph using an appropriate minimum-cost edge.

Important concepts:

- Greedy expansion
- Weighted edges
- Frontier management
- Minimum-cost connectivity

---

### Dynamic Programming

Dynamic programming is used when a problem can be decomposed into overlapping subproblems whose results can be reused.

The repository covers:

- Recognizing overlapping subproblems
- Building recurrence relations
- Memoization concepts
- Bottom-up computation
- Sequence optimization
- Grid-based problems
- Edit-distance problems

Implemented problems include:

- Fibonacci
- Move Down/Right
- Longest Common Subsequence
- Longest Increasing Subsequence
- Binomial Coefficients
- Word Differences
- Connecting Cables
- Minimum Edit Distance
- Longest String Chain
- Longest Zigzag Subsequence

---

## Learning Objectives

By working through this repository, a learner should be able to:

- Explain recursion and identify appropriate base cases
- Compare recursive and iterative approaches
- Apply backtracking to combinatorial search problems
- Implement binary search
- Implement fundamental sorting algorithms
- Explain the trade-offs between simple and efficient sorting techniques
- Represent and traverse graphs
- Implement Breadth-First Search
- Implement Depth-First Search
- Identify connected components
- Reason about cycles in graphs
- Perform topological sorting
- Select an appropriate shortest-path algorithm
- Understand the principles behind Dijkstra's algorithm
- Understand the principles behind Bellman-Ford
- Build minimum spanning trees with Kruskal's algorithm
- Build minimum spanning trees with Prim's algorithm
- Recognize dynamic programming problems
- Construct and populate dynamic-programming tables
- Solve sequence and optimization problems
- Analyze basic time and space complexity
- Translate mathematical or conceptual algorithms into working Python implementations
- Approach unfamiliar algorithmic problems systematically

---

## Repository Structure

| Directory | Area | Description |
|---|---|---|
| [`00_Exam_Preparation`](00_Exam_Preparation) | Exam Preparation | Timed practice problems combining multiple algorithmic topics |
| [`00_Exam_Real`](00_Exam_Real) | Practical Exam | Solutions from the real practical exam |
| [`01_Recursion_and_Backtracking_Lab`](01_Recursion_and_Backtracking_Lab) | Recursion & Backtracking | Introductory implementations and guided problems |
| [`01_Recursion_and_Backtracking_Exercise`](01_Recursion_and_Backtracking_Exercise) | Recursion & Backtracking | More challenging recursive and backtracking problems |
| [`02_Searching_and_Sorting_Algorithms_Lab`](02_Searching_and_Sorting_Algorithms_Lab) | Searching & Sorting | Binary search and classic sorting-algorithm implementations |
| [`03_Graph_Th_Traversal_and_Topological_Sorting_Lab`](03_Graph_Th_Traversal_and_Topological_Sorting_Lab) | Graphs | Connected components and topological sorting |
| [`03_Graph_Th_Traversal_and_Topological_Sorting_Exercise`](03_Graph_Th_Traversal_and_Topological_Sorting_Exercise) | Graphs | Matrix regions, cycles, dependencies and graph reconstruction problems |
| [`04_Graphs_Shortest_Path_and_MST_Lab`](04_Graphs_Shortest_Path_and_MST_Lab) | Weighted Graphs | BFS shortest paths, Dijkstra, Bellman-Ford, Kruskal and Prim |
| [`04_Graphs_Shortest_Path_and_MST_Exercise`](04_Graphs_Shortest_Path_and_MST_Exercise) | Weighted Graphs | Applied shortest-path and minimum-spanning-tree problems |
| [`05_Dynamic_Programming_Lab`](05_Dynamic_Programming_Lab) | Dynamic Programming | Fundamental DP techniques and sequence problems |
| [`05_Dynamic_Programming_Exercise`](05_Dynamic_Programming_Exercise) | Dynamic Programming | More advanced optimization and sequence-based DP problems |

---

## Algorithm Overview

| Category | Algorithms / Techniques |
|---|---|
| Recursion | Recursive decomposition, base cases, recursive traversal |
| Backtracking | State-space search, constraint exploration, branch reversal |
| Searching | Binary Search |
| Sorting | Selection Sort, Bubble Sort, Insertion Sort, QuickSort, Merge Sort |
| Graph Traversal | BFS, DFS |
| Graph Analysis | Connected Components, Cycle Detection, Topological Sorting |
| Shortest Paths | BFS for unweighted graphs, Dijkstra, Bellman-Ford |
| Minimum Spanning Tree | Kruskal, Prim |
| Dynamic Programming | Fibonacci, grid DP, subsequence problems, edit distance, combinatorial DP |
| Problem Solving | Greedy reasoning, graph modeling, recurrence design, decomposition |

---

## Problem Highlights

### Recursion and Backtracking

The laboratory section contains implementations such as:

```text
01_Recursive_Array_Sum.py
02_Recursive_Factorial.py
03_Recursive_Drawing.py
04_Generating_0_1_Vectors.py
05_Paths_in_Labyrinth.py
06_8_Queens_Puzzle.py
07_Recursive_Fibonacci.py
```

The exercise section expands the topic with:

```text
01_Reverse_Array.py
02_Nested_Loops.py
03_Move_Down_Right.py
04_Connected_Areas_in_Matrix.py
05_Word_Cruncher.py
```

---

### Searching and Sorting

Implemented algorithms include:

```text
01_Binary_Search.py
02_Selection_Sort.py
03_Bubble_Sort.py
04_Insertion_Sort.py
05_Quicksort.py
06_Merge_Sort.py
```

These implementations provide a useful progression from straightforward quadratic sorting algorithms to divide-and-conquer approaches.

---

### Graph Traversal and Topological Sorting

Laboratory problems include:

```text
01_Connected_Components.py
02_Topological_Sorting.py
```

Exercise problems include:

```text
01_Areas_in_Matrix.py
02_Cycles_in_Graph.py
03_Salaries.py
04_Break_Cycles.py
05_Road_Reconstruction.py
```

Together, these exercises cover graph traversal, dependencies, connectivity and cycle-related reasoning.

---

### Shortest Paths and Minimum Spanning Trees

Core algorithm implementations include:

```text
01_Shortest_Path_in_Unweighted_Graph.py
02_Dijkstra_Algorithm.py
03_Bellman-Ford.py
04_Kruskal_Algorithm.py
05_Prim_Algorithm.py
```

Applied exercises include:

```text
01_Distance_Between_Vertices.py
02_Most_Reliable_Path.py
03_Cheap_Town_Tour.py
04_Undefined.py
05_Cable_Network.py
```

This section moves from implementing the fundamental algorithms themselves to recognizing when and how those algorithms should be applied to concrete graph problems.

---

### Dynamic Programming

Laboratory problems include:

```text
01_Fibonacci.py
02_Move_Down-Right.py
03_Longest_Common_Subsequence.py
04_Longest_Increasing_Subsequence.py
```

Exercise problems include:

```text
01_Binomial_Coefficients.py
02_Word_Differences.py
03_Connecting_Cables.py
04_Minimum_Edit_Distance.py
05_Longest_String_Chain.py
06_Longest_Zigzag_Subsequence.py
```

These problems demonstrate several common dynamic-programming patterns, including sequence comparison, path optimization, combinatorial counting, edit operations and subsequence construction.

---

### Exam Preparation

The exam-preparation directory contains three larger problems:

```text
01_The_Story_Telling.py
02_Time.py
03_Chain_Lightning.py
```

The preparation material combines concepts from across the curriculum, including:

- Recursion and backtracking
- Combinatorial problems
- Searching and sorting
- Greedy techniques
- Graph theory
- Dynamic programming

The original exam format consisted of **three practical problems within four hours**, making this section useful for practicing both correctness and time management.

---

### Practical Exam

The repository also preserves solutions from the practical examination:

```text
problem_01.py
problem_02.py
problem_03.py
```

This section is intentionally separated from the normal laboratories and exercises so that it can be treated as a final assessment after studying the other topics.

---

## Labs, Exercises and Exams

The repository follows a progression designed around increasing independence.

### Labs

The `*_Lab` directories focus primarily on learning and implementing the core algorithm.

A productive way to use them is to:

1. Understand the algorithm conceptually.
2. Trace a small example manually.
3. Implement the algorithm.
4. Run it with several inputs.
5. Inspect edge cases.
6. Analyze its complexity.

### Exercises

The `*_Exercise` directories apply the same ideas to less direct problems.

The challenge is often not merely implementing an algorithm, but determining:

> **Which algorithmic model fits the problem?**

That distinction is one of the most important skills in algorithmic problem solving.

### Exam Preparation

The exam-preparation problems combine topics and introduce stronger time constraints.

### Real Exam

The real-exam folder should ideally be approached only after completing the preceding material.

---

## Getting Started

### Prerequisites

You will need:

- **Python 3**
- **Git**
- A terminal or command prompt
- A code editor or IDE such as:
  - PyCharm
  - Visual Studio Code
  - another Python-compatible editor

No project-wide installation process is required for exploring the repository; the material is organized primarily as standalone Python algorithm and problem-solving scripts.

---

### Clone the Repository

```bash
git clone https://github.com/SimeonChifligarov/Algorithms_with_Python.git
cd Algorithms_with_Python
```

Verify Python:

```bash
python --version
```

Depending on your operating system, the command may instead be:

```bash
python3 --version
```

---

### Optional Virtual Environment

A virtual environment is not normally necessary for these standalone algorithm exercises, but it can be useful for keeping development environments isolated.

#### Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
```

#### Windows PowerShell

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

#### Windows Command Prompt

```cmd
py -m venv .venv
.venv\Scripts\activate.bat
```

---

## Running the Solutions

Navigate to the repository root and run an individual Python file.

For example:

```bash
python 01_Recursion_and_Backtracking_Lab/01_Recursive_Array_Sum.py
```

or:

```bash
python 02_Searching_and_Sorting_Algorithms_Lab/01_Binary_Search.py
```

On systems where Python 3 is invoked explicitly:

```bash
python3 05_Dynamic_Programming_Lab/03_Longest_Common_Subsequence.py
```

Many exercises are designed in competitive-programming style and therefore expect input through standard input.

When working through a problem, it is recommended to test:

- The smallest valid input
- Typical input
- Boundary cases
- Empty or minimal structures when valid
- Duplicate values
- Already sorted data
- Reverse-sorted data
- Disconnected graphs
- Graphs containing cycles
- Large inputs where complexity becomes significant

---

## Recommended Learning Path

For the strongest learning progression, work through the repository in the following order.

### 1. Recursion and Backtracking

Start with:

```text
01_Recursion_and_Backtracking_Lab
```

Then continue with:

```text
01_Recursion_and_Backtracking_Exercise
```

Focus on understanding the call stack and identifying exactly what information must be carried between recursive calls.

---

### 2. Searching and Sorting

Continue with:

```text
02_Searching_and_Sorting_Algorithms_Lab
```

Implement each sorting algorithm without looking at another implementation first.

For each algorithm, ask:

- What is the invariant?
- What portion is already sorted?
- How many comparisons are performed?
- Is extra memory required?
- What happens on already-sorted input?

---

### 3. Graph Traversal

Work through:

```text
03_Graph_Th_Traversal_and_Topological_Sorting_Lab
03_Graph_Th_Traversal_and_Topological_Sorting_Exercise
```

Practice recognizing when a problem should be modeled as a graph even when the original statement does not explicitly use graph terminology.

---

### 4. Shortest Paths and Minimum Spanning Trees

Continue with:

```text
04_Graphs_Shortest_Path_and_MST_Lab
04_Graphs_Shortest_Path_and_MST_Exercise
```

At this stage, focus on algorithm selection.

Ask:

- Is the graph weighted?
- Can weights be negative?
- Do I need one shortest path or global connectivity?
- Is the objective shortest distance or minimum total network cost?

The answers determine which algorithm is appropriate.

---

### 5. Dynamic Programming

Continue with:

```text
05_Dynamic_Programming_Lab
05_Dynamic_Programming_Exercise
```

Before writing code, identify:

1. The state.
2. The recurrence.
3. The base case.
4. The evaluation order.
5. The final state containing the answer.

This makes dynamic programming much easier to reason about than attempting to construct a table immediately.

---

### 6. Exam Preparation

After completing the topic-based material:

```text
00_Exam_Preparation
```

Try solving the problems under realistic time constraints.

Avoid checking existing solutions until your own attempt is complete.

---

### 7. Practical Exam

Finally:

```text
00_Exam_Real
```

Treat these solutions as a final reference or review of the material.

---

> [!TIP]
> The most useful way to study algorithms is not to memorize finished code.
>
> Reconstruct the implementation from the underlying idea, trace it manually on small inputs, explain why it works, and only then compare your implementation with an existing solution.

---

## Algorithmic Complexity

Understanding an algorithm requires more than obtaining the correct result.

A solution should also be evaluated in terms of how its resource requirements grow as the input grows.

### Common Growth Rates

| Complexity | Typical Interpretation |
|---|---|
| `O(1)` | Constant time |
| `O(log n)` | Logarithmic |
| `O(n)` | Linear |
| `O(n log n)` | Efficient comparison-based sorting |
| `O(n²)` | Quadratic |
| `O(2ⁿ)` | Exponential |
| `O(n!)` | Factorial |

### Examples from This Repository

| Algorithm | Typical Time Complexity |
|---|---:|
| Binary Search | `O(log n)` |
| Selection Sort | `O(n²)` |
| Bubble Sort | `O(n²)` |
| Insertion Sort | `O(n²)` average/worst |
| Merge Sort | `O(n log n)` |
| QuickSort | `O(n log n)` average |
| BFS | `O(V + E)` |
| DFS | `O(V + E)` |

Actual performance can also depend on:

- Data representation
- Input characteristics
- Graph density
- Pivot selection
- Auxiliary data structures
- Implementation details

Complexity analysis should therefore be combined with an understanding of the concrete implementation.

---

## Educational Scope

This repository is intended for:

- Studying algorithms
- Practicing Python
- Revising graph theory
- Learning dynamic programming
- Preparing for algorithmic examinations
- Reviewing common interview-style concepts
- Experimenting with alternative implementations
- Building stronger problem-solving intuition

It is **not** intended to be:

- A production application
- An installable Python package
- A general-purpose algorithms library
- A stable public API
- A formal performance benchmark
- A replacement for the original course
- A collection of mathematically verified reference implementations

Some solutions were written specifically in the context of educational exercises and online-judge requirements. In those cases, clarity and solving the given task may take precedence over designing a reusable software abstraction.

---

## Contributing

Corrections and improvements are welcome.

Useful contributions may include:

- Fixing bugs
- Correcting edge cases
- Improving naming
- Improving algorithm explanations
- Adding complexity notes
- Improving type hints
- Adding tests
- Improving Python compatibility
- Refactoring code while preserving the original algorithm
- Adding comments where an implementation is difficult to follow
- Documenting alternative algorithmic approaches

A typical workflow:

```bash
git checkout -b improvement/description
```

Make the change and test it, then:

```bash
git add .
git commit -m "Improve Dijkstra implementation"
git push origin improvement/description
```

Open a pull request explaining:

- What was changed
- Why it was changed
- Whether algorithmic complexity changed
- Which test cases were used

Please do not submit copyrighted course statements, paid educational materials, proprietary judge content, or other material that you do not have permission to redistribute.

---

## Course Attribution and Disclaimer

This repository is based on concepts and exercises studied during the:

**SoftUni — Algorithms with Python, July 2022**

The repository was also inspired by **Atanas Atanasov**.

All credit for original educational materials, problem statements, course organization, lectures and associated teaching content belongs to their respective authors and rights holders.

This repository:

- Is independently maintained
- Contains personal implementations created during study
- Is not an official SoftUni repository
- Is not affiliated with or endorsed by SoftUni
- Does not provide access to paid or restricted course materials
- Is intended for educational and reference purposes

The inclusion of names, terminology, exercises or references associated with third parties does not imply ownership of those materials.

---

## License

The original code in this repository is distributed under the terms of the [MIT License](LICENSE).

```text
MIT License

Copyright (c) 2022 Simeon Chifligarov
```

The MIT License applies to material for which the repository owner holds the necessary rights.

It does not override the ownership, copyright, licensing terms, or other rights associated with third-party educational materials, problem statements, trademarks or course content.

---

## Author

**Simeon Chifligarov**

- GitHub: [@SimeonChifligarov](https://github.com/SimeonChifligarov)
- Repository: [Algorithms with Python](https://github.com/SimeonChifligarov/Algorithms_with_Python)

---

### If this repository helped you, consider giving it a star.

**Understand the problem. Choose the algorithm. Prove the idea. Analyze the complexity.**
