# 可调式文件

需要在使用gcc编译的时候，在编译命令上面加-g。

给gdb传入命令行参数（可执行文件），即可进入调试界面。

# list

列出代码

```shell
list 1 30 //列出第1到30行代码
```



# run

运行命令，如果有断点就在断点处停下来。

可简写r

# break

可简写b

设置断点，两种方式。

1. 1.

   b + 函数名 

2. 2.

   b + 行数

使用list命令列出所有命令和行数

# next

可简写n

按步执行

#  step

步入函数中

# delete

删除断点

# watch

watch + 变量名来监控变量的变化。

也可以使用地址来监控，但是比较麻烦：

```shell
watch *(int*)0x7fffffffdfbc
```

条件观察点

```shell
(gdb) watch variable if condition  # 当变量被写入且条件为真时触发
```

查看所有观察点

```shell
(gdb) info watchpoints  # 显示所有观察点信息（编号、位置、条件等）
```

禁用/启用观察点

```shell
(gdb) disable N  # 禁用编号为N的观察点
(gdb) enable N   # 重新启用编号为N的观察点
```

# info

可以使用info产看断点信息和watchpoint信息

# shell

可以用shell在gdb中执行控制台命令

#  print

简写p

可以打印出数据的值，同时也可以用这个命令来查看变量的地址（用取地址符）

# 使用core文件来调试

一般情况下，在运行出错后不会生成这个core文件，需要使用ulimit命令来打开这个限制。

```shell
ulimit -c unlimited
```

这样运行出错后会生成一个core文件，在使用gdb时带上这个core文件即可直接运行到出错的地方。

# 调试运行中的程序

在shell中运行可执行文件的时候，在末尾加一个&可以在后台运行

```shell
./test &
```

使用返回的进程号给gdb就可以调试正在运行的程序。

```shell
gdb -p 进程号
```

## 如何让输出不显示在控制台

在linux中有一个虚空设备/dev/null，可以把输出重新定向到这里即可

```shell
./test > /dev/null &
```