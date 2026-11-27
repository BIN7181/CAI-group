---
title: ''
date: 2022-10-24
type: landing
sections:
  # ① 首页顶部：课题组合照轮播（照片清单在 layouts/_shortcodes/hero-carousel.html 里改）
  - block: markdown
    content:
      text: |-
        {{< hero-carousel >}}
    design:
      columns: '1'
      spacing:
        padding: ['0', '0', '0', '0']
  # ② 团队简介 / 新闻动态 / 研究方向 / 友情链接：四块都在 layouts/_shortcodes/home-sections.html 里
  - block: markdown
    content:
      text: |-
        {{< home-sections >}}
    design:
      columns: '1'
      spacing:
        padding: ['0', '0', '0', '0']
---
