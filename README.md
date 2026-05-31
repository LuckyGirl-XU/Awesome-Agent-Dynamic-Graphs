# Awesome Agent Dynamic Graphs

[![Awesome](https://awesome.re/badge.svg)](https://awesome.re)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](#contributing)
![Last Commit](https://img.shields.io/github/last-commit/LuckyGirl-XU/Awesome-Agent-Dynamic-Graphs)
![Visitors](https://visitor-badge.laobi.icu/badge?page_id=LuckyGirl-XU.Awesome-Agent-Dynamic-Graphs)

This repository organizes papers on self-evolving agents, dynamic graph transformation, dynamic graph learning infrastructure, and graph-aware benchmarks.

> Based on the survey: **Self-Evolving Agents as Dynamic Graph Transformation: A Survey and Roadmap**

![Framework overview](figs/overview.png)

## News

**[05/30/26]** Initial reading list released. The taxonomy follows the survey structure, with a separate benchmark section.

## Table of Contents

- [Agent Evolution as Dynamic Graph Transformation](#agent-evolution-as-dynamic-graph-transformation)
  - [Node and Feature Evolution](#node-and-feature-evolution)
  - [Edge and Topology Evolution](#edge-and-topology-evolution)
  - [Subgraph Activation](#subgraph-activation)
  - [Cross-Component Co-Evolution](#cross-component-co-evolution)
- [Dynamic Graph Learning as Agent-Evolution Infrastructure](#dynamic-graph-learning-as-agent-evolution-infrastructure)
  - [Dynamic Graph Learning](#dynamic-graph-learning)
  - [Dynamic Text-Attributed Graphs](#dynamic-text-attributed-graphs)
  - [Dynamic Graph Generation](#dynamic-graph-generation)
  - [Continual Learning on Dynamic Graphs](#continual-learning-on-dynamic-graphs)
  - [Out-of-Distribution Generalization on Dynamic Graphs](#out-of-distribution-generalization-on-dynamic-graphs)
  - [Temporal Knowledge Graph Reasoning](#temporal-knowledge-graph-reasoning)
  - [Anomaly Detection on Dynamic Graphs](#anomaly-detection-on-dynamic-graphs)
  - [Dynamic Graph Unlearning](#dynamic-graph-unlearning)
  - [Explanation for Temporal GNNs](#explanation-for-temporal-gnns)
- [Graph-Aware Evaluation and Governance](#graph-aware-evaluation-and-governance)
  - [Graph-Aware Evaluation](#graph-aware-evaluation)
  - [Leakage-Free Temporal Protocols](#leakage-free-temporal-protocols)
  - [Privacy and Deletion in Evolving Agent Graphs](#privacy-and-deletion-in-evolving-agent-graphs)
  - [Safety, Rollback, and Audit](#safety-rollback-and-audit)
  - [Open Challenges](#open-challenges)
- [Benchmarks](#benchmarks)

---

## Introduction

Large language model agents are becoming long-running systems that store memories, use tools, acquire skills, refine workflows, and collaborate with other agents. This repository follows a dynamic-graph view of these systems: evolving agent state is represented through typed nodes, edges, features, subgraphs, and temporal rewrites.

## Agent Evolution as Dynamic Graph Transformation

![Agent evolution taxonomy](figs/agent-evolution.png)

### Node and Feature Evolution

| Paper | Year |
| --- | --- |
| [MemGPT: Towards LLMs as operating systems](https://arxiv.org/abs/2310.08560) | 2023 |
| [A-MEM: Agentic memory for LLM agents](https://arxiv.org/abs/2502.12110) | 2025 |
| [Gorilla: Large language model connected with massive APIs](https://arxiv.org/abs/2305.15334) | 2023 |
| [Voyager: An open-ended embodied agent with large language models](https://arxiv.org/abs/2305.16291) | 2024 |
| [ExpeL: LLM agents are experiential learners](https://doi.org/10.1609/aaai.v38i17.29936) | 2024 |
| [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversations](https://arxiv.org/abs/2308.08155) | 2024 |
| [A dynamic LLM-powered agent network for task-oriented agent collaboration](https://arxiv.org/abs/2310.02170) | 2024 |
| [Zep: A temporal knowledge graph architecture for agent memory](https://arxiv.org/abs/2501.13956) | 2025 |
| [Generative agents: Interactive simulacra of human behavior](https://doi.org/10.1145/3586183.3606763) | 2023 |
| [LangChain](https://github.com/langchain-ai/langchain) | 2022 |
| [LlamaIndex: A data framework for LLM applications](https://github.com/run-llama/llama_index) | 2023 |
| [Mem0: Building production-ready AI agents with scalable long-term memory](https://arxiv.org/abs/2504.19413) | 2025 |
| [MemoryBank: Enhancing large language models with long-term memory](https://arxiv.org/abs/2305.10250) | 2023 |
| [Larimar: Large language models with episodic memory control](https://arxiv.org/abs/2403.11901) | 2024 |
| [MemoryLLM: Towards self-updatable large language models](https://arxiv.org/abs/2402.04624) | 2024 |
| [Memory OS of AI Agent](https://arxiv.org/abs/2506.06326) | 2025 |
| [Evaluating very long-term conversational memory of LLM agents](https://aclanthology.org/2024.acl-long.747/) | 2024 |
| [LongMemEval: Benchmarking chat assistants on long-term interactive memory](https://arxiv.org/abs/2410.10813) | 2025 |
| [MemBench: Towards more comprehensive evaluation on the memory of LLM-based agents](https://aclanthology.org/2025.findings-acl.989/) | 2025 |
| [ToolNet: Connecting large language models with massive tools via tool graph](https://arxiv.org/abs/2403.00839) | 2024 |
| [SEARL: Joint Optimization of Policy and Tool Graph Memory for Self-Evolving Agents](https://arxiv.org/abs/2604.07791) | 2026 |
| [Toolformer: Language models can teach themselves to use tools](https://arxiv.org/abs/2302.04761) | 2023 |
| [ToolLLM: Facilitating large language models to master 16000+ real-world APIs](https://arxiv.org/abs/2307.16789) | 2024 |
| [An LLM compiler for parallel function calling](https://arxiv.org/abs/2312.04511) | 2024 |
| [ToolAlpaca: Generalized tool learning for language models with 3000 simulated cases](https://arxiv.org/abs/2306.05301) | 2023 |
| [API-Bank: A comprehensive benchmark for tool-augmented LLMs](https://aclanthology.org/2023.emnlp-main.187/) | 2023 |
| [ToolSandbox: A stateful, conversational, interactive evaluation benchmark for LLM tool use capabilities](https://arxiv.org/abs/2408.04682) | 2024 |
| [Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard) | 2024 |
| [AutoAct: Automatic agent learning from scratch for QA via self-planning](https://arxiv.org/abs/2401.05268) | 2024 |
| [Symbolic learning enables self-evolving agents](https://arxiv.org/abs/2406.18532) | 2024 |
| [Agent hospital: A simulacrum of hospital with evolvable medical agents](https://arxiv.org/abs/2405.02957) | 2024 |
| [MetaGPT: Meta programming for a multi-agent collaborative framework](https://arxiv.org/abs/2308.00352) | 2024 |
| [AgentBoard: An analytical evaluation board of multi-turn LLM agents](https://arxiv.org/abs/2401.13178) | 2024 |
| [AgentVerse: Facilitating multi-agent collaboration and exploring emergent behaviors](https://arxiv.org/abs/2308.10848) | 2024 |
| [Temporal graph networks for deep learning on dynamic graphs](https://arxiv.org/abs/2006.10637) | 2020 |
| [DyRep: Learning representations over dynamic graphs](https://arxiv.org/abs/1809.02699) | 2019 |
| [Unlocking multi-modal potentials for link prediction on dynamic text-attributed graphs](https://arxiv.org/abs/2502.19651) | 2026 |
| [Dynamic graph unlearning: a general and efficient post-processing method via gradient transformation](https://arxiv.org/abs/2405.14407) | 2025 |
| [AFlow: Automating agentic workflow generation](https://arxiv.org/abs/2410.10762) | 2025 |
| [DynTaskMAS: A Dynamic Task Graph-driven Framework for Asynchronous and Parallel LLM-based Multi-Agent Systems](https://arxiv.org/abs/2503.07675) | 2025 |
| [Cut the crap: An economical communication pipeline for LLM-based multi-agent systems](https://arxiv.org/abs/2410.02506) | 2024 |
| [AgentDropout: Dynamic Agent Elimination for Token-Efficient and High-Performance LLM-Based Multi-Agent Collaboration](https://arxiv.org/abs/2503.18891) | 2025 |
| [DyTopo: Dynamic Topology Routing for Multi-Agent Reasoning via Semantic Matching](https://arxiv.org/abs/2602.06039) | 2026 |
| [Dynamic Generation of Multi-LLM Agents Communication Topologies with Graph Diffusion Models](https://arxiv.org/abs/2510.07799) | 2025 |
| [AMAS: Adaptively Determining Communication Topology for LLM-based Multi-Agent System](https://arxiv.org/abs/2510.01617) | 2025 |
| [Guardian: Safeguarding llm multi-agent collaborations with temporal graph modeling](https://arxiv.org/abs/2505.19234) | 2025 |
| [SentinelAgent: Graph-based Anomaly Detection in Multi-Agent Systems](https://arxiv.org/abs/2505.24201) | 2025 |

### Edge and Topology Evolution

| Paper | Year |
| --- | --- |
| [AFlow: Automating agentic workflow generation](https://arxiv.org/abs/2410.10762) | 2025 |
| [DynTaskMAS: A Dynamic Task Graph-driven Framework for Asynchronous and Parallel LLM-based Multi-Agent Systems](https://arxiv.org/abs/2503.07675) | 2025 |
| [Cut the crap: An economical communication pipeline for LLM-based multi-agent systems](https://arxiv.org/abs/2410.02506) | 2024 |
| [AgentDropout: Dynamic Agent Elimination for Token-Efficient and High-Performance LLM-Based Multi-Agent Collaboration](https://arxiv.org/abs/2503.18891) | 2025 |
| [DyTopo: Dynamic Topology Routing for Multi-Agent Reasoning via Semantic Matching](https://arxiv.org/abs/2602.06039) | 2026 |
| [Dynamic Generation of Multi-LLM Agents Communication Topologies with Graph Diffusion Models](https://arxiv.org/abs/2510.07799) | 2025 |
| [ToolNet: Connecting large language models with massive tools via tool graph](https://arxiv.org/abs/2403.00839) | 2024 |
| [Voyager: An open-ended embodied agent with large language models](https://arxiv.org/abs/2305.16291) | 2024 |
| [GPTSwarm: Language agents as optimizable graphs](https://arxiv.org/abs/2402.16823) | 2024 |
| [AgentSquare: Automatic LLM agent search in modular design space](https://arxiv.org/abs/2410.06153) | 2025 |
| [DSPy: Compiling Declarative Language Model Calls into State-of-the-Art Pipelines](https://arxiv.org/abs/2310.03714) | 2024 |
| [An LLM compiler for parallel function calling](https://arxiv.org/abs/2312.04511) | 2024 |
| [Tree of thoughts: Deliberate problem solving with large language models](https://doi.org/10.52202/075280-0517) | 2023 |
| [Graph of thoughts: Solving elaborate problems with large language models](https://doi.org/10.1609/aaai.v38i16.29720) | 2024 |
| [Plan-and-solve prompting: Improving zero-shot chain-of-thought reasoning by large language models](https://aclanthology.org/2023.acl-long.147/) | 2023 |
| [ReAct: Synergizing reasoning and acting in language models](https://arxiv.org/abs/2210.03629) | 2023 |
| [Chain-of-thought prompting elicits reasoning in large language models](https://arxiv.org/abs/2201.11903) | 2022 |
| [Self-consistency improves chain of thought reasoning in language models](https://arxiv.org/abs/2203.11171) | 2023 |
| [Language agent tree search unifies reasoning, acting, and planning in language models](https://arxiv.org/abs/2310.04406) | 2024 |
| [ReWOO: Decoupling reasoning from observations for efficient augmented language models](https://arxiv.org/abs/2305.18323) | 2023 |
| [PDDL2.1: An extension to PDDL for expressing temporal planning domains](https://doi.org/10.1613/jair.1129) | 2003 |
| [SHOP2: An HTN planning system](https://doi.org/10.1613/jair.1141) | 2003 |
| [Process mining manifesto](https://doi.org/10.1007/978-3-642-28108-2_19) | 2011 |
| [The application of Petri nets to workflow management](https://doi.org/10.1142/S0218126698000043) | 1998 |
| [Business process management: A comprehensive survey](https://doi.org/10.1155/2013/507984) | 2013 |
| [Conformance checking of processes based on monitoring real behavior](https://doi.org/10.1016/j.is.2008.07.001) | 2008 |
| [From process mining to augmented process execution](https://doi.org/10.1007/s10270-023-01132-2) | 2023 |
| [The vision of autonomic computing](https://doi.org/10.1109/MC.2003.1160055) | 2003 |
| [Self-adaptive software: Landscape and research challenges](https://doi.org/10.1145/1516533.1516538) | 2009 |
| [ChatDev: Communicative agents for software development](https://aclanthology.org/2024.acl-long.810/) | 2024 |
| [CAMEL: Communicative agents for "mind" exploration of large language model society](https://doi.org/10.52202/075280-2264) | 2023 |
| [MetaGPT: Meta programming for a multi-agent collaborative framework](https://arxiv.org/abs/2308.00352) | 2024 |
| [AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversations](https://arxiv.org/abs/2308.08155) | 2024 |
| [AgentScope: A flexible yet robust multi-agent platform](https://arxiv.org/abs/2402.14034) | 2024 |
| [A dynamic LLM-powered agent network for task-oriented agent collaboration](https://arxiv.org/abs/2310.02170) | 2024 |
| [AgentVerse: Facilitating multi-agent collaboration and exploring emergent behaviors](https://arxiv.org/abs/2308.10848) | 2024 |
| [Improving factuality and reasoning in language models through multiagent debate](https://arxiv.org/abs/2305.14325) | 2024 |
| [Encouraging divergent thinking in large language models through multi-agent debate](https://aclanthology.org/2024.emnlp-main.992/) | 2024 |
| [Automated design of agentic systems](https://arxiv.org/abs/2408.08435) | 2024 |
| [TodyComm: Task-Oriented Dynamic Communication for Multi-Round LLM-based Multi-Agent System](https://arxiv.org/abs/2602.03688) | 2026 |
| [AMAS: Adaptively Determining Communication Topology for LLM-based Multi-Agent System](https://arxiv.org/abs/2510.01617) | 2025 |
| [Graph-of-Agents: A Graph-based Framework for Multi-Agent LLM Collaboration](https://arxiv.org/abs/2604.17148) | 2026 |
| [Multi-Agent Collaboration via Evolving Orchestration](https://arxiv.org/abs/2505.19591) | 2025 |
| [Scaling large language model based multi-agent collaboration](https://arxiv.org/abs/2406.07155) | 2024 |
| [Methods for task allocation via agent coalition formation](https://doi.org/10.1016/S0004-3702%2898%2900045-9) | 1998 |
| [Trust in multi-agent systems](https://doi.org/10.1017/S0269888904000116) | 2004 |
| [Review on computational trust and reputation models](https://doi.org/10.1007/s10462-004-0041-5) | 2005 |
| [Learning multiagent communication with backpropagation](https://arxiv.org/abs/1605.07736) | 2016 |
| [Learning to communicate with deep multi-agent reinforcement learning](https://arxiv.org/abs/1605.06676) | 2016 |
| [TarMAC: Targeted multi-agent communication](https://proceedings.mlr.press/v97/das19a.html) | 2019 |
| [Cognitive architectures for language agents](https://arxiv.org/abs/2309.02427) | 2024 |
| [HuggingGPT: Solving AI tasks with ChatGPT and its friends in Hugging Face](https://doi.org/10.52202/075280-1657) | 2023 |
| [ChatDB: Augmenting LLMs with databases as their symbolic memory](https://arxiv.org/abs/2306.03901) | 2023 |
| [Inductive representation learning on temporal graphs](https://openreview.net/forum?id=rJeW1yHYwH) | 2020 |
| [TimeSGN: Scalable and effective temporal graph neural network](https://doi.org/10.1109/ICDE60146.2024.00133) | 2024 |
| [AddGraph: Anomaly detection in dynamic graph using attention-based temporal GCN](https://www.ijcai.org/proceedings/2019/614) | 2019 |
| [Anomaly detection in dynamic graphs via transformer](https://doi.org/10.1109/TKDE.2021.3124061) | 2021 |
| [Slade: Detecting dynamic anomalies in edge streams without labels via self-supervised learning](https://doi.org/10.1145/3637528.3671861) | 2024 |

### Subgraph Activation

| Paper | Year |
| --- | --- |
| [Think-on-Graph 3.0: Efficient and Adaptive LLM Reasoning on Heterogeneous Graphs via Multi-Agent Dual-Evolving Context Retrieval](https://arxiv.org/abs/2509.21710) | 2025 |
| [A dynamic LLM-powered agent network for task-oriented agent collaboration](https://arxiv.org/abs/2310.02170) | 2024 |
| [DyTopo: Dynamic Topology Routing for Multi-Agent Reasoning via Semantic Matching](https://arxiv.org/abs/2602.06039) | 2026 |
| [MemGPT: Towards LLMs as operating systems](https://arxiv.org/abs/2310.08560) | 2023 |
| [A-MEM: Agentic memory for LLM agents](https://arxiv.org/abs/2502.12110) | 2025 |
| [Zep: A temporal knowledge graph architecture for agent memory](https://arxiv.org/abs/2501.13956) | 2025 |
| [AFlow: Automating agentic workflow generation](https://arxiv.org/abs/2410.10762) | 2025 |
| [GPTSwarm: Language agents as optimizable graphs](https://arxiv.org/abs/2402.16823) | 2024 |
| [AgentSquare: Automatic LLM agent search in modular design space](https://arxiv.org/abs/2410.06153) | 2025 |
| [Automated design of agentic systems](https://arxiv.org/abs/2408.08435) | 2024 |
| [DynTaskMAS: A Dynamic Task Graph-driven Framework for Asynchronous and Parallel LLM-based Multi-Agent Systems](https://arxiv.org/abs/2503.07675) | 2025 |
| [Voyager: An open-ended embodied agent with large language models](https://arxiv.org/abs/2305.16291) | 2024 |
| [TodyComm: Task-Oriented Dynamic Communication for Multi-Round LLM-based Multi-Agent System](https://arxiv.org/abs/2602.03688) | 2026 |
| [AMAS: Adaptively Determining Communication Topology for LLM-based Multi-Agent System](https://arxiv.org/abs/2510.01617) | 2025 |
| [Ranking on dynamic graphs: An effective and robust band-pass disentangled approach](https://openreview.net/forum?id=cah0ZYeMz0) | 2025 |
| [Rush: Real-time burst subgraph detection in dynamic graphs](https://doi.org/10.14778/3681954.3682028) | 2024 |
| [AgentBench: Evaluating LLMs as agents](https://arxiv.org/abs/2308.03688) | 2024 |
| [GAIA: A benchmark for general AI assistants](https://arxiv.org/abs/2311.12983) | 2024 |
| [SWE-bench: Can language models resolve real-world GitHub issues?](https://arxiv.org/abs/2310.06770) | 2024 |
| [tau-bench: A benchmark for tool-agent-user interaction in real-world domains](https://arxiv.org/abs/2406.12045) | 2024 |
| [OSWorld: Benchmarking multimodal agents for open-ended tasks in real computer environments](https://doi.org/10.52202/079017-1650) | 2024 |
| [Mind2Web: Towards a generalist agent for the web](https://doi.org/10.52202/075280-1220) | 2023 |

### Cross-Component Co-Evolution

| Paper | Year |
| --- | --- |
| [Reflexion: Language agents with verbal reinforcement learning](https://doi.org/10.52202/075280-0377) | 2023 |
| [Self-Refine: Iterative refinement with self-feedback](https://doi.org/10.52202/075280-2019) | 2023 |
| [ExpeL: LLM agents are experiential learners](https://doi.org/10.1609/aaai.v38i17.29936) | 2024 |
| [AFlow: Automating agentic workflow generation](https://arxiv.org/abs/2410.10762) | 2025 |
| [GPTSwarm: Language agents as optimizable graphs](https://arxiv.org/abs/2402.16823) | 2024 |
| [Guardian: Safeguarding llm multi-agent collaborations with temporal graph modeling](https://arxiv.org/abs/2505.19234) | 2025 |
| [SentinelAgent: Graph-based Anomaly Detection in Multi-Agent Systems](https://arxiv.org/abs/2505.24201) | 2025 |
| [Automated design of agentic systems](https://arxiv.org/abs/2408.08435) | 2024 |
| [A dynamic LLM-powered agent network for task-oriented agent collaboration](https://arxiv.org/abs/2310.02170) | 2024 |
| [DyTopo: Dynamic Topology Routing for Multi-Agent Reasoning via Semantic Matching](https://arxiv.org/abs/2602.06039) | 2026 |
| [Agent hospital: A simulacrum of hospital with evolvable medical agents](https://arxiv.org/abs/2405.02957) | 2024 |
| [AutoAct: Automatic agent learning from scratch for QA via self-planning](https://arxiv.org/abs/2401.05268) | 2024 |
| [Memory OS of AI Agent](https://arxiv.org/abs/2506.06326) | 2025 |

---

## Dynamic Graph Learning as Agent-Evolution Infrastructure

![Dynamic graph learning infrastructure](figs/infrastructure.png)

### Dynamic Graph Learning

| Paper | Year |
| --- | --- |
| [Temporal graph networks for deep learning on dynamic graphs](https://arxiv.org/abs/2006.10637) | 2020 |
| [Towards better dynamic graph learning: New architecture and unified library](https://doi.org/10.52202/075280-2960) | 2023 |
| [Do we really need complicated model architectures for temporal networks?](https://arxiv.org/abs/2302.11636) | 2023 |
| [State space models on temporal graphs: A first-principles study](https://doi.org/10.52202/079017-4034) | 2024 |
| [Supra-laplacian encoding for transformer on dynamic graphs](https://doi.org/10.52202/079017-0547) | 2024 |
| [Freedyg: Frequency enhanced continuous-time dynamic graph model for link prediction](https://openreview.net/forum?id=82Mc5ilInM) | 2024 |
| [SALoM: Structure Aware Temporal Graph Networks with Long-Short Memory Updater](https://papers.neurips.cc/paper_files/paper/2025/hash/20f94998511f25bb6378cae0e098bc46-Abstract-Conference.html) | 2025 |
| [Simple: Efficient temporal graph neural network training at scale with dynamic data placement](https://doi.org/10.1145/3654977) | 2024 |
| [Etc: Efficient training of temporal graph neural networks over large-scale dynamic graphs](https://doi.org/10.14778/3641204.3641215) | 2024 |
| [On the scalability of temporal relative positional encoding for dynamic link prediction](https://doi.org/10.1145/3711896.3737069) | 2025 |
| [Repeat-Aware Neighbor Sampling for Dynamic Graph Learning](https://doi.org/10.1145/3637528.3672001) | 2024 |
| [Neighborhood-aware scalable temporal network representation learning](https://arxiv.org/abs/2209.01084) | 2022 |
| [Long Range Propagation on Continuous-Time Dynamic Graphs](https://arxiv.org/abs/2406.02740) | 2024 |
| [Towards better dynamic graph learning: New architecture and unified library](https://doi.org/10.52202/075280-2960) | 2023 |
| [FreeDyG: Frequency Enhanced Continuous-Time Dynamic Graph Model for Link Prediction](https://openreview.net/forum?id=82Mc5ilInM) | 2024 |
| [Robust knowledge adaptation for dynamic graph neural networks](https://doi.org/10.1109/TKDE.2024.3388453) | 2024 |
| [Co-Neighbor Encoding Schema: A Light-cost Structure Encoding Method for Dynamic Link Prediction](https://doi.org/10.1145/3637528.3671682) | 2024 |
| [Retrieval augmented generation for dynamic graph modeling](https://doi.org/10.1145/3726302.3730030) | 2025 |
| [Representation learning for dynamic graphs: A survey](https://jmlr.org/papers/v21/19-447.html) | 2020 |
| [Foundations and modeling of dynamic networks using dynamic graph neural networks: A survey](https://doi.org/10.1109/ACCESS.2021.3082932) | 2021 |
| [Graph neural networks for temporal graphs: State of the art, open challenges, and opportunities](https://openreview.net/forum?id=1GVpwr2Tfdg) | 2023 |
| [dyngraph2vec: Capturing network dynamics using dynamic graph representation learning](https://doi.org/10.1016/j.knosys.2019.06.024) | 2020 |
| [DySAT: Deep neural representation learning on dynamic graphs via self-attention networks](https://arxiv.org/abs/1812.09430) | 2020 |
| [EvolveGCN: Evolving graph convolutional networks for dynamic graphs](https://doi.org/10.1609/aaai.v34i04.5984) | 2020 |
| [ROLAND: Graph learning framework for dynamic graphs](https://doi.org/10.1145/3534678.3539300) | 2022 |
| [A novel representation learning for dynamic graphs based on graph convolutional networks](https://doi.org/10.1109/TCYB.2022.3159661) | 2022 |
| [HGWaveNet: A Hyperbolic Graph Neural Network for Temporal Link Prediction](https://doi.org/10.1145/3543507.3583423) | 2023 |
| [SEIGN: A Simple and Efficient Graph Neural Network for Large Dynamic Graphs](https://doi.org/10.1109/ICDE55515.2023.00206) | 2023 |
| [An Attentional Multi-scale Co-evolving Model for Dynamic Link Prediction](https://doi.org/10.1145/3543507.3583358) | 2023 |
| [Scaling Up Dynamic Graph Representation Learning via Spiking Neural Networks](https://doi.org/10.1609/aaai.v37i7.26004) | 2023 |
| [High-quality temporal link prediction for weighted dynamic graphs via inductive embedding aggregation](https://doi.org/10.1109/TKDE.2023.3238360) | 2023 |
| [Event-based dynamic graph representation learning for patent application trend prediction](https://doi.org/10.1109/TKDE.2023.3312333) | 2023 |
| [Simple and Efficient Heterogeneous Temporal Graph Neural Network](https://arxiv.org/abs/2510.18467) | 2025 |

### Dynamic Text-Attributed Graphs

| Paper | Year |
| --- | --- |
| [DTGB: A comprehensive benchmark for dynamic text-attributed graphs](https://doi.org/10.52202/079017-2901) | 2024 |
| [Unlocking multi-modal potentials for link prediction on dynamic text-attributed graphs](https://arxiv.org/abs/2502.19651) | 2026 |
| [Unifying Text Semantics and Graph Structures for Temporal Text-attributed Graphs with Large Language Models](https://arxiv.org/abs/2503.14411) | 2025 |
| [Llm-driven knowledge distillation for dynamic text-attributed graphs](https://arxiv.org/abs/2502.10914) | 2025 |
| [Global-Recent Semantic Reasoning on Dynamic Text-Attributed Graphs with Large Language Models](https://arxiv.org/abs/2509.18742) | 2025 |
| [Exploring the potential of large language models as predictors in dynamic text-attributed graphs](https://arxiv.org/abs/2503.03258) | 2025 |

### Dynamic Graph Generation

| Paper | Year |
| --- | --- |
| [TG-GAN: Continuous-time temporal graph deep generative models with time-validity constraints](https://doi.org/10.1145/3442381.3449818) | 2021 |
| [A data-driven graph generative model for temporal interaction networks](https://doi.org/10.1145/3394486.3403082) | 2020 |
| [TIGGER: Scalable generative modelling for temporal interaction graphs](https://doi.org/10.1609/aaai.v36i6.20638) | 2022 |
| [A deep probabilistic framework for continuous time dynamic graph generation](https://ojs.aaai.org/index.php/AAAI/article/view/33456) | 2025 |
| [Efficient dynamic attributed graph generation](https://doi.org/10.1109/ICDE65448.2025.00221) | 2025 |
| [GDGB: A Benchmark for Generative Dynamic Text-Attributed Graph Learning](https://arxiv.org/abs/2507.03267) | 2025 |

### Continual Learning on Dynamic Graphs

| Paper | Year |
| --- | --- |
| [A Selective Learning Method for Temporal Graph Continual Learning](https://arxiv.org/abs/2503.01580) | 2025 |
| [Overcoming catastrophic forgetting in graph neural networks with experience replay](https://doi.org/10.1609/aaai.v35i5.16602) | 2021 |
| [A unified replay-based continuous learning framework for spatio-temporal prediction on streaming data](https://doi.org/10.1109/ICDE60146.2024.00232) | 2024 |
| [TOWARDS OPEN TEMPORAL GRAPH NEURAL NETWORKS](https://arxiv.org/abs/2303.15015) | 2023 |
| [Continual learning on dynamic graphs via parameter isolation](https://doi.org/10.1145/3539618.3591652) | 2023 |

### Out-of-Distribution Generalization on Dynamic Graphs

| Paper | Year |
| --- | --- |
| [Dynamic graph neural networks under spatio-temporal distribution shift](https://doi.org/10.52202/068431-0440) | 2022 |
| [Spectral invariant learning for dynamic graphs under distribution shifts](https://doi.org/10.52202/075280-0290) | 2023 |
| [Environment-Aware Dynamic Graph Learning for Out-of-Distribution Generalization](https://doi.org/10.52202/075280-2164) | 2023 |
| [Evolving Graph Learning for Out-of-Distribution Generalization in Non-stationary Environments](https://arxiv.org/abs/2511.02354) | 2025 |

### Temporal Knowledge Graph Reasoning

| Paper | Year |
| --- | --- |
| [Explainable subgraph reasoning for forecasting on temporal knowledge graphs](https://openreview.net/forum?id=pGIHq1m7PU) | 2021 |
| [HyTE: Hyperplane-based temporally aware knowledge graph embedding](https://aclanthology.org/D18-1225/) | 2018 |
| [TeMP: Temporal message passing for temporal knowledge graph completion](https://aclanthology.org/2020.emnlp-main.462/) | 2020 |
| [Tensor decompositions for temporal knowledge base completion](https://arxiv.org/abs/2004.04926) | 2020 |
| [Know-Evolve: Deep temporal reasoning for dynamic knowledge graphs](https://arxiv.org/abs/1705.05742) | 2017 |
| [Recurrent event network: Autoregressive structure inference over temporal knowledge graphs](https://aclanthology.org/2020.emnlp-main.541/) | 2020 |
| [Learning from history: Modeling temporal knowledge graphs with sequential copy-generation networks](https://doi.org/10.1609/aaai.v35i5.16604) | 2021 |
| [Temporal knowledge graph reasoning based on evolutional representation learning](https://doi.org/10.1145/3404835.3462963) | 2021 |
| [GenTKG: Generative forecasting on temporal knowledge graph with large language models](https://aclanthology.org/2024.findings-naacl.268/) | 2024 |
| [Integrate Temporal Graph Learning into LLM-based Temporal Knowledge Graph Model](https://arxiv.org/abs/2501.11911) | 2025 |
| [Enhancing Temporal Knowledge Graph Forecasting with Large Language Models via Chain-of-History Reasoning](https://arxiv.org/abs/2402.14382) | 2024 |

### Anomaly Detection on Dynamic Graphs

| Paper | Year |
| --- | --- |
| [AgentDojo: A dynamic environment to evaluate prompt injection attacks and defenses for LLM agents](https://doi.org/10.52202/079017-2636) | 2024 |
| [Agent security bench (ASB): Formalizing and benchmarking attacks and defenses in LLM-based agents](https://arxiv.org/abs/2410.02644) | 2025 |
| [Not what you've signed up for: Compromising real-world LLM-integrated applications with indirect prompt injection](https://doi.org/10.1145/3605764.3623985) | 2023 |
| [SentinelAgent: Graph-based Anomaly Detection in Multi-Agent Systems](https://arxiv.org/abs/2505.24201) | 2025 |
| [Anomaly Detection in Dynamic Graphs: A Comprehensive Survey](https://doi.org/10.1145/3669906) | 2024 |
| [Structural temporal graph neural networks for anomaly detection in dynamic graphs](https://doi.org/10.1145/3459637.3481955) | 2021 |
| [Anonymous Edge Representation for Inductive Anomaly Detection in Dynamic Bipartite Graph](https://doi.org/10.14778/3579075.3579088) | 2023 |
| [AddGraph: Anomaly detection in dynamic graph using attention-based temporal GCN](https://www.ijcai.org/proceedings/2019/614) | 2019 |
| [Anomaly detection in dynamic graphs via transformer](https://doi.org/10.1109/TKDE.2021.3124061) | 2021 |
| [Slade: Detecting dynamic anomalies in edge streams without labels via self-supervised learning](https://doi.org/10.1145/3637528.3671861) | 2024 |

### Dynamic Graph Unlearning

| Paper | Year |
| --- | --- |
| [Dynamic graph unlearning: a general and efficient post-processing method via gradient transformation](https://arxiv.org/abs/2405.14407) | 2025 |
| [Spatio-Temporal Graph Unlearning](https://arxiv.org/abs/2511.09404) | 2025 |

### Explanation for Temporal GNNs

| Paper | Year |
| --- | --- |
| [Explaining temporal graph models through an explorer-navigator framework](https://openreview.net/forum?id=BR_ZhvcYbGJ) | 2023 |
| [DyExplainer: Self-explainable dynamic graph neural network with sparse attentions](https://doi.org/10.1145/3729173) | 2025 |
| [Causality-inspired spatial-temporal explanations for dynamic graph neural networks](https://openreview.net/forum?id=AJBkfwXh3u) | 2024 |

---

## Graph-Aware Evaluation and Governance

### Graph-Aware Evaluation

| Paper | Year |
| --- | --- |
| [Evaluating very long-term conversational memory of LLM agents](https://aclanthology.org/2024.acl-long.747/) | 2024 |
| [LongMemEval: Benchmarking chat assistants on long-term interactive memory](https://arxiv.org/abs/2410.10813) | 2025 |
| [MemBench: Towards more comprehensive evaluation on the memory of LLM-based agents](https://aclanthology.org/2025.findings-acl.989/) | 2025 |
| [From local to global: A graph RAG approach to query-focused summarization](https://arxiv.org/abs/2404.16130) | 2024 |
| [Graph retrieval-augmented generation: A survey](https://arxiv.org/abs/2408.08921) | 2024 |
| [Locating and editing factual associations in GPT](https://arxiv.org/abs/2202.05262) | 2022 |
| [Mass-editing memory in a transformer](https://arxiv.org/abs/2210.07229) | 2023 |
| [Fast model editing at scale](https://arxiv.org/abs/2110.11309) | 2022 |
| [Editing large language models: Problems, methods, and opportunities](https://aclanthology.org/2023.emnlp-main.632/) | 2023 |
| [ToolSandbox: A stateful, conversational, interactive evaluation benchmark for LLM tool use capabilities](https://arxiv.org/abs/2408.04682) | 2024 |
| [Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard) | 2024 |
| [AgentBench: Evaluating LLMs as agents](https://arxiv.org/abs/2308.03688) | 2024 |
| [GAIA: A benchmark for general AI assistants](https://arxiv.org/abs/2311.12983) | 2024 |
| [WebArena: A realistic web environment for building autonomous agents](https://arxiv.org/abs/2307.13854) | 2024 |
| [VisualWebArena: Evaluating multimodal agents on realistic visual web tasks](https://aclanthology.org/2024.acl-long.50/) | 2024 |
| [Mind2Web: Towards a generalist agent for the web](https://doi.org/10.52202/075280-1220) | 2023 |
| [WebVoyager: Building an end-to-end web agent with large multimodal models](https://aclanthology.org/2024.acl-long.371/) | 2024 |
| [TravelPlanner: A benchmark for real-world planning with language agents](https://arxiv.org/abs/2402.01622) | 2024 |
| [OSWorld: Benchmarking multimodal agents for open-ended tasks in real computer environments](https://doi.org/10.52202/079017-1650) | 2024 |
| [AppWorld: A controllable world of apps and people for benchmarking interactive coding agents](https://aclanthology.org/2024.acl-long.850/) | 2024 |
| [SWE-bench: Can language models resolve real-world GitHub issues?](https://arxiv.org/abs/2310.06770) | 2024 |
| [Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/) | 2024 |
| [SWE-agent: Agent-computer interfaces enable automated software engineering](https://arxiv.org/abs/2405.15793) | 2024 |

### Leakage-Free Temporal Protocols

| Paper | Year |
| --- | --- |
| [Temporal graph benchmark for machine learning on temporal graphs](https://doi.org/10.52202/075280-0099) | 2023 |
| [Towards better evaluation for dynamic link prediction](https://doi.org/10.52202/068431-2386) | 2022 |

### Privacy and Deletion in Evolving Agent Graphs

| Paper | Year |
| --- | --- |
| [Graph unlearning](https://doi.org/10.1145/3548606.3559352) | 2022 |
| [Efficient model updates for approximate unlearning of graph-structured data](https://openreview.net/forum?id=fhcu4FBLciL) | 2023 |
| [GIF: A general graph unlearning strategy via influence function](https://doi.org/10.1145/3543507.3583521) | 2023 |
| [GNNDelete: A general strategy for unlearning in graph neural networks](https://arxiv.org/abs/2302.13406) | 2023 |

### Safety, Rollback, and Audit

| Paper | Year |
| --- | --- |
| [Identifying the risks of LM agents with an LM-emulated sandbox](https://arxiv.org/abs/2309.15817) | 2024 |
| [AgentDojo: A dynamic environment to evaluate prompt injection attacks and defenses for LLM agents](https://doi.org/10.52202/079017-2636) | 2024 |
| [AgentHarm: A benchmark for measuring harmfulness of LLM agents](https://arxiv.org/abs/2410.09024) | 2025 |
| [Agent security bench (ASB): Formalizing and benchmarking attacks and defenses in LLM-based agents](https://arxiv.org/abs/2410.02644) | 2025 |
| [ToolSandbox: A stateful, conversational, interactive evaluation benchmark for LLM tool use capabilities](https://arxiv.org/abs/2408.04682) | 2024 |
| [Explainability in graph neural networks: A taxonomic survey](https://doi.org/10.1109/TPAMI.2022.3204236) | 2023 |
| [Explaining temporal graph models through an explorer-navigator framework](https://openreview.net/forum?id=BR_ZhvcYbGJ) | 2023 |
| [Causality-inspired spatial-temporal explanations for dynamic graph neural networks](https://openreview.net/forum?id=AJBkfwXh3u) | 2024 |

### Open Challenges

| Paper | Year |
| --- | --- |
| [Evaluating very long-term conversational memory of LLM agents](https://aclanthology.org/2024.acl-long.747/) | 2024 |
| [LongMemEval: Benchmarking chat assistants on long-term interactive memory](https://arxiv.org/abs/2410.10813) | 2025 |
| [MemBench: Towards more comprehensive evaluation on the memory of LLM-based agents](https://aclanthology.org/2025.findings-acl.989/) | 2025 |
| [ToolSandbox: A stateful, conversational, interactive evaluation benchmark for LLM tool use capabilities](https://arxiv.org/abs/2408.04682) | 2024 |
| [Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard) | 2024 |
| [DTGB: A comprehensive benchmark for dynamic text-attributed graphs](https://doi.org/10.52202/079017-2901) | 2024 |
| [Unlocking multi-modal potentials for link prediction on dynamic text-attributed graphs](https://arxiv.org/abs/2502.19651) | 2026 |
| [Retrieval augmented generation for dynamic graph modeling](https://doi.org/10.1145/3726302.3730030) | 2025 |
| [TG-GAN: Continuous-time temporal graph deep generative models with time-validity constraints](https://doi.org/10.1145/3442381.3449818) | 2021 |
| [A data-driven graph generative model for temporal interaction networks](https://doi.org/10.1145/3394486.3403082) | 2020 |
| [TIGGER: Scalable generative modelling for temporal interaction graphs](https://doi.org/10.1609/aaai.v36i6.20638) | 2022 |
| [Dynamic graph neural networks under spatio-temporal distribution shift](https://doi.org/10.52202/068431-0440) | 2022 |
| [Environment-Aware Dynamic Graph Learning for Out-of-Distribution Generalization](https://doi.org/10.52202/075280-2164) | 2023 |
| [Spectral invariant learning for dynamic graphs under distribution shifts](https://doi.org/10.52202/075280-0290) | 2023 |
| [Graph unlearning](https://doi.org/10.1145/3548606.3559352) | 2022 |
| [Efficient model updates for approximate unlearning of graph-structured data](https://openreview.net/forum?id=fhcu4FBLciL) | 2023 |
| [GIF: A general graph unlearning strategy via influence function](https://doi.org/10.1145/3543507.3583521) | 2023 |
| [GNNDelete: A general strategy for unlearning in graph neural networks](https://arxiv.org/abs/2302.13406) | 2023 |
| [Explaining temporal graph models through an explorer-navigator framework](https://openreview.net/forum?id=BR_ZhvcYbGJ) | 2023 |
| [Causality-inspired spatial-temporal explanations for dynamic graph neural networks](https://openreview.net/forum?id=AJBkfwXh3u) | 2024 |

---

## Benchmarks

| Paper | Year |
| --- | --- |
| [API-Bank: A comprehensive benchmark for tool-augmented LLMs](https://aclanthology.org/2023.emnlp-main.187/) | 2023 |
| [ToolSandbox: A stateful, conversational, interactive evaluation benchmark for LLM tool use capabilities](https://arxiv.org/abs/2408.04682) | 2024 |
| [Berkeley Function-Calling Leaderboard](https://gorilla.cs.berkeley.edu/leaderboard) | 2024 |
| [AgentBoard: An analytical evaluation board of multi-turn LLM agents](https://arxiv.org/abs/2401.13178) | 2024 |
| [Evaluating very long-term conversational memory of LLM agents](https://aclanthology.org/2024.acl-long.747/) | 2024 |
| [LongMemEval: Benchmarking chat assistants on long-term interactive memory](https://arxiv.org/abs/2410.10813) | 2025 |
| [MemBench: Towards more comprehensive evaluation on the memory of LLM-based agents](https://aclanthology.org/2025.findings-acl.989/) | 2025 |
| [AgentBench: Evaluating LLMs as agents](https://arxiv.org/abs/2308.03688) | 2024 |
| [GAIA: A benchmark for general AI assistants](https://arxiv.org/abs/2311.12983) | 2024 |
| [WebArena: A realistic web environment for building autonomous agents](https://arxiv.org/abs/2307.13854) | 2024 |
| [VisualWebArena: Evaluating multimodal agents on realistic visual web tasks](https://aclanthology.org/2024.acl-long.50/) | 2024 |
| [Mind2Web: Towards a generalist agent for the web](https://doi.org/10.52202/075280-1220) | 2023 |
| [TravelPlanner: A benchmark for real-world planning with language agents](https://arxiv.org/abs/2402.01622) | 2024 |
| [OSWorld: Benchmarking multimodal agents for open-ended tasks in real computer environments](https://doi.org/10.52202/079017-1650) | 2024 |
| [AppWorld: A controllable world of apps and people for benchmarking interactive coding agents](https://aclanthology.org/2024.acl-long.850/) | 2024 |
| [SWE-bench: Can language models resolve real-world GitHub issues?](https://arxiv.org/abs/2310.06770) | 2024 |
| [Introducing SWE-bench Verified](https://openai.com/index/introducing-swe-bench-verified/) | 2024 |
| [tau-bench: A benchmark for tool-agent-user interaction in real-world domains](https://arxiv.org/abs/2406.12045) | 2024 |
| [Temporal graph benchmark for machine learning on temporal graphs](https://doi.org/10.52202/075280-0099) | 2023 |
| [DTGB: A comprehensive benchmark for dynamic text-attributed graphs](https://doi.org/10.52202/079017-2901) | 2024 |
| [GDGB: A Benchmark for Generative Dynamic Text-Attributed Graph Learning](https://arxiv.org/abs/2507.03267) | 2025 |
| [Identifying the risks of LM agents with an LM-emulated sandbox](https://arxiv.org/abs/2309.15817) | 2024 |
| [AgentDojo: A dynamic environment to evaluate prompt injection attacks and defenses for LLM agents](https://doi.org/10.52202/079017-2636) | 2024 |
| [AgentHarm: A benchmark for measuring harmfulness of LLM agents](https://arxiv.org/abs/2410.09024) | 2025 |
| [Agent security bench (ASB): Formalizing and benchmarking attacks and defenses in LLM-based agents](https://arxiv.org/abs/2410.02644) | 2025 |

---

## Contributing

This collection is an ongoing effort. We welcome pull requests and issues for adding papers, fixing links, and improving categorization.

## Citation

If you find this repository useful, please consider citing the survey paper:

```bibtex
@misc{xu2026selfevolving,
  title={Self-Evolving Agents as Dynamic Graph Transformation: A Survey and Roadmap},
  author={Xu, Yuanyuan and Zhang, Wenjie and Chen, Yin and Lin, Xuemin and Zhang, Ying},
  year={2026},
  note={Manuscript}
}
```
