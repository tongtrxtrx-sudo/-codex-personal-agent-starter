# 角色主视觉子场景模板

## 目标
给 `role_key_visual` 子场景提供一套正式模板，支持：
- 动漫角色图
- IP 风格启发图
- Q版角色图
- 角色海报主视觉
- 角色壁纸 / 封面图

让图片 workflow 在处理角色类需求时，先把角色设定和视觉边界说清楚，再生成 2 到 3 个稳定可选方向。

## 来源类别
- `10_卡通漫画电影角色`
- `12_手工玩具手办`

## 适用场景
- 单人角色主视觉
- 双人角色对视或对战
- Q版角色海报
- 动漫 / 游戏风格启发图
- 高质感角色壁纸

## 不适用场景
- 已有完整角色设定文档和官方品牌规范，只需要执行绘制
- 需要故事分镜、九宫格关键帧或多镜头叙事
- 只是对现成角色图做局部修图

## 最少需要拿到的信息
- 角色主体
- 目标受众
- 使用场景
- 风格或品牌感
- 必须出现元素
- 不希望出现元素

## 推荐补问模板

```text
按角色主视觉场景处理，现在还缺最少这几项，我补齐后就直接给你 visual brief 和方向稿：

角色主体：
目标受众：
使用场景：
想要的风格/品牌感：
必须出现元素：
不希望出现元素：
```

## 角色描述骨架

### 角色基础层
- 角色身份：原创 / 启发式 / 已知角色
- 年龄感：儿童 / 少年 / 青年 / 成年
- 性别表达：男 / 女 / 中性 / 不强调
- 气质：冷感 / 热血 / 可爱 / 王者 / 神秘 / 治愈

### 角色外观层
- 发型
- 服装
- 面部特征
- 表情
- 姿态
- 标志性道具

### 画面控制层
- 构图：全身 / 半身 / 特写
- 比例：横版 / 竖版 / 1:1
- 背景复杂度：极简 / 氛围背景 / 环境背景
- 光线：自然光 / 电影光 / 边缘光 / 戏剧光

## 官方对齐 Prompt 结构

```text
Scene / Background:
{{背景类型和氛围，通常克制}}

Subject:
single character or dual character key visual, {{角色身份和核心气质}}

Key details:
{{发型、服装、表情、姿态、道具、风格方向、材质、光影}}

Composition and use:
{{海报 / 壁纸 / 封面，主体位置、留白、比例}}

Constraints:
{{不要低幼、不要廉价游戏海报感、不要背景喧宾夺主、若已有角色则保持一致}}
```

## 默认方向结构

### 方向 A：主角压场感
适合：
- 海报主视觉
- 封面图
- 高完成度单人角色图

重点：
- 主体轮廓强
- 角色是唯一视觉中心
- 背景克制
- 更强调“海报感”和“主角感”

Prompt 骨架：

```text
Scene / Background:
restrained background

Subject:
single character key visual, {{角色描述}}

Key details:
{{服装和特征}}, {{表情和姿态}}, {{风格方向}}, {{光影氛围}}

Composition and use:
poster-ready composition with strong silhouette and clear focal center

Constraints:
no cheap game poster feel, no childish rendering, no cluttered background
```

### 方向 B：情绪壁纸感
适合：
- 手机壁纸
- 情绪氛围角色图
- 轻传播图

重点：
- 角色气质和氛围感
- 背景有层次但不喧宾夺主
- 更强调“可看性”和“陪伴感”

Prompt 骨架：

```text
Scene / Background:
atmospheric background

Subject:
single character illustration, {{角色描述}}

Key details:
{{气质和表情}}, {{风格方向}}, premium cinematic mood

Composition and use:
clean composition, suitable for smartphone wallpaper

Constraints:
no weak subject focus, no noisy effects, no cheap rendering
```

### 方向 C：风格变体
适合：
- Q版
- 手办感
- 手工玩具感
- 风格探索备用方向

重点：
- 保留角色核心特征
- 放大风格化表达
- 作为方向 B/C 的探索位，不默认作为主商业方向

Prompt 骨架：

```text
Scene / Background:
clean background

Subject:
stylized character illustration, {{角色描述}}

Key details:
{{Q版或手办风说明}}, {{风格变体关键词}}, {{光线或材质感}}

Composition and use:
collectible visual quality

Constraints:
no plastic toy cheapness, no overdecorated scene, no broken character features
```

## Negative Prompt 推荐片段

### 廉价游戏海报感
```text
cheap mobile game splash art, flashy combat poster style, overpowered effects, noisy composition
```

### 低幼卡通感
```text
overly childish cartoon, low-end kids illustration, plush toy look, childish proportions
```

### 塑料玩具感
```text
plastic toy rendering, glossy figurine look, fake material texture, cheap collectible style
```

### 背景喧宾夺主
```text
cluttered background, overdecorated scene, busy effects, weak subject focus
```

## 二轮修改模板

### 模板 A：主体加强
```text
保留角色设定和配色不变。
请让主体更清楚、更有存在感，轮廓更明确，视觉中心更集中。
不要改变角色核心特征。
```

### 模板 B：高级感提升
```text
保留构图和角色设定不变。
请提升整体高级感、材质感和完成度，减少廉价感和游戏宣传图感。
不要增加夸张特效。
```

### 模板 C：背景减法
```text
保留角色不变。
请把背景再简洁一点，只保留氛围层次，不要让背景抢主体。
```

### 模板 D：角色一致性
```text
保留角色身份、面部特征、服装核心元素和整体比例不变。
只调整 {{局部目标}}。
不要重新设计角色，也不要新增无关道具。
```

## 审校重点
- 角色核心特征是否明确
- 主体是否足够强
- 是否一眼能看出角色气质
- 是否滑向廉价游戏海报感或低幼卡通感
- 如果是海报主视觉，是否具备留白和标题区空间
- 如果是连续角色图，角色一致性是否保持

## 待确认项
- 是否允许直接使用版权角色名
- 是否需要上版文字或 logo
- 最终更偏：
  - 海报主视觉
  - 手机壁纸
  - 社媒封面
- 是否需要 Q版 / 手办感 / 电影感中的哪一个优先
- 是否需要和上一张角色图保持一致
