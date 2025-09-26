# 快捷键

将游标移动到世界的中心点

------

shift + c

将选中对象放置到世界中心点

------

alt + g

将选中的物体作为用户视角中心

------

.(This is the dot in the vice number area)

只显示选中的对象

------

/

设置游标

------

shift + mouse-Right

选择一圈线或一圈面

------

alt + twice-mouse-left

删除快捷键

------

x

分离物体

------

p

复制并移动物体

------

shift + d 重建复制

alt + d 关联复制

合并物体

------

m

晶格形变

------

First add a lattice to the canvas, adjust it wraps the target. Then you can change the resolution ratio of the lattice.(This parameter will allow you adjust the target in which degree.)

Then select the target and the lattice, ctrl + p to use lattice shape change. Now the lattice will be bound to the target.

Tick the lattice and go into editor mode. You can adjust the lattice's point to adjust the shape of the target.

应用所有修改器的一种简单方法

------

Select the target and tick it with mouse-right, tick the transform to, and select gridding.

通用填充快捷键

------

F

You can use this shortcut key with selected dot or area, then, blender will fill it automatically.

调整一条曲线的半径

------

alt + S

As we all know, shortcut key S is used to adjust the objects' scale. However, when you use this way to curve, it Invalid. At this situation, you should use alt + S to adjust it.

选中父级和清空父级

------

ctrl + P

alt + P

蒙皮修改器

------

ctrl + A 改半径（和曲线的改半径是不一样的）

蒙皮修改器对于分叉比较容易实现，可以对某一个点向外延申。

tips：蒙皮构建树枝看起来使用了一条路径曲线，实际上是一个平面线合并成一个点然后再拉成曲线。（我在试的时候发现曲线是没有蒙皮修改器的）

一些理解：如果是一个常规的多面体的话，如果想再一个结点拉出一个新的体，是需要一个 面的。但是如果用了蒙皮修改器，可以只用一个点就拉出一个体。

网格没了

------

shift +alt + z

# 模型导出到ue

![1754353245639](assets/1754353245639.png)

![1754353272748](assets/1754353272748.png)

取消导出动画选项

# 对象贴面

在blender编辑器的上方中间部分，有一个磁铁一样的东西。它旁边的按钮用来设置和什么东西相贴。

加入现在需要让一条表贴到另外一个物体上的一条边，则设置为“边”，选中需要去贴的边移动即可。

此时如何过图形的面数太少就会导致埋藏问题，需要根据被贴物体的形状特征去切割主贴物体的面，以确保不会发生埋藏。