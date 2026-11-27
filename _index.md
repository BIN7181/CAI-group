---
# 首页标题留空则使用站点标题
title: ''
summary: ''
date: 2022-10-24
type: landing
sections:
  - block: resume-biography-3
    content:
      # 选择展示的作者（对应 data/authors/ 下的文件名）
      username: me
      text: ''
      headings:
        about: 个人简介
        education: 教育经历
        interests: 研究方向
    design:
      background:
        gradient_mesh:
          enable: true
      name:
        size: md
      avatar:
        size: large
        shape: circle
  - block: markdown
    content:
      title: '课题组简介'
      subtitle: ''
      text: |-
        本课题组依托南京大学能源与资源学院，聚焦**电解水制氢关键材料与器件**，围绕阴离子交换膜（AEM）与质子交换膜（PEM）电解水体系，开展催化电极、膜电极组件与电解槽器件的设计、制备与性能调控研究。

        同时，结合同步辐射**工况（operando）与时间分辨 XAFS 谱学**，原位追踪催化剂在反应条件下的结构演化与活性物种，揭示析氧/析氢反应机制；并探索电解水制氢与**废塑料升级回收**的耦合新路径，推动绿氢技术的低成本化与高值化。

        课题组常年招收硕士、博士研究生与博士后，欢迎对电催化、原位表征与器件工程感兴趣的同学联系。
    design:
      columns: '1'
  - block: collection
    id: papers
    content:
      title: '代表性论文'
      subtitle: ''
      text: ''
      filters:
        folders:
          - publications
        featured_only: true
    design:
      view: citation
      columns: 2
---
