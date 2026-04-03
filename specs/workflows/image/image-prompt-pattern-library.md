# 图片 Prompt 模式库

## 目标
给图片 workflow 提供一套可直接复用的 prompt 写法模式，帮助 `image-prompt-generator` 和 ChatGPT Pro 手动成图流程输出更稳定、可改、可复盘的图片提示词。

## 官方对齐原则
- 先有 `visual brief`，再写 prompt，不要倒过来。
- 先选方向，再套 prompt 结构，不要把 prompt 当 brief。
- 生成 prompt 默认按 `scene -> subject -> key details -> constraints` 顺序写。
- 复杂任务优先使用带标签或换行的 prompt，不要把所有要求挤成一段。
- 写实图优先用摄影语言和真实材质语言，不要只堆 `8k`、`ultra detailed`。
- 改图任务必须明确区分 `改什么` 和 `绝对不能变什么`。
- 图中文字必须写成精确文本，并附排版约束。
- 多图输入必须按 `Image 1 / Image 2 / Image 3` 明确角色分工。
- 二轮迭代优先做小步修改，不要每轮重写全部要求。
- negative prompt 优先压具体风险，不要只写泛泛的 `bad quality`。

## 通用生成 Prompt 结构

### 简版顺序
1. Scene / Background
2. Subject
3. Key details
4. Composition and use
5. Constraints

### 推荐骨架

```text
Scene / Background:
{{场景、环境、氛围}}

Subject:
{{主体是谁 / 是什么}}

Key details:
{{服装、材质、颜色、姿态、镜头、光线、风格、必须出现元素}}

Composition and use:
{{比例、留白、版式、用途}}

Constraints:
{{不要什么、必须保留什么、品牌或版权边界}}
```

## 通用改图 Prompt 结构

### 单图编辑骨架

```text
Change only:
{{只改什么}}

Keep exactly the same:
{{主体身份、构图、透视、背景、几何、品牌元素、文字}}

Target result:
{{改成什么效果}}

Constraints:
{{不要新增元素、不要改其他部分、输出比例或用途}}
```

### 多图参考编辑骨架

```text
Image 1:
{{主图，作为被编辑对象}}

Image 2:
{{风格参考 / 物件参考 / 角色参考}}

Image 3:
{{可选附加参考}}

Instruction:
{{把哪张图的什么应用到哪张图}}

Keep exactly the same:
{{主图中绝对不能变的内容}}

Constraints:
{{不要新增无关元素、不要改文字、不要改构图}}
```

## 常见主 Prompt 模式

### 1. 角色主视觉

正式子场景模板：
- [image-role-key-visual-template.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-role-key-visual-template.md)

适合：
- 动漫角色
- 原创人物
- IP 风格启发图

骨架：

```text
Scene / Background:
{{背景类型，通常克制}}

Subject:
single character key visual, {{角色身份和核心气质}}

Key details:
{{发型、服装、表情、姿态、道具、风格方向、光影}}

Composition and use:
{{海报 / 壁纸 / 封面，主体中心、轮廓清楚、留白位置}}

Constraints:
{{不要低幼、不要廉价游戏海报感、不要背景喧宾夺主}}
```

示例：

```text
Scene / Background:
restrained atmospheric background

Subject:
single character key visual, anime-inspired female warrior

Key details:
long dark hair, white and gold costume, calm confident expression, cinematic illustration style, dramatic rim light

Composition and use:
poster-ready composition with clean information space

Constraints:
no childish rendering, no cheap game poster feel, no cluttered background
```

### 2. 人物写真

适合：
- 海边写真
- 生活方式人像
- 杂志感主视觉

骨架：

```text
Scene / Background:
{{真实场景、时间段、环境状态}}

Subject:
full-body or half-body portrait of {{人物描述}}

Key details:
{{写真风格、镜头语言、光线、表情、姿态、服装、真实材质}}

Composition and use:
{{竖版或横版、主体位置、背景控制、用途}}

Constraints:
{{不要磨皮、不要影楼感、不要低俗感}}
```

示例：

```text
Scene / Background:
quiet seaside beach at golden hour

Subject:
full-body portrait of an adult Chinese woman

Key details:
realistic cinematic editorial photography style, warm natural sunlight, relaxed confident expression, natural skin texture, soft wind in hair

Composition and use:
clean seaside background, vertical wallpaper composition

Constraints:
no plastic skin, no cheap studio portrait feel, no cluttered background
```

### 3. 海报主视觉

适合：
- 活动海报
- 招生海报
- 品牌 KV

骨架：

```text
Scene / Background:
{{场景和品牌氛围}}

Subject:
{{主体}}

Key details:
{{风格关键词、品牌感、必须出现元素}}

Composition and use:
clear information area for headline and facts, {{比例和海报构图要求}}

Constraints:
{{不要廉价促销感、不要杂乱版式、不要文字错误}}
```

示例：

```text
Scene / Background:
bright English classroom with warm education atmosphere

Subject:
children in small-group interaction

Key details:
warm and trustworthy education branding, clean modern illustration

Composition and use:
clear information area for headline and deadline, poster-ready layout

Constraints:
no cheap promo flyer feel, no cluttered text area, no weak information hierarchy
```

### 4. 手机壁纸

适合：
- 单人角色图
- 单人写真人像
- 情绪氛围图

骨架：

```text
{{主体}}, {{竖版或横版说明}}, {{强主体}}, {{背景克制}}, {{高质感风格}}, suitable for smartphone wallpaper
```

示例：

```text
single cute electric creature, vertical composition, strong central focus, restrained atmospheric background, premium cinematic illustration, suitable for smartphone wallpaper
```

### 5. 社媒封面

适合：
- 小红书 / B站 / 视频封面
- 品牌栏目封面

骨架：

```text
{{主体}}, {{封面场景}}, {{风格}}, clean readable composition, leave clear space for title area, {{平台气质要求}}
```

### 6. 参考图编辑

适合：
- 修图
- 换背景
- 换材质
- 局部改造
- 多图合成

骨架：

```text
Change only:
{{只改什么}}

Keep exactly the same:
{{主体、透视、构图、文字、品牌元素}}

Target result:
{{目标效果}}

Constraints:
{{不要新增元素、不要结构漂移、输出用途}}
```

### 7. 图中文字海报

适合：
- 广告图
- billboard mockup
- 活动促销图
- 带主标题海报

骨架：

```text
Scene / Background:
{{场景}}

Subject:
{{主体}}

Key details:
{{品牌感、风格、主体细节}}

Exact text:
"{{逐字文本}}"

Typography:
{{字体风格、大小、颜色、位置}}

Composition and use:
{{标题区、副标题区、留白区}}

Constraints:
text must be verbatim, no extra characters, no duplicate text, no watermark
```

### 8. 参考图反推模板

正式子场景模板：
- [image-reference-to-template-template.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-reference-to-template-template.md)

适合：
- 给一张图反推出可复用模板
- 提炼“这一类图”的共性
- 给 ChatGPT Pro 生成相似方向

骨架：

```text
Scene / Background:
{{从参考图提炼的场景和氛围}}

Subject:
{{主体身份和核心类型}}

Key details:
{{光线、材质、姿态、配色、风格、必须保留特征}}

Composition and use:
{{构图、比例、留白、用途}}

Constraints:
{{不要跑偏的方向、不要新增的元素、版权和品牌边界}}
```

## Negative Prompt 写法模式

## 原则
- 压具体风险
- 压最容易跑偏的部分
- 和场景对应

### 1. 廉价感抑制

```text
cheap poster style, low-end flyer look, discount-store promotion feel, tacky composition
```

### 2. 卡通低幼抑制

```text
overly childish cartoon, toy-like rendering, plush toy appearance, low-end kids illustration
```

### 3. 背景杂乱抑制

```text
cluttered background, overdecorated scene, busy composition, noisy visual elements
```

### 4. 塑料质感抑制

```text
plastic skin, toy-like material, over-smoothed texture, fake glossy rendering
```

### 5. 游戏海报感抑制

```text
cheap mobile game splash art, exaggerated effects, overpowered aura, flashy combat poster style
```

### 6. 影楼 / 低端写真抑制

```text
cheap studio portrait style, plastic beauty retouching, tacky glamour pose, low-end catalog photo look
```

### 7. 文字错误抑制

```text
extra characters, duplicate text, incorrect spelling, illegible typography, weak text contrast
```

### 8. 编辑漂移抑制

```text
identity drift, structural drift, perspective distortion, background mismatch, artificial blending, added unrelated elements
```

## 二轮修改模板

### 模板 A：背景减法

```text
保留人物设定和整体配色不变。
请把背景再简洁一点，只保留氛围层次，不要增加装饰元素。
不要让背景抢主体。
```

### 模板 B：主体加强

```text
保留场景和光线不变。
请让主体更清楚、更有存在感，轮廓更明确，视觉中心更集中。
不要改变角色设定。
```

### 模板 C：高级感提升

```text
保留构图不变。
请提升整体高级感和材质感，减少廉价商业视觉感。
不要增加夸张特效，不要变得花哨。
```

### 模板 D：写真自然化

```text
保留人物设定和场景不变。
请让皮肤、表情和姿态更自然，减少磨皮和摆拍感。
不要做成影楼样片风。
```

### 模板 E：文字纠偏

```text
保留主体和配色不变。
请严格按原文显示图中文字，不要新增字符，不要重复，不要改拼写。
同时提升文字清晰度和对比度。
```

### 模板 F：编辑保真

```text
只调整 {{局部目标}}。
保留主体身份、透视、构图和原始背景不变。
不要新增无关元素，不要出现融合痕迹。
```

## ChatGPT Pro 手动成图推荐拼装

把方向整理给 ChatGPT 时，建议至少拼成下面这个结构：

```text
请生成一张图片。

用途：
{{用途}}

主 Prompt：
{{主 prompt}}

Negative Prompt：
{{negative prompt}}

必须保留：
{{必须保留的主体或事实}}

不要改变：
{{不能变的约束}}
```

## 官方来源
- OpenAI 官方总指南：`Image generation guide`
- OpenAI 官方提示词指南：`Gpt-image-1.5 Prompting Guide`
- OpenAI 官方示例：`Generate and edit images with GPT Image`

这些来源共同支持当前模式库的 4 个关键做法：
- 统一 prompt 顺序
- 明确 change vs preserve
- 精确控制 in-image text
- 采用小步迭代而不是一次过载

## 使用边界
- 本模式库用于补强 prompt 质量，不替代 brief。
- 不要直接照抄示例，优先按当前 brief 改写。
- 如果任务涉及版权角色或真人风格模仿，先把风险放进 `human-check items`。
