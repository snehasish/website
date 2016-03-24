Title: Research 
Date: 2015-03-19
Slug: research 
Author: Snehasish


### Peruse and Profit : Estimating the profitability of loops 
#### Snehasish Kumar, Vijayalakshmi Srinivasan, Amirali Sharifian, Nick Sumner, Arrvindh Shriraman
#### (2016) Proceedings of the 30th Annual ACM International Conference on Supercomputing  

There exist a multitude of execution models available today for a developer to target. The choices vary from general purpose processors to fixed-function hardware accelerators with a large number of variations in-between. There is a growing demand to assess the potential benefits of porting or rewriting an application to a target architecture in order to  fully exploit the benefits of performance and/or energy efficiency offered by such targets. However, as a first step of this process, it is necessary to determine whether the application has characteristics suitable for acceleration.

In this paper, we present Peruse, a tool to characterize the features of loops in an application and to help the programmer understand the amenability of loops for acceleration. We consider a diverse set of features ranging from loop characteristics (e.g., loop exit points) and operation mixes (e.g., control vs data operations) to wider code region characteristics (e.g., idempotency, vectorizability). Peruse is language, architecture, and input independent and uses the intermediate representations of compilers to do the characterization. Using static analyse makes Peruse scalable and enables analysis of large applications of identify and extract interesting loops suitable for acceleration. We show analysis results for unmodified applications from the SPEC CPU benchmark suite, Polybench, and HPC workloads.

For an end-user it is more desirable to get an estimate of the potential speedup due to acceleration. We use the workload characterization results of Peruse as features and develop a machine-learning based model to predict the potential speedup of a loop when off-loaded to a fixed function hardware accelerator. We use the model to predict the speedup of loops selected by Peruse and achieve an accuracy of 79%.

---

### Fusion : Design Tradeoffs in Coherent Cache Hierarchies for Accelerators 
#### Snehasish Kumar, Arrvindh Shriraman, Naveen Vedula
#### (2015) Proceedings of the 42nd Annual IEEE/ACM International Symposium on Computer Architecture 

Chip designers have shown increasing interest in integrating specialized fixed-function coprocessors into multicore designs to improve energy efficiency. Recent work in academia and industry has sought to enable more fine-grain offloading at the granularity of functions and loops. The sequential program now needs to migrate across the chip utilizing the appropriate accelerator for each program region. As the execution migrates, it has become increasingly challenging to retain the temporal and spatial locality of the original program as well as manage the data sharing.

We show that with the increasing energy cost of wires and caches relative to compute operations, it is imperative to optimize data movement to retain the energy benefits of accelerators. We develop FUSION, a lightweight coherent cache hierarchy for accelerators and study the tradeoffs compared to a scratchpad based architecture. We find that coherency, both between the accelerators and with the CPU, can help minimize data movement and save energy. FUSION leverages temporal coherence to optimize data movement within the accelerator tile. The accelerator tile includes small per-accelerator L0 caches to minimize hit energy and a per-tile shared cache to improve localized-sharing between accelerators and minimize data exchanges with the host LLC. We find that overall FUSION improves performance by 4.3× compared to an oracle DMA that pushes data into the scratchpad. In workloads with inter-accelerator sharing we save up to 10x the dynamic energy of the cache hierarchy by minimizing the host-accelerator data ping-ponging.

[PDF from ACM DL](http://dl.acm.org/citation.cfm?id=2750421)  
[Conference PPTX]({filename}/docs/ISCA15_Kumar_Fusion.pptx)  
[Conference Video](https://youtu.be/TIUQ2FlDVPQ)  

---

### DASX : Hardware Accelerator for Collecting Software Data Structures 
#### Snehasish Kumar, Naveen Vedula, Arrvindh Shriraman, Vijayalakshmi Srinivasan
#### (2015) Proceedings of the 29th Annual ACM International Conference on Supercomputing

Recent research has proposed compute accelerators to
address the energy efficiency challenge. While these compute accelerators
specialize and improve the compute efficiency, they have
tended to rely on address-based load/store memory interface that closely
resembles a traditional processor core; in some cases accelerators
even tend to use the core for loads and stores. The address-based
load/store interface is particularly challenging in datacentric applications
that tend to access different software data structures. While
accelerators optimize the compute section, the address-based interface
leads to wasteful instructions and low memory level parallelism
(MLP). We study the benefits of raising the abstraction of the memory
interface to data structures.
We propose DAX (Datastructure Accelerator), a specialized data
fetch state machine that enables compute accelerators to efficiently
access data structure elements in iterative program regions. DAX enables
the compute accelerators to employ data structure based memory
operations and relieves the compute unit from having to generate
addresses for each individual object. DAX exploits knowledge of the
program’s iteration to i) run ahead of the compute units and gather
data objects for the compute unit (i.e., compute unit memory operations
do not encounter cache misses) and ii) throttle the fetch rate
and adaptively tile the dataset based on the locality characteristics
and guarantee cache residency. We demonstrate three types of data
structure accelerators, Vector, Key-Value, and a BTree. We demonstrate
the benefits of DAX on datacentric applications which have
varied computation kernels but access a few regular data structures.
DAX achieves higher energy efficiency by eliminating the data structure
instructions and enabling energy efficient compute accelerators
to efficiently access the data elements. We demonstrate that DAX can
achieve 4.4× the performance improvement of the multicore system
by discovering more parallelism from the data structure.

