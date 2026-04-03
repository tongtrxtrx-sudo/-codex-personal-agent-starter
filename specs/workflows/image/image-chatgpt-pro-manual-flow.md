# ChatGPT Pro 手动成图流程

## 目标
在没有 OpenAI API key、只有 ChatGPT Pro 订阅的情况下，让仓库里的图片 workflow 仍然能稳定产出可执行的成图材料。

## 适用场景
- 当前只有 ChatGPT Pro
- 想先用仓库整理方向，再去 ChatGPT 手动出图
- 暂时不接 API，但希望流程清楚、可复盘

## 核心思路
仓库里的图片 workflow 负责：
1. 视觉 brief
2. 3 个视觉方向
3. 品牌审校
4. 待确认项

ChatGPT Pro 负责：
1. 接收已选定方向的 prompt
2. 进行手动出图
3. 如有需要，再做 1 到 2 轮手动改图

## 推荐流程

### Step 1：在仓库里跑图片 workflow
拿到：
- `visual brief`
- `prompt directions`
- `brand review`
- `human-check items`

### Step 2：人工选定一个方向
优先选：
- 最符合受众
- 最符合品牌感
- 最适合承载标题和事实信息

### Step 3：整理成 ChatGPT 可直接使用的成图输入
至少保留：
- 方向名
- 主 prompt
- negative prompt
- 标题和必须保留事实
- 需要保留的风格限制

整理前建议先看：
- [image-prompt-pattern-library.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-prompt-pattern-library.md)

## 推荐交给 ChatGPT 的输入结构

```text
请按下面这个方向生成一张图片：

用途：
海报 / 封面 / 主视觉

方向名：
{{direction_name}}

主 prompt：
{{prompt}}

负向限制：
{{negative_prompt}}

必须保留的文字信息：
{{headline}}
{{facts_to_keep}}

不要改变的约束：
{{must_keep_constraints}}
```

## 更适合复制的最终交付卡片

如果你只是想快速复制给 ChatGPT，优先给下面这 3 段，不要把所有中间分析都贴进去：

```text
主 Prompt：
{{main_prompt}}

Negative Prompt：
{{negative_prompt}}

二轮微调 Prompt：
{{iteration_prompt}}
```

如果是带图中文字的海报，再补：

```text
图中文字：
"{{exact_text}}"

排版要求：
{{typography_and_layout_constraints}}
```

如果是改图，再补：

```text
只改：
{{change_only}}

保持不变：
{{keep_exactly_the_same}}
```

## 第二轮修改建议
如果第一轮图不满意，不要只说“重来一张”。
优先这样改：
- 保留不变的部分
- 只指出需要调整的地方
- 明确不要动的约束

可直接复用的改图模板见：
- [image-prompt-pattern-library.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-prompt-pattern-library.md)

例如：

```text
保留整体风格和配色不变。
请把人物表情改得更自然一些，留白区再大一点，文字信息区更清楚。
不要增加装饰元素，不要变成卡通风。
```

## 最低复盘记录
即使是手动出图，也建议在仓库里记录：
- 选定方向
- 最终交给 ChatGPT 的 prompt
- 最终交给 ChatGPT 的 negative prompt
- 主要改图指令
- 选中的结果截图或文件路径
- 为什么采用这张图

## 适合当前仓库的原因
- 不依赖 API key
- 适合当前已有 ChatGPT Pro 订阅
- 先把 workflow 跑顺，再决定要不要接自动执行层
