#!/usr/bin/env python3
"""
HTML PPT 生成辅助脚本
- 验证 HTML PPT 文件的结构完整性
- 检查页码、缩略图、CSS 类是否匹配
"""

import sys
import re
import argparse


def validate(filepath: str) -> list:
    """验证 HTML PPT 文件，返回问题列表"""
    issues = []

    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        return [f"文件不存在: {filepath}"]
    except UnicodeDecodeError:
        return [f"文件编码错误，期望 UTF-8: {filepath}"]

    # 1. 检查 slide-card 数量
    slide_cards = re.findall(r'class="slide-card[^"]*"', content)
    num_slides = len(slide_cards)

    if num_slides == 0:
        issues.append("未找到任何 slide-card 页面")
        return issues

    print(f"✅ 找到 {num_slides} 页幻灯片")

    # 2. 检查总封面
    has_main_cover = bool(re.search(r'class="slide-card slide-cover(?:\s+active)?(?!\s+slide-chapter-cover)"', content))
    if not has_main_cover:
        issues.append("缺少总封面页 (slide-cover without slide-chapter-cover)")
    else:
        print("✅ 总封面页存在")

    # 3. 检查章节封面
    chapter_covers = re.findall(r'class="slide-card slide-cover slide-chapter-cover"', content)
    print(f"✅ 找到 {len(chapter_covers)} 个章节封面")

    # 4. 检查页码一致性
    page_numbers = re.findall(r'<span>\d+\s*/\s*(\d+)</span>', content)
    if page_numbers:
        max_total = max(int(n) for n in page_numbers)
        if max_total != num_slides:
            issues.append(f"页码总数 {max_total} 与实际页数 {num_slides} 不一致")
        else:
            print(f"✅ 页码总数一致: {num_slides}")

    # 5. 检查缩略图数量
    thumbs = re.findall(r'<div class="thumb[^>]*onclick', content)
    if len(thumbs) != num_slides:
        issues.append(f"缩略图数量 {len(thumbs)} 与页数 {num_slides} 不一致")
    else:
        print(f"✅ 缩略图数量一致: {num_slides}")

    # 6. 检查必需的封面元素
    for element in ["top-accent", "bottom-accent", "cover-bottom-area"]:
        if element not in content:
            issues.append(f"缺少封面元素: {element}")

    # 7. 检查 JS total 变量
    total_match = re.search(r'const total\s*=\s*(\d+)', content)
    if total_match:
        js_total = int(total_match.group(1))
        if js_total != num_slides:
            issues.append(f"JS total 变量 {js_total} 与实际页数 {num_slides} 不一致")
        else:
            print(f"✅ JS total 变量一致: {num_slides}")

    # 8. 检查 active 页
    active_slides = re.findall(r'slide-card[^"]* active', content)
    if len(active_slides) == 0:
        issues.append("没有设置 active 的初始页面")
    elif len(active_slides) > 1:
        issues.append(f"有 {len(active_slides)} 个 active 页面，应该只有 1 个")

    # 9. 检查 aspect-ratio
    if "aspect-ratio" not in content and "16 / 9" not in content and "16/9" not in content:
        issues.append("未找到 16:9 宽高比设置")

    return issues


def main():
    parser = argparse.ArgumentParser(description="HTML PPT 验证工具")
    parser.add_argument("filepath", help="HTML PPT 文件路径")
    parser.add_argument("--strict", action="store_true", help="严格模式，有警告也返回非零退出码")
    args = parser.parse_args()

    print(f"🔍 验证 HTML PPT: {args.filepath}\n")

    issues = validate(args.filepath)

    print()
    if issues:
        print("❌ 发现问题:")
        for i, issue in enumerate(issues, 1):
            print(f"  {i}. {issue}")
        if args.strict:
            sys.exit(1)
    else:
        print("🎉 验证通过！HTML PPT 结构完整。")


if __name__ == "__main__":
    main()
