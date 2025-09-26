# 学习路线

## 🎯 学习目标

- 掌握虚幻引擎5的核心功能
- 熟练使用 C++ 进行游戏逻辑开发
- 理解 UE5 的架构（如 Gameplay Framework、Actor、Component 等）
- 能够结合蓝图与 C++ 协同开发
- 能独立开发中小型 3D 游戏项目



------



## 📚 学习路线（分阶段）

------



### 🔹 阶段一：基础准备（1-2周）

#### 1. 编程基础（C++）

- **目标**：掌握 C++ 基础语法，理解面向对象编程（OOP）
- 学习内容
  - 变量、控制结构、函数
  - 指针、引用、动态内存管理（new/delete）
  - 类、继承、多态、构造/析构函数
  - STL 基础（vector, string, map）
  - RAII、智能指针（unique_ptr, shared_ptr）
- 推荐资源
  - 《C++ Primer》（第5版）
  - B站：[侯捷C++课程](https://www.bilibili.com/video/BV1kb411Q7Kn)
  - [LearnCpp.com ](https://www.learncpp.com/)（免费）



> ✅ 重点：UE5 使用的是 **C++17 标准**，且有自己的宏系统（如 `UCLASS`, `UFUNCTION`），但底层仍是标准 C++。 



------



### 🔹 阶段二：UE5 入门与蓝图（2-3周）

#### 1. 安装与环境配置

- 下载 Epic Games Launcher，安装 UE5（建议使用 5.3 或更新稳定版）
- 配置 Visual Studio（推荐 VS2022）用于 C++ 开发
- 创建第一个 C++ 项目（选择 "C++" 而非 "Blueprint" 项目）



#### 2. 学习 UE5 编辑器基础

- 界面介绍：Viewport、Content Browser、World Outliner、Details
- 场景构建：放置 Actor、调整 Transform
- 材质、灯光、地形系统（Landscape）、Nanite、Lumen 初步了解



#### 3. 蓝图可视化编程

- 为什么学蓝图？C++ 和蓝图协同开发是 UE 的核心模式
- 学习内容：
  - 蓝图类（Blueprint Class）
  - 变量、函数、事件（Event Graph）
  - 控制流（Branch, ForEach, Delay）
  - 与 C++ 的交互（暴露变量/函数给蓝图）
- 推荐资源
  - 官方文档：[Unreal Engine Blueprint 虚幻蓝图](https://docs.unrealengine.com/5.3/en-US/blueprints-api-programming-guide/)
  - YouTube/B站搜索 “UE5 蓝图入门”



> ✅ 目标：能用蓝图实现简单的角色移动、UI 显示、交互逻辑 



------



### 🔹 阶段三：C++ 与 UE5 框架深度学习（4-6周）

#### 1. UE5 C++ 基础语法与宏系统

- 理解 UE 的反射系统（UObject、UCLASS、UFUNCTION、UPROPERTY）
- 创建第一个 C++ 类（继承自 `AActor` 或 `APawn`）
- 编译流程与模块系统（Build.cs 文件）



#### 2. 核心 Gameplay 框架

- Gameplay Framework
  - `AActor`：场景中一切可放置的对象
  - `UActorComponent`：组件化设计（如 `USpringArmComponent`, `UCameraComponent`）
  - `AController`：控制 Pawn（如 `APlayerController`）
  - `APawn` / `ACharacter`：可被控制的角色
  - `AGameModeBase`：游戏规则
  - `APlayerState` / `AGameStateBase`：状态管理



#### 3. 实战：创建 C++ 角色类

- 继承 `ACharacter`，实现移动、跳跃
- 添加摄像机（SpringArm + Camera）
- 暴露变量给蓝图（`UPROPERTY(BlueprintReadWrite)`）
- 绑定输入（在 `SetupPlayerInputComponent` 中使用 `BindAction`, `BindAxis`）



#### 4. 内存管理与智能指针

- `TSharedPtr`, `TUniquePtr`, `TWeakPtr`
- `UObject` 的 GC 管理（`UObject` 派生类自动垃圾回收）
- 避免循环引用



#### 5. 委托（Delegates）与事件系统

- `TDelegate`, `TMultiCastDelegate`
- 实现事件通知机制（如角色死亡广播）



> ✅ 推荐项目：用 C++ 实现一个可移动的角色，带摄像机跟随和输入响应 



------



### 🔹 阶段四：高级功能与系统设计（4-6周）

#### 1. 物理与碰撞

- 碰撞通道（Collision Channel）
- `OnComponentHit` / `OnComponentBeginOverlap`
- 简单物理模拟（RigidBody）



#### 2. UI 系统（UMG）

- 使用 `UUserWidget` 创建 HUD、菜单
- C++ 控制 UI 更新（如血条、分数）
- 绑定事件（按钮点击响应）



#### 3. 动画系统（Skeletal Mesh & Animation Blueprint）

- 使用 `UAnimInstance` 控制动画状态机
- C++ 与动画蓝图通信（如设置 `Speed` 变量驱动动画）



#### 4. 游戏状态与数据管理

- `SaveGame` 系统（保存/读取游戏进度）
- `GameInstance`：跨关卡数据存储
- 数据表（Data Table）与曲线（Curve）



#### 5. 多人游戏基础（可选）

- 网络同步（Replication）
- `ROLE_Authority`, `ROLE_AutonomousProxy`
- RPC（Remote Procedure Call）



> ✅ 推荐项目：实现一个带血条、UI、动画、存档功能的小型第三人称游戏 



------



### 🔹 阶段五：项目实战（4-8周）

#### 项目建议：开发一个小型 3D 游戏

- 类型：第三人称射击 / 平台跳跃 / 解谜游戏
- 必须包含：
  - C++ 主导的游戏逻辑
  - 角色控制、摄像机、UI
  - 物理交互（门、开关、可拾取物）
  - 音效、粒子效果（Niagara）
  - 蓝图与 C++ 协同使用
  - 打包发布（Standalone 或 Windows）



#### 推荐参考：

- Epic 官方示例：

  Lyra Starter Game

  （UE5.3+ 推荐学习）

  - 包含完整角色系统、输入、UI、网络架构
  - GitHub 开源，适合进阶学习

- **Action RPG** 示例项目（UE Marketplace 免费）



------



### 🔹 阶段六：持续进阶（长期）

#### 1. 深入引擎源码

- 编译 UE5 源码版本（从 GitHub 下载）
- 阅读核心模块源码（如 Engine、GameplayAbilities）
- 自定义引擎功能（高级）



#### 2. 插件开发

- 创建自己的 C++ 插件（Plugin）
- 扩展编辑器功能（Editor Utility Widget）



#### 3. 性能优化

- Profiling（Unreal Insights）
- 内存优化、GC 调优
- Niagara 粒子性能、LOD 设置



#### 4. 工具链与自动化

- 使用 Python 编写编辑器脚本（Unreal Python）
- 自动化构建与 CI/CD

## 📚 推荐学习资源

| 类型         | 资源                                                         |
| ------------ | ------------------------------------------------------------ |
| **官方文档** | [docs.unrealengine.com](https://docs.unrealengine.com/)（必看） |
| **视频教程** | Unreal Engine 官方 YouTube 频道、Mathew Wadstein（Twitch）、夸克课堂（B站） |
| **书籍**     | 《Unreal Engine 5 游戏开发实战》、《C++ Primer》             |
| **社区**     | Unreal Slackers Discord、Unreal Forums、知乎、CSDN           |
| **代码示例** | GitHub 搜索 "UE5 C++ tutorial"、Epic 的 Sample Games         |

## 🎉 总结：学习路线图

```
C++ 基础 → UE5 编辑器 + 蓝图 → C++ 与 Gameplay 框架 → 高级系统 → 项目实战 → 深入源码
```







# 实用函数

## 获取actor世界坐标

| 函数                  | 说明                                         |
| --------------------- | -------------------------------------------- |
| `GetActorLocation()`  | 获取 Actor 的世界坐标                        |
| `GetActorRotation()`  | 获取 Actor 的世界旋转（FRotator）            |
| `GetActorScale()`     | 获取 Actor 的缩放                            |
| `GetActorTransform()` | 获取完整的世界变换（T = 位置 + 旋转 + 缩放） |

## 获取场景中对象

```c++
void AReceiverAircraft::InitSkyLight()
{
	UWorld* World = GetWorld();
	if (!World) return;

	TArray<AActor*> FoundActors;
	UGameplayStatics::GetAllActorsOfClass(World, ASkyLight::StaticClass(), FoundActors);

	for (AActor* Actor : FoundActors)
	{
		skyLight = Cast<ASkyLight>(Actor);
		if (skyLight)
		{
			PrintMessage(FString("成功找到 SkyLight: ") + skyLight->GetName());
			break;
		}
	}
}
```



## 输出信息到屏幕上

使用 `GEngine->AddOnScreenDebugMessage`

```c++

GEngine->AddOnScreenDebugMessage(
    -1,                       // Key: -1 表示每帧刷新（不覆盖旧消息）
    0.0f,                     // 显示时间（0.0f 表示持续显示）
    FColor::Green,            // 文本颜色
    FString::Printf(TEXT("Player Location: X=%.2f, Y=%.2f, Z=%.2f"), 
                    Location.X, Location.Y, Location.Z)  // 内容
);

```

| 参数            | 说明                                                         |
| --------------- | ------------------------------------------------------------ |
| `-1`            | 消息 ID，-1 表示每帧刷新，不重复覆盖；可以用其他数字控制不同行 |
| `0.0f`          | 显示时间（秒），0 表示持续显示                               |
| `FColor::Green` | 颜色（可选`Red`,`Blue`,`Yellow`等）                          |
| `FString`       | 要显示的文本                                                 |

## 整形转FString

✅ 方法 1：使用 `FString::FromInt()`（最简单）

```c++
int32 MyInt = 123;
FString MyString = FString::FromInt(MyInt);

// 输出示例
GEngine->AddOnScreenDebugMessage(-1, 5.0f, FColor::Green, MyString);
```

> ✅ 适用于 `int32`、`int16`、`int64` 等整数类型。 

✅ 方法 2：使用 `FString::Printf()`（更灵活，支持格式化）

```c++
int32 MyInt = 456;
FString MyString = FString::Printf(TEXT("Score: %d"), MyInt);
```

你也可以只转换整数：

```c++
FString MyString = FString::Printf(TEXT("%d"), MyInt);
```

> 🌟 优点：可以和其他文本一起格式化输出，适合调试或 UI 显示。 



## 游戏结束运行

### ✅ 方法一：使用 `UKismetSystemLibrary::QuitGame()`（推荐）

这是最标准、最安全的方式，适用于客户端、服务器、独立进程等。

示例代码：

```c++
#include "Kismet/KismetSystemLibrary.h"
#include "Engine/World.h"

void UMyBlueprintFunctionLibrary::ExitGame(UObject* WorldContextObject)
{
    if (UWorld* World = GEngine->GetWorldFromContextObject(WorldContextObject, EGetWorldErrorMode::LogAndReturnNull))
    {
        UKismetSystemLibrary::QuitGame(
            World,
            EQuitPreference::Quit,
            true // bIgnoreAllWarnings = 是否忽略警告（如未保存）
        );
    }
}
```

✅ 说明： 

- `WorldContextObject`：通常传入一个 Actor 或 PlayerController
- `EQuitPreference::Quit`：表示立即退出
- `true` 表示忽略所有警告（比如“是否保存”）



# 内置数据结构

在 **Unreal Engine 5 (UE5)** 中，数据结构是游戏开发中组织和管理数据的核心工具。UE5 提供了一套高效、类型安全且与引擎深度集成的容器类（数据结构），适用于 C++ 编程和蓝图交互。

✅ UE5 主要数据结构概览

| 数据结构                              | 用途                   | 类似c++标准库              |
| ------------------------------------- | ---------------------- | -------------------------- |
| `TArray<T>`                           | 动态数组（最常用）     | `std::vector<T>`           |
| `TSet<T>`                             | 无序唯一集合           | `std::unordered_set<T>`    |
| `TMap<K, V>`                          | 键值对映射（字典）     | `std::unordered_map<K, V>` |
| `TQueue<T>`                           | 队列（先进先出）       | `std::queue<T>`            |
| `TStack<T>`                           | 栈（后进先出）         | `std::stack<T>`            |
| `TLinkedList<T>`                      | 链表（节点式）         | `std::list<T>`（较少用）   |
| `TMultiMap<K, V>`                     | 一键多值映射           | ——                         |
| `TSparseArray<T>`/`TIndirectArray<T>` | 高效内存管理（底层用） | ——                         |

### 1. `TArray<T>` —— 动态数组（最常用）

**特点**：自动扩容、支持索引访问、高效尾部插入。

```c++
TArray<int32> Numbers;
Numbers.Add(1);
Numbers.Add(2);
Numbers.Add(3);

for (int32 Num : Numbers)
{
    UE_LOG(LogTemp, Warning, TEXT("Number: %d"), Num);
}
```

📌 **常用操作**：

- `Add()` / `Emplace()`：添加
- `Num()`：获取数量
- `IsEmpty()`：是否为空
- `Remove()` / `RemoveAt()`：删除
- `Find()`：查找
- `[]`：索引访问



> ✅ 推荐用于大多数“列表”场景，如物品栏、敌人列表等。 

### 2. `TSet<T>` —— 无序唯一集合

**特点**：元素不重复，插入/查找快（哈希实现）。

```c++
TSet<FString> PlayerNames;
PlayerNames.Add(TEXT("Alice"));
PlayerNames.Add(TEXT("Bob"));
PlayerNames.Add(TEXT("Alice")); // 不会重复添加

if (PlayerNames.Contains(TEXT("Alice")))
{
    UE_LOG(LogTemp, Warning, TEXT("Player exists!"));
}
```

📌 适合：去重、成员检测、标签系统。

### 3. `TMap<K, V>` —— 键值对映射（字典）

**特点**：通过键快速查找值。

```c++
TMap<FString, int32> Scores;
Scores.Add(TEXT("Alice"), 95);
Scores.Add(TEXT("Bob"), 87);

int32* ScorePtr = Scores.Find(TEXT("Alice"));
if (ScorePtr)
{
    UE_LOG(LogTemp, Warning, TEXT("Score: %d"), *ScorePtr);
}
```

📌 适合：ID 映射、配置表、缓存系统。

### 4. `TQueue<T>` —— 队列（FIFO）

**特点**：先进先出，常用于任务调度、消息系统。

```c++
TQueue<FString> MessageQueue;
MessageQueue.Enqueue(TEXT("Hello"));
MessageQueue.Enqueue(TEXT("World"));

FString Message;
if (MessageQueue.Dequeue(Message))
{
    UE_LOG(LogTemp, Warning, TEXT("Dequeued: %s"), *Message); // 输出 Hello
}
```

📌 适合：事件队列、网络包处理。

### 5. `TStack<T>` —— 栈（LIFO）

**特点**：后进先出。

```c++
TStack<int32> Stack;
Stack.Push(1);
Stack.Push(2);
int32 Top;
if (Stack.Pop(Top))
{
    UE_LOG(LogTemp, Warning, TEXT("Popped: %d"), Top); // 输出 2
}
```

📌 适合：撤销操作、递归替代、路径回溯。

### 6. `TMultiMap<K, V>` —— 一键多值

**特点**：一个键可以对应多个值。

```c++
TMultiMap<FString, FString> Tags;
Tags.Add(TEXT("Weapon"), TEXT("Rifle"));
Tags.Add(TEXT("Weapon"), TEXT("Pistol"));
Tags.Add(TEXT("Armor"),  TEXT("Helmet"));

for (const auto& It : Tags)
{
    UE_LOG(LogTemp, Warning, TEXT("Key: %s, Value: %s"), *It.Key, *It.Value);
}
```

📌 适合：标签系统、多属性绑定。



