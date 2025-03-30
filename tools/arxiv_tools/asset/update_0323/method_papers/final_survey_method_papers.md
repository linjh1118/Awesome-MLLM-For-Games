# Paper List of method_papers.md
- [25/03] **JARVIS-VLA: Post-Training Large-Scale Vision Language Models to Play Visual Games with Keyboards and Mouse**  
[[Paper](http://arxiv.org/pdf/2503.16365v1)] [[Code/Page](https://craftjarvis.github.io/JarvisVLA)] [[TLDR/Notes](#jarvis-vla--post-training-large-scale-vision-language-models-to-play-visual-games-with-keyboards-and-mouse)]

- [25/02] **Optimus-2: Multimodal Minecraft Agent with Goal-Observation-Action Conditioned Policy**  
[[Paper](http://arxiv.org/pdf/2502.19902v2)] [[Code/Page](https://cybertronagent.github.io/Optimus-2.github.io)] [[TLDR/Notes](#optimus-2--multimodal-minecraft-agent-with-goal-observation-action-conditioned-policy)]

- [24/12] **MineStudio: A Streamlined Package for Minecraft AI Agent Development**  
[[Paper](http://arxiv.org/pdf/2412.18293v2)] [[Code/Page](https://github.com/CraftJarvis/MineStudio)] [[TLDR/Notes](#minestudio--a-streamlined-package-for-minecraft-ai-agent-development)]

- [23/10] **GROOT: Learning to Follow Instructions by Watching Gameplay Videos**  
[[Paper](http://arxiv.org/pdf/2310.08235v2)] [[Code/Page](https://craftjarvis-groot.github.io)] [[TLDR/Notes](#groot--learning-to-follow-instructions-by-watching-gameplay-videos)]

- [25/03] **ROCKET-2: Steering Visuomotor Policy via Cross-View Goal Alignment**  
[[Paper](http://arxiv.org/pdf/2503.02505v1)] [[Code/Page]()] [[TLDR/Notes](#rocket-2--steering-visuomotor-policy-via-cross-view-goal-alignment)]

- [24/10] **Open-World Reinforcement Learning over Long Short-Term Imagination**  
[[Paper](http://arxiv.org/pdf/2410.03618v2)] [[Code/Page]()] [[TLDR/Notes](#open-world-reinforcement-learning-over-long-short-term-imagination)]

- [18/06] **VirtualHome: Simulating Household Activities via Programs**  
[[Paper](http://arxiv.org/pdf/1806.07011v1)] [[Code/Page]()] [[TLDR/Notes](#virtualhome--simulating-household-activities-via-programs)]

- [24/03] **EnvGen: Generating and Adapting Environments via LLMs for Training Embodied Agents**  
[[Paper](http://arxiv.org/pdf/2403.12014v2)] [[Code/Page]()] [[TLDR/Notes](#envgen--generating-and-adapting-environments-via-llms-for-training-embodied-agents)]

- [22/01] **Multi-Stage Episodic Control for Strategic Exploration in Text Games**  
[[Paper](http://arxiv.org/pdf/2201.01251v3)] [[Code/Page]()] [[TLDR/Notes](#multi-stage-episodic-control-for-strategic-exploration-in-text-games)]

- [21/07] **Pre-trained Language Models as Prior Knowledge for Playing Text-based Games**  
[[Paper](http://arxiv.org/pdf/2107.08408v2)] [[Code/Page]()] [[TLDR/Notes](#pre-trained-language-models-as-prior-knowledge-for-playing-text-based-games)]

- [23/02] **Guiding Pretraining in Reinforcement Learning with Large Language Models**  
[[Paper](http://arxiv.org/pdf/2302.06692v2)] [[Code/Page](https://github.com/yuqingd/ellm)] [[TLDR/Notes](#guiding-pretraining-in-reinforcement-learning-with-large-language-models)]

- [24/01] **PokerGPT: An End-to-End Lightweight Solver for Multi-Player Texas Hold'em via Large Language Model**  
[[Paper](http://arxiv.org/pdf/2401.06781v1)] [[Code/Page]()] [[TLDR/Notes](#pokergpt--an-end-to-end-lightweight-solver-for-multi-player-texas-hold-em-via-large-language-model)]

- [24/02] **Enhance Reasoning for Large Language Models in the Game Werewolf**  
[[Paper](http://arxiv.org/pdf/2402.02330v2)] [[Code/Page]()] [[TLDR/Notes](#enhance-reasoning-for-large-language-models-in-the-game-werewolf)]

- [23/11] **ADaPT: As-Needed Decomposition and Planning with Language Models**  
[[Paper](http://arxiv.org/pdf/2311.05772v2)] [[Code/Page]()] [[TLDR/Notes](#adapt--as-needed-decomposition-and-planning-with-language-models)]

- [23/12] **Cooperation on the Fly: Exploring Language Agents for Ad Hoc Teamwork in the Avalon Game**  
[[Paper](http://arxiv.org/pdf/2312.17515v1)] [[Code/Page]()] [[TLDR/Notes](#cooperation-on-the-fly--exploring-language-agents-for-ad-hoc-teamwork-in-the-avalon-game)]

- [18/06] **Counting to Explore and Generalize in Text-based Games**  
[[Paper](http://arxiv.org/pdf/1806.11525v2)] [[Code/Page]()] [[TLDR/Notes](#counting-to-explore-and-generalize-in-text-based-games)]

- [23/09] **Suspicion-Agent: Playing Imperfect Information Games with Theory of Mind Aware GPT-4**  
[[Paper](http://arxiv.org/pdf/2309.17277v3)] [[Code/Page]()] [[TLDR/Notes](#suspicion-agent--playing-imperfect-information-games-with-theory-of-mind-aware-gpt-4)]

- [24/07] **Enhancing Agent Learning through World Dynamics Modeling**  
[[Paper](http://arxiv.org/pdf/2407.17695v2)] [[Code/Page]()] [[TLDR/Notes](#enhancing-agent-learning-through-world-dynamics-modeling)]



# TLDR/Notes
## jarvis-vla--post-training-large-scale-vision-language-models-to-play-visual-games-with-keyboards-and-mouse
### Abstract
Recently, action-based decision-making in open-world environments has gained
significant attention. Visual Language Action (VLA) models, pretrained on
large-scale web datasets, have shown promise in decision-making tasks. However,
previous work has primarily focused on action post-training, often neglecting
enhancements to the foundational model itself. In response, we introduce a
novel approach, Act from Visual Language Post-Training, which refines Visual
Language Models (VLMs) through visual and linguistic guidance in a
self-supervised manner. This enhancement improves the models' capabilities in
world knowledge, visual recognition, and spatial grounding in open-world
environments. Following the above post-training paradigms, we obtain the first
VLA models in Minecraft that can follow human instructions on over 1k different
atomic tasks, including crafting, smelting, cooking, mining, and killing. Our
experiments demonstrate that post-training on non-trajectory tasks leads to a
significant 40% improvement over the best agent baseline on a diverse set of
atomic tasks. Furthermore, we demonstrate that our approach surpasses
traditional imitation learning-based policies in Minecraft, achieving
state-of-the-art performance. We have open-sourced the code, models, and
datasets to foster further research. The project page can be found in
https://craftjarvis.github.io/JarvisVLA.
### 🌟 论文解读 | JARVIS-VLA：通过视觉语言后训练提升大型视觉语言模型在开放世界环境中的决策能力

### 📌 背景痛点/本文动机
近年来，基于动作的决策在开放世界环境中受到了广泛关注。视觉语言动作（VLA）模型在大型网络数据集上进行了预训练，并在决策任务中显示出潜力。然而，先前的工作主要集中在动作后训练上，往往忽略了基础模型本身的改进。为了解决这个问题，本文提出了一种新的方法，即“从视觉语言后训练中学习动作”，通过视觉和语言指导以自监督的方式对视觉语言模型（VLM）进行微调。这种增强提高了模型在开放世界环境中的世界知识、视觉识别和空间定位能力。

### 🚀 核心方法
💡 创新点1：视觉语言后训练（ActVLP）
本文提出了一种新的训练范式——视觉语言后训练（ActVLP），将视觉语言任务整合到VLA模型的后训练阶段。ActVLP包括三个阶段：
1. 对语言模型进行后训练，使用与下游环境相关的世界知识文本数据集进行微调。
2. 对视觉编码器和语言模型进行后训练，使用多模态视觉语言对齐和空间定位数据集进行微调。
3. 在轨迹数据集上进行模仿学习，要求模型模仿专家动作。

💡 创新点2：JARVIS-VLA模型结构
JARVIS-VLA采用了一种类似于Llava的架构，但进行了轻微的修改。它包括视觉编码器、图像投影模块、语言模型Transformer和动作解码器等关键组件。此外，JARVIS-VLA还采用了非马尔可夫架构，通过在提示中包含观察图像的历史来确保模型保留时间上下文。

### 📈 实验结果
实验结果表明，JARVIS-VLA在Minecraft游戏中表现出色，能够遵循人类指令完成超过1k个不同的原子任务，包括制作、熔炼、烹饪、采矿和杀戮等。与最佳代理基线相比，在非轨迹任务上进行后训练导致在一系列原子任务上显著提高了40%。此外，JARVIS-VLA在Minecraft中超越了传统的基于模仿学习的策略，实现了最先进的性能。

### 💬 可借鉴之处
本文提出的ActVLP训练范式和JARVIS-VLA模型结构为视觉语言动作模型在开放世界环境中的决策能力提升提供了新的思路和方法。此外，本文还探讨了VLA模型的缩放规律，为未来研究提供了重要的参考。

## optimus-2--multimodal-minecraft-agent-with-goal-observation-action-conditioned-policy
### Abstract
Building an agent that can mimic human behavior patterns to accomplish
various open-world tasks is a long-term goal. To enable agents to effectively
learn behavioral patterns across diverse tasks, a key challenge lies in
modeling the intricate relationships among observations, actions, and language.
To this end, we propose Optimus-2, a novel Minecraft agent that incorporates a
Multimodal Large Language Model (MLLM) for high-level planning, alongside a
Goal-Observation-Action Conditioned Policy (GOAP) for low-level control. GOAP
contains (1) an Action-guided Behavior Encoder that models causal relationships
between observations and actions at each timestep, then dynamically interacts
with the historical observation-action sequence, consolidating it into
fixed-length behavior tokens, and (2) an MLLM that aligns behavior tokens with
open-ended language instructions to predict actions auto-regressively.
Moreover, we introduce a high-quality Minecraft Goal-Observation-Action (MGOA)}
dataset, which contains 25,000 videos across 8 atomic tasks, providing about
30M goal-observation-action pairs. The automated construction method, along
with the MGOA dataset, can contribute to the community's efforts to train
Minecraft agents. Extensive experimental results demonstrate that Optimus-2
exhibits superior performance across atomic tasks, long-horizon tasks, and
open-ended instruction tasks in Minecraft. Please see the project page at
https://cybertronagent.github.io/Optimus-2.github.io/.
### 🌟 论文解读 | Optimus-2：基于多模态大语言模型的Minecraft智能体

### 📌 背景痛点/本文动机
在开放世界环境中，构建能够模仿人类行为模式并完成各种任务的智能体一直是人工智能领域的长期目标。然而，要使智能体有效地学习跨任务的行为模式，关键挑战在于建模观察、动作和语言之间的复杂关系。现有的智能体在处理开放世界环境中的多样化任务时，通常采用任务规划器和目标条件策略的框架。尽管现有的智能体在利用多模态大语言模型（MLLM）作为规划器方面取得了进展，但目标条件策略的性能瓶颈仍然存在。现有的策略通常忽略了观察和动作之间的关系，并且难以建模开放式的子目标和观察-动作序列之间的关系。

### 🚀 核心方法
为了解决上述挑战，本文提出了Optimus-2，一个新颖的Minecraft智能体，它结合了MLLM进行高级规划，并采用目标-观察-动作条件策略（GOAP）进行低级控制。GOAP包含两个关键组件：

💡 创新点1：动作引导的行为编码器
动作引导的行为编码器用于建模观察-动作序列。它首先使用因果感知器将动作嵌入到观察特征中，利用任务相关的动作信息作为指导来调整观察特征，从而为动作预测提供细粒度的观察-动作信息。此外，为了在不超出输入长度限制的情况下对长期观察-动作序列进行建模，引入了历史聚合器，将当前观察-动作信息与历史序列动态地整合成固定长度的行为标记。行为标记可以以固定且适当的长度捕获观察-动作序列的长期依赖关系，使智能体能够预测与观察-动作序列逻辑一致的动作，而不是仅基于当前观察进行孤立的动作预测。

💡 创新点2：多模态大语言模型
为了明确编码子目标的语义，引入了MLLM作为GOAP的骨干网络。它将子目标与行为标记对齐，以自回归方式预测后续动作。利用MLLM的语言理解和多模态感知能力，它可以更好地整合开放式子目标和观察-动作序列的特征，从而增强策略的动作预测能力。

### 📈 实验结果
在Minecraft的开放世界环境中进行了广泛的评估，实验结果表明Optimus-2在原子任务、长期任务和开放式指令任务中表现出优异的性能。与之前的SOTA相比，Optimus-2在原子任务、长期任务和开放式子目标任务上分别实现了平均27%、10%和18%的提升。

### 💬 可借鉴之处
本文提出的Optimus-2智能体及其GOAP策略为开放世界环境中的智能体设计提供了新的思路。动作引导的行为编码器和MLLM的引入有效地解决了观察、动作和语言之间的复杂关系建模问题，使得智能体能够更好地理解和执行开放式指令。此外，本文提出的MGOA数据集为训练Minecraft智能体提供了高质量的数据资源，有助于推动相关研究的发展。

## minestudio--a-streamlined-package-for-minecraft-ai-agent-development
### Abstract
Minecraft has emerged as a valuable testbed for embodied intelligence and
sequential decision-making research, yet the development and validation of
novel agents remains hindered by significant engineering challenges. This paper
presents MineStudio, an open-source software package designed to streamline
embodied policy development in Minecraft. MineStudio represents the first
comprehensive integration of seven critical engineering components: simulator,
data, model, offline pretraining, online finetuning, inference, and benchmark,
thereby allowing users to concentrate their efforts on algorithm innovation. We
provide a user-friendly API design accompanied by comprehensive documentation
and tutorials. The complete codebase is publicly available at
https://github.com/CraftJarvis/MineStudio.
### 🌟 论文解读 | “MineStudio：打造Minecraft AI智能体开发的利器”

### 📌 背景痛点/本文动机
Minecraft因其开放世界和丰富的游戏性，已成为研究具身智能和顺序决策的重要平台。然而，新型智能体的开发和验证面临着巨大的工程挑战。本文提出了MineStudio，一个开源软件包，旨在简化Minecraft中具身策略的开发流程。MineStudio集成了七个关键的工程组件：模拟器、数据、模型、离线预训练、在线微调、推理和基准测试，使用户能够集中精力进行算法创新。

### 🚀 核心方法（介绍本文的几个创新点）
💡 创新点1
MineStudio提供了一个钩子式的Minecraft包装器，允许用户高度定制环境，包括监控渲染帧率、发出作弊命令、模拟快速重置等。此外，它还提供了一套常用的回调函数，减少用户的工作量。

💡 创新点2
该软件包引入了一种灵活高效的数据结构来处理离线轨迹数据，支持对超长轨迹的分布式批量采样，有助于训练需要长期记忆的模型。

💡 创新点3
提供了一个统一的策略模型模板，以及专门为Minecraft领域设计的动作和价值头，允许用户专注于模型架构设计。

💡 创新点4
集成了高效的训练和推理管道，支持分布式训练和推理，以及一个自动化的评估管道，可以分析任务视频并提供批量任务执行能力。

### 📈 实验结果
本文通过与现有Minecraft开发框架的比较，展示了MineStudio在环境定制、智能体创建、训练、评估等方面的优势。它不仅提供了无缝的管道来集成构建、训练和评估智能体，还提供了分布式推理框架和最先进的基线实现，为Minecraft智能体提供了一个标准化的评估范式。

### 💬 可借鉴之处
MineStudio通过模块化设计，降低了开发Minecraft智能体时的工程难度，使得研究人员可以更多地关注算法创新而不是工程细节。它的开源特性和丰富的文档和教程，为快速上手提供了便利。此外，其高效的训练和推理管道，以及集成的基准测试，为Minecraft智能体的研究和开发提供了有力的支持。

## groot--learning-to-follow-instructions-by-watching-gameplay-videos
### Abstract
We study the problem of building a controller that can follow open-ended
instructions in open-world environments. We propose to follow reference videos
as instructions, which offer expressive goal specifications while eliminating
the need for expensive text-gameplay annotations. A new learning framework is
derived to allow learning such instruction-following controllers from gameplay
videos while producing a video instruction encoder that induces a structured
goal space. We implement our agent GROOT in a simple yet effective
encoder-decoder architecture based on causal transformers. We evaluate GROOT
against open-world counterparts and human players on a proposed Minecraft
SkillForge benchmark. The Elo ratings clearly show that GROOT is closing the
human-machine gap as well as exhibiting a 70% winning rate over the best
generalist agent baseline. Qualitative analysis of the induced goal space
further demonstrates some interesting emergent properties, including the goal
composition and complex gameplay behavior synthesis. The project page is
available at https://craftjarvis-groot.github.io.
### 🌟 论文解读 | GROOT：通过观看游戏视频学习指令遵循

### 📌 背景痛点/本文动机
在开放世界环境中，构建能够遵循开放指令的控制器一直是人工智能领域的长期目标。然而，现有的控制器通常只能完成预定义的、有限的程序性任务，这限制了它们在开放世界环境中的应用。本文旨在解决这个问题，提出了一种新的学习框架，通过观看游戏视频来学习指令遵循控制器。

### 🚀 核心方法
💡 创新点1：将目标指定为参考游戏视频片段，从而提供丰富的目标规范，同时消除对昂贵的文本-游戏注释的需求。
💡 创新点2：引入了一种新的学习框架，该框架同时产生一个目标空间和一个视频指令遵循控制器，从而实现从游戏视频中学习指令遵循控制器。

### 📈 实验结果
在Minecraft SkillForge基准测试中，GROOT在整体Elo评分比较中超过了最先进的基线，并且在解决具有挑战性的获取钻石任务中表现出色。

### 💬 可借鉴之处
本文提出的学习框架和GROOT代理的架构设计为构建能够遵循开放指令的控制器提供了新的思路和方法。此外，本文还展示了目标空间和控制器策略的潜在应用，为解决开放世界环境中的复杂任务提供了新的可能性。

## rocket-2--steering-visuomotor-policy-via-cross-view-goal-alignment
### Abstract
We aim to develop a goal specification method that is semantically clear,
spatially sensitive, and intuitive for human users to guide agent interactions
in embodied environments. Specifically, we propose a novel cross-view goal
alignment framework that allows users to specify target objects using
segmentation masks from their own camera views rather than the agent's
observations. We highlight that behavior cloning alone fails to align the
agent's behavior with human intent when the human and agent camera views differ
significantly. To address this, we introduce two auxiliary objectives:
cross-view consistency loss and target visibility loss, which explicitly
enhance the agent's spatial reasoning ability. According to this, we develop
ROCKET-2, a state-of-the-art agent trained in Minecraft, achieving an
improvement in the efficiency of inference 3x to 6x. We show ROCKET-2 can
directly interpret goals from human camera views for the first time, paving the
way for better human-agent interaction.
### 🌟 论文解读 | ROCKET-2：通过跨视图目标对齐引导视觉运动策略

### 📌 背景痛点/本文动机
在机器人学习和虚拟玩家领域，让智能体实现人类期望的目标是一个长期挑战。关键在于找到既能让人类用户轻松指定，又能精确捕捉多种任务的表示方法。现有的方法往往只关注其中一个方面，例如语言指令直观但表达空间关系模糊，视觉模态则容易受到光照、物体外观等因素的影响。

### 🚀 核心方法
💡 创新点1：用户友好的跨视图目标指定方法
ROCKET-2 允许用户使用自己的相机视图中的分割掩码来指定目标对象，而不是使用智能体的观察结果。这种方法将目标指定与智能体的相机视图解耦，从而显著提高了人机交互的效率。

💡 创新点2：跨视图一致性损失和目标可见性损失
为了解决开放世界中部分可观察性的挑战，ROCKET-2 引入了两个辅助目标函数：跨视图一致性损失和目标可见性损失。这些损失函数可以显式地增强智能体在跨视图目标对齐方面的能力，并提高其可操控性。

### 📈 实验结果
在 Minecraft 环境中，ROCKET-2 实现了最先进的性能，并在推理效率方面比 ROCKET-1 提高了 3 倍到 6 倍。实验结果表明，ROCKET-2 可以直接从人类的相机视图中解释目标，为更好的人机交互铺平了道路。

### 💬 可借鉴之处
ROCKET-2 的跨视图目标对齐方法为更直观的人机交互提供了新的思路。其引入的辅助目标函数和架构设计也为解决开放世界中部分可观察性的挑战提供了新的解决方案。

## open-world-reinforcement-learning-over-long-short-term-imagination
### Abstract
Training visual reinforcement learning agents in a high-dimensional open
world presents significant challenges. While various model-based methods have
improved sample efficiency by learning interactive world models, these agents
tend to be "short-sighted", as they are typically trained on short snippets of
imagined experiences. We argue that the primary challenge in open-world
decision-making is improving the exploration efficiency across a vast state
space, especially for tasks that demand consideration of long-horizon payoffs.
In this paper, we present LS-Imagine, which extends the imagination horizon
within a limited number of state transition steps, enabling the agent to
explore behaviors that potentially lead to promising long-term feedback. The
foundation of our approach is to build a $\textit{long short-term world
model}$. To achieve this, we simulate goal-conditioned jumpy state transitions
and compute corresponding affordance maps by zooming in on specific areas
within single images. This facilitates the integration of direct long-term
values into behavior learning. Our method demonstrates significant improvements
over state-of-the-art techniques in MineDojo.
### 🌟 论文解读 | Open-World Reinforcement Learning over Long Short-Term Imagination

### 📌 背景痛点/本文动机
在开放世界中训练视觉强化学习智能体面临着重大挑战。虽然各种基于模型的强化学习方法通过学习交互式世界模型提高了样本效率，但这些智能体往往“目光短浅”，因为它们通常是在由世界模型生成的短期想象经验片段上进行训练的。本文认为，开放世界决策中的主要挑战是在广阔的状态空间中提高探索效率，特别是对于需要考虑长期回报的任务。

### 🚀 核心方法
💡 创新点1：长短期世界模型
本文提出了LS-Imagine，它扩展了想象范围，在有限的状态转换步骤内，使智能体能够探索可能带来有希望长期反馈的行为。LS-Imagine的基础是构建一个长短期世界模型，通过模拟目标条件下的跳跃状态转换，并通过对单个图像中的特定区域进行缩放来计算相应的可利用性图，从而将直接长期价值整合到行为学习中。

💡 创新点2：可利用性图和内在奖励
为了提高开放世界中基于模型的强化学习的样本效率，本文使用视觉观察和文本任务定义来生成可利用性图。可利用性图突出了观察区域与任务描述的相关性，作为空间先验，有效地引导智能体的探索朝着感兴趣的区域进行。此外，本文引入了基于可利用性图的内在奖励函数，以鼓励智能体向目标移动。

💡 创新点3：混合长短期想象路径
LS-Imagine采用演员-评论家算法，根据世界模型生成的有限序列的长期和短期想象来优化智能体的策略。智能体从编码的初始状态开始，根据跳跃标志动态选择长期或短期状态转换模型来预测后续状态。对于长期想象预测的跳跃状态，间隔预测器估计从ˆst−1到ˆst的步骤数ˆ∆t和ˆ∆t时间间隔内的潜在折扣累积奖励ˆGt。否则，对于通过短期想象获得的状态，对应于环境中的单步转换，我们设置ˆ∆t = 1和ˆGt = ˆrt。因此，在一个想象集中，我们获得一个步骤间隔序列ˆ∆2:L和一个预测奖励序列ˆG2:L，这些奖励在连续的想象状态之间。

### 📈 实验结果
本文在MineDojo基准测试中对LS-Imagine进行了评估，MineDojo是一个基于Minecraft游戏的综合模拟平台，具有各种开放性任务。结果表明，LS-Imagine在完成挑战性任务方面显著优于现有视觉强化学习方法，特别是在稀疏目标分布的任务中。

### 💬 可借鉴之处
LS-Imagine提出了一种新颖的基于模型的强化学习方法，该方法捕获即时和跳跃状态转换，并利用它们在行为学习中提高开放世界的探索效率。该方法具有以下可借鉴之处：

*   长短期世界模型架构，能够模拟长期和短期状态转换，并利用它们进行行为学习。
*   通过图像缩放生成可利用性图的方法，有效地引导智能体的探索。
*   基于可利用性图的内在奖励函数，鼓励智能体向目标移动。
*   混合长短期想象路径，使智能体能够更好地理解长期价值，提高决策能力。

LS-Imagine为开放世界强化学习提供了一种有前景的方法，并为未来研究提供了灵感。

## virtualhome--simulating-household-activities-via-programs
### Abstract
In this paper, we are interested in modeling complex activities that occur in
a typical household. We propose to use programs, i.e., sequences of atomic
actions and interactions, as a high level representation of complex tasks.
Programs are interesting because they provide a non-ambiguous representation of
a task, and allow agents to execute them. However, nowadays, there is no
database providing this type of information. Towards this goal, we first
crowd-source programs for a variety of activities that happen in people's
homes, via a game-like interface used for teaching kids how to code. Using the
collected dataset, we show how we can learn to extract programs directly from
natural language descriptions or from videos. We then implement the most common
atomic (inter)actions in the Unity3D game engine, and use our programs to
"drive" an artificial agent to execute tasks in a simulated household
environment. Our VirtualHome simulator allows us to create a large activity
video dataset with rich ground-truth, enabling training and testing of video
understanding models. We further showcase examples of our agent performing
tasks in our VirtualHome based on language descriptions.
### 🌟 论文解读 | VirtualHome：通过程序模拟家庭活动

### 📌 背景痛点/本文动机
随着人工智能和机器人技术的发展，让机器人执行复杂的家庭活动成为可能。然而，如何有效地描述和执行这些活动仍然是一个挑战。本文提出了一个名为 VirtualHome 的模拟器，旨在通过程序来模拟家庭活动，从而为机器人执行复杂任务提供一种新的方法。

### 🚀 核心方法
💡 创新点1：构建家庭活动知识库
本文首先通过众包的方式收集了大量的家庭活动描述，并将其转化为程序形式。这些程序包含了执行任务所需的全部步骤，包括一些常识性步骤，从而为机器人提供了清晰的执行指南。

💡 创新点2：开发 VirtualHome 模拟器
本文开发了一个名为 VirtualHome 的 3D 模拟器，可以模拟家庭环境中的各种活动。通过将程序输入到 VirtualHome 中，可以生成丰富的活动视频数据集，并用于训练和测试视频理解模型。

💡 创新点3：从文本和视频中生成程序
本文提出了一个基于 seq2seq 模型的方法，可以从自然语言描述或视频演示中自动生成程序。这使得机器人可以通过自然语言或视频演示来学习执行新的任务。

### 📈 实验结果
本文在 VirtualHome 模拟器上进行了实验，结果表明，从文本和视频中生成的程序可以有效地驱动机器人执行各种家庭活动。此外，本文还进行了一项人类研究，结果表明，生成的程序与人类对活动的理解具有较高的相关性。

### 💬 可借鉴之处
本文提出的 VirtualHome 模拟器和程序生成方法为机器人执行复杂任务提供了一种新的思路。此外，本文收集的家庭活动知识库和视频数据集也为相关研究提供了宝贵的资源。

## envgen--generating-and-adapting-environments-via-llms-for-training-embodied-agents
### Abstract
Recent SOTA approaches for embodied learning via interaction directly employ
large language models (LLMs) as agents to determine the next steps in an
environment. Due to their world knowledge and reasoning capabilities, LLM
agents achieve stronger performance than previous smaller agents based on
reinforcement learning (RL); however, frequently calling LLMs is slow and
expensive. Instead of directly employing LLMs as agents, can we use LLMs'
reasoning capabilities to adaptively create training environments to help
smaller RL agents learn useful skills that they are weak at? We propose EnvGen,
a novel framework to address this question. We first prompt an LLM to generate
training environments by giving it the task description and simulator
objectives that the agents should learn and then asking it to generate a set of
environment configurations (e.g., different terrains, items initially given to
agents, etc). Next, we train a small RL agent in a mixture of the original and
LLM-generated environments. Then, we enable the LLM to continuously adapt the
generated environments to progressively improve the skills that the agent is
weak at, by providing feedback to the LLM in the form of the agent's
performance. We demonstrate the usefulness of EnvGen with comprehensive
experiments in Crafter and Heist environments. We find that a small RL agent
trained with EnvGen can outperform SOTA methods, including a GPT-4 agent, and
learns long-horizon tasks significantly faster. We also show that using an LLM
to adapt environments dynamically outperforms curriculum learning approaches
and how the environments are adapted to help improve RL agents' weaker skills
over time. Additionally, EnvGen is substantially more efficient as it only uses
a small number of LLM calls (e.g., 4 in total), whereas LLM agents require
thousands of calls. Lastly, we present detailed ablation studies for EnvGen
design choices.
### 🌟 论文解读 | EnvGen：利用LLM生成和适应环境，训练具身智能体

### 📌 背景痛点/本文动机
随着具身智能体在开放世界游戏中的兴起，如何让智能体快速学习并掌握各种技能成为了一个挑战。传统的强化学习（RL）方法在处理长时任务时效率低下，而直接使用大型语言模型（LLM）作为智能体虽然性能强大，但调用成本高昂。本文提出了一种新的框架EnvGen，旨在利用LLM的推理能力来生成和适应训练环境，帮助小型RL智能体学习它们不擅长的技能。

### 🚀 核心方法
💡 创新点1：LLM生成环境
EnvGen首先通过向LLM提供任务描述和模拟器目标，让LLM生成一系列环境配置，例如不同的地形、初始物品等。这些环境可以并行训练智能体，使其快速学习不同的技能。

💡 创新点2：LLM适应环境
EnvGen通过将智能体在原始环境中的表现反馈给LLM，让LLM不断调整生成的环境，使其更加专注于智能体不擅长的技能。这种动态适应过程可以帮助智能体逐步提高其技能水平。

### 📈 实验结果
在Crafter和Heist游戏环境中进行的实验表明，使用EnvGen训练的小型RL智能体在性能上超过了包括GPT-4在内的SOTA方法，并且学习长时任务的速度显著提高。此外，EnvGen的效率也远高于直接使用LLM作为智能体的方法，因为它只需要很少的LLM调用次数。

### 💬 可借鉴之处
EnvGen提供了一种利用LLM推理能力来提高RL智能体性能的有效方法。它可以应用于各种开放世界游戏和模拟器，帮助智能体快速学习并掌握各种技能。此外，EnvGen的动态适应机制也为RL智能体的训练提供了一种新的思路。

## multi-stage-episodic-control-for-strategic-exploration-in-text-games
### Abstract
Text adventure games present unique challenges to reinforcement learning
methods due to their combinatorially large action spaces and sparse rewards.
The interplay of these two factors is particularly demanding because large
action spaces require extensive exploration, while sparse rewards provide
limited feedback. This work proposes to tackle the explore-vs-exploit dilemma
using a multi-stage approach that explicitly disentangles these two strategies
within each episode. Our algorithm, called eXploit-Then-eXplore (XTX), begins
each episode using an exploitation policy that imitates a set of promising
trajectories from the past, and then switches over to an exploration policy
aimed at discovering novel actions that lead to unseen state spaces. This
policy decomposition allows us to combine global decisions about which parts of
the game space to return to with curiosity-based local exploration in that
space, motivated by how a human may approach these games. Our method
significantly outperforms prior approaches by 27% and 11% average normalized
score over 12 games from the Jericho benchmark (Hausknecht et al., 2020) in
both deterministic and stochastic settings, respectively. On the game of Zork1,
in particular, XTX obtains a score of 103, more than a 2x improvement over
prior methods, and pushes past several known bottlenecks in the game that have
plagued previous state-of-the-art methods.
### 🌟 论文解读 | 多阶段策略探索：文本游戏中的强化学习新突破

### 📌 背景痛点/本文动机
文本冒险游戏为强化学习算法提供了独特的测试平台，但同时也带来了巨大的挑战。这些游戏具有组合爆炸式的动作空间和稀疏的奖励，这使得探索与利用之间的平衡变得尤为困难。大动作空间需要广泛的探索，而稀疏的奖励则提供了有限的反馈。现有的方法通常采用单一策略和动作选择策略，难以在探索与利用之间找到合适的平衡点。

### 🚀 核心方法
本文提出了名为 eXploit-Then-eXplore (XTX) 的多阶段控制算法，该算法在每个回合中明确地将探索和利用策略分离。XTX 算法包含两个阶段：

* **利用阶段**：该阶段使用一个模仿过去成功轨迹的策略，使智能体能够返回到游戏空间中已探索的前沿状态。
* **探索阶段**：该阶段使用一个基于好奇心驱动的策略，旨在发现新颖的动作，并探索未知的游戏状态空间。

这种策略分解允许智能体结合全局决策和局部探索，从而更好地应对稀疏奖励和动态动作空间的挑战。

### 📈 实验结果
在 Jericho 基准测试的 12 个游戏中，XTX 算法在确定性和随机性设置下分别比现有方法提高了 27% 和 11% 的平均归一化分数。特别是在 Zork1 游戏中，XTX 算法取得了 103 分的成绩，比现有方法提高了 2 倍以上，并克服了游戏中一些已知的瓶颈。

### 💬 可借鉴之处
* **多阶段策略**：将探索和利用策略分离，可以更好地平衡两者之间的关系，从而提高学习效率。
* **模仿学习**：利用过去成功的经验来指导智能体的行为，可以加快学习速度。
* **好奇心驱动探索**：通过奖励新颖的动作，可以鼓励智能体探索未知的游戏状态空间。
* **混合策略**：使用混合策略可以提供更细粒度的控制，从而更好地适应不同的游戏环境。

### 🌟 总结
XTX 算法为文本冒险游戏中的强化学习提供了一种新的思路，通过多阶段策略和混合策略，有效地解决了探索与利用之间的平衡问题，并在实际游戏中取得了显著的性能提升。

## pre-trained-language-models-as-prior-knowledge-for-playing-text-based-games
### Abstract
Recently, text world games have been proposed to enable artificial agents to
understand and reason about real-world scenarios. These text-based games are
challenging for artificial agents, as it requires an understanding of and
interaction using natural language in a partially observable environment.
Agents observe the environment via textual descriptions designed to be
challenging enough for even human players. Past approaches have not paid enough
attention to the language understanding capability of the proposed agents.
Typically, these approaches train from scratch, an agent that learns both
textual representations and the gameplay online during training using a
temporal loss function. Given the sample-inefficiency of RL approaches, it is
inefficient to learn rich enough textual representations to be able to
understand and reason using the textual observation in such a complicated game
environment setting. In this paper, we improve the semantic understanding of
the agent by proposing a simple RL with LM framework where we use
transformer-based language models with Deep RL models. We perform a detailed
study of our framework to demonstrate how our model outperforms all existing
agents on the popular game, Zork1, to achieve a score of 44.7, which is 1.6
higher than the state-of-the-art model. Overall, our proposed approach
outperforms 4 games out of the 14 text-based games, while performing comparable
to the state-of-the-art models on the remaining games.
### 🌟 论文解读 | 利用预训练语言模型提升文本游戏中的智能体表现

### 📌 背景痛点/本文动机
文本世界游戏为人工智能体提供了理解和推理现实世界场景的机会。然而，这些游戏对智能体来说极具挑战性，因为它们需要在部分可观察的环境中理解和交互自然语言。现有的方法往往忽略了智能体的语言理解能力，并且通常从头开始训练，导致样本效率低下。本文旨在通过引入预训练语言模型来提升智能体的语义理解能力，从而在文本游戏中取得更好的表现。

### 🚀 核心方法
💡 创新点1：预训练语言模型作为先验知识
本文提出了一种简单的RL与LM框架，使用基于Transformer的语言模型（如DistilBERT）与深度强化学习模型相结合。通过在大型通用英语语料库上进行预训练，然后针对特定下游任务进行微调，预训练语言模型能够为智能体提供丰富的语言理解和先验知识。

💡 创新点2：游戏感知的预训练语言模型
为了使预训练语言模型更好地适应游戏环境，本文使用独立的人类游戏播放轨迹数据集对DistilBERT进行微调，从而使其具备游戏感知能力。这种微调过程有助于将语言模型的知识和世界感知能力转移到不同的游戏和智能体中。

### 📈 实验结果
本文在14个文本游戏中对所提出的框架进行了评估，结果显示，在Zork1游戏中，模型取得了44.7分的成绩，比现有最佳模型高出1.6分。总体而言，该框架在4个游戏中超越了现有模型，并在其他游戏中表现与现有模型相当。

### 💬 可借鉴之处
本文提出的预训练语言模型作为先验知识的方法，为文本游戏中的智能体设计提供了新的思路。通过利用预训练语言模型的知识和世界感知能力，智能体能够更好地理解和推理游戏环境，从而在游戏中取得更好的表现。此外，本文还强调了微调预训练语言模型以适应特定游戏环境的重要性，这为未来研究提供了有价值的启示。

## guiding-pretraining-in-reinforcement-learning-with-large-language-models
### Abstract
Reinforcement learning algorithms typically struggle in the absence of a
dense, well-shaped reward function. Intrinsically motivated exploration methods
address this limitation by rewarding agents for visiting novel states or
transitions, but these methods offer limited benefits in large environments
where most discovered novelty is irrelevant for downstream tasks. We describe a
method that uses background knowledge from text corpora to shape exploration.
This method, called ELLM (Exploring with LLMs) rewards an agent for achieving
goals suggested by a language model prompted with a description of the agent's
current state. By leveraging large-scale language model pretraining, ELLM
guides agents toward human-meaningful and plausibly useful behaviors without
requiring a human in the loop. We evaluate ELLM in the Crafter game environment
and the Housekeep robotic simulator, showing that ELLM-trained agents have
better coverage of common-sense behaviors during pretraining and usually match
or improve performance on a range of downstream tasks. Code available at
https://github.com/yuqingd/ellm.
### 🌟 论文解读 | 利用大型语言模型引导强化学习的预训练

### 📌 背景痛点/本文动机
强化学习算法在缺乏密集、良好形状的奖励函数时通常会遇到困难。内在动机探索方法通过奖励代理访问新颖状态或转换来解决这一限制，但在大多数发现的新颖性对下游任务无关紧要的大型环境中，这些方法提供的益处有限。本文提出了一种方法，该方法使用来自文本语料库的背景知识来塑造探索。这种方法称为ELLM（使用大型语言模型进行探索），它奖励代理实现由语言模型提出的与代理当前状态描述相关的目标。通过利用大规模语言模型预训练，ELLM引导代理朝着人类有意义且可能有用的行为发展，而无需人工干预。

### 🚀 核心方法
💡 创新点1：利用大型语言模型（LLM）的背景知识来塑造探索。LLM是概率文本模型，其预测编码了丰富的关于人类常识知识和文化习俗的信息。ELLM通过查询LLM来获取可能的目标，并奖励代理实现这些建议，从而引导探索朝着完成多样化、上下文敏感和人类有意义的目标。

💡 创新点2：使用LLM生成的目标作为内在奖励函数。ELLM通过测量LLM生成的目标与环境中代理转换的描述之间的语义相似性来计算奖励。当转换的描述与目标描述足够接近时，代理将获得与相似度成比例的奖励。

### 📈 实验结果
本文在Crafter游戏环境和Housekeep机器人模拟器中评估了ELLM。结果表明，ELLM训练的代理在预训练期间对常识行为的覆盖范围更好，并且在下游任务上的性能通常与基线相当或有所提高。

### 💬 可借鉴之处
本文提出的方法可以用于引导强化学习代理在缺乏外部定义的奖励的情况下学习有用的行为。通过利用LLM的背景知识，ELLM可以引导代理朝着人类有意义且可能有用的行为发展，从而提高强化学习算法的性能。此外，本文还探讨了LLM性能对提示选择、状态和转换描述的敏感性，并提出了改进LLM性能的潜在方法。

## pokergpt--an-end-to-end-lightweight-solver-for-multi-player-texas-hold-em-via-large-language-model
### Abstract
Poker, also known as Texas Hold'em, has always been a typical research target
within imperfect information games (IIGs). IIGs have long served as a measure
of artificial intelligence (AI) development. Representative prior works, such
as DeepStack and Libratus heavily rely on counterfactual regret minimization
(CFR) to tackle heads-up no-limit Poker. However, it is challenging for
subsequent researchers to learn CFR from previous models and apply it to other
real-world applications due to the expensive computational cost of CFR
iterations. Additionally, CFR is difficult to apply to multi-player games due
to the exponential growth of the game tree size. In this work, we introduce
PokerGPT, an end-to-end solver for playing Texas Hold'em with arbitrary number
of players and gaining high win rates, established on a lightweight large
language model (LLM). PokerGPT only requires simple textual information of
Poker games for generating decision-making advice, thus guaranteeing the
convenient interaction between AI and humans. We mainly transform a set of
textual records acquired from real games into prompts, and use them to
fine-tune a lightweight pre-trained LLM using reinforcement learning human
feedback technique. To improve fine-tuning performance, we conduct prompt
engineering on raw data, including filtering useful information, selecting
behaviors of players with high win rates, and further processing them into
textual instruction using multiple prompt engineering techniques. Through the
experiments, we demonstrate that PokerGPT outperforms previous approaches in
terms of win rate, model size, training time, and response speed, indicating
the great potential of LLMs in solving IIGs.
### 🌟 论文解读 | PokerGPT：基于大型语言模型的轻量级多玩家德州扑克解决方案

### 📌 背景痛点/本文动机
德州扑克作为一种典型的非完美信息游戏（IIG），一直是人工智能研究的重要目标。然而，现有的解决方案，如DeepStack和Libratus，主要依赖于反事实后悔最小化（CFR）算法，该算法在计算成本和扩展性方面存在局限性。CFR算法的计算成本高昂，难以应用于多玩家游戏，且难以从现有模型中学习并应用于其他现实世界应用。

### 🚀 核心方法
本文提出了PokerGPT，一种基于轻量级大型语言模型（LLM）的端到端德州扑克解决方案。PokerGPT通过以下创新点克服了现有方法的局限性：

💡 创新点1：端到端学习框架
PokerGPT采用端到端学习框架，避免了复杂的特征工程和中间步骤。它仅需要简单的文本信息即可生成决策建议，实现了人机交互的便捷性。

💡 创新点2：轻量级LLM
PokerGPT基于轻量级LLM，具有更少的参数和更快的推理速度，同时训练时间也更短，实现了资源的有效利用。

💡 创新点3：高效的数据处理
PokerGPT采用数据清洗和提示工程技术，将真实游戏数据转换为可理解的文本提示，并使用强化学习人类反馈技术进行微调，提高了模型性能。

### 📈 实验结果
实验结果表明，PokerGPT在胜率、模型大小、训练时间和响应速度等方面均优于现有方法。此外，PokerGPT能够处理任意数量的玩家，并展现出出色的灵活性和适应性。

### 💬 可借鉴之处
PokerGPT的成功表明，LLM在解决IIG方面具有巨大潜力。其端到端学习框架、轻量级模型和高效的数据处理技术为其他IIG研究提供了可借鉴的经验。此外，PokerGPT的交互式特性使其在现实世界应用中具有广阔前景。

## enhance-reasoning-for-large-language-models-in-the-game-werewolf
### Abstract
This paper presents an innovative framework that integrates Large Language
Models (LLMs) with an external Thinker module to enhance the reasoning
capabilities of LLM-based agents. Unlike augmenting LLMs with prompt
engineering, Thinker directly harnesses knowledge from databases and employs
various optimization techniques. The framework forms a reasoning hierarchy
where LLMs handle intuitive System-1 tasks such as natural language processing,
while the Thinker focuses on cognitive System-2 tasks that require complex
logical analysis and domain-specific knowledge. Our framework is presented
using a 9-player Werewolf game that demands dual-system reasoning. We introduce
a communication protocol between LLMs and the Thinker, and train the Thinker
using data from 18800 human sessions and reinforcement learning. Experiments
demonstrate the framework's effectiveness in deductive reasoning, speech
generation, and online game evaluation. Additionally, we fine-tune a 6B LLM to
surpass GPT4 when integrated with the Thinker. This paper also contributes the
largest dataset for social deduction games to date.
### 🌟 论文解读 | 大型语言模型推理能力提升：以狼人杀游戏为案例

### 📌 背景痛点/本文动机
随着大型语言模型（LLMs）在自然语言处理（NLP）任务上的突破，其在推理、规划和决策等领域的潜力也逐渐显现。然而，LLMs在处理复杂推理任务时仍面临挑战，尤其是在需要领域特定知识和深度逻辑分析的任务中。本文旨在通过引入外部推理模块，即“思考者”（Thinker），来增强LLM的推理能力，使其在特定任务中表现更佳。

### 🚀 核心方法
💡 创新点1：双系统推理框架
本文提出了一个创新的框架，将LLMs与外部Thinker模块相结合，形成了一个推理层次结构。LLMs负责处理直观的System-1任务，如自然语言处理和常识推理，而Thinker则专注于需要复杂逻辑分析和领域特定知识的System-2任务。

💡 创新点2：Thinker模块的设计与训练
Thinker模块直接从数据库中获取知识，并采用各种优化技术进行训练。它通过模仿学习、强化学习和基于群体的训练等方法，学习生成合理的游戏动作和LLM的语音指令。

💡 创新点3：数据集贡献
本文收集了18,800场真实人类游戏会话数据，构建了迄今为止最大的社交推理游戏数据集，为研究提供了宝贵资源。

### 📈 实验结果
实验结果表明，引入Thinker模块显著提高了LLMs的推理和生成能力。在狼人杀游戏中，Thinker模块在推理、语音生成和在线游戏评估方面均表现出色。此外，通过将Thinker与一个较小的LLM模型（6B）进行微调，其性能甚至超过了GPT4。

### 💬 可借鉴之处
本文提出的框架和方法为LLMs在复杂推理任务中的应用提供了新的思路。通过将LLMs与外部推理模块相结合，可以有效提升LLMs在特定领域的推理能力，使其在更多实际应用中发挥更大的作用。此外，本文构建的大规模数据集也为社交推理游戏的研究提供了重要的数据基础。

## adapt--as-needed-decomposition-and-planning-with-language-models
### Abstract
Large Language Models (LLMs) are increasingly being used for interactive
decision-making tasks requiring planning and adapting to the environment.
Recent works employ LLMs-as-agents in broadly two ways: iteratively determining
the next action (iterative executors) or generating plans and executing
sub-tasks using LLMs (plan-and-execute). However, these methods struggle with
task complexity, as the inability to execute any sub-task may lead to task
failure. To address these shortcomings, we introduce As-Needed Decomposition
and Planning for complex Tasks (ADaPT), an approach that explicitly plans and
decomposes complex sub-tasks as-needed, i.e., when the LLM is unable to execute
them. ADaPT recursively decomposes sub-tasks to adapt to both task complexity
and LLM capability. Our results demonstrate that ADaPT substantially
outperforms established strong baselines, achieving success rates up to 28.3%
higher in ALFWorld, 27% in WebShop, and 33% in TextCraft -- a novel
compositional dataset that we introduce. Through extensive analysis, we
illustrate the importance of multilevel decomposition and establish that ADaPT
dynamically adjusts to the capabilities of the executor LLM as well as to task
complexity.
### 🌟 论文解读 | ADaPT：按需分解与规划，提升大型语言模型在复杂任务中的表现

### 📌 背景痛点/本文动机
随着大型语言模型（LLMs）在自然语言处理领域的广泛应用，它们也逐渐被应用于需要规划和适应环境的交互式决策任务中。然而，现有的方法在处理复杂任务时面临着挑战，因为LLMs在执行子任务时可能会失败，从而导致整个任务的失败。

### 🚀 核心方法
为了解决上述问题，本文提出了ADaPT（As-Needed Decomposition and Planning for complex Tasks），一种按需分解和规划复杂任务的方法。ADaPT的核心思想是，当LLM作为执行者无法执行子任务时，将其分解为更小的子任务，并递归地进行分解，以适应任务的复杂性和LLM的能力。

#### 💡 创新点1：按需分解
ADaPT通过递归地分解子任务，动态地适应任务的复杂性和LLM的能力。当LLM作为执行者无法执行子任务时，它会调用LLM作为规划者来生成更小的子任务，并递归地调用ADaPT来执行这些子任务。

#### 💡 创新点2：多级分解
ADaPT支持多级分解，这意味着它可以进一步分解子任务，直到它们变得足够简单，可以被LLM作为执行者成功执行。这种多级分解的能力使得ADaPT能够处理更复杂的任务，并提高任务的成功率。

### 📈 实验结果
在ALFWorld、WebShop和TextCraft三个数据集上进行的实验结果表明，ADaPT显著优于现有的强基线方法，在ALFWorld上提高了28.3%的成功率，在WebShop上提高了27%，在TextCraft上提高了33%。

### 💬 可借鉴之处
ADaPT提供了一种有效的方法来处理LLMs在复杂任务中的执行失败问题。它通过按需分解和规划，动态地适应任务的复杂性和LLM的能力，从而提高了任务的成功率。此外，ADaPT的多级分解能力使其能够处理更复杂的任务，并提高任务的成功率。

## cooperation-on-the-fly--exploring-language-agents-for-ad-hoc-teamwork-in-the-avalon-game
### Abstract
Multi-agent collaboration with Large Language Models (LLMs) demonstrates
proficiency in basic tasks, yet its efficiency in more complex scenarios
remains unexplored. In gaming environments, these agents often face situations
without established coordination protocols, requiring them to make intelligent
inferences about teammates from limited data. This problem motivates the area
of ad hoc teamwork, in which an agent may potentially cooperate with a variety
of teammates to achieve a shared goal. Our study focuses on the ad hoc teamwork
problem where the agent operates in an environment driven by natural language.
Our findings reveal the potential of LLM agents in team collaboration,
highlighting issues related to hallucinations in communication. To address this
issue, we develop CodeAct, a general agent that equips LLM with enhanced memory
and code-driven reasoning, enabling the repurposing of partial information for
rapid adaptation to new teammates.
### 🌟 论文解读 | 探索大型语言模型在动态环境中的协作能力

### 📌 背景痛点/本文动机
随着大型语言模型（LLMs）在推理和泛化能力上的不断提升，它们在构建自主代理和推动人工智能领域的发展方面展现出巨大潜力。然而，在多智能体协作中，特别是在没有预先设定的协调协议的动态环境中，LLMs的协作效率仍然是一个未充分探索的领域。本文旨在研究LLMs在动态环境中的协作能力，特别是在没有明确团队策略的情况下，如何与不同的队友进行有效合作。

### 🚀 核心方法
💡 创新点1：引入AvalonPlay基准
本文提出了AvalonPlay基准，这是一个基于自然语言的多智能体平台，用于模拟动态环境中的协作任务。在这个基准中，智能体需要在有限的信息和没有预先设定的团队策略的情况下，通过观察队友的行为来推断他们的角色，并动态调整团队策略以实现共同目标。

💡 创新点2：开发CodeAct智能体
为了解决LLMs在动态环境中协作时可能出现的记忆遗忘和幻觉生成等问题，本文提出了CodeAct智能体。CodeAct利用LLMs的代码驱动推理能力，通过将复杂的语义任务转化为灵活的代码结构，从而提高智能体在动态环境中的协作效率。

### 📈 实验结果
实验结果表明，GPT-4模型在AvalonPlay基准中表现出最佳的协作能力，而CodeAct智能体在团队选择准确性方面优于其他语义推理方法。此外，实验还发现，引入自然语言通信协议并不总是能显著提高LLMs的协作效率。

### 💬 可借鉴之处
本文的研究结果表明，LLMs在动态环境中的协作能力仍然面临一些挑战，如记忆遗忘和幻觉生成。为了提高LLMs的协作效率，可以借鉴本文提出的CodeAct智能体的设计思路，利用代码驱动推理和记忆检索系统来增强智能体的推理能力和信息处理能力。此外，还可以进一步研究如何减少幻觉生成的影响，并探索LLMs在现实世界场景中的应用。

## counting-to-explore-and-generalize-in-text-based-games
### Abstract
We propose a recurrent RL agent with an episodic exploration mechanism that
helps discovering good policies in text-based game environments. We show
promising results on a set of generated text-based games of varying difficulty
where the goal is to collect a coin located at the end of a chain of rooms. In
contrast to previous text-based RL approaches, we observe that our agent learns
policies that generalize to unseen games of greater difficulty.
### 🌟 论文解读 | 基于计数探索和泛化的文本游戏强化学习

### 📌 背景痛点/本文动机
文本游戏是一种复杂的交互式模拟，使用自然语言描述游戏状态、接受玩家动作并报告环境变化。玩家必须通过探索来发现游戏目标，而游戏中的观察和动作空间都是组合和复合的，玩家必须应对部分可观察性，因为描述性文本并不提供关于底层游戏状态的完整、明确的信息。

### 🚀 核心方法
💡 创新点1：提出了一种基于循环的强化学习代理，具有情节探索机制，有助于在基于文本的游戏环境中发现良好的策略。
💡 创新点2：提出了一种情节计数探索方案，其中状态计数在每个情节开始时重置。这种奖励充当情节记忆，推动代理访问当前情节中尚未遇到的状态。

### 📈 实验结果
在一系列生成的基于文本的游戏中，该代理在收集位于一系列房间末尾的硬币的目标上取得了有希望的结果。与之前的基于文本的强化学习方法相比，观察到该代理学习的策略可以泛化到未见的更具挑战性的游戏。

### 💬 可借鉴之处
该论文提出的基于计数探索和泛化的文本游戏强化学习方法，为解决文本游戏中的探索和泛化问题提供了一种新的思路。该方法可以应用于其他需要探索和记忆能力的强化学习任务，例如迷宫探索、路径规划等。

## suspicion-agent--playing-imperfect-information-games-with-theory-of-mind-aware-gpt-4
### Abstract
Unlike perfect information games, where all elements are known to every
player, imperfect information games emulate the real-world complexities of
decision-making under uncertain or incomplete information. GPT-4, the recent
breakthrough in large language models (LLMs) trained on massive passive data,
is notable for its knowledge retrieval and reasoning abilities. This paper
delves into the applicability of GPT-4's learned knowledge for imperfect
information games. To achieve this, we introduce \textbf{Suspicion-Agent}, an
innovative agent that leverages GPT-4's capabilities for performing in
imperfect information games. With proper prompt engineering to achieve
different functions, Suspicion-Agent based on GPT-4 demonstrates remarkable
adaptability across a range of imperfect information card games. Importantly,
GPT-4 displays a strong high-order theory of mind (ToM) capacity, meaning it
can understand others and intentionally impact others' behavior. Leveraging
this, we design a planning strategy that enables GPT-4 to competently play
against different opponents, adapting its gameplay style as needed, while
requiring only the game rules and descriptions of observations as input. In the
experiments, we qualitatively showcase the capabilities of Suspicion-Agent
across three different imperfect information games and then quantitatively
evaluate it in Leduc Hold'em. The results show that Suspicion-Agent can
potentially outperform traditional algorithms designed for imperfect
information games, without any specialized training or examples. In order to
encourage and foster deeper insights within the community, we make our
game-related data publicly available.
### 🌟 论文解读 | 利用GPT-4的“心智理论”能力玩不完美信息游戏

### 📌 背景痛点/本文动机
在现实世界中，决策往往是在信息不完整或不确定的情况下进行的。然而，大多数现有的AI算法都是在完美信息游戏中训练的，即所有玩家都能看到所有信息。这限制了它们在现实世界中的应用。本文旨在探索如何利用大型语言模型（LLM）的知识和推理能力来处理不完美信息游戏，从而更好地模拟现实世界的决策过程。

### 🚀 核心方法
本文提出了一个名为Suspicion-Agent的创新型自主代理，它基于GPT-4，并利用其强大的知识检索和推理能力来玩不完美信息游戏。Suspicion-Agent的核心创新点包括：

💡 创新点1：利用GPT-4的“心智理论”（ToM）能力，即理解他人并有意影响他人行为的能力。这使得Suspicion-Agent能够预测对手的行为，并根据对手的行为调整自己的策略。

💡 创新点2：将游戏过程分解为多个子模块，如观察解释器、游戏模式分析和规划模块。每个模块都使用不同的提示来引导GPT-4执行特定的功能，从而实现更有效的决策。

### 📈 实验结果
在实验中，Suspicion-Agent在三个不同的不完美信息游戏中展示了其能力，并在Leduc Hold'em游戏中进行了定量评估。结果表明，Suspicion-Agent可以潜在地超越传统算法，而无需任何专门的训练或示例。

### 💬 可借鉴之处
本文提出的Suspicion-Agent框架为利用LLM在不完美信息游戏中进行决策提供了一个新的思路。其核心思想是将LLM的知识和推理能力与ToM能力相结合，从而实现更有效的决策。此外，本文还公开了所有与游戏相关的数据，这将有助于研究人员更好地理解LLM的能力，并开发更有效的模型。

## enhancing-agent-learning-through-world-dynamics-modeling
### Abstract
Large language models (LLMs) have been increasingly applied to tasks in
language understanding and interactive decision-making, with their impressive
performance largely attributed to the extensive domain knowledge embedded
within them. However, the depth and breadth of this knowledge can vary across
domains. Many existing approaches assume that LLMs possess a comprehensive
understanding of their environment, often overlooking potential gaps in their
grasp of actual world dynamics. To address this, we introduce Discover, Verify,
and Evolve (DiVE), a framework that discovers world dynamics from a small
number of demonstrations, verifies the accuracy of these dynamics, and evolves
new, advanced dynamics tailored to the current situation. Through extensive
evaluations, we assess the impact of each component on performance and compare
the dynamics generated by DiVE to human-annotated dynamics. Our results show
that LLMs guided by DiVE make more informed decisions, achieving rewards
comparable to human players in the Crafter environment and surpassing methods
that require prior task-specific training in the MiniHack environment.
### 🌟 论文解读 | 通过世界动态建模增强智能体学习

### 📌 背景痛点/本文动机
大型语言模型（LLMs）在语言理解和交互式决策任务中表现出色，这主要归功于它们嵌入的广泛领域知识。然而，这种知识的深度和广度在不同领域之间可能存在差异。许多现有方法假设LLMs对其环境有全面的理解，但往往忽视了它们对实际世界动态的掌握可能存在差距。为了解决这个问题，本文提出了Discover, Verify, and Evolve (DiVE)框架，该框架从少量演示中发现世界动态，验证这些动态的准确性，并根据当前情况演化新的、先进的动态。

### 🚀 核心方法
💡 创新点1：DiVE框架
DiVE框架由三个主要组件组成：
- Discoverer：使用课程学习方法从演示中迭代地发现环境动态。
- Verifier：消除LLMs由于幻觉倾向而导致的不可靠动态。
- Evolver：根据学习的动态，推理出针对当前情况的深入、特定于状态的知识。

💡 创新点2：层次课程学习
DiVE采用层次课程学习方法，从简单到复杂的动态逐步学习，从而更有效地学习。具体来说，它从任务分解层次结构中的元素（如动作、对象、子任务和子目标）开始，逐步学习它们的动态。

💡 创新点3：动态验证
为了确保动态的准确性，DiVE引入了动态验证器，它可以过滤掉可能无效和冲突的动态候选者，从而提高决策过程的可靠性。

💡 创新点4：在线策略学习
DiVE不仅学习基本规则，还专注于根据这些动态开发高级游戏策略。它通过在线学习方法将动态演化为策略，从而生成更符合当前游戏场景的策略。

### 📈 实验结果
在Crafter和MiniHack环境中进行的实验表明，DiVE在性能方面优于所有其他基线模型。在Crafter环境中，DiVE在分数和奖励方面分别比SOTA LLM方法SPRING提高了337.8%和110.1%，并且超过了SOTA RL方法DreamerV3。在MiniHack环境中，DiVE在Lava Crossing任务上与SSO和Reflexion（都需要30次迭代训练）的性能相当，并且在Wand of Death和Quest任务上超过了这两个基线。

### 💬 可借鉴之处
DiVE框架为解决LLMs在特定领域中的知识差距问题提供了一种有效的方法。它通过发现、验证和演化世界动态，提高了LLMs的决策能力。此外，DiVE的层次课程学习和动态验证方法可以应用于其他需要长期规划和决策的任务中。

