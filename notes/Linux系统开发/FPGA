# 开发环境

1. Quartus II
2. ModelSim
3. Visio

# 基本语法

## 常量表示

(位宽)'(进制)(数值)

```verilog
8'd171
8'hab
8'o253
8'b1010_1011
```

## 赋值

=： 阻塞赋值，赋值过程是顺序执行的 

<=:  非阻塞赋值，赋值过程是并行执行的



**官方推荐编写组合逻辑时使用阻塞赋值，编写时序逻辑时使用非阻塞赋值。**



## 参数的定义

parameter

名称一般大写

```verilog
parameter CNT_MAX = 8'b0000_0000;
```

还有

localparam

其中，localparam只能用于模块內部参数的定义；

而parameter可以用在模块接口定义时，在实例化可以用于参数传递。

```verilog
module counter
    #(
        parameter CNT_MAX = 8'b0000_0000,
    )
    (
    	input 	....	,
        ...
        
        output 	... 	
    )
```

实例化的时候也是一样的，在原本的括号之前加一个#（）在里面传入参数即可。

```verilog
module counter
    #(
        .CNT_MAX(100),
    )
    (
        .xxx(),
        .xxx()
    )
```







## &

当其作为单目运算符时，是将一个数的所有二进制位相与最终获得一位。

双目运算符时就是正常的与运算。

## {}位拼接运算符

将想要拼接的不同位数的二进制数放到这个花括号里面，用逗号隔开，就拼接好了。

## 系统函数

系统内预定了一些任务和函数，用于完成一些特殊的功能。但大部分只能在Testbench方针中使用。

```verilog
`timescale 1ns/1ns  //时间尺度预编译指令 时间单位/时间精度
```

#数字：延时相应时间单位的时间

$display:用于输出打印信息，用法和c语言的printf相似

$ write: 也是用于输出打印信息但是这个不能自动换行，display是可以自动换行的

$strobe: 输出打印信息，只在最后执行。

$monitor:用于监控变量，当monitor中的任何一个变量发生变化时，就会执行这条语句。monitor的使用格式和其他信息输出语句是一样的。

$stop: 用于暂停仿真

$finish: 用于结束仿真

$time: 返回当前仿真时间64位

$random:生成随机数

$readmemb: 用于读二进制文件函数

$readmemh:用于读16进制文件的函数

```verilog
$readmemb("<数据文件名>", <存储器名>)
```



## assign 和 always

assign只能用=赋值，always既可以用=也可以用<=；





# 编写一个模块示例

```verilog
module  decoder
(
    input   wire        in_1,
    input   wire        in_2,
    input   wire        in_3,

    output  reg [7:0]   out
);

always@(*)
    if ({in_1, in_2, in_3} == 3'b000)
        out = 8'b0000_0001;
    else if({in_1, in_2, in_3} == 3'b001)
        out = 8'b0000_0010;
    else if({in_1, in_2, in_3} == 3'b010)
        out = 8'b0000_0100;
    else if({in_1, in_2, in_3} == 3'b011)
        out = 8'b0000_1000;
    else if({in_1, in_2, in_3} == 3'b100)
        out = 8'b0001_0000;
    else if({in_1, in_2, in_3} == 3'b101)
        out = 8'b0010_0000;
    else if({in_1, in_2, in_3} == 3'b110)
        out = 8'b0100_0000;
    else if({in_1, in_2, in_3} == 3'b111)
        out = 8'b1000_0000;

endmodule
```

以上是一个3-8译码器，可以看到文件需要包裹在module和endmodule之间。

编写完这个器件以后，需要编写测试文件，通常命名为tb_原文件名。

```verilog
`timescale 1ns/1ns

module tb_decoder();

//用always赋值一律是reg型变量，用assign赋值的一律是wire型变量
reg     in_1;
reg     in_2;
reg     in_3;

wire [7:0] out;

initial
    begin
        in_1 <= 1'b0;
        in_2 <= 1'b0;
        in_3 <= 1'b0;
    end

initial 
    begin
        $timeformat(-9, 0, "ns", 6);
        $monitor("@time %t:in_1=%b, in_2=%b, in_3=%b, out=%b", $time, in_1, in_2, in_3, out);
    end

always #10 in_1 <= {$random} % 2;
always #10 in_2 <= {$random} % 2;
always #10 in_3 <= {$random} % 2;

decoder decoder_inst
(
    .in_1 (in_1),
    .in_2 (in_2),
    .in_3 (in_3),

    .out (out)
);

endmodule
```

仿真文件中，首先需要指定时间单位和精度

```verilog
`timescale 1ns/1ns
```

在编写仿真文件时，initial标识符内的所有指令只在初始化的时候执行一次，常用来初始化赋值。



仿真文件中还涉及到模块的实例化，在实例化中，定义的引脚名前加上一个.表示连线。 



# 触发器的同步复位和异步复位

我们在always@()中如果只写时钟信号的上升沿，就是同步复位。如果在其中加上检测复位按钮的下降沿（复位口低电平有效），就可以实现异步复位。

同步复位：

```verilog
always@(posedge sys_clk)
    if (sys_rst_n == 1'b0)
        led_out <= 1'b0;
    else if (key_in == 1'b1)
        led_out <= 1'b1;
```

异步复位：

```verilog
always@(posedge sys_clk or negedge sys_rst_n)
    if (sys_rst_n == 1'b0)
        led_out <= 1'b0;
    else if (key_in == 1'b1)
        led_out <= 1'b1;
```





