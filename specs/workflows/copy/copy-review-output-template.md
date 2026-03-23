# 文案审校输出模板

## 目标
让审校结果不仅指出问题，还要明确说明为什么推荐某个版本、为什么不推荐其他版本。

## 必须包含的部分

```md
## Review Summary
- Overall status:
- Main risk:

## Problems
1. ...
2. ...

## Fix Suggestions
1. ...
2. ...

## Recommended Version
- Title / main version:
- Reason:
  - Most complete
  - Most stable
  - Best fit for current scene

## Not Recommended
- Version:
- Reason:
  - Too long
  - Missing critical fact
  - Tone mismatch

## Next Edit Priority
1. What should be fixed first
2. What can wait

## Human Check Items
- ...
- ...
```

## 使用时机
- 存在多个标题版本
- 存在多个正文版本
- 用户没有明确指定偏好
- 某一个版本明显更稳妥、更可用
