# 幼儿园开学 / 首次返园通知模板

## 目标
让 `copy-workflow` 在处理小班开学、首次返园、假期后返园提醒时，优先产出像老师真实在家长群里发的消息，而不是行政通知。

这是一个快捷模板。
如果已经明确属于 `welcome_new_term` 或 `return_to_school_reminder`，优先分别参考：
- [copy-kindergarten-welcome-new-term-template.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-kindergarten-welcome-new-term-template.md)
- [copy-kindergarten-return-to-school-reminder-template.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/copy/copy-kindergarten-return-to-school-reminder-template.md)

## 适用场景
- 9 月开学通知
- 新学期首次返园提醒
- 长假后返园提醒
- 开学前一晚提醒
- 开学当天早晨提醒
- 入园物品准备通知

## 语料优先级
1. 先看 [kindergarten-group-style-profile.md](D:/work/myclaw/codex-personal-agent-starter/wechat-style-samples/profile/kindergarten-group-style-profile.md)
2. 再看 [kindergarten-group-scene-map.md](D:/work/myclaw/codex-personal-agent-starter/wechat-style-samples/profile/kindergarten-group-scene-map.md)
3. 再看最接近的 `normalized/kindergarten-group` 样本
4. 最后再用本模板补齐结构、槽位和待确认项

## 最少需要拿到的信息
- 开学或返园日期
- 是否有具体入园时间
- 家长需要准备的物品
- 是否需要写名字、带园服、带床品或午睡用品
- 是否有过敏、用药、请假等需要提前沟通的要求

如果以上信息不完整：
- 先保证日期、动作要求和通用物品清单能成稿
- 未确认的本园固定要求统一放入 `待确认项`

## 默认口吻
- 老师真实发群消息
- 温柔、亲近、带一点聊天感
- 提醒在前，温度在后
- 句子短，能直接复制进微信群
- 默认使用 1 到 3 组真实 emoji

## 默认结构
1. 开场称呼
2. 开学或返园时间提醒
3. 物品清单或动作要求
4. 补充注意事项
5. 温和收尾

## 高频表达锚点
- `爸爸妈妈们：`
- `小班宝贝们 9 月 1 日就要正式开学啦`
- `这些开学需要的物品提前准备好带过来就可以哈`
- `物品尽量都写上名字`
- `也请家长帮宝贝检查一下指甲哦`
- `如有过敏、用药或其他需要特别注意的情况，请提前和老师沟通`
- `老师在幼儿园里等你们回来`
- `我们 9 月 1 日不见不散哦`

使用原则：
- 只借节奏和口吻，不要把整句机械拼接
- 先保硬信息，再补表情和温度

## 物品清单推荐槽位
- 小书包
- 水杯
- 纸巾或湿巾
- 备用衣物 1 到 2 套
- 换洗裤子
- 小毛巾
- 室内鞋或拖鞋
- 园服
- 床品或午睡用品

使用原则：
- 优先保留高频且安全的通用项
- 园服、床品、名字贴、体检表等本园专属要求，未确认前不要写死

## 输出骨架

```md
爸爸妈妈们：

小班宝贝们 9 月 1 日就要正式开学啦😊 请大家这几天帮宝贝把作息慢慢调整回来，尽量早睡早起，方便孩子更快适应开学节奏哦。

1⃣️这些开学需要的物品提前准备好带过来就可以哈：小书包、水杯、纸巾或湿巾、备用衣物、换洗裤子、小毛巾、室内鞋或拖鞋。

2⃣️孩子的个人物品尽量都写上名字，方便老师整理，也方便宝贝自己辨认。

3⃣️也请家长帮宝贝检查一下指甲，如有过敏、用药或其他需要特别注意的情况，欢迎提前和老师沟通一下❤️

期待见到宝贝们可爱的笑脸，我们 9 月 1 日不见不散哦🌷
```

## 审校重点
- 像老师群消息，不像行政通知
- 时间、动作要求、物品清单清楚
- emoji 控制在 1 到 3 组
- 未确认的本园要求没有被写死
- 收尾自然，不出现 `特此通知`、`望周知`

## 待确认项
- 具体入园时间
- 是否保留 `@所有人`
- 班级名称和老师署名
- 是否要加 `收到请回复`
- 是否有园服、床品、名字贴、体检表等固定要求
