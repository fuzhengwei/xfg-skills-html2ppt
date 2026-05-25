---
name: xfg-skills-html2ppt
description: |
  HTML PPT 演示文稿生成技能。当用户需要制作 HTML 格式的 PPT、幻灯片、演示文稿、
  课件、演讲稿、课程页面时使用此技能。特别适合：课程教学、技术分享、视频录制（B站/小红书）、
  会议演讲等场景。生成的 HTML PPT 支持：键盘/点击翻页、缩略图导航、深色科技风封面、
  多章节结构、响应式布局、代码高亮、架构图等。
license: Apache-2.0
compatibility: 需要现代浏览器（Chrome/Firefox/Safari），支持 CSS3 + ES6
metadata:
  author: xfg-studio
  version: "1.0.0"
  category: presentation
  homepage: https://github.com/xfg-skills/xfg-skills-html2ppt
---

# HTML PPT 演示文稿生成

将用户内容转化为精美的 HTML 演示文稿，适合演讲、录视频、发 B 站和小红书。

## 核心设计理念

1. **单文件交付**：一个 HTML 文件包含所有样式和脚本，零依赖即可打开
2. **16:9 舞台**：aspect-ratio: 16/9，深色背景上的白色卡片，影院感
3. **深蓝+金色配色**：封面页深蓝渐变 + 金色装饰线，专业且有质感
4. **多章节结构**：总封面 → 课程大纲 → 章节封面 → 内容页 → 总结，层次清晰
5. **视频友好**：每个章节封面可作为独立视频封面使用

## 页面类型与结构

### 页面类型一览

| 类型 | CSS 类 | 用途 |
|------|--------|------|
| 总封面 | `.slide-cover` | 课程首屏，项目名 + 副标题 + 讲师 |
| 课程大纲 | `.slide-content` | 列出所有章节，步骤流展示 |
| 章节封面 | `.slide-cover .slide-chapter-cover` | 每节独立封面，可作视频封面 |
| 内容页 | `.slide-content` | 正文、卡片、代码、架构图 |
| 总结页 | `.slide-content` | 课程总结 + 作业 + 链接 |

### 必需页面结构

```
第1页：总封面（slide-cover）
第2页：课程大纲（slide-content）
第3页：章节1封面（slide-chapter-cover）
第4~N页：章节1内容（slide-content）
第N+1页：章节2封面（slide-chapter-cover）
...
最后一页：总结（slide-content）
```

## 设计规范

### 配色系统（CSS 变量）

```css
:root {
  --blue: #1a3a5c;        /* 主色 - 深蓝 */
  --blue-dark: #0d2137;   /* 封面背景深色端 */
  --blue-light: #285680;  /* 辅助蓝 */
  --gold: #c8960c;        /* 金色装饰 */
  --gold-light: #e8b730;  /* 金色高亮 */
  --red: #c0392b;         /* 警告/强调 */
  --text: #1a1c23;        /* 正文黑 */
  --text-dim: #6b7280;    /* 次要文字 */
  --gray-50: #f8f9fa;     /* 卡片背景 */
  --gray-200: #e0e2e6;    /* 边框 */
}
```

### 封面页设计

**总封面**包含（从上到下）：
1. 顶部金色装饰线（`.top-accent`，5px 高）
2. 课程徽章（`.course-badge`）：金色边框胶囊，如"AI Shell 智能终端 · 系列课程"
3. 项目名（`.proj-name`）：84px/900 超大字
4. 英文副标题（`.proj-sub`）：20px/300，字母间距 10px
5. 金色分隔线（`.sep-line`）：80px 宽
6. 章节标题（`.chapter-title`）：44px/700
7. 标签（`.chapter-num`）：22px 金色
8. 难度星级（`.difficulty-stars`）：金色星号
9. 右下角讲师信息（`.cover-bottom-area`）：毛玻璃胶囊卡片，头像+讲师名+官网
10. 底部信息栏（`.bottom-accent`）：30px 高半透明条

**章节封面**额外包含：
- `.cover-course-info`：左上角课程品牌信息（毛玻璃卡片）
- `.course-badge`：显示"第 N 节"
- `.chapter-icon`：64px emoji 图标
- `.chapter-main-title`：48px/900 大标题
- `.chapter-sub-title`：20px 英文章节名，字母间距
- `.chapter-divider`：100px 金色分隔线
- `.chapter-desc`：17px 描述文字

