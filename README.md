# xfg-skills-html2ppt

HTML PPT 演示文稿生成技能，专为课程教学、技术分享、视频录制设计。

## 特性

- 🎨 深蓝+金色科技风配色，专业质感
- 📐 16:9 宽屏布局，适配演讲和录屏
- 🎯 多章节结构，章节封面可独立作视频封面
- ⌨️ 键盘/点击/缩略图三种导航方式
- 💻 代码高亮、架构图、卡片网格等丰富组件
- 📦 单文件交付，零依赖打开

## 安装

```bash
# OpenClaw
cp -r xfg-skills-html2ppt ~/.qclaw/skills/

# Claude Code
cp -r xfg-skills-html2ppt ~/.claude/skills/
```

## 使用

向 AI Agent 描述你的课程/演讲内容，技能会自动：

1. 分析内容结构，规划页面
2. 使用模板生成完整 HTML PPT
3. 验证页码、缩略图、CSS 类一致性

示例对话：
```
帮我做一个 HTML PPT，主题是《Spring Boot 入门实战》，
分3节：1.环境搭建 2.REST API 3.数据持久化，
讲师小傅哥，官网 bugstack.cn
```

## 目录结构

```
xfg-skills-html2ppt/
├── SKILL.md              # 技能入口（必读）
├── README.md             # 项目说明
├── scripts/
│   └── validate.py       # HTML PPT 结构验证工具
├── references/
│   ├── specification.md  # CSS 类名和 API 速查
│   └── best-practices.md # 设计最佳实践
├── assets/
│   └── template.html     # 完整模板文件
└── evals/
    └── evals.json        # 评估用例
```

## 验证

```bash
python3 scripts/validate.py ./your-ppt.html
python3 scripts/validate.py ./your-ppt.html --strict
```

## License

Apache-2.0
