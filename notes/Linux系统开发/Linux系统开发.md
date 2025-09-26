#  	makefile标准模板

```makefile
# 编译器
CC = gcc

# 编译选项：启用警告、调试信息、C99 标准
CFLAGS = -Wall -g -std=c99

# 可执行文件名（根据你的项目改名字）
TARGET = fopen_learn

# 源文件（把你的 .c 文件列在这里，用空格隔开）
SRCS = fopen_learn.c

# 自动生成目标文件（.o），名字和源文件对应
OBJS = $(SRCS:.c=.o)

# 默认目标：构建可执行文件
all: $(TARGET)

# 链接目标：将 .o 文件链接成可执行文件
$(TARGET): $(OBJS)
	$(CC) $(OBJS) -o $(TARGET)

# 编译规则：将每个 .c 文件编译成 .o 文件
%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

# 清理生成的文件
clean:
	rm -f $(OBJS) $(TARGET)

# 重新构建（先清理，再编译）
rebuild: clean all

# 打印帮助信息
help:
	@echo "可用命令："
	@echo "  make      - 编译程序"
	@echo "  make clean - 删除编译生成的文件"
	@echo "  make rebuild - 清理并重新编译"
	@echo "  make help  - 显示此帮助信息"

# 设置默认目标
.PHONY: all clean rebuild help
```

注意需要用tab缩进，不可以用空格。

# 📦 常用库函数

|                         |                                     |
| ----------------------- | ----------------------------------- |
| `dprintf(fd, fmt, ...)` | 按格式输出到指定文件描述符          |
| `system(cmd)`           | 执行 shell 命令（自动 fork + exec） |
| `perror(str)`           | 输出`str: 错误原因`（基于`errno`）  |

# 📁 文件操作（stdio.h）

|                                   |                                   |
| --------------------------------- | --------------------------------- |
| `fopen("file", "r/w/a/r+/w+/a+")` | 打开文件，返回`FILE*`             |
| `fputc(ch, fp)`                   | 写一个字符到文件                  |
| `fputs(str, fp)`                  | 写字符串（不自动加`\n`）          |
| `fprintf(fp, fmt, ...)`           | 格式化输出到文件                  |
| `fgetc(fp)`                       | 读一个字符（返回`int`，EOF 结束） |
| `fgets(buf, size, fp)`            | 读一行（保留`\n`）                |
| `fscanf(fp, fmt, ...)`            | 格式化读取文件数据                |

> ✅ 必须 `fclose(fp)` 关闭文件。 

# 🖥️ 标准流（FILE*）

|          |                                |
| -------- | ------------------------------ |
| `stdin`  | 标准输入（键盘）               |
| `stdout` | 标准输出（屏幕）               |
| `stderr` | 标准错误输出（屏幕，用于报错） |

# 🔧 系统调用（unistd.h / fcntl.h）

|                             |                                                  |
| --------------------------- | ------------------------------------------------ |
| `open(path, flags, mode)`   | 打开/创建文件，返回文件描述符（fd）              |
| `read(fd, buf, count)`      | 从 fd 读数据到 buf，返回字节数（0=EOF，-1=错误） |
| `write(fd, buf, count)`     | 向 fd 写数据，返回实际写入字节数（可能 < count） |
| `close(fd)`                 | 关闭文件描述符                                   |
| `lseek(fd, offset, whence)` | 移动文件偏移量（`SEEK_SET/CUR/END`）             |
| `exit(status)`              | 终止进程，刷新缓冲区、调用 atexit                |
| `_exit(status)`             | 立即终止，不清理缓冲区                           |
| `mkfifo(path, mode)`        | 创建命名管道（FIFO）文件                         |

# 🧬 内置数据类型

|           |                                         |
| --------- | --------------------------------------- |
| `pid_t`   | 进程 ID 类型（`fork`,`getpid`等返回值） |
| `ssize_t` | 有符号字节计数（`read/write`返回值）    |
| `off_t`   | 文件偏移量类型（`lseek`使用）           |

# 🔗 文件描述符（fd）

- `0` = `STDIN_FILENO`（标准输入）
- `1` = `STDOUT_FILENO`（标准输出）
- `2` = `STDERR_FILENO`（标准错误）

> 所有 I/O 操作基于 fd，由内核管理。 

# 🧭 进程控制

|                                  |                                         |
| -------------------------------- | --------------------------------------- |
| `fork()`                         | 创建子进程：父返 PID，子返 0，失败返 -1 |
| `execve(path, argv, envp)`       | 替换当前进程为新程序（成功不返回）      |
| `waitpid(pid, &status, options)` | 等待子进程结束，回收资源                |
| `getpid()`/`getppid()`           | 获取当前/父进程 PID                     |

> ❗ 不调用 `waitpid` 会产生**僵尸进程**。 

# 🌲 进程树

- 所有进程源自 `PID=1`（`init` 或 `systemd`）
- `fork()` 构建父子关系树
- 孤儿进程 → 被 `init` 收养
- 僵尸进程 → 子已死，父未 wait

# 💬 进程通信（IPC）

|                       |                                |
| --------------------- | ------------------------------ |
| 匿名管道`pipe(fd[2])` | 单向，父子进程间通信           |
| 有名管道（FIFO）      | 文件系统中存在，支持非亲缘进程 |
| 信号（Signal）        | 异步通知（如`SIGCHLD`）        |
| 共享内存              | 最快，需同步机制（如信号量）   |
| 消息队列              | 进程间异步消息传递             |
| Socket                | 本地或网络通信                 |
| mmap                  | 内存映射文件共享数据           |

> ❗ 进程内存隔离 → 必须通过内核机制通信。 

# 🚪 匿名管道（pipe）

- `pipe(int fd[2])`：`fd[0]` 读端，`fd[1]` 写端
- 单向通信，常用于父子进程
- 需关闭不用的端口（避免阻塞）
- 内核缓冲（通常 4KB），满则写阻塞，空则读阻塞

# 📮 有名管道（FIFO）

- `mkfifo("path", mode)` 创建
- 文件系统中可见，支持任意进程通信
- 打开方式：
  - 写端：`open(path, O_WRONLY)`
  - 读端：`open(path, O_RDONLY)`
- 读写阻塞，直到另一端就绪

