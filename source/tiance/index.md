---
title: 天策
date: 2020-07-25 15:48:46
---
{% img [fullimage] /images/tiance-foot.jpg [title 七秀 [alt text]] %}
## 心法：傲血战意 （手动渊）

**版本：结庐人境20200602**

### 奇穴： 扬戈 神勇 骁勇 击水 劲风 牧云 风虎 战心 渊 夜征 龙血 虎贲

### 秘籍：
穿云——2会心+2伤害（这里建议新人和懒鬼下一本会心，点减cd）
龙吟——1减cd+3伤害（命中不够的自行下伤害上命中，保证龙吟满命中）
龙牙——3伤害+1会心
灭——1减cd+2伤害+1会心
战八方——随便
守如山——3减cd+1加持续
啸如虎——3减cd+1加持续
断魂刺——2伤害+2减cd
突——2伤害剩下随便
	
### 急速：19/828
{% codeblock 马下： %}
/cast 突
/cast [nobuff:驰骋] 任驰骋
/cast [buff:渊] 撼如雷
/cast [rage>4] 龙牙
/cast [rage<3] 灭
/cast 龙吟
/cast 穿云
{% endcodeblock %}

{% codeblock 马上： %}
/cast 啸如虎
/cast [nobuff:牧云] 骑御
/cast 断魂刺
/cast [rage>4] 撼如雷
/cast [rage>4] 龙牙
/cast 龙吟
/cast [nearby_enemy>1] 战八方
/cast 穿云
{% endcodeblock %}
### 循环打法：
想偷懒可以把 /cast [buff:渊] 撼如雷 改成 /cast 撼如雷 ，奇穴 渊 改 破楼兰 ，dps会掉
需要任驰骋配合断魂刺爆发可删除  /cast 断魂刺  ，避免断魂刺cd。
起手：手动给队友渊后切boss按宏。另外0豆起手（懒鬼）建议点上穿云减cd秘籍，1豆起手（神仙，如果你一直按这个宏是永远莫得一豆的）建议上天台。
爆发：风手动按（这里建议新人好了就开，熟练了慢慢会知道时机的），任驰骋之后可以配合断魂刺在位移的时候用。
#### 手动渊的方法：
* 1.添加一名靠谱近战作为茗伊或者剑心的焦点目标
* 2.设置茗伊或者剑心的“循环焦点选择”的快捷键为一个顺手的键位
* 3.战斗中侧跳与焦点队友拉开六尺距离，按下焦点目标快捷键，再渊回去，然后TAB选中boss继续输出。

---

## 心法：铁牢律 （正常单T）

**版本：结庐人境20200602**

### 奇穴： 定军 龙痕 大漠 仗剑 劲风 掠如火 金甲 战心 长征 昂如岳 载戎 号令三军

### 秘籍：
穿云——2会心+2伤害（这里建议新人和懒鬼下一本会心，点减cd）
龙吟——1减cd+3伤害（命中不够的自行下伤害上命中，保证龙吟满命中）
龙牙——3伤害+1会心
灭——1减cd+2伤害+1会心
战八方——随便
守如山——3减cd+1加持续
啸如虎——3减cd+1加持续
断魂刺——2伤害+2减cd
突——2伤害剩下随便
	
### 急速：随意
{% codeblock 正常一键： %}
/cast [life<=0.2] 啸如虎
/cast 沧月
/cast [rage>4] 龙牙
/cast [rage<5|tnobuff:流血|tbufftime:流血<2] 龙吟
/cast [rage<3] 灭
/cast 穿云
{% endcodeblock %}

{% codeblock 范阳老二： %}
/cast [bufftime:铁马血河<1] 后撤
/cast [life<=0.2] 啸如虎
/cast 沧月
/cast [rage>4] 龙牙
/cast 龙吟
/cast [rage<3] 灭
/cast 穿云
{% endcodeblock %}
### 循环打法：
减伤，定军手动打
* 必背功能技能：
定军（强仇），沧月（群拉大量仇恨），
风（提高自身仇恨，全团无威胁气劲，并可以触发啸如虎），
守如山（减伤），啸如虎（锁血挂）。

---

## 心法：铁牢律 （群T）

**版本：结庐人境20200602**

### 奇穴： 定军 坚韧 徐如林 望西京 出云 掠如火 金甲 傲骨 长征 激雷 载戎 号令三军

### 秘籍：
穿云——2会心+2伤害（这里建议新人和懒鬼下一本会心，点减cd）
龙吟——1减cd+3伤害（命中不够的自行下伤害上命中，保证龙吟满命中）
龙牙——3伤害+1会心
灭——1减cd+2伤害+1会心
战八方——随便
守如山——3减cd+1加持续
啸如虎——3减cd+1加持续
断魂刺——2伤害+2减cd
突——2伤害剩下随便
	
### 急速：随意
{% codeblock %}
/cast [life<=0.2] 啸如虎
/cast [rage>4] 龙牙
/cast [rage<5|tnobuff:流血|tbufftime:流血<2] 龙吟
/cast [rage<3] 灭
/cast 穿云
{% endcodeblock %}

### 循环打法：
减伤，沧月，定军手动打
本套奇穴以战八方+沧月作为基础群体输出技能，坚韧提供常驻5%减伤，双突+大雷作为群体强仇技能。点出望西京增加自身血量和蓝量，点出突徐如林增加自身续航能力，定军作为单点接仇使用。
* 必背功能技能：
定军（强仇），沧月（群拉大量仇恨），
风（提高自身仇恨，全团无威胁气劲，并可以触发啸如虎），
守如山（减伤），啸如虎（锁血挂）。

---