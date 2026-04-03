# 图片 Prompt 模式库

## 目标
给图片 workflow 提供一套可直接复用的 prompt 写法模式，帮助 `image-prompt-generator` 和 ChatGPT Pro 手动成图流程输出更稳定、可改、可复盘的图片提示词。

## 使用原则
- 先有 `visual brief`，再用本模式库，不要倒过来。
- 先选方向，再套 prompt 结构，不要把 prompt 当 brief。
- prompt 负责执行，brief 负责约束。
- negative prompt 优先压具体风险，不要只写泛泛的 “bad quality”。

## 主 Prompt 推荐结构

默认顺序：
1. 主体
2. 场景
3. 风格
4. 光线 / 氛围 / 色彩
5. 构图 / 留白 / 用途
6. 质量和边界约束

推荐骨架：

```text
{{主体}}, in {{场景}}, {{风格}}, {{光线或氛围}}, {{色彩方向}}, {{构图要求}}, {{用途要求}}, {{质量边界}}
```

## 改图 Prompt 推荐结构

当第一轮图已经接近可用时，优先这样改：

```text
保留 {{不要变的部分}} 不变。
请把 {{需要调整的部分}} 改成 {{目标效果}}。
不要出现 {{明确禁止项}}。
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
single character key visual, {{角色描述}}, {{服装和特征}}, {{表情和姿态}}, {{风格方向}}, {{光影氛围}}, {{背景控制}}, {{构图用途}}
```

示例：

```text
single character key visual, anime-inspired female warrior, long dark hair, white and gold costume, calm confident expression, cinematic illustration style, dramatic rim light, restrained background, poster-ready composition with clean information space
```

### 2. 人物写真

适合：
- 海边写真
- 生活方式人像
- 杂志感主视觉

骨架：

```text
full-body portrait of {{人物描述}}, in {{真实场景}}, {{写真风格}}, {{自然光或电影光}}, {{人物气质}}, {{背景复杂度控制}}, {{构图用途}}
```

示例：

```text
full-body portrait of an adult Chinese woman on a beach, realistic cinematic editorial photography style, warm natural sunlight, relaxed confident expression, clean seaside background, vertical wallpaper composition
```

### 3. 海报主视觉

适合：
- 活动海报
- 招生海报
- 品牌 KV

骨架：

```text
{{主体}}, {{场景}}, {{品牌感}}, {{风格关键词}}, {{必须出现元素}}, clear information area for headline and facts, {{海报构图要求}}
```

示例：

```text
children in a bright English classroom, small-group interaction, warm and trustworthy education branding, clean modern illustration, clear information area for headline and deadline, poster-ready layout
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

## 使用边界
- 本模式库用于补强 prompt 质量，不替代 brief。
- 不要直接照抄示例，优先按当前 brief 改写。
- 如果任务涉及版权角色或真人风格模仿，先把风险放进 `human-check items`。
