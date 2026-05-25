# HTML PPT 完整规范

## CSS 类名速查

### 布局类

| 类名 | 用途 |
|------|------|
| `.stage` | 主舞台容器，居中 16:9 |
| `.slide-card` | 每页幻灯片，absolute 定位 |
| `.slide-card.active` | 当前显示页 |
| `.slide-cover` | 封面页（总封面 + 章节封面） |
| `.slide-chapter-cover` | 章节封面（需同时加 .slide-cover） |
| `.slide-content` | 内容页 |

### 封面元素

| 类名 | 位置 | 说明 |
|------|------|------|
| `.top-accent` | absolute top | 金色装饰线 |
| `.bottom-accent` | absolute bottom | 页脚信息栏 |
| `.cover-bottom-area` | absolute bottom-right | 讲师信息胶囊 |
| `.course-badge` | 居中 | 课程/章节徽章 |
| `.proj-name` | 居中 | 项目名（84px） |
| `.proj-sub` | 居中 | 英文副标题 |
| `.sep-line` | 居中 | 金色分隔线 |
| `.chapter-title` | 居中 | 主标题 |
| `.chapter-num` | 居中 | 标签 |
| `.difficulty-stars` | 居中 | 难度星级 |
| `.chapter-icon` | 居中 | 章节图标 |
| `.chapter-main-title` | 居中 | 章节标题（48px） |
| `.chapter-sub-title` | 居中 | 英文章节名 |
| `.chapter-divider` | 居中 | 章节分隔线 |
| `.chapter-desc` | 居中 | 章节描述 |

### 内容页元素

| 类名 | 位置 | 说明 |
|------|------|------|
| `.slide-header` | 顶部 | 导航栏 |
| `.course-tag` | header 左 | 课程标签 |
| `.section-label` | header 中 | 章节标签 |
| `.avatar-img` | header 右 | 讲师头像 |
| `.slide-body` | 中间 | 内容区 |
| `.slide-footer` | 底部 | 页脚 |

### 组件

| 类名 | 说明 |
|------|------|
| `.steps` / `.step` / `.step-num` | 步骤流程 |
| `.cards` / `.card` / `.card-head` | 卡片网格 |
| `.two-col` / `.col-box` | 两栏布局 |
| `.code-block` | 代码块 |
| `.arch-diagram` / `.arch-row` / `.arch-box` | 架构图 |
| `.tip` / `.info` / `.warn` | 提示框 |
| `.hw-cards` / `.hw-card` | 作业卡片 |
| `.tag` / `.tag-grn` `.tag-blu` `.tag-gld` `.tag-red` `.tag-gry` | 标签 |
| `.hl` `.hl2` `.hl3` | 文字高亮 |

### 导航

| 类名 | 说明 |
|------|------|
| `.thumb-strip` | 缩略图导航栏 |
| `.thumb` | 缩略图 |
| `.thumb.active` | 当前页缩略图 |
| `.cover-thumb` | 封面页缩略图 |
| `.chapter-thumb` | 章节封面缩略图 |
| `.nav-arrows` / `.nav-arrow` | 左右箭头 |

## JS API

```javascript
showSlide(n)        // 跳转到第 n 页
changeSlide(dir)    // dir=1 下一页，dir=-1 上一页
```

## 尺寸规范

| 元素 | 尺寸 |
|------|------|
| 舞台 | 94vw, max-width 1200px, 16:9 |
| 封面项目名 | 84px / 900 |
| 章节标题 | 48px / 900 |
| 内容页 H2 | 34px / 700 |
| 正文 | 17px, line-height 1.8 |
| 代码块 | 14px, Menlo/JetBrains Mono |
| 讲师大头像 | 52px |
| 讲师小头像 | 46px |
| 缩略图 | 80×45px |
