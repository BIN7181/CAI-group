#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""生成课题组代表性论文页面（内容严格按蔡亮老师简历截图）"""
import os

PUB_DIR = "content/publications"

PAPERS = [
    dict(
        slug="2025-ru-modified-manganese-oxybromide",
        title="Regulating the Oxygen Evolution Mechanism through In Situ Reconstruction of Ru-Modified Manganese Oxybromide",
        authors=["Ci Lin", "Tsung-Yi Chen", "Tao Zhou", "Yingqiang Wu", "Ching Kit Tommy Wun",
                 "Weicheng Chen", "Han-Yi Chen", "Vincent Tung", "Zhengxiao Guo",
                 "Tsz Woon Benedict Lo", "me", "Yida Deng", "Philip C Y Chow"],
        date="2025-10-01",
        journal="ACS Energy Letters",
        volume="10",
        pages="2641-2649",
        tags=["AEMWE", "酸性析氧", "原位重构", "Ru"],
    ),
    dict(
        slug="2025-iridates-for-pem-water-electrolysis",
        title="Iridates for PEM water electrolysis",
        authors=["Chen Gong", "Renjie Zhang", "Hengyu Guo", "Yuening Yan", "Ci Lin", "me"],
        date="2025-05-01",
        journal="Applied Catalysis O: Open",
        volume="201",
        pages="207035",
        note="Invited review article",
        tags=["PEM电解水", "铱基催化剂", "综述"],
    ),
    dict(
        slug="2022-ca2-xir o4-stable-water-oxidation-intermediates".replace(" ", ""),
        title="Operando direct observation of stable water-oxidation intermediates on Ca2-xIrO4 nanocrystals for efficient acidic oxygen evolution",
        authors=["Na Li", "me", "Guoping Gao", "Yue Lin", "Chao Wang", "Hengjie Liu", "Yuying Liu",
                 "Hengli Duan", "Qianqian Ji", "Wei Hu", "Hao Tan", "Zeming Qi", "Lin-Wang Wang",
                 "Wensheng Yan"],
        date="2022-09-01",
        journal="Nano Letters",
        volume="22",
        pages="6988-6996",
        tags=["酸性析氧", "operando", "XAFS", "Ca2-xIrO4"],
    ),
    dict(
        slug="2022-dual-active-sites-ca2iro4-yttrium",
        title="Operando Identification of Dual Active Sites in Ca2IrO4 Nanocrystals with Yttrium Substitutions Boosting Acidic Oxygen Evolution Reaction",
        authors=["Yuying Liu", "me", "Qianqian Ji", "Chao Wang", "Ziyi Liu", "Liyang Lv", "Bing Tang",
                 "Hengli Duan", "Fengchun Hu", "Na Li", "Zhihu Sun", "Wensheng Yan"],
        date="2022-07-01",
        journal="ACS Energy Letters",
        volume="7",
        pages="3798-3806",
        tags=["酸性析氧", "双活性位点", "Y掺杂"],
    ),
    dict(
        slug="2022-surface-amorphization-ca2-xir o4".replace(" ", ""),
        title="Origin of Surface Amorphization and Catalytic Stability of Ca2-xIrO4 Nanocrystals for Acidic Oxygen Evolution: Critical Roles of Acid Anions",
        authors=["Na Li", "me", "Guoping Gao", "Yuying Liu", "Chao Wang", "Ziyi Liu", "Qianqian Ji",
                 "Hengli Duan", "Lin-Wang Wang", "Wensheng Yan"],
        date="2022-11-01",
        journal="ACS Catalysis",
        volume="12",
        pages="13475-13481",
        tags=["酸性析氧", "表面非晶化", "稳定性"],
    ),
    dict(
        slug="2022-fe3o4-sulfide-interface-alkaline-oer",
        title="Operando Identification of Active Species and Intermediates on Sulfide Interfaced by Fe3O4 for Ultrastable Alkaline Oxygen Evolution at Large Current Density",
        authors=["Qianqian Ji", "Yuan Kong", "Hao Tan", "Hengli Duan", "Na Li", "Bing Tang",
                 "Yao Wang", "Sihua Feng", "Liyang Lv", "Chao Wang", "Fengchun Hu",
                 "Wenhua Zhang", "me", "Wensheng Yan"],
        date="2022-05-01",
        journal="ACS Catalysis",
        volume="12",
        pages="4318-4326",
        note="ESI 高被引论文（引用 > 100 次）",
        tags=["碱性析氧", "大电流密度", "界面催化", "ESI高被引"],
    ),
    dict(
        slug="2022-room-temperature-ferromagnetism-tmdc",
        title="Room-temperature ferromagnetism in two-dimensional transition metal chalcogenides: strategies and origin",
        authors=["me", "Vincent Tung", "Andrew Wee"],
        date="2022-03-01",
        journal="Journal of Alloys and Compounds",
        volume="913",
        pages="165289",
        note="Invited review article",
        tags=["二维材料", "铁磁性", "综述"],
    ),
    dict(
        slug="2022-band-gap-tmdc-nanoribbons",
        title="Direct Band Gap in Multilayer Transition Metal Dichalcogenide Nanoribbons with Enhanced Photoluminescence",
        authors=["Ci Lin", "me", "Jui-Han Fu", "Shahid Sattar", "Qingxiao Wang", "Yi Wan",
                 "Chien-Chih Tseng", "Chih-Wen Yang", "Areej Aljarb", "Ke Jiang",
                 "Kuo-Wei Huang", "Lain-Jong Li", "Carlo Maria Canali", "Yumeng Shi", "Vincent Tung"],
        date="2022-04-01",
        journal="ACS Materials Letters",
        volume="4",
        pages="1547-1555",
        tags=["二维材料", "能带工程", "光致发光"],
    ),
]


def build(paper):
    lines = ["---"]
    lines.append('title: "%s"' % paper["title"].replace('"', "'"))
    lines.append("authors:")
    for a in paper["authors"]:
        lines.append("- %s" % a)
    lines.append('date: "%sT00:00:00Z"' % paper["date"])
    lines.append('publishDate: "%sT00:00:00Z"' % paper["date"])
    lines.append('publication_types: ["article-journal"]')
    lines.append("publication:")
    lines.append('  name: "%s"' % paper["journal"])
    lines.append('  volume: "%s"' % paper["volume"])
    lines.append('  pages: "%s"' % paper["pages"])
    lines.append("peer_reviewed: true")
    lines.append("featured: true")
    lines.append("tags:")
    for t in paper["tags"]:
        lines.append("- %s" % t)
    if paper.get("note"):
        lines.append('note: "%s"' % paper["note"])
    lines.append("projects: []")
    lines.append('slides: ""')
    lines.append("---")
    body = []
    if paper.get("note"):
        body.append("> %s" % paper["note"])
    body.append("%s, %s, %s, %s." % (paper["journal"], paper["date"][:4], paper["volume"], paper["pages"]))
    lines.append("\n".join(body))
    return "\n".join(lines) + "\n"


def main():
    for p in PAPERS:
        d = os.path.join(PUB_DIR, p["slug"])
        os.makedirs(d, exist_ok=True)
        with open(os.path.join(d, "index.md"), "w", encoding="utf-8") as f:
            f.write(build(p))
        print("wrote", d)


if __name__ == "__main__":
    main()
