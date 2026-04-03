# 试穿试用子场景模板

## 目标
用于服饰试穿、搭配预览和试用展示。

## 最少需要的信息
- 主体人物
- 试穿或试用物
- 使用场景
- 风格方向
- 需要保持不变的部分

## 推荐补问模板
```text
按试穿试用场景处理，现在还缺最少这几项：

主体人物：
试穿/试用物：
使用场景：
想要的风格：
需要保持不变的部分：
```

## Prompt 骨架
```text
virtual try-on preview, {{主体人物}}, {{试穿物或试用物}}, {{风格方向}}, keep {{不变部分}} unchanged, suitable for preview use
```

## Negative Prompt 片段
```text
body distortion, garment drift, texture mismatch, unrealistic fit, cheap fashion catalog feel
```

## 审校重点
- 人物一致性
- 服饰或产品贴合度
- 材质和比例是否可信

## 待确认项
- 是否需要正侧背多视角
- 是否用于电商
