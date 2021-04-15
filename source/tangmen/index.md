---
title: 唐门
date: 2020-07-25 15:49:09
---
{% img [fullimage] /images/tangmen-foot.jpg [title 唐门 [alt text]] %}
## 心法：天罗诡道

**版本：结庐江湖20200702**

### 奇穴： 毒手尊拳 劫数难逃 弩击急骤 千机之威 千机巨搫 聚精凝神 化血迷心 蚀肌化血 秋风散影 回肠荡气 曙色催寒 雷甲三铉

### 秘籍：
蚀肌弹：2读条1会心1易伤（多田螺时可以偷偷把易伤秘籍换成伤害秘籍）
暗藏杀机：3伤害1范围（距离秘籍在移动BOSS或是群攻BOSS时看情况读1-2本）
天绝地灭：3伤害1加人
暴雨梨花针：1会心2伤害1特效
惊鸿游龙：3减CD 1持续
其他技能看自己喜好吧
	
### 急速：19
{% codeblock %}
/cast 暗藏杀机
/cast [tnobuff:化血|tbufftime:化血<9] 天女散花
/cast [buff:扬威] 心无旁骛
/cast 暴雨梨花针
/cast 天绝地灭
/cast [buff:暗藏杀机C] 图穷匕见
/cast 蚀肌弹
{% endcodeblock %}

### 循环打法：
机关放置模式
暗藏杀机：目标脚下
天绝地灭：目标脚下
千机变：传统模式（鼠标点击地面位置放置）
模式更改流程:剑心插件—技能增强—添加技能ID（ctrl+鼠标指向技能）—进行设置并激活方案
手动下千机变，毒刹群攻，连弩单体
开 BOSS 前提前放好 [千机变] 和三个 [暗藏杀机] ；
当团长倒数五四三二一时，数到四的时候手动开 [鬼斧神工] 和 [连弩形态]；
请务必注意 [鬼斧神工] 读条开始后再开启按键，否则会打断 [鬼斧神工] 的读条；
在 BOSS 进入战斗的时候手动开启一次按键并关闭一下按键，在 [鬼斧神工] 的读条结束的瞬间手动使用特效腰坠，并在使用特效腰坠的瞬间再次开启按键（后面的输出循环依然如此）；
手动开 [鬼斧神工] 之后，宏会自动使用 [心无旁骛] ，这样也就不存在浪费[心无旁骛] 的问题；

---

## 心法：惊羽诀（百里）

**版本：结庐人境20200730**

### 奇穴：迅电流光 千里无痕 狂风暴雨 摧心 掠影穹苍 浴血沁骨 声若惊雷 梨花带雨 秋风散影 回肠荡气 妙手连环 百里追魂

### 秘籍：
夺魄箭：2会心2伤害 如果换成穿林打叶就是换成2减CD 1伤害1会心
追命箭：2减CD2 1伤害 1追命无声伤害+20%
逐星箭：1神机3伤害
暴雨梨花针：1会心2伤害1气魄
穿心弩：1减cd2伤害1持续时间
惊鸿游龙：3cd1回神机
鸟翔碧空：3cd
	
### 急速：19/2704
{% codeblock %}
/cast [tbufftime:穿心<2] 穿心弩
/cast 暴雨梨花针
/cast 百里追魂
/cast 心无旁骛
/cast [buff:追命无声] 追命箭
/cast [energy>51] 夺魄箭
/cast 逐星箭
{% endcodeblock %}
### 循环打法：
起手自己手动打一个穿心弩

---