# conda

| 功能分类        | 命令                                       | 说明                                         |
| --------------- | ------------------------------------------ | -------------------------------------------- |
| 🔍 查看版本      | `conda --version`                          | 显示 Conda 版本                              |
|                 | `conda info`                               | 显示 Conda 系统信息                          |
| 📦 包管理        | `conda list`                               | 列出当前环境中的所有包                       |
|                 | `conda install 包名`                       | 安装包                                       |
|                 | `conda install 包名=版本号`                | 安装指定版本的包                             |
|                 | `conda update 包名`                        | 更新某个包                                   |
|                 | `conda remove 包名`                        | 删除某个包                                   |
| 📁 环境创建      | `conda create -n 环境名`                   | 创建新环境（默认最新 Python）                |
|                 | `conda create -n 环境名 python=版本号`     | 创建指定 Python 版本的环境，如 `python=3.12` |
| 🚪 环境激活/退出 | `conda activate 环境名`                    | 进入环境                                     |
|                 | `conda deactivate`                         | 退出当前环境                                 |
| 📜 环境查看      | `conda env list`                           | 查看所有 Conda 环境                          |
|                 | `conda info --envs`                        | 同上，列出所有环境                           |
| 🔁 环境更新      | `conda update conda`                       | 更新 Conda 本身                              |
| 🧼 环境删除      | `conda remove -n 环境名 --all`             | 删除整个环境                                 |
| ⛓ 包源配置      | `conda config --show channels`             | 显示当前配置的镜像源                         |
|                 | `conda config --add channels URL`          | 添加新的镜像源                               |
|                 | `conda config --set show_channel_urls yes` | 显示包安装来源                               |
| 📦 导出依赖      | `conda list --explicit > env.txt`          | 导出当前环境为 `.txt`（可重建环境）          |
|                 | `conda env export > environment.yml`       | 导出为 `.yml` 文件（推荐）                   |
|                 | `conda env create -f environment.yml`      | 使用 `.yml` 文件创建新环境                   |
| 🧪 临时测试包    | `conda run -n 环境名 命令`                 | 在某个环境中运行某个命令，无需激活           |

# try-except

You can use try and except to avoid system big bang, and use except Exception as e then print str(e) to get the details of why the system went error.

```python
try:
    # your code
except Exception as e:
    print(str(e))
```

# pathlib.Path

`pathlib.Path` 是 `pathlib` 模块中的一个类，表示一个文件或目录的路径。

> ✅ 推荐在新项目中使用 `Path` 替代 `os` 和 `os.path`。 

### 1. 导入并创建 Path 对象

```python
from pathlib import Path

# 创建路径对象（不检查文件是否存在）
path = Path("my_folder/my_file.txt")
```

支持绝对路径或相对路径：

```python
Path("/home/user/documents")  # Linux/macOS 绝对路径
Path(r"C:\Users\John\Documents")  # Windows 绝对路径（注意 r 前缀）
Path(".")  # 当前目录
Path("..")  # 上一级目录
```

### 2. 常用属性和方法

#### ✅ `.name`：获取文件名（含扩展名）

```python
p = Path("docs/readme.md")
print(p.name)        # 输出: readme.md
```

#### ✅ `.stem`：文件名（不含扩展名）

```python
print(p.stem)        # 输出: readme
```

#### ✅ `.suffix`：扩展名

```python
print(p.suffix)      # 输出: .md
```

#### ✅ `.parent`：父目录

```python
print(p.parent)      # 输出: docs
print(p.parent.parent)  # 上两级
```

#### ✅ `.rename`：重命名

```python
from pathlib import Path

# 假设有一个文件：old_name.txt
path = Path("old_name.txt")

# 重命名为 new_name.txt
path.rename("new_name.txt")
```



#### ✅ `.exists()`：检查路径是否存在

```python
if p.exists():
    print("文件存在")
```

#### ✅ `.is_file()` 和 `.is_dir()`：判断是文件还是目录

```python
p.is_file()   # 是否是文件
p.is_dir()    # 是否是目录
```

### 3. 路径拼接（推荐方式）

使用 `/` 运算符拼接路径，非常直观！