### 左上角课程品牌信息

章节封面左上角展示主课程信息，让观众始终知道当前属于哪个课程：

```css
.cover-course-info {
  position: absolute;
  top: 22px;
  left: 28px;
  display: flex;
  align-items: center;
  gap: 12px;
  background: rgba(0,0,0,0.2);
  backdrop-filter: blur(8px);
  padding: 10px 20px 10px 14px;
  border-radius: 8px;
  border: 1px solid rgba(255,255,255,0.06);
}
```

HTML 结构：
```html
<div class="cover-course-info">
  <div class="course-logo">W</div>
  <div class="course-text">
    <div class="course-main">WaLiCode</div>
    <div class="course-sub">AI Shell 手把手操作云服务器</div>
  </div>
</div>
```

设计要点：
- **毛玻璃卡片**：与右下角讲师信息统一风格
- **Logo 渐变填充**：金色渐变方块（`linear-gradient(135deg, gold, gold-light)`），深色字
- **两行文字**：上行课程名（15px/700 白色 90%），下行课程副标题（11px 白色 35%）
- **左上角 + 右下角呼应**：两个毛玻璃卡片对角布局，视觉平衡

### 右下角讲师信息

采用毛玻璃胶囊设计，所有封面页通用：

```css
.cover-bottom-area {
  position: absolute;
  bottom: 44px;
  right: 36px;
  display: flex;
  align-items: center;
  gap: 14px;
  background: rgba(0,0,0,0.25);
  backdrop-filter: blur(8px);
  padding: 12px 18px 12px 22px;
  border-radius: 40px;
  border: 1px solid rgba(255,255,255,0.08);
}
```

HTML 结构：
```html
<div class="cover-bottom-area">
  <div class="author-info">
    <div class="author-name">讲师：小傅哥</div>
    <div class="author-site">walicode.xiaofuge.cn</div>
  </div>
  <img class="avatar-cover" src="头像URL" alt="讲师名">
</div>
```

### 内容页设计

**顶部导航栏**（`.slide-header`）：
- 左：课程标签（`.course-tag`），蓝色方块图标 + 文字
- 中：章节标签（`.section-label`），金色高亮节号
- 右：讲师小头像（`.avatar-img`，46px 圆形）

**内容区**（`.slide-body`）：
- H2 标题：34px/700 深蓝 + 底部 3px 金色边框
- 正文：17px，行高 1.8
- 列表项：`▸` 金色三角标记

**底部栏**（`.slide-footer`）：
- 左：课程名称，右：页码

## 组件库

### 步骤流程（.steps）

适合展示操作步骤、课程大纲：

```html
<div class="steps">
  <div class="step">
    <div class="step-num">1</div>
    <div class="step-content">
      <h4>步骤标题</h4>
      <p>步骤描述</p>
    </div>
  </div>
</div>
```

### 卡片网格（.cards）

适合并列展示特性、功能：

```html
<div class="cards">
  <div class="card">
    <div class="card-head">
      <span class="card-icon">🚀</span>
      <h4>卡片标题</h4>
    </div>
    <p>卡片描述</p>
    <div class="card-tags">
      <span class="tag tag-grn">标签1</span>
      <span class="tag tag-blu">标签2</span>
    </div>
  </div>
</div>
```

标签颜色：`.tag-grn`（绿）、`.tag-blu`（蓝）、`.tag-gld`（金）、`.tag-red`（红）、`.tag-gry`（灰）

### 两栏布局（.two-col）

适合对比、代码+说明：

```html
<div class="two-col">
  <div class="col-box">
    <h4>左栏标题</h4>
    <ul>...</ul>
  </div>
  <div class="col-box">
    <h4>右栏标题</h4>
    <div class="code-block">...</div>
  </div>
</div>
```

### 代码块（.code-block）

深色背景代码展示，支持语法着色：

```html
<div class="code-block">
  <span class="comment"># 注释</span>
  <span class="cmd">命令</span> 参数
  <span class="str">字符串值</span>
</div>
```

- `.cmd`：蓝色命令
- `.comment`：灰色注释
- `.str`：绿色字符串

### 架构图（.arch-diagram）

流程图/架构图：

