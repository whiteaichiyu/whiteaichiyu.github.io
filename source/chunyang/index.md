---
title: 纯阳
date: 2020-07-25 15:49:05
---
{% img [fullimage] /images/chunyang-foot.jpg [title 纯阳 [alt text]] %}
## 心法：紫霞功（心固流）
目前版本最优流派

**版本：结庐江湖20200702**

### 奇穴： 白虹 心固/霜锋 无形 归元 同尘 跬步 万物 抱阳 浮生 期声 自化 固本

### 秘籍：
两仪化形——1回豆2伤害1会心
四象轮回——2读条2会心
万世不竭——3伤害1命中
破苍穹——3范围1消耗
凭虚御风——2减CD1移速1回血
坐忘无我——2减CD1移速1减伤
生太极——3范围1消耗
太极无极——3伤害1会心	
### 急速：19/828
{% codeblock 输出： %}
/cast [nobuff:破苍穹] 破苍穹
/cast [qidian<8] 六合独尊
/cast [nobuff:气剑|bufftime:气剑<1.7&nobuff:紫气东来] 万世不竭
/cast [qidian>7] 两仪化形
/cast 四象轮回
{% endcodeblock %}

{% codeblock 爆发： %}
/fcast 凭虚御风
/fcast [nobuff:紫气东来] 万世不竭
/fcast [nobuff:气剑] 紫气东来
/fcast [qidfian>7] 两仪化形
/cast 四象轮回
{% endcodeblock %}

### 循环打法：

#### 起手 ：
剑出-一段-破苍穹-六合-不断按爆发宏直到读出一个四象-输出宏正常循环
#### 输出循环下：
六合独尊每波紫气时放一个，紫气CD一半时放一个
#### 爆发条件：
破苍穹气场持续时间大于10秒，六合在cd较久，最好是刚打出
#### 临场技巧：
* 当副本机制需要频繁强制停手第十一层奇穴可以点出重光。
* 在气场时间剩余3秒，且身上的豆不够的时候，可以优先补气场。这样就不用担心出现气场时间结束了，而浪费身上满豆去补气场的尴尬情况。
* 点自化情况下由于[三才化生]、[九转归一]没有公共CD，可以在补气场时用这2个技能去触发[气竭];当目标多又选不中带有[气竭]的目标，可以用[五方行尽]去触发[气竭]。

---

## 心法：太虚剑意 （无意流）

**版本：凌雪藏锋20191218**

### 奇穴：心固 深埋 化三清 无意 风逝 叠刃 切玉 负阴 和光 期声 无欲 玄门

### 秘籍：
气场：减读条点满
人剑：减CD点满 
无我：2伤1会1回豆 or 3伤1会
三环套月：2伤2会
凭虚御风：2减CD1闪1移速
坐忘无我：减CD点满
八荒归元：3伤1回豆
	
### 急速：19/828
{% codeblock %}
/cast [bufftime:玄门<4] 人剑合一
/cast [buff:紫气东来|qidian>8] 无我无剑
/cast [nobuff:碎星辰] 碎星辰
/cast 八荒归元
/cast [qidian>7] 无我无剑
/cast 三环套月
{% endcodeblock %}

### 循环打法：
二段加速一定不够蓝所以请洗化三清，不推荐使用全自动宏，手动补人剑和碎最好。

---

## 心法：太虚剑意（云中剑仙）
伤害不如手动

**版本：结庐江湖20200730**

### 奇穴：心固 深埋 昆吾/化三清 云中剑 风逝 叠刃 长生 负阴 和光 期声 无欲 玄门

### 秘籍：
气场：减读条点满
人剑：减CD点满 
无我：2伤1会1回豆 or 3伤1会
三环套月：2伤2会
凭虚御风：2减CD1闪1移速
坐忘无我：减CD点满
八荒归元：3伤1回豆
	
### 急速：828
{% codeblock 起手下圈 %}
/cast 剑冲阴阳
/fcast [nobuff:碎星辰] 碎星辰
/cast 生太极
/cast 吞日月
{% endcodeblock %}

{% codeblock 循环 %}
/cast [nobuff:碎星辰] 碎星辰
/cast 生太极
/cast 人剑合一
/cast [tbuff:叠刃] 八荒归元
/cast [qidian<7] 吞日月
/cast [qidian>8] 无我无剑
/cast 三环套月
{% endcodeblock %}

{% codeblock 爆发 %}
/fcast [qidian<10&buff:玄门=3&buff:碎星辰&bufftime:玄门>10&npclevel=6] 紫气东来
/cast [nobuff:碎星辰] 碎星辰
{% endcodeblock %}

### 循环打法：
起手按下圈宏，设置气场落在目标点。生太极、吞日月会开怪。
剑冲突进后按循环宏，爆发宏仅对boss有效。

---