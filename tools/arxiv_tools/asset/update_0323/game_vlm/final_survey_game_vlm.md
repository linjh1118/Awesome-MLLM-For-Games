# Paper List of Terms(MLLM+game)
- [25/03] **How Do Multimodal Large Language Models Handle Complex Multimodal Reasoning? Placing Them in An Extensible Escape Game**  
[[Paper](http://arxiv.org/pdf/2503.10042v1)] [[Code/Page]()] [[TLDR/Notes](#how-do-multimodal-large-language-models-handle-complex-multimodal-reasoning?-placing-them-in-an-extensible-escape-game)]

- [24/12] **From Multimodal LLMs to Generalist Embodied Agents: Methods and Lessons**  
[[Paper](http://arxiv.org/pdf/2412.08442v1)] [[Code/Page]()] [[TLDR/Notes](#from-multimodal-llms-to-generalist-embodied-agents-methods-and-lessons)]

- [24/10] **Trans4D: Realistic Geometry-Aware Transition for Compositional Text-to-4D Synthesis**  
[[Paper](http://arxiv.org/pdf/2410.07155v1)] [[Code/Page](https://github.com/YangLing0818/Trans4D)] [[TLDR/Notes](#trans4d-realistic-geometry-aware-transition-for-compositional-text-to-4d-synthesis)]

- [24/10] **ING-VP: MLLMs cannot Play Easy Vision-based Games Yet**  
[[Paper](http://arxiv.org/pdf/2410.06555v1)] [[Code/Page](https://github.com/Thisisus7/ING-VP.git.)] [[TLDR/Notes](#ing-vp-mllms-cannot-play-easy-vision-based-games-yet)]

- [24/08] **Talk Less, Interact Better: Evaluating In-context Conversational Adaptation in Multimodal LLMs**  
[[Paper](http://arxiv.org/pdf/2408.01417v1)] [[Code/Page](https://github.com/lil-lab/ICCA.)] [[TLDR/Notes](#talk-less,-interact-better-evaluating-in-context-conversational-adaptation-in-multimodal-llms)]

- [24/06] **MLVU: Benchmarking Multi-task Long Video Understanding**  
[[Paper](http://arxiv.org/pdf/2406.04264v3)] [[Code/Page]()] [[TLDR/Notes](#mlvu-benchmarking-multi-task-long-video-understanding)]

- [24/04] **A Survey on Large Language Model-Based Game Agents**  
[[Paper](http://arxiv.org/pdf/2404.02039v1)] [[Code/Page](https://github.com/git-disl/awesome-LLM-game-agent-papers.)] [[TLDR/Notes](#a-survey-on-large-language-model-based-game-agents)]

- [24/02] **GenCeption: Evaluate Vision LLMs with Unlabeled Unimodal Data**  
[[Paper](http://arxiv.org/pdf/2402.14973v4)] [[Code/Page]()] [[TLDR/Notes](#genception-evaluate-vision-llms-with-unlabeled-unimodal-data)]

- [24/02] **PCA-Bench: Evaluating Multimodal Large Language Models in Perception-Cognition-Action Chain**  
[[Paper](http://arxiv.org/pdf/2402.15527v1)] [[Code/Page]()] [[TLDR/Notes](#pca-bench-evaluating-multimodal-large-language-models-in-perception-cognition-action-chain)]



# TLDR/Notes
## How Do Multimodal Large Language Models Handle Complex Multimodal Reasoning? Placing Them in An Extensible Escape Game
### Abstract
The rapid advancing of Multimodal Large Language Models (MLLMs) has spurred
interest in complex multimodal reasoning tasks in the real-world and virtual
environment, which require coordinating multiple abilities, including visual
perception, visual reasoning, spatial awareness, and target deduction. However,
existing evaluations primarily assess the final task completion, often
degrading assessments to isolated abilities such as visual grounding and visual
question answering. Less attention is given to comprehensively and
quantitatively analyzing reasoning process in multimodal environments, which is
crucial for understanding model behaviors and underlying reasoning mechanisms
beyond merely task success. To address this, we introduce MM-Escape, an
extensible benchmark for investigating multimodal reasoning, inspired by
real-world escape games. MM-Escape emphasizes intermediate model behaviors
alongside final task completion. To achieve this, we develop EscapeCraft, a
customizable and open environment that enables models to engage in free-form
exploration for assessing multimodal reasoning. Extensive experiments show that
MLLMs, regardless of scale, can successfully complete the simplest room escape
tasks, with some exhibiting human-like exploration strategies. Yet, performance
dramatically drops as task difficulty increases. Moreover, we observe that
performance bottlenecks vary across models, revealing distinct failure modes
and limitations in their multimodal reasoning abilities, such as repetitive
trajectories without adaptive exploration, getting stuck in corners due to poor
visual spatial awareness, and ineffective use of acquired props, such as the
key. We hope our work sheds light on new challenges in multimodal reasoning,
and uncovers potential improvements in MLLMs capabilities.
### 🌟 论文解读 | 多模态大型语言模型如何处理复杂的多模态推理？通过可扩展的逃脱游戏进行评估

### 📌 背景痛点/本文动机
随着多模态大型语言模型（MLLMs）的快速发展，人们对现实世界和虚拟环境中复杂的多模态推理任务产生了浓厚的兴趣。这些任务需要协调多种能力，包括视觉感知、视觉推理、空间意识和目标推理。然而，现有的评估主要关注最终的任务完成情况，往往将评估降级为孤立的能力，如视觉定位和视觉问答。较少关注在多模态环境中全面和定量地分析推理过程，这对于理解模型行为和推理机制至关重要。为了解决这个问题，本文提出了MM-Escape，一个可扩展的基准，用于研究多模态推理，灵感来自现实世界的逃脱游戏。

### 🚀 核心方法
💡 创新点1：MM-Escape基准
MM-Escape强调最终任务完成和中间模型行为。为了实现这一点，本文开发了EscapeCraft，一个可定制的开放环境，使模型能够进行自由探索，以评估多模态推理。

💡 创新点2：EscapeCraft环境
EscapeCraft是一个可定制的开放环境，允许模型进行自由探索，以评估多模态推理。它支持自定义和可扩展的场景生成，并定义了任务的推理路径。

### 📈 实验结果
实验结果表明，无论规模大小，MLLMs都能成功完成最简单的房间逃脱任务，其中一些模型表现出类似人类的探索策略。然而，随着任务难度的增加，性能急剧下降。此外，观察到性能瓶颈因模型而异，揭示了它们在多模态推理能力方面的不同失败模式和局限性，例如没有自适应探索的重复轨迹、由于视觉空间意识差而陷入角落，以及无效地使用获得的道具，如钥匙。

### 💬 可借鉴之处
本文提出的MM-Escape基准和EscapeCraft环境为评估和改进MLLMs的多模态推理能力提供了新的思路和方法。通过关注中间模型行为和推理过程，可以更全面地理解模型行为和推理机制，从而推动MLLMs在多模态推理任务上的发展。

## From Multimodal LLMs to Generalist Embodied Agents Methods and Lessons
### Abstract
We examine the capability of Multimodal Large Language Models (MLLMs) to
tackle diverse domains that extend beyond the traditional language and vision
tasks these models are typically trained on. Specifically, our focus lies in
areas such as Embodied AI, Games, UI Control, and Planning. To this end, we
introduce a process of adapting an MLLM to a Generalist Embodied Agent (GEA).
GEA is a single unified model capable of grounding itself across these varied
domains through a multi-embodiment action tokenizer. GEA is trained with
supervised learning on a large dataset of embodied experiences and with online
RL in interactive simulators. We explore the data and algorithmic choices
necessary to develop such a model. Our findings reveal the importance of
training with cross-domain data and online RL for building generalist agents.
The final GEA model achieves strong generalization performance to unseen tasks
across diverse benchmarks compared to other generalist models and
benchmark-specific approaches.
### 🌟 论文解读 | 从多模态大型语言模型到通用具身智能体：方法与经验

### 📌 背景痛点/本文动机
随着人工智能技术的不断发展，多模态大型语言模型（MLLMs）在语言和视觉理解任务中展现出强大的能力。然而，这些模型通常只在特定的训练领域表现出色，难以应对多样化的任务和场景。本文旨在探索MLLMs在更广泛领域中的应用潜力，特别是具身AI、游戏、UI控制和规划等领域。

### 🚀 核心方法
💡 创新点1：通用具身智能体（GEA）
本文提出了一种将MLLMs转化为通用具身智能体（GEA）的方法。GEA是一个统一的模型，能够通过多具身动作分词器在各个领域中进行自我定位。GEA通过在大规模具身经验数据集上进行监督学习和在线强化学习（RL）进行训练。

💡 创新点2：多具身动作分词器
为了使GEA能够控制多样化的具身形态，本文引入了一种统一的学习分词机制，用于处理所有连续和离散的动作空间。这种机制将连续动作映射到一系列新的分词，从而使得MLLMs能够理解和执行这些动作。

### 📈 实验结果
GEA在多个基准测试中展现出强大的泛化能力，与现有的通用智能体模型相比，甚至在某些特定领域中的表现也优于或接近于专业系统。例如，在CALVIN操作基准测试中，GEA在处理未见过的指令和背景时达到了90%的成功率，比类似方法高出近10%，并且与专业系统的性能相当。

### 💬 可借鉴之处
本文的研究结果表明，使用跨领域数据进行训练和在线强化学习对于构建通用智能体至关重要。此外，本文还强调了预训练MLLMs在GEA架构中的重要性，以及模型规模对性能的影响。这些发现为未来开发更强大的通用智能体提供了重要的启示和指导。

## Trans4D Realistic Geometry-Aware Transition for Compositional Text-to-4D Synthesis
### Abstract
Recent advances in diffusion models have demonstrated exceptional
capabilities in image and video generation, further improving the effectiveness
of 4D synthesis. Existing 4D generation methods can generate high-quality 4D
objects or scenes based on user-friendly conditions, benefiting the gaming and
video industries. However, these methods struggle to synthesize significant
object deformation of complex 4D transitions and interactions within scenes. To
address this challenge, we propose Trans4D, a novel text-to-4D synthesis
framework that enables realistic complex scene transitions. Specifically, we
first use multi-modal large language models (MLLMs) to produce a physic-aware
scene description for 4D scene initialization and effective transition timing
planning. Then we propose a geometry-aware 4D transition network to realize a
complex scene-level 4D transition based on the plan, which involves expressive
geometrical object deformation. Extensive experiments demonstrate that Trans4D
consistently outperforms existing state-of-the-art methods in generating 4D
scenes with accurate and high-quality transitions, validating its
effectiveness. Code: https://github.com/YangLing0818/Trans4D
### 🌟 论文解读 | Trans4D：基于文本的4D场景合成新框架

### 📌 背景痛点/本文动机
随着扩散模型在图像和视频生成方面的突破，4D合成技术也得到了快速发展。现有的4D生成方法可以基于用户友好的条件生成高质量的4D对象或场景，为游戏和视频行业带来了巨大价值。然而，这些方法在合成复杂4D过渡和场景内交互中的显著对象变形方面仍然存在挑战。

### 🚀 核心方法
💡 创新点1：物理感知的4D过渡规划
Trans4D利用多模态大型语言模型（MLLMs）生成物理感知的场景描述，用于4D场景初始化和有效的过渡时间规划。这种方法能够确保4D场景的物理合理性和空间关系的正确性。

💡 创新点2：几何感知的4D过渡网络
Trans4D提出了一个几何感知的过渡网络（TransNet），它能够根据规划动态地确定4D场景中每个点云是否应该出现或消失。这使得Trans4D能够自然地处理大规模的对象变形，例如导弹变成爆炸云。

### 📈 实验结果
Trans4D在生成具有准确和高质量过渡的4D场景方面始终优于现有的最先进方法，验证了其有效性。

### 💬 可借鉴之处
Trans4D为4D场景合成提供了一种新的思路，其物理感知的过渡规划和几何感知的过渡网络为生成具有复杂交互和显著变形的4D场景提供了有效的方法。此外，Trans4D的训练策略平衡了效率和质量，使其能够在有限的计算资源下生成高质量的4D场景。

## ING-VP MLLMs cannot Play Easy Vision-based Games Yet
### Abstract
As multimodal large language models (MLLMs) continue to demonstrate
increasingly competitive performance across a broad spectrum of tasks, more
intricate and comprehensive benchmarks have been developed to assess these
cutting-edge models. These benchmarks introduce new challenges to core
capabilities such as perception, reasoning, and planning. However, existing
multimodal benchmarks fall short in providing a focused evaluation of
multi-step planning based on spatial relationships in images. To bridge this
gap, we present ING-VP, the first INteractive Game-based Vision Planning
benchmark, specifically designed to evaluate the spatial imagination and
multi-step reasoning abilities of MLLMs. ING-VP features 6 distinct games,
encompassing 300 levels, each with 6 unique configurations. A single model
engages in over 60,000 rounds of interaction. The benchmark framework allows
for multiple comparison settings, including image-text vs. text-only inputs,
single-step vs. multi-step reasoning, and with-history vs. without-history
conditions, offering valuable insights into the model's capabilities. We
evaluated numerous state-of-the-art MLLMs, with the highest-performing model,
Claude-3.5 Sonnet, achieving an average accuracy of only 3.37%, far below the
anticipated standard. This work aims to provide a specialized evaluation
framework to drive advancements in MLLMs' capacity for complex spatial
reasoning and planning. The code is publicly available at
https://github.com/Thisisus7/ING-VP.git.
### 🌟 论文解读 | ING-VP：大型多模态语言模型在视觉规划任务上的挑战

### 📌 背景痛点/本文动机
随着多模态大型语言模型（MLLMs）在各类任务中展现出越来越强的竞争力，评估这些模型的复杂性和全面性的基准测试也变得越来越重要。然而，现有的多模态基准测试在评估基于图像空间关系的多步规划能力方面存在不足。为了填补这一空白，本文提出了ING-VP，一个基于交互式游戏的视觉规划基准测试，旨在评估MLLMs的空间想象力和多步推理能力。

### 🚀 核心方法
💡 创新点1：ING-VP基准测试
ING-VP基准测试包含6个不同的游戏，涵盖300个关卡，每个关卡有6种独特的配置。单个模型参与超过60,000轮交互。基准测试框架允许多种比较设置，包括图像-文本与仅文本输入、单步与多步推理以及带历史与不带历史条件，为模型的能力提供有价值的见解。

💡 创新点2：评估MLLMs的能力
本文评估了众多最先进的MLLMs，发现即使是表现最好的模型Claude-3.5 Sonnet，其平均准确率也只有3.37%，远低于预期标准。这表明当前的MLLMs在空间想象力和多步规划能力方面存在显著不足。

### 📈 实验结果
实验结果表明，即使是表现最好的模型Claude-3.5 Sonnet，在ING-VP基准测试上的平均准确率也只有3.37%，远低于人类在这些简单任务上的表现。这表明当前的MLLMs在空间想象力和多步规划能力方面存在显著不足。

### 💬 可借鉴之处
ING-VP基准测试为评估MLLMs的空间想象力和多步推理能力提供了一个专门的评估框架，有助于推动MLLMs在复杂空间推理和规划能力方面的进步。此外，ING-VP基准测试的结果也为MLLMs的未来设计和训练策略提供了有价值的见解。

## Talk Less, Interact Better Evaluating In-context Conversational Adaptation in Multimodal LLMs
### Abstract
Humans spontaneously use increasingly efficient language as interactions
progress, by adapting and forming ad-hoc conventions. This phenomenon has been
studied extensively using reference games, showing properties of human language
that go beyond relaying intents. It remains unexplored whether multimodal large
language models (MLLMs) similarly increase communication efficiency during
interactions, and what mechanisms they may adopt for this purpose. We introduce
ICCA, an automated framework to evaluate such conversational adaptation as an
in-context behavior in MLLMs. We evaluate several state-of-the-art MLLMs, and
observe that while they may understand the increasingly efficient language of
their interlocutor, they do not spontaneously make their own language more
efficient over time. This latter ability can only be elicited in some models
(e.g., GPT-4) with heavy-handed prompting. This shows that this property of
linguistic interaction does not arise from current training regimes, even
though it is a common hallmark of human language. ICCA is available at
https://github.com/lil-lab/ICCA.
### 🌟 论文解读 | 多模态大语言模型中的对话适应性评估

### 📌 背景痛点/本文动机
人类在交流过程中会自发地使用越来越高效的语言，通过适应和形成临时的约定来提高沟通效率。这种现象在参考游戏中得到了广泛的研究，揭示了人类语言的特性，超越了仅仅传达意图的功能。然而，目前尚不清楚多模态大语言模型（MLLMs）是否在交互过程中同样能够提高沟通效率，以及它们可能采用哪些机制来实现这一目标。

### 🚀 核心方法
本文提出了ICCA（In-context Conversational Adaptation），一个自动化的框架，用于评估MLLMs在上下文中的对话适应性。ICCA使用人类-人类参考游戏交互的语料库，允许完全自动化的评估，无需进一步的人类交互，使其易于部署以分析新模型。该框架模拟了模型与人类交互的场景，通过比较模型行为的变化来评估其对话适应性。

### 📈 实验结果
本文评估了五个具有代表性的MLLMs：IDEFICS、LLaVa-1.5、GPT4-vision、Gemini 1.0 Pro Vision和Claude 3 opus。研究发现，所有模型都难以自发地引入约定并作为说话者进行适应。通过为每个模型设计特定的指令，可以部分解决这一问题。最强的模型（GPT4、Gemini和Claude）可以逐渐使用更短的消息（获得词汇效率），但仍然难以实现收敛或稳定性，这阻碍了真正高效沟通的出现。当作为听众时，GPT4显示出接近人类的适应趋势，随着交互的进行，其准确性不断提高，而其他模型则表现出较少的这种行为或仅在简化的设置下表现出这种行为。

### 💬 可借鉴之处
本文的研究结果表明，尽管当前的MLLMs可能被动地理解其对话者的不断发展变化的语言，但它们适应自身语言以提高沟通效率的能力并没有自然地从它们的训练或指令调整中产生。这为未来的研究指明了重要的方向，包括提高模型的自发语言效率、保持语言一致性、避免过度重复倾向以及处理单个查询中的更多图像。

## MLVU Benchmarking Multi-task Long Video Understanding
### Abstract
The evaluation of Long Video Understanding (LVU) performance poses an
important but challenging research problem. Despite previous efforts, the
existing video understanding benchmarks are severely constrained by several
issues, especially the insufficient lengths of videos, a lack of diversity in
video types and evaluation tasks, and the inappropriateness for evaluating LVU
performances. To address the above problems, we propose a new benchmark called
MLVU (Multi-task Long Video Understanding Benchmark) for the comprehensive and
in-depth evaluation of LVU. MLVU presents the following critical values:
\textit{1)} The substantial and flexible extension of video lengths, which
enables the benchmark to evaluate LVU performance across a wide range of
durations. \textit{2)} The inclusion of various video genres, e.g., movies,
surveillance footage, egocentric videos, cartoons, game videos, etc., which
reflects the models' LVU performances in different scenarios. \textit{3)} The
development of diversified evaluation tasks, which enables a comprehensive
examination of MLLMs' key abilities in long-video understanding. The empirical
study with 23 latest MLLMs reveals significant room for improvement in today's
technique, as all existing methods struggle with most of the evaluation tasks
and exhibit severe performance degradation when handling longer videos.
Additionally, it suggests that factors such as context length,
image-understanding ability, and the choice of LLM backbone can play critical
roles in future advancements. We anticipate that MLVU will advance the research
of long video understanding by providing a comprehensive and in-depth analysis
of MLLMs.
### 🌟 论文解读 | MLVU：多任务长视频理解基准

### 📌 背景痛点/本文动机
随着大型语言模型（LLMs）在多模态能力上的扩展，多模态大型语言模型（MLLMs）在处理文本、图像和视频等多模态信息方面取得了显著进展。然而，现有的视频理解基准主要针对短视频，无法有效评估MLLMs在处理长视频方面的能力。此外，现有基准在视频类型和评估任务的多样性方面存在不足，且评估任务的设计往往无法充分利用长视频中的复杂信息。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1：视频长度的大幅扩展
MLVU基准包含时长从3分钟到2小时不等的多样化长视频，平均视频长度约为15分钟，远超现有基准。此外，每个视频被进一步分割成多个片段，以便针对不同片段创建评估任务，从而灵活评估MLLMs在不同视频长度下的表现。

💡 创新点2：多样化的视频类型
MLVU基准涵盖了多种视频类型，包括电影、生活记录、第一人称视角视频、体育、教程、监控录像等真实世界视频，以及动画系列和游戏视频等模拟视频。这种多样性使得MLLMs在不同应用场景下的表现可以得到全面评估。

💡 创新点3：多样化的评估任务
MLVU基准包含9个不同的评估任务，旨在全面评估MLLMs在长视频理解方面的关键能力。这些任务包括多项选择题和开放式生成任务，以及需要利用整个视频的全局信息或特定片段的局部信息的任务。此外，所有涉及局部信息的任务都带有明确的上下文标注，要求MLLMs能够准确定位或推断长视频中的相关片段。

### 📈 实验结果
通过对23个最新的MLLMs进行实证研究，MLVU基准揭示了现有技术在长视频理解方面仍有很大的改进空间。所有现有方法在大多数评估任务上都表现不佳，并且在处理更长的视频时性能严重下降。此外，研究结果表明，上下文长度、图像理解能力和LLM骨干的选择等因素对未来长视频理解技术的进步起着关键作用。

### 💬 可借鉴之处
MLVU基准为长视频理解研究提供了一个全面而深入的评估框架，有助于研究人员了解MLLMs在长视频理解方面的优势和不足，并为未来的技术改进提供方向。此外，MLVU基准的设计理念和方法可以为其他多模态任务评估基准的开发提供参考。

## A Survey on Large Language Model-Based Game Agents
### Abstract
The development of game agents holds a critical role in advancing towards
Artificial General Intelligence (AGI). The progress of LLMs and their
multimodal counterparts (MLLMs) offers an unprecedented opportunity to evolve
and empower game agents with human-like decision-making capabilities in complex
computer game environments. This paper provides a comprehensive overview of
LLM-based game agents from a holistic viewpoint. First, we introduce the
conceptual architecture of LLM-based game agents, centered around six essential
functional components: perception, memory, thinking, role-playing, action, and
learning. Second, we survey existing representative LLM-based game agents
documented in the literature with respect to methodologies and adaptation
agility across six genres of games, including adventure, communication,
competition, cooperation, simulation, and crafting & exploration games.
Finally, we present an outlook of future research and development directions in
this burgeoning field. A curated list of relevant papers is maintained and made
accessible at: https://github.com/git-disl/awesome-LLM-game-agent-papers.
### 🌟 论文解读 | 基于大型语言模型的智能游戏代理：迈向通用人工智能的探索

### 📌 背景痛点/本文动机
随着大型语言模型（LLMs）和其多模态版本（MLLMs）的快速发展，它们在自然语言理解和生成式人工智能方面取得了突破性进展。然而，现有的游戏代理大多基于强化学习（RL），在复杂游戏环境中缺乏类似人类的决策能力。本文旨在探讨如何利用LLMs构建具有人类决策能力的游戏代理，以推动通用人工智能（AGI）的发展。

### 🚀 核心方法
本文提出了一个统一的框架，用于构建基于LLMs的游戏代理（LLMGAs），并详细介绍了其六个核心功能组件：

1. **感知**：LLMGAs通过多种方式感知游戏环境，包括文本、视觉、声音等，以获取必要的游戏状态信息。
2. **记忆**：LLMGAs利用记忆系统存储过去的观察、思考和行动，以便在未来的决策中检索和利用。
3. **思考**：LLMGAs通过推理和规划进行决策，推理包括演绎、归纳和假设推理，规划则将复杂任务分解为可执行的子任务。
4. **角色扮演**：LLMGAs能够模拟游戏中的不同角色，生成符合角色特征和目标的对话和行为。
5. **行动**：LLMGAs将生成的文本决策转换为可执行的行动，以与游戏环境进行交互。
6. **学习**：LLMGAs通过积累游戏经验和环境反馈，不断改进其认知和游戏能力。

### 📈 实验结果
本文对现有文献进行了综述，涵盖了六种类型的游戏，包括冒险、沟通、竞争、合作、模拟和制作与探索游戏。对于每种类型的游戏，本文分析了技术挑战、支持的游戏环境和常用的优化策略。

### 💬 可借鉴之处
本文提出的LLMGAs框架为构建具有人类决策能力的游戏代理提供了重要的参考。此外，本文还指出了未来研究的三个方向：

1. **环境中的LLMs接地**：通过多模态感知、外部可用性函数、环境反馈和经验学习，使LLMs更好地适应现实环境。
2. **通过游戏玩知识发现**：利用游戏机制中的复杂知识，设计能够从观察和经验中提取底层知识的LLM代理。
3. **代理社会模拟**：在现实游戏环境中开发更好的认知架构，模拟更复杂的社交互动和合作，以更好地理解和表示复杂的人类交互。

### 📚 参考资料
[1] The Embodied Cognition Hypothesis
[2] ChatGPT
[3] GPT-4V
[4] Gemini
[5] LLM-based agent (LLMA)
[6] Pre-existing knowledge
[7] Real-world learning
[8] Real-world experience
[9] Chess
[10] Poker
[11] Atari games
[12] StarCraft II
[13] Minecraft
[14] DOTA II
[15] Reinforcement Learning (RL)
[16] Behavior-level policy learning
[17] Cognitive abilities
[18] Reasoning
[19] LLMs survey papers
[20] LLMAs survey papers
[21] LLMGAs survey papers
[22] Game development survey papers
[23] Game agents survey papers
[24] LLMGAs taxonomy
[25] Game categories
[26] Technical challenges
[27] Game environments
[28] Optimization strategies
[29] Future research directions
[30] LLMGAs in games
[31] Perception module
[32] Memory module
[33] Role-playing module
[34] Thinking module
[35] Action module
[36] Learning module
[37] Adventure games
[38] Communication games
[39] Competition games
[40] Cooperation games
[41] Simulation games
[42] Crafting & exploration games
[43] Evaluation metrics
[44] Grounding LLMs in environments
[45] Knowledge discovery through game-playing
[46] Agent society simulation

## GenCeption Evaluate Vision LLMs with Unlabeled Unimodal Data
### Abstract
Multimodal Large Language Models (MLLMs) are typically assessed using
expensive annotated multimodal benchmarks, which often lag behind the rapidly
evolving demands of MLLM evaluation. This paper outlines and validates
GenCeption, a novel, annotation-free evaluation method that requires only
unimodal data to measure inter-modality semantic coherence and inversely
assesses MLLMs' tendency to hallucinate. This approach eliminates the need for
costly data annotation, minimizes the risk of training data contamination, is
expected to result in slower benchmark saturation, and avoids the illusion of
emerging abilities. Inspired by the DrawCeption game, GenCeption begins with a
non-textual sample and proceeds through iterative description and generation
steps. The semantic drift across iterations is quantified using the GC@T
metric. While GenCeption is principally applicable to MLLMs across various
modalities, this paper focuses on its implementation and validation for Vision
LLMs (VLLMs). Based on the GenCeption method, we establish the MMECeption
benchmark for evaluating VLLMs, and compare the performance of several popular
VLLMs and human annotators. Our empirical results validate GenCeption's
effectiveness, demonstrating strong correlations with established VLLM
benchmarks. VLLMs still significantly lag behind human performance and struggle
especially with text-intensive tasks.
### 🌟 论文解读 | GenCeption：一种无需标注的多模态语言模型评估方法

### 📌 背景痛点/本文动机
随着多模态大型语言模型（MLLMs）的快速发展，现有的评估方法主要依赖于昂贵的多模态标注数据集，这些数据集往往滞后于MLLMs的快速演进需求。此外，现有的评估方法还存在以下挑战：
1. 依赖高质量标注的多模态数据集，成本高昂且难以捕捉MLLMs的动态发展。
2. 使用离散指标（如准确率）评估，可能导致对模型能力的误判。
3. 评估分数可能无法反映真实世界任务上的表现，因为训练数据可能受到基准数据集的污染。
4. 评估过程中，一个模态的内容可能并不需要回答基准问题，因为答案可以从问题或MLLMs的预训练知识中推断出来。

### 🚀 核心方法
本文提出了GenCeption，一种新颖的无标注评估方法，它只需要单模态数据来衡量跨模态语义一致性和评估MLLMs的幻觉倾向。GenCeption的主要特点包括：
1. **无标注评估**：无需昂贵的数据标注，只需使用单模态数据集即可进行评估。
2. **跨模态语义一致性**：通过迭代生成和描述非文本样本，评估MLLMs在不同模态之间保持语义一致性的能力。
3. **幻觉倾向评估**：通过衡量语义漂移，间接评估MLLMs的幻觉倾向。
4. **连续指标**：使用GC@T指标，提供更细粒度的评估，避免对模型能力的误判。

### 📈 实验结果
本文在MMECeption基准上评估了七种流行的视觉语言模型（VLLMs），并与人类标注者的表现进行了比较。结果表明，GenCeption与现有VLLM基准具有强相关性，能够有效评估VLLMs的语义一致性和幻觉倾向。此外，VLLMs在文本密集型任务上的表现仍然显著落后于人类。

### 💬 可借鉴之处
GenCeption提供了一种新颖的无标注评估方法，可以有效地评估MLLMs的跨模态语义一致性和幻觉倾向。该方法具有以下优势：
1. **成本效益**：无需昂贵的数据标注，降低了评估成本。
2. **动态适应**：能够适应MLLMs的快速演进需求。
3. **全面评估**：能够评估MLLMs的多种能力，包括描述、生成和推理等。
4. **可扩展性**：可以扩展到其他非文本模态，如音频、视频和图形等。

### 🌟 总结
GenCeption为MLLMs的评估提供了一种新颖且有效的无标注方法，能够有效地评估MLLMs的跨模态语义一致性和幻觉倾向。该方法具有成本效益、动态适应、全面评估和可扩展性等优势，为MLLMs的评估提供了新的思路和方法。

## PCA-Bench Evaluating Multimodal Large Language Models in Perception-Cognition-Action Chain
### Abstract
We present PCA-Bench, a multimodal decision-making benchmark for evaluating
the integrated capabilities of Multimodal Large Language Models (MLLMs).
Departing from previous benchmarks focusing on simplistic tasks and individual
model capability, PCA-Bench introduces three complex scenarios: autonomous
driving, domestic robotics, and open-world games. Given task instructions and
diverse contexts, the model is required to seamlessly integrate multiple
capabilities of Perception, Cognition, and Action in a reasoning chain to make
accurate decisions. Moreover, PCA-Bench features error localization
capabilities, scrutinizing model inaccuracies in areas such as perception,
knowledge, or reasoning. This enhances the reliability of deploying MLLMs. To
balance accuracy and efficiency in evaluation, we propose PCA-Eval, an
automatic evaluation protocol, and assess 10 prevalent MLLMs. The results
reveal significant performance disparities between open-source models and
powerful proprietary models like GPT-4 Vision. To address this, we introduce
Embodied-Instruction-Evolution (EIE), an automatic framework for synthesizing
instruction tuning examples in multimodal embodied environments. EIE generates
7,510 training examples in PCA-Bench and enhances the performance of
open-source MLLMs, occasionally surpassing GPT-4 Vision (+3\% in decision
accuracy), thereby validating the effectiveness of EIE. Our findings suggest
that robust MLLMs like GPT4-Vision show promise for decision-making in embodied
agents, opening new avenues for MLLM research.
### 🌟 论文解读 | PCA-Bench：评估多模态大语言模型在感知-认知-行动链中的决策能力

### 📌 背景痛点/本文动机
随着多模态大语言模型（MLLMs）在处理复杂任务方面的能力日益增强，现有的评估基准往往只关注单个模型能力的评估，而忽略了模型在感知、认知和行动方面的综合能力。此外，现有的基准缺乏对模型错误进行定位的能力，这使得难以确定模型在哪些方面需要改进。

### 🚀 核心方法
💡 创新点1：PCA-Bench
本文提出了PCA-Bench，这是一个用于评估MLLMs在感知-认知-行动链中决策能力的多模态决策基准。PCA-Bench引入了三个复杂的场景：自动驾驶、家庭机器人和开放世界游戏。在这些场景中，模型需要根据任务指令和不同的上下文，无缝地整合感知、认知和行动的能力，以做出准确的决策。

💡 创新点2：PCA-Eval
为了平衡评估的准确性和效率，本文提出了PCA-Eval，这是一个自动评估协议。PCA-Eval利用LLMs强大的语义解析能力，根据数据注释中的锚点信息，自动进行错误定位。实验结果表明，PCA-Eval与人类评估结果具有高度的一致性，平均Kappa系数达到0.8+。

💡 创新点3：Embodied-Instruction-Evolution (EIE)
为了解决PCA-Bench数据集标注工作量大的问题，本文提出了Embodied-Instruction-Evolution (EIE)框架。EIE利用LLMs自动合成多模态具身环境中的指令调整示例，从而减少了人工劳动，并提高了PCA-Bench的多样性和可扩展性。

### 📈 实验结果
实验结果表明，GPT-4 Vision在感知、认知和行动方面都表现出色，超过了现有的开源MLLMs。EIE方法能够显著提高开源MLLMs的性能，在某些指标上甚至超过了GPT-4 Vision。PCA-Eval能够有效地定位模型错误，从而提高了模型评估的可靠性。

### 💬 可借鉴之处
本文提出的PCA-Bench和PCA-Eval为评估MLLMs的决策能力提供了一个新的基准和评估工具。EIE框架为自动合成多模态具身环境中的指令调整示例提供了一种有效的方法。本文的研究结果表明，强大的MLLMs在具身智能体中的决策能力具有很大的潜力，为MLLMs的研究开辟了新的方向。

