---
title: ''
date: 2022-10-24
type: landing
sections:
  - block: markdown
    content:
      text: |-
        {{< hero-carousel >}}
    design:
      columns: '1'
      spacing:
        padding: ['0', '0', '0', '0']
  - block: markdown
    id: about
    content:
      title: 团队简介
      subtitle: 南京大学能源与资源学院 · 电催化与电解水制氢实验室
      text: |-
        本课题组依托南京大学能源与资源学院，聚焦**电解水制氢关键材料与器件**，围绕阴离子交换膜（AEM）与质子交换膜（PEM）电解水体系，开展催化电极、膜电极组件与电解槽器件的设计、制备与性能调控研究。

        同时，课题组结合同步辐射**工况（operando）与时间分辨 XAFS 谱学**，原位追踪催化剂在反应条件下的结构演化与活性物种，揭示析氧/析氢反应机制；并探索电解水制氢与**废塑料升级回收**耦合的新路径，推动绿氢技术的低成本化与高值化。

        相关研究成果发表于 *Journal of the American Chemical Society*、*ACS Energy Letters*、*Applied Catalysis O: Open* 等期刊。
    design:
      columns: '1'
  - block: collection
    content:
      title: 新闻动态
      filters:
        folders:
          - blog
    design:
      view: card
      columns: 3
  - block: collection
    content:
      title: 研究方向
      subtitle: 面向绿氢制备的材料、器件与原位表征
      filters:
        folders:
          - projects
    design:
      view: card
      columns: 3
  - block: collection
    content:
      title: 代表性成果
      subtitle: Selected Publications
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: citation
      columns: 2
---
