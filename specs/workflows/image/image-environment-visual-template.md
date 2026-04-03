# 环境视觉子场景模板

## 目标
用于环境氛围图、世界观场景图和特定空间生成。

## 最少需要的信息
- 场景主题
- 受众
- 使用场景
- 风格方向
- 主体权重
- 不希望出现的元素

## 推荐补问模板
```text
按环境视觉场景处理，现在还缺最少这几项：

场景主题：
目标受众：
使用场景：
想要的风格：
主体权重（环境主导还是人物主导）：
不希望出现元素：
```

## Prompt 骨架
```text
environment-focused visual, {{场景主题}}, {{风格方向}}, {{光线和氛围}}, {{主体权重说明}}, cinematic depth, suitable for {{用途}}
```

## Negative Prompt 片段
```text
generic background, weak atmosphere, cluttered environment, unclear focal hierarchy, cheap fantasy scene, noisy details
```

## 二轮修改模板
```text
保留场景主题不变。
请加强环境氛围和空间深度，同时明确主体权重。
不要让背景变成杂乱贴图。
```

## 审校重点
- 氛围是否成立
- 主体和环境关系是否清楚
- 是否具备主视觉价值

## 待确认项
- 是否需要加入人物
- 是横版还是竖版
