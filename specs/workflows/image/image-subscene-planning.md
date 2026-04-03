# 图片 Workflow 子场景规划

## 目标
把 [Leader Prompt Gallery 全类别抽样报告](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/leaderai-prompt-gallery-all-category-sampling-report.md) 转成适合当前仓库落地的图片 workflow 子场景规划，指导后续：
- 最小补问
- brief 抽取
- prompt 生成
- negative prompt 词库
- 案例扩展

## 设计原则
1. 保留当前图片 workflow 的主结构，不让外部 prompt 库反向定义流程。
2. 子场景只负责“输入补问和输出模式差异”，不改变顶层 4 步链路。
3. 先做高频、稳定、可训练的子场景，再做小众长尾。
4. 方向探索层和执行层继续分开。

## 子场景总览

### P0 - 第一优先级

#### 1. `portrait_realistic`
- 来源类别：
  - `05_人物肖像与写实摄影`
- 适用任务：
  - 单人 / 双人人像
  - 海边写真
  - 杂志感写真人像
  - 情绪人像壁纸
- 关键输入：
  - 人物主体
  - 表情 / 姿态
  - 光线
  - 写真风格
  - 皮肤与质感边界
- 输出重点：
  - 写真 prompt 骨架
  - 写真类 negative prompt
  - 二轮自然化修改模板

#### 2. `poster_kv`
- 来源类别：
  - `03_创意广告品牌设计`
  - `06_图文排版视觉传达`
- 适用任务：
  - 活动海报主视觉
  - 招生海报
  - 品牌 KV
  - 带标题区的视觉图
- 关键输入：
  - 主体
  - 受众
  - 场景
  - 品牌感
  - 标题和必须保留事实
  - 版式比例
- 输出重点：
  - 海报主视觉 prompt 骨架
  - 信息区 / 留白控制
  - 商业图 negative prompt

#### 3. `role_key_visual`
- 来源类别：
  - `10_卡通漫画电影角色`
  - `12_手工玩具手办`
- 适用任务：
  - 动漫角色图
  - IP 风格启发图
  - Q版角色图
  - 角色海报主视觉
- 关键输入：
  - 发型
  - 服装
  - 面部特征
  - 姿态
  - 角色气质
  - 风格边界
- 输出重点：
  - 角色图 prompt 骨架
  - 角色图风险压制词
  - 二轮“主体加强”模板
- 已有模板：
  - [image-role-key-visual-template.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-role-key-visual-template.md)

#### 4. `reference_edit`
- 来源类别：
  - `11_图像编辑与修复增强`
  - `01_建筑室内空间设计`
- 适用任务：
  - 保持主体不变做编辑
  - 老照片修复
  - 风格迁移
  - 场景替换 / 材质替换 / 结构保持
- 关键输入：
  - 原图是什么
  - 保留什么不变
  - 改什么
  - 改成什么效果
- 输出重点：
  - 编辑指令骨架
  - “保持不变”字段
  - 结果复审清单

#### 5. `reference_to_template`
- 来源类别：
  - `05_人物肖像与写实摄影`
  - `03_创意广告品牌设计`
  - `07_艺术插画创意风格`
- 适用任务：
  - 给一张图反推出可复用模板
  - 从参考图提炼风格骨架
  - 从优秀图片总结 negative prompt 风险
  - 给 ChatGPT Pro 复刻相似质感
- 关键输入：
  - 参考图是什么
  - 想复用哪类感觉
  - 必须保留什么
  - 哪些允许变化
  - 最终用途
- 输出重点：
  - 参考图拆解后的 prompt 模板
  - 风险压制词
  - 相似图生成模板
  - 二轮微调模板

### P1 - 第二优先级

#### 6. `creative_concept`
- 来源类别：
  - `04_创意脑洞特效合成`
  - `07_艺术插画创意风格`
- 适用任务：
  - 双重曝光
  - 抽象概念图
  - 脑洞创意图
  - 艺术化备用方向
- 风险：
  - 容易华而不实
  - 容易失控
- 输出重点：
  - 概念型方向
  - 强 negative prompt
  - brand review 加严

