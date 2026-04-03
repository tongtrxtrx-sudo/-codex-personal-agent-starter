# 参考图编辑子场景模板

## 目标
用于基于现有图片做替换、修复、迁移、增强或结构保持类编辑任务。

## 适用场景
- 局部改造
- 场景替换
- 材质替换
- logo / 贴图 / 包装调整
- 多图合成
- 透明背景产品提取

## 不适用场景
- 从零生成一张完全新图
- 单纯想复刻一张图的感觉而不是编辑原图
- 需要故事分镜或多镜头连续叙事

## 最少需要的信息
- 原图是什么
- 是单图编辑还是多图合成
- 保留什么不变
- 需要改什么
- 改成什么效果
- 是否有 mask
- 输出比例或用途

## 推荐补问模板
```text
按参考图编辑场景处理，现在还缺最少这几项：

原图是什么：
单图还是多图：
保留什么不变：
需要改什么：
改成什么效果：
是否有 mask：
输出比例或用途：
```

## 官方对齐编辑指令骨架

### 单图编辑
```text
Change only:
{{需要修改的部分}}

Keep exactly the same:
{{保持不变的部分}}

Target result:
{{目标效果}}

Constraints:
maintain original perspective, structure, subject identity, lighting logic, and text/logo integrity; output should be suitable for {{用途或比例}}
```

### 多图参考编辑
```text
Image 1:
{{主图，作为被编辑对象}}

Image 2:
{{风格参考 / 物件参考 / logo / 第二主体}}

Instruction:
{{把图2的什么应用到图1}}

Keep exactly the same:
{{图1中绝对不能变的内容}}

Constraints:
preserve composition and perspective; do not add unrelated elements; keep output suitable for {{用途或比例}}
```

## Negative Prompt 片段
```text
structural drift, identity drift, perspective distortion, background mismatch, low-detail patching, artificial blending, added unrelated elements, logo distortion, text corruption
```

## 二轮修改模板
```text
保留主体、透视和结构不变。
只调整 {{局部目标}}。
不要改变整体构图、文字或 logo，也不要新增无关元素。
```

## 高保真建议
- 如果输入图中有脸、logo、品牌包装、服装纹理等需要精确保留的元素，优先开启高保真思路。
- 多图输入时，先明确哪一张是主图，再补充其他参考图的角色。
- 使用 mask 时，要把 `mask 区域要改什么` 说清楚，同时重复 `其他区域保持不变`。

## 审校重点
- 保留项有没有漂
- 改动项是否准确
- 是否出现融合痕迹或结构错乱
- 文字、logo、包装是否被误改
- 光线和接触阴影是否协调

## 待确认项
- 主图是否固定为 `Image 1`
- 是否需要高保真保留
- 是否需要透明背景
- 是否需要 mask 精修
- 是否需要多版本对比
