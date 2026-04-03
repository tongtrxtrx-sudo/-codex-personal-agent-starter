# 信息可视化子场景模板

## 目标
用于信息图、分析图、图文说明图和结构拆解图。

## 最少需要的信息
- 主题
- 目标受众
- 信息层级
- 必须保留的数据或结论
- 风格方向
- 输出比例

## 推荐补问模板
```text
按信息可视化场景处理，现在还缺最少这几项：

主题：
目标受众：
必须保留的信息：
信息层级：
想要的风格：
输出比例：
```

## Prompt 骨架
```text
information visual about {{主题}}, clear hierarchy, {{风格方向}}, readable labels area, structured layout, suitable for {{比例或用途}}
```

## Negative Prompt 片段
```text
cluttered infographic, unreadable hierarchy, decorative noise, weak labels area, chaotic layout, data confusion
```

## 二轮修改模板
```text
保留主题和信息结构不变。
请让层级更清楚，留白更好，信息区更容易读。
不要为了装饰牺牲可读性。
```

## 审校重点
- 信息是否清楚
- 图文区块是否合理
- 是否可落地上版

## 待确认项
- 是否需要真实数据
- 是否需要品牌色