#### 7. `product_visual`
- 来源类别：
  - `02_电商产品虚拟摄影`
  - `03_创意广告品牌设计`
- 适用任务：
  - 电商详情主图
  - 产品海报
  - 白底产品图
  - 产品摄影概念图
- 输出重点：
  - 产品摄影 prompt 骨架
  - 产品细节和材质控制
  - 白底 / 棚拍 / 广告风分支

#### 8. `storyboard_keyframes`
- 来源类别：
  - `09_故事分镜角色设定`
- 适用任务：
  - 九宫格分镜
  - 多镜头关键帧
  - 角色设定页
- 输出重点：
  - 多画面结构
  - 镜头差异控制
  - 角色一致性约束

### P2 - 第三优先级

#### 9. `info_visual`
- 来源类别：
  - `06_图文排版视觉传达`
  - `08_图像分析信息拆解`
- 适用任务：
  - 信息图
  - 分析图
  - 图文说明图
- 输出重点：
  - 图文区块控制
  - 信息层级
  - 版面留白

#### 10. `environment_visual`
- 来源类别：
  - `15_特定场景环境生成`
- 适用任务：
  - 特定场景环境图
  - 世界观场景图
  - 环境氛围主视觉
- 输出重点：
  - 环境主导 prompt
  - 氛围和主体权重

### P3 - 暂缓

#### 11. `social_cover`
- 来源类别：
  - `14_社交媒体营销`
- 说明：
  - 当前可以先并入 `poster_kv`
  - 后续如果社媒封面量足够，再独立拆出

#### 12. `tryon_preview`
- 来源类别：
  - `13_虚拟购物试穿试用`
- 说明：
  - 当前样本量少，暂不优先

#### 13. `meme_sticker`
- 来源类别：
  - `16_表情包趣味拼图`
- 说明：
  - 当前不属于主线
  - 后续如果角色表情差分需求增加，再独立扩

## 推荐落地顺序

### 第一批
1. `portrait_realistic`
2. `poster_kv`
3. `role_key_visual`
4. `reference_edit`
5. `reference_to_template`

### 第二批
6. `creative_concept`
7. `product_visual`
8. `storyboard_keyframes`

### 第三批
9. `info_visual`
10. `environment_visual`

## 每个子场景建议补的资产

### `portrait_realistic`
- 最小补问模板
- 写真人像 prompt 模板
- 写真 negative prompt 词库
- 二轮自然化修改模板
- 2 个真实案例

### `poster_kv`
- 海报主视觉 prompt 模板
- 标题区 / 留白规则
- 商业图 negative prompt 词库
- 2 个真实案例

### `role_key_visual`
- 角色描述骨架
- 角色图 prompt 模板
- 角色图风险压制词
- Q版 / 高质感 / 海报主视觉分支
- 2 个真实案例

### `reference_edit`
- 编辑类最小补问模板
- “保持不变 / 改什么”结构模板
- 执行记录模板
- 结果复审模板
- 2 个真实案例

### `reference_to_template`
- 看图反推模板补问
- 参考图拆解结构
- 相似图 prompt 模板
- 风险压制词提炼规则
- 1 到 2 个真实案例

## 对现有仓库的最小改造建议
1. 保持当前顶层 `image-workflow` 不变。
2. 在 `image-minimal-intake.md` 后续扩成“按子场景补问”。
3. 在 `image-prompt-pattern-library.md` 里按子场景分区。
4. 示例目录后续按子场景补齐。

## 当前建议执行动作
1. 已完成高频子场景正式模板
2. 已补 `poster_kv` 双案例
3. 已补 `portrait_realistic`、`role_key_visual`、`reference_edit` 真实案例
4. 下一步可补 `reference_to_template` 真实案例

## 判断标准
当某个子场景至少满足以下条件时，才算真正落地：
- 有最小补问模板
- 有 prompt 模板
- 有 negative prompt 词库或风险压制规则
- 有至少 2 个真实案例
- 有清晰的人工确认项

## 已完成模板入口
当前全部子场景模板已落成，统一入口见：
- [image-subscene-template-index.md](D:/work/myclaw/codex-personal-agent-starter/specs/workflows/image/image-subscene-template-index.md)
