#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""创建研究方向页与首条新闻，并清理模板示例内容"""
import os

PROJECTS = [
    dict(
        slug="aem-water-electrolysis",
        title="AEM 电解水制氢电极与器件研发",
        summary="围绕阴离子交换膜（AEM）电解水体系，开展非贵金属催化电极、膜电极组件与电解槽器件设计，研究流道结构、集流体与气液传质对电解性能的影响。",
        tags=["AEMWE", "膜电极", "器件工程"],
    ),
    dict(
        slug="pem-water-electrolysis",
        title="PEM 电解水制氢催化材料与器件",
        summary="面向质子交换膜（PEM）酸性析氧环境，研究铱基/钌基催化材料的结构调控与稳定性机制，兼顾活性与长寿命。",
        tags=["PEMWE", "酸性析氧", "贵金属催化剂"],
    ),
    dict(
        slug="operando-xafs",
        title="工况与时间分辨 XAFS 谱学及应用",
        summary="依托同步辐射光源，发展原位（operando）与时间分辨 XAFS 方法，追踪电催化过程中活性物种与结构演化，并探索电解水制氢与废塑料升级回收的耦合路径。",
        tags=["XAFS", "原位表征", "废塑料升级回收"],
    ),
]

NEWS = dict(
    slug="site-launched",
    title="课题组网站正式上线",
    date="2026-11-27",
    summary="课题组成立新的官方主页，后续将在此发布研究进展、学术活动与招生信息。",
    tags=["网站", "通知"],
)


def project_md(p):
    return "\n".join([
        "---",
        'title: "%s"' % p["title"],
        'summary: "%s"' % p["summary"],
        'date: "2026-11-01T00:00:00Z"',
        "authors:",
        "- me",
        "tags:",
    ] + ["- %s" % t for t in p["tags"]] + [
        "featured: false",
        'projects: []',
        'slides: ""',
        "---",
        p["summary"],
    ]) + "\n"


def news_md(n):
    return "\n".join([
        "---",
        'title: "%s"' % n["title"],
        'date: "%sT00:00:00Z"' % n["date"],
        'summary: "%s"' % n["summary"],
        "authors:",
        "- me",
        "tags:",
    ] + ["- %s" % t for t in n["tags"]] + [
        "featured: false",
        'projects: []',
        'slides: ""',
        "---",
        n["summary"],
        "",
        "课题组网站已完成基础搭建，后续的新闻动态、研究进展、成员介绍与招生信息都会在这里发布。",
    ]) + "\n"


def main():
    for p in PROJECTS:
        d = os.path.join("content/projects", p["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.md"), "w", encoding="utf-8") as f:
            f.write(project_md(p))
        print("project:", d)
    d = os.path.join("content/blog", NEWS["slug"])
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "index.md"), "w", encoding="utf-8") as f:
        f.write(news_md(NEWS))
    print("news:", d)


if __name__ == "__main__":
    main()
