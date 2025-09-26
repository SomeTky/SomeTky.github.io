## ✅ Makefile & GCC 常用命令速查表

| 类别       | 命令 / 变量         | 含义 / 用途                          | 示例                       |
| ---------- | ------------------- | ------------------------------------ | -------------------------- |
| 🔧 GCC 编译 | `gcc file.c`        | 编译并链接成可执行文件               | `gcc main.c`               |
|            | `gcc -o out file.c` | 编译并指定输出文件名                 | `gcc -o myprog main.c`     |
|            | `gcc -c file.c`     | **仅编译生成 .o 文件**，不链接       | `gcc -c foo.c`             |
|            | `gcc -Wall`         | 开启所有警告信息                     | `gcc -Wall main.c`         |
|            | `gcc -g`            | 生成调试信息（配合 gdb）             | `gcc -g main.c`            |
|            | `gcc -O2`           | 启用优化（速度更快）                 | `gcc -O2 main.c`           |
|            | `gcc -I<dir>`       | 添加头文件搜索路径                   | `gcc -I./include main.c`   |
|            | `gcc -L<dir>`       | 添加库文件搜索路径                   | `gcc -L./lib -lmylib`      |
|            | `gcc -l<name>`      | 链接库（lib<name>.so / lib<name>.a） | `gcc -lm` 链接数学库       |
|            | `gcc *.o -o prog`   | 链接多个目标文件                     | `gcc main.o util.o -o app` |



------

| 类别       | Makefile语法                                 | 含义 / 用途                | 示例                 |
| ---------- | -------------------------------------------- | -------------------------- | -------------------- |
| 🔨 规则格式 | `target: deps` `<TAB> command`               | 定义构建规则               | `main.o: main.c`     |
| 变量定义   | `CC = gcc`                                   | 定义变量（编译器）         | `$(CC) -c main.c`    |
| 内置变量   | `$@`：目标名 `$<`：第一个依赖 `$^`：所有依赖 | 常用于命令中自动替换       | `$(CC) -o $@ $^`     |
| 伪目标     | `.PHONY: clean`                              | 标记非文件目标（如 clean） | `make clean`         |
| 清理命令   | `rm -f *.o`                                  | 删除中间文件               | 写在 `clean:` 规则中 |
| 默认目标   | 放在第一个规则                               | 执行 `make` 时默认构建它   | `all: main`          |
| 自动依赖   | `main: main.o util.o`                        | 自动追踪依赖变化           | 用于链接阶段         |
| 注释       | `# comment`                                  | 注释语句                   | `# 编译所有源文件`   |



------

## 📂 示例 Makefile

```
makefile复制编辑CC = gcc
CFLAGS = -Wall -g

all: app

app: main.o util.o
	$(CC) $(CFLAGS) -o $@ $^

main.o: main.c
	$(CC) $(CFLAGS) -c $<

util.o: util.c
	$(CC) $(CFLAGS) -c $<

clean:
	rm -f *.o app
```

------

## 📌 其他小技巧

- 使用 `make -n` 查看将执行哪些命令（dry run）
- 使用 `make -j4` 开启 4 个并发任务，加速编译
- 使用 `make VERBOSE=1` 查看详细命令



# 批量生成独立可执行文件

```makefile
# 编译器和参数
CC = gcc
CFLAGS = -Wall -g

# 所有源文件
SRCS = main.c foo.c bar.c utils.c log.c

# 自动生成可执行文件名（去掉.c）
TARGETS = $(SRCS:.c=)

# 默认规则：构建所有可执行文件
all: $(TARGETS)

# 每个目标: 单独编译对应的 .c 文件
%: %.c
	$(CC) $(CFLAGS) $< -o $@

# 清理所有中间和输出文件
clean:
	rm -f $(TARGETS)

```