```python
folder = Path("data")
file_path = folder / "images" / "photo.jpg"
print(file_path)  # data/images/photo.jpg（Windows 上会自动变成反斜杠）
```

### 4. 读写文件（无需 open/close）

#### 读取文本文件 `.read_text()`

```python
content = Path("hello.txt").read_text(encoding="utf-8")
print(content)
```

#### 写入文本文件 `.write_text()`

```python
Path("output.txt").write_text("Hello, pathlib!", encoding="utf-8")
```

#### 读取/写入字节 `.read_bytes()` / `.write_bytes()`

```python
data = Path("image.png").read_bytes()
Path("copy.png").write_bytes(data)
```

### 5. 创建目录

```python
Path("new_folder/subfolder").mkdir(parents=True, exist_ok=True)
```

- `parents=True`：自动创建中间目录
- `exist_ok=True`：如果已存在不报错

### 6. 遍历目录（glob 模式）

#### 列出所有 `.py` 文件

```python
for pyfile in Path(".").glob("*.py"):
    print(pyfile)
```

#### 递归查找（包括子目录）

```python
for pyfile in Path(".").rglob("*.py"):
    print(pyfile)
```

#### 查找特定结构

```python
Path("docs").glob("*.md")           # 当前目录下的 .md 文件
Path("docs").glob("**/*.md")        # 递归查找（等同于 rglob）
```

### 7. 获取文件信息

```python
p = Path("example.txt")

print(p.stat().st_size)      # 文件大小（字节）
print(p.stat().st_mtime)     # 修改时间（时间戳）

# 更现代的方式：使用 path.stat() 或 path.lstat()
```

### 8. 其他实用方法

| `p.resolve()`            | 返回绝对路径（解析`..`和`.`）   |
| ------------------------ | ------------------------------- |
| `p.absolute()`           | 返回绝对路径（不解析符号链接）  |
| `p.rename(target)`       | 重命名/移动文件                 |
| `p.unlink()`             | 删除文件（相当于`os.remove()`） |
| `p.rmdir()`              | 删除空目录                      |
| `p.with_name("new.txt")` | 替换文件名                      |
| `p.with_suffix(".log")`  | 替换扩展名                      |

# 正则表达式提取字符串数字

```python
import re

def get_trailing_digits(s):
    match = re.search(r'(\d+)$', s)
    return match.group(1) if match else None

# 示例
print(get_trailing_digits("abc123"))        # 输出: 123
print(get_trailing_digits("file_007"))      # 输出: 007
print(get_trailing_digits("price: 456"))    # 输出: 456
print(get_trailing_digits("no_digits"))     # 输出: None
print(get_trailing_digits("version2.3.1"))  # 输出: 1
```

- `\d+`：匹配一个或多个数字（0-9）
- `$`：表示字符串的**结尾**
- `()`：捕获括号，把匹配的数字提取出来
- `re.search()`：在整个字符串中查找符合模式的部分

> 因为 `$` 的存在，只会匹配**结尾处的连续数字** 

### 💡 提示

- 返回的是字符串，如需转整数：`int(match.group(1))`
- 使用 `group(1)` 获取捕获组内容，避免返回整个匹配对象

```python
num_str = match.group(1)      # 字符串 "123"
num_int = int(match.group(1)) # 整数 123
```

# 生成唯一id

uuid



# flask事件流的一种优化方案

```python
import queue
import json
import threading

# 创建线程安全的消息队列
event_queue = queue.Queue()

def event_stream():
    """SSE 事件流生成器"""
    while True:
        try:
            # 阻塞等待新事件（可设置超时）
            data = event_queue.get(timeout=30)  # 30秒超时，避免连接长时间挂起
            yield f"data: {json.dumps(data)}\n\n"
        except queue.Empty:
            # 发送心跳，防止连接断开
            yield ":\n\n"  # 注释行，保持连接
            continue

# 更新房间
def update_room():
    event_queue.put({'type': 'update-room'})

# 更新状态
def update_status():
    event_queue.put({'type': 'update-status'})
```

上面列出的仅为样例代码，实际上queue是一个消费性队列，无法处理多个连接的情况，实际应用时建议针对每一个连接创建一个queue。