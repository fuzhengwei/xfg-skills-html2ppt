# HTML PPT 最佳实践

## 设计原则

1. **封面页克制留白**：封面是"大字报"不是"信息墙"，元素越少越高级
2. **右下角放讲师信息**：不抢封面视觉焦点，毛玻璃胶囊精致不突兀
3. **金色只做装饰**：金色用于分隔线、徽章边框、星号，绝不大面积使用
4. **内容页每页一个核心观点**：不要在一页里塞太多内容，宁可多分几页
5. **代码块配说明**：左栏代码 + 右栏说明，或代码块下方加 tip 框

## 常见错误

### ❌ 封面讲师信息居中
```html
<!-- 错误：居中放置 -->
<div class="cover-bottom-area" style="left:0; right:0; align-items:center;">
```

### ✅ 封面讲师信息右下角
```html
<!-- 正确：右下角放置 -->
<div class="cover-bottom-area">
  <!-- CSS 已设置 right: 36px; bottom: 44px -->
</div>
```

### ❌ 章节封面样式不生效
```css
/* 错误：.slide-cover 的 left:0 覆盖了章节封面的定位 */
.slide-chapter-cover .cover-bottom-area {
  right: 36px;
  /* 忘了加 left: auto !important */
}
```

### ✅ 使用 !important 覆盖
```css
.slide-chapter-cover .cover-bottom-area {
  left: auto !important;
  right: 36px;
  flex-direction: row !important;
}
```

### ❌ 页码硬编码
```html
<span>3 / 10</span>
<!-- 如果增删页面，需要手动更新所有页码 -->
```

### ✅ 生成时计算页码
生成 HTML 时动态计算总页数，确保所有 N / Total 一致。

## 视频优化技巧

1. **章节封面 = 视频封面**：每个章节封面独立使用，尺寸 16:9 适合 B 站
2. **大字号高对比**：录视频时字号要比现场演讲更大，确保小屏可读
3. **动画克制**：翻页用 0.35s fade 即可，不要花哨转场，录屏时容易翻车
4. **代码块字号 14px**：录 1080p 时 14px 代码刚好，12px 太小
5. **底部信息栏**：`bottom-accent` 文字不要太大，避免被 B 站播放器进度条遮挡

## 适配不同场景

### B 站视频（横屏 16:9）
- 默认设计即适配，无需调整
- 建议总页数 8-15 页，5-15 分钟视频

### 小红书（竖屏 3:4）
- 需要调整 `aspect-ratio: 3 / 4`
- 内容区改单栏，字号适当放大
- 缩略图导航隐藏

### 现场演讲
- 字号放大 120%
- 增加动画效果
- 缩略图导航可隐藏
