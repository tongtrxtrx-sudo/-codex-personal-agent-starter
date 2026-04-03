# 参考图编辑子场景模板

## 目标
用于基于现有图片做替换、修复、迁移、增强或结构保持类编辑任务。

## 最少需要的信息
- 原图是什么
- 保留什么不变
- 需要改什么
- 改成什么效果
- 输出比例或用途

## 推荐补问模板
```text
按参考图编辑场景处理，现在还缺最少这几项：

原图是什么：
保留什么不变：
需要改什么：
改成什么效果：
输出比例或用途：
```

## 编辑指令骨架
```text
Keep {{保持不变的部分}} unchanged.
Change {{需要修改的部分}} into {{目标效果}}.
Maintain original perspective, structure, and subject identity.
Output should be suitable for {{用途或比例}}.
```

## Negative Prompt 片段
```text
structural drift, identity drift, perspective distortion, background mismatch, low-detail patching, artificial blending
```

## 二轮修改模板
```text
保留主体、透视和结构不变。
只调整 {{局部目标}}。
不要改变整体构图，也不要新增无关元素。
```

## 审校重点
- 保留项有没有漂
- 改动项是否准确
- 是否出现融合痕迹或结构错乱

## 待确认项
- 是否需要透明背景
- 是否需要多版本对比
