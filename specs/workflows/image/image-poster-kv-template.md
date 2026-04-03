# 海报主视觉子场景模板

## 目标
用于活动海报、招生海报、品牌 KV 以及需要明确标题区和信息区的视觉图。

## 适用场景
- 活动海报主视觉
- 品牌 KV
- 招生海报
- 促销图主视觉
- billboard 或 banner 概念图

## 不适用场景
- 纯情绪氛围图
- 没有任何标题区或信息区需求的壁纸图
- 只需要修一张现有海报图而不是生成方向

## 最少需要的信息
- 主体
- 受众
- 场景
- 品牌感
- 主标题或必须保留事实
- 是否需要图中文字
- 图中文字是否必须逐字正确
- 文字位置或标题区要求
- 版式比例

## 推荐补问模板
```text
按海报主视觉场景处理，现在还缺最少这几项：

画面主体：
目标受众：
使用场景：
想要的风格/品牌感：
主标题或必须保留事实：
是否需要图中文字：
文字位置或标题区要求：
版式比例：
```

## 官方对齐 Prompt 骨架
```text
Scene / Background:
{{场景和品牌氛围}}

Subject:
{{主体}}

Key details:
{{品牌感、风格关键词、必须出现元素}}

Exact text:
"{{逐字文本，若无则留空}}"

Typography:
{{字体风格、大小、颜色、位置，若无则留空}}

Composition and use:
clear information area for headline and facts, poster-ready layout, suitable for {{比例}}

Constraints:
text must be verbatim, no extra characters, no duplicate text, no watermark, no cheap promo flyer feel
```

## Negative Prompt 片段
```text
cheap promo poster, tacky flyer look, cluttered text area, busy composition, overdecorated background, weak information hierarchy, incorrect text, duplicate text, illegible typography
```

## 二轮修改模板
```text
保留主体和配色不变。
请增加清楚的标题区和留白区，让画面更像可落地的海报主视觉。
不要把背景做得过满，也不要破坏文字可读性。
```

## 使用建议
- 如果标题和卖点必须严格正确，先生成纯 KV，再单独做图中文字版会更稳。
- 如果第一轮就直接带文字，必须给出逐字文本和排版约束。
- 对品牌名、生僻词、英文词，必要时按字母逐个拼写，减少错字。

## 审校重点
- 是否有足够留白
- 必保留事实是否可上版
- 图中文字是否逐字正确
- 文字对比度和层级是否足够
- 是否偏概念图而不是可用海报

## 待确认项
- 是否需要 logo
- 是否需要副标题
- 图中文字是否必须首轮完成
- 是否允许后续单独补字
- 最终比例是否锁定