[PDF from ACM DL](http://dl.acm.org/citation.cfm?id=2751231)  
[Conference PPTX]({filename}/docs/ICS15_Kumar_DASX.pptx)  

---

### Protozoa : Adaptive Granularity Cache Coherence 
#### Hongzhou Zhao, Arrvindh Shriraman, Snehasish Kumar, Sandhya Dwarkadas
#### (2013) Proceedings of the 40th Annual IEEE/ACM International Symposium on Computer Architecture 

State-of-the-art multiprocessor cache hierarchies propagate the use
of a fixed granularity in the cache organization to the design of the
coherence protocol. Unfortunately, the fixed granularity, generally
chosen to match average spatial locality across a range of applications,
not only results in wasted bandwidth to serve an individual
thread’s access needs, but also results in unnecessary coherence traf-
fic for shared data. The additional bandwidth has a direct impact on
both the scalability of parallel applications and overall energy consumption.
In this paper, we present the design of Protozoa, a family of coherence
protocols that eliminate unnecessary coherence traffic and
match data movement to an application’s spatial locality. Protozoa
continues to maintain metadata at a conventional fixed cache
line granularity while 1) supporting variable read and write caching
granularity so that data transfer matches application spatial granularity,
2) invalidating at the granularity of the write miss request so
that readers to disjoint data can co-exist with writers, and 3) potentially
supporting multiple non-overlapping writers within the cache
line, thereby avoiding the traditional ping-pong effect of both readwrite
and write-write false sharing. Our evaluation demonstrates that
Protozoa consistently reduce miss rate and improve the fraction of
transmitted data that is actually utilized.

[PDF from ACM DL](http://dl.acm.org/citation.cfm?id=2485969)  

---

### Amoeba-Cache: Adaptive Blocks for Eliminating Waste in the Memory Hierarchy
#### Snehasish Kumar, Hongzhou Zhao, Arrvindh Shriraman, Eric Matthews, Sandhya Dwarkadas, Lesley Shannon
#### (2012) Proceedings of the 45th Annual IEEE/ACM International Symposium on Microarchitecture 

The fixed geometries of current cache designs do not adapt to the
working set requirements of modern applications, causing significant
inefficiency. The short block lifetimes and moderate spatial locality
exhibited by many applications result in only a few words in the
block being touched prior to eviction. Unused words occupy between
17—80% of a 64K L1 cache and between 1%—79% of a 1MB private
LLC. This effectively shrinks the cache size, increases miss rate, and
wastes on-chip bandwidth. Scaling limitations of wires mean that
unused-word transfers comprise a large fraction (11%) of on-chip
cache hierarchy energy consumption.

We propose Amoeba-Cache, a design that supports a variable number
of cache blocks, each of a different granularity. Amoeba-Cache
employs a novel organization that completely eliminates the tag array,
treating the storage array as uniform and morphable between tags
and data. This enables the cache to harvest space from unused words
in blocks for additional tag storage, thereby supporting a variable
number of tags (and correspondingly, blocks). Amoeba-Cache adjusts
individual cache line granularities according to the spatial locality
in the application. It adapts to the appropriate granularity both for
different data objects in an application as well as for different phases
of access to the same data. Overall, compared to a fixed granularity
cache, the Amoeba-Cache reduces miss rate on average (geometric
mean) by 18% at the L1 level and by 18% at the L2 level and reduces
L1—L2 miss bandwidth by '46%. Correspondingly, Amoeba-Cache
reduces on-chip memory hierarchy energy by as much as 36% (mcf)
and improves performance by as much as 50% (art).

[PDF from ACM DL](http://dl.acm.org/citation.cfm?id=2457513)  

---

### MiCi : A Novel Micro-Level Temporal Channel Imploration for Mobile Hosts 
#### Snehasish Kumar, SC Rai, Rajib Mall, Sateesh K Pradhan 
#### (2011) InterJRI : Computer Science and Networking

The exponential increase of multimedia services by the mobile users requires seamless connectivity with costeffective
Quality of Service (QoS) provisioning. For providing such on-demand QoS, the network needs to utilize the radio
channels among the Mobile Hosts (MHs) effectively. We use vector genetic algorithm (VGA) for temporal imploration of
sharable channel(s) from the neighbouring cell(s) to fulfill the needs of a cell. We propose a new micro-level temporal
channel imploration mechanism (MiCi), which promptly allocates available borrowing channel(s) of the neighbouring cell(s)
to the needy cell. The novelty of MiCi is scalability, high availability, and on-demand allocation of the channels to the
desired cells. The performance of our model has been tested by simulation against a standard FCA scheme as well as a
Greedy Borrowing Heuristic. In all the test cases MiCi shows promising results in comparison to both the schemes.

[PDF from Arxiv](http://arxiv.org/ftp/arxiv/papers/1104/1104.4204.pdf)  

---
