# 推荐算法工程师
## 第一部分：推荐系统之内容理解与画像构建
### Week1：机器学习基础
- 逻辑回归模型
- 梯度下降法
- 神经网络模型
- 过拟合与正则
- 常用的评价指标
- 常用的优化算法
- 向量、矩阵基础

### Week2：推荐系统基础
- 推荐系统概述、架构设计
- 推荐系统后台数据流设计
- 常用的技术栈
- 推荐系统中的评价指标
- 简单的用户协同
- 环境搭建

### Week3：内容画像的构建以及NLP技术
- 内容画像的搭建基础
- 关键词提取技术tf-idf, textRank
- LSTM与注意力机制
- Attention的几种常用方式
- Self-Attention
- Multi-head Attention
- 双线性Attention
- NLP工具的使用
- MySQL数据库的搭建与内容画像存储

### Week4：用户画像的构建
- 用户画像与内容画像的关系
- 用户画像的架构
- 用户画像的扩展
- 用户画像与排序特征
- 用途：基于标签的用户画像
- 标签权重的计算方法（贝叶斯平滑、时间衰减）
- 基于用户画像的召回方法
- Redis的搭建与使用
- 基于Redis的用户画像存储
- Hadoop, Hive, Spark等工具使用

## 第二部分：召回模型与策略、数据与采样的学问
### Week5：传统Matching方法
- MF召回法以及求解
- 特征值分解
- 传统奇异值分解之SVM
- FunkSVD 
- ALS方法
- SVD++
- 基于物品的协同Item-CF

### Week6：深度 Matching方法
- MF召回法以及求解
- 理解Embedding技术
- Embedding为什么有效
- Embedding与稀疏ID类特征的关系
- Item-CF召回与Item2Vec
- Airbnb序列召回与冷启动缓解思路
- NCF召回以及变种
- YouTube召回方法
- 从DSSM到双塔模型
- 双塔模型工业界的部署方法
- 多兴趣召回
- MIND召回
- Faiss工具介绍
- KD树，LSH，Simhash

### Week7: Graph Embedding与用户行为构建图
- MIND召回
- 随机游走于传统协同方法
- Deepwalk
- Node2Vec及其同质性与结构性
- LINE 
- 随机游走的实现
- Alias采样方法
- Neo4j讲解
- Graph Embedding的实现
- Node2Vec的实现

### Week8: 图推荐、图神经网络、采样与热度打压
- MIND召回
- Graph Embedding优化
- EGS，注意力机制及其变种
- Ripple网络方法
- 召回层采样的坑与技巧
- 热度抑制
- EGES的实现
- GCN和GAT 
- GraphSage

## 第三部分：排序模型、重排序与多目标
### Week9: 经典Ranking模型方法
- MIND召回
- Ranking与用户画像
- 物品画像
- LR模型
- GBDT+ LR
- FM模型详解、业界使用方法与坑
- FFM模型
- AUC与GAUC
- 增量学习与Online Learning
- 从L1稀疏化、FOBOS到FTRL算法
- 基于FM实现Ranking精排序

### Week10: 深度Ranking模型与工业采样技巧
- 粗排与精排及其意义
- 主流深度推荐模型的集中范式
- 特征自动组合：Deep&Cross, XDeepFM, PNN
- 特征重要度提取以及无用特征去噪：AFM， DeepFFM
- 序列推荐模型：DIN，DIEN， AttRes，Stamp
- 独辟蹊径之序列推荐的优化思路
- 深度模型工具的介绍与使用
- MLSQL
- DeepCTR等与工业界采样方法

### Week11: 重排序与多目标学习
- 多目标学习的几种范式
- 范式一：样本加权
- 范式二：多模型融合
- 范式三：联合训练、ESMM，MMOE框架，ESM2等
- ESMM的实现

## 第四部分：实时召回策略与前沿推荐技术
### Week12-13: 工业界新闻推荐系统中冷启动与热点文章实时召回
- 人群分桶
- 实时交互正反馈
- 实时召回与实时画像技术
- 人群投票
- 人群等级投票
- 降维分发
- 后验与先验的结合
- 引入注意力机制的优化兴趣增加和衰减
- 热点文章召回策略
- 本地文章召回策略
- 算法策略与运营配合协作

### Week14: 强化学习与推荐系统、AutoML与推荐系统
- 强化学习概念、以及在推荐系统中的对应
- DP算法本质思想
- 马尔科夫决策
- 蒙特卡洛搜索所树(MCTS)
- UCB及其在推荐系统中的应用
- 汤普森采样法
- Q-Learning、DRN、策略梯度
- 强化学习在推荐场景中的应用

### Week15: 项目总结，部署以职业规划
- 工业界项目的部署
- 推荐系统岗位的面试要点
- 大厂的面试攻略
- 如何准备简历、包装自己
- 职业规划

你了解FM模型与SVM有什么相似之处吗？FM固然可以用作为打分模型，但它可以用来做matching吗，如果可以，如何做？item2Vec模型在业界是如何缓解冷启动的问题的？双塔模型优势在哪？DeepFM具体实现时，wide端和deep端的优化方式是一样的吗？基于Graph的推荐方法在业界的应用目前是怎样的？
