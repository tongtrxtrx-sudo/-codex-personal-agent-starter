# 写真人像子场景模板

## 目标
用于单人 / 双人人像、海边写真、杂志感人像、情绪壁纸等真实人物图的方向探索。

## 适用场景
- 海边写真
- 杂志感写真人像
- 单人生活方式人像
- 情绪型壁纸
- 轻商业写真主视觉

## 不适用场景
- 强风格化动漫角色图
- 明显依赖图中文字的海报
- 需要局部修图或换背景的编辑任务

## 最少需要的信息
- 人物主体
- 目标受众
- 使用场景
- 写真风格
- 光线或时间段
- 不希望出现的低质感问题

## 推荐补问模板
```text
按写真人像场景处理，现在还缺最少这几项：

人物主体：
目标受众：
使用场景：
想要的写真风格：
光线/时间段：
服装或造型：
不希望出现元素：
```

## 官方对齐 Prompt 骨架
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
natural skin texture, no heavy retouching, no cheap studio portrait feel, no vulgar styling
```

## Negative Prompt 片段
```text
cheap studio portrait style, plastic skin, over-smoothed beauty filter, tacky glamour pose, low-end catalog photo look, cluttered background, glamorized staging, excessive retouching
```

## 二轮修改模板
```text
保留人物设定和场景不变。
请让表情和姿态更自然，减少摆拍感和磨皮感。
不要做成廉价影楼样片风，也不要把皮肤修成塑料质感。
```

## 写实强化建议
- 想要更真实时，优先补摄影语言，比如 `50mm lens`、`eye-level`、`golden hour`、`shallow depth of field`。
- 想要更自然时，明确写出 `real skin texture`、`fabric wear`、`subtle imperfections`。
- 避免使用会引导摆拍或棚拍的词，例如 `glamour`、`studio polish`、`beauty campaign`。

## 审校重点
- 人物主体是否清楚
- 光线是否服务气质
- 皮肤和材质是否自然
- 是否误入低俗、影楼或塑料质感
- 是否过度摆拍或过度精修

## 待确认项
- 是否需要明确服装
- 是否需要竖版或横版锁定
- 是否需要上文字