```html
<div class="arch-diagram">
  <div class="arch-row">
    <div class="arch-box af">🖥️ 终端</div>
  </div>
  <div class="arch-arrow">↓ 说明</div>
  <div class="arch-row">
    <div class="arch-box ab">🧠 AI</div>
  </div>
</div>
```

盒子样式：`.af`（蓝）、`.ab`（金）、`.at`（绿）

### 提示框

```html
<div class="tip"><p>💡 提示信息</p></div>
<div class="info"><p>📌 信息说明</p></div>
<div class="warn"><p>⚠️ 警告信息</p></div>
```

### 作业卡片（.hw-cards）

```html
<div class="hw-cards">
  <div class="hw-card">
    <div class="lvl ez">⭐ 简单作业</div>
    <h4>作业标题</h4>
    <p>作业描述</p>
  </div>
  <div class="hw-card">
    <div class="lvl hd">⭐⭐ 进阶作业</div>
    <h4>作业标题</h4>
    <p>作业描述</p>
  </div>
</div>
```

### 文字高亮

- `.hl`：红色强调（危险/重要）
- `.hl2`：蓝色强调（技术名词）
- `.hl3`：绿色强调（成功/推荐）

## 交互功能

### 键盘导航

- `←` / `↑`：上一页
- `→` / `↓` / `空格`：下一页
- `Home`：第一页
- `End`：最后一页

### 点击翻页

- 点击幻灯片左 30% 区域：上一页
- 点击右 30% 区域：下一页

### 缩略图导航

底部浮动缩略图条：
- 深色毛玻璃背景
- 每页缩略图 80×45px
- 封面页蓝色渐变底，内容页灰色底
- 当前页金色边框高亮
- 点击跳转，自动滚动到可见区域

### 左右箭头

屏幕两侧固定箭头按钮，hover 时蓝色+金色边框

## 生成流程

### 第 1 步：分析内容

从用户输入中提取：
- 课程/项目名
- 章节结构（每节标题 + 内容要点）
- 讲师信息（姓名、头像 URL、官网）
- 难度等级

### 第 2 步：规划页面

按页面类型分配：
1. 总封面（1 页）
2. 课程大纲（1 页）
3. 每个章节：封面（1 页）+ 内容（1-3 页）
4. 总结（1 页）

### 第 3 步：生成 HTML

使用 `assets/template.html` 作为基础模板，替换内容区域。

关键替换点：
- `<title>` 标签
- `.proj-name` 项目名
- `.chapter-title` 标题
- 课程徽章文字
- 章节封面内容
- 内容页正文
- 缩略图标签
- 页码（N / Total）
- 讲师信息

### 第 4 步：写入文件

使用 `scripts/generate.py` 脚本写入 HTML 文件，确保 UTF-8 编码、正确换行符。

## Gotchas

1. **封面页讲师信息必须在右下角**：`.cover-bottom-area` 使用 `position: absolute; right: 36px; bottom: 44px;`，不要居中放置
2. **章节封面左上角课程品牌信息**：`.cover-course-info` 使用毛玻璃卡片（`background: rgba(0,0,0,0.2); backdrop-filter: blur(8px)`），与右下角讲师信息对角呼应
3. **章节封面继承总封面样式**：`.slide-chapter-cover` 需要用 `!important` 覆盖 `.slide-cover` 的某些属性（如 `left: auto !important`、`flex-direction: row !important`）
4. **页码必须准确**：每页的 `N / Total` 必须与实际页数一致，缩略图数量也要匹配
5. **aspect-ratio: 16/9**：舞台和每张幻灯片卡片都保持 16:9
6. **单个 HTML 文件**：所有 CSS 和 JS 内联，不引用外部文件（Google Fonts 除外）
7. **缩略图导航**：`.thumb-strip` 固定在底部，z-index: 200，不遮挡内容
8. **代码块字体**：使用 JetBrains Mono / Menlo 等等宽字体
9. **中文排版**：使用 Noto Sans SC 字体，行高不低于 1.6
10. **金色装饰线位置**：封面 `.top-accent` 在最顶部，`.bottom-accent` 在最底部，都是 absolute 定位
11. **底部信息栏和讲师区域不重叠**：`.bottom-accent` 高 30px 在最底，`.cover-bottom-area` bottom: 44px 在上方
12. **Logo 渐变优于边框**：`.course-logo` 使用 `linear-gradient(135deg, gold, gold-light)` 填充 + 深色字，比半透明背景+金色边框更有品牌质感
