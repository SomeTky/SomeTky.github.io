# 官方接口生成图片

在 Unity 中，你可以使用官方提供的接口来生成图片（例如截图、渲染纹理保存为图片等）。Unity 提供了 `ScreenCapture` 类（推荐）以及 `Texture2D` 的 `EncodeToPNG` / `EncodeToJPG` 方法来实现图片生成和保存。



以下是几种常见的生成图片的方式：

### ✅ 方法一：使用 `ScreenCapture.CaptureScreenshot`（推荐，最简单）

这是 Unity 官方推荐的方式，用于截取当前屏幕画面并保存为图片。

```c#
using UnityEngine;

public class ScreenshotTaker : MonoBehaviour
{
    public void TakeScreenshot()
    {
        // 参数：文件名（含路径），截图质量（对 JPG 有效，PNG 无效）
        ScreenCapture.CaptureScreenshot("MyScreenshot.png");
        Debug.Log("截图已保存为 MyScreenshot.png");
    }

    // 示例：按下键盘 S 键截图
    void Update()
    {
        if (Input.GetKeyDown(KeyCode.S))
        {
            TakeScreenshot();
        }
    }
}
```

📌 说明： 

- 文件会保存在项目的根目录（与 `Assets` 同级）。
- 支持 `.png`、`.jpg`、`.tga` 等格式。
- 可以添加时间戳避免覆盖：
- 这种方法生成的图像分辨率与运行窗口是一致的，无法做到$1920 \times 1080$的运行窗口生成$1280 \times 1280$的图片

```c#
ScreenCapture.CaptureScreenshot($"Screenshots/Screenshot_{System.DateTime.Now:yyyyMMdd_HHmmss}.png");
```

### ✅ 方法二：使用 `RenderTexture` + `Texture2D` 手动渲染并保存

适用于自定义相机渲染、UI 截图、或非主屏幕内容。

```c#
using UnityEngine;
using System.IO;

public class CustomRenderScreenshot : MonoBehaviour
{
    public Camera renderCamera;  // 要截图的相机
    public int width = 1920;
    public int height = 1080;

    public void CaptureCamera()
    {
        // 创建 RenderTexture
        RenderTexture rt = new RenderTexture(width, height, 24);
        renderCamera.targetTexture = rt;

        // 渲染一帧
        renderCamera.Render();

        // 激活 RenderTexture 并复制到 Texture2D
        RenderTexture.active = rt;
        Texture2D screenShot = new Texture2D(width, height, TextureFormat.RGB24, false);
        screenShot.ReadPixels(new Rect(0, 0, width, height), 0, 0);
        screenShot.Apply();

        // 恢复状态
        renderCamera.targetTexture = null;
        RenderTexture.active = null;
        Object.Destroy(rt);

        // 编码为 PNG 并保存
        byte[] bytes = screenShot.EncodeToPNG();
        string filePath = Path.Combine(Application.dataPath, "Screenshots", $"Custom_{System.DateTime.Now:yyyyMMdd_HHmmss}.png");
        
        // 确保目录存在
        Directory.CreateDirectory(Path.GetDirectoryName(filePath));
        
        File.WriteAllBytes(filePath, bytes);
        Debug.Log("截图已保存: " + filePath);
    }
}
```

⚠️ 注意： 

- `Texture2D.ReadPixels` 只能在主 OpenGL 纹理上使用，不能直接读取 `RenderTexture`，所以需要 `RenderTexture.active`。
- 在 WebGL 上不支持 `ReadPixels`，此方法仅适用于 PC/Android/iOS 等平台。

### ✅ 方法三：截图 UI（使用 `RectTransform` 裁剪区域）

如果你只想截图 UI 的某一部分，可以使用 `RenderTexture` 结合 `Camera` 或 `GraphicRaycaster`，或者使用 `Canvas` 的 `ScreenSpace - Camera` 模式。



或者使用 `UnityEngine.UI.Image` + `RawImage` 配合截图。

### ✅ 方法四：保存 Texture2D 为图片（已有纹理）

```c#
Texture2D tex = ...; // 你的纹理
byte[] bytes = tex.EncodeToPNG(); // 或 EncodeToJPG(quality)
File.WriteAllBytes(Application.dataPath + "/SavedTexture.png", bytes);
```

⚠️ 注意：`EncodeToPNG` 要求纹理是可读的（在导入设置中勾选 "Read/Write Enabled"）。 





# 添加静态模型

------

### ✅ 1. **普通静态模型（如建筑、石头、家具）**

→ 添加：**Mesh Filter + Mesh Renderer**



| 组件              | 作用                                 |
| ----------------- | ------------------------------------ |
| **Mesh Filter**   | 用于存储或引用模型的网格数据（Mesh） |
| **Mesh Renderer** | 用于将网格渲染到场景中（配合材质）   |



📌 操作步骤：

1. 在 Hierarchy 中创建空 GameObject
2. 添加组件：
   - `Add Component` → **Mesh Filter**
   - `Add Component` → **Mesh Renderer**
3. 将模型（如 `.fbx` 文件）从 Project 窗口拖到 **Mesh Filter 的 Mesh 字段**
4. 为 **Mesh Renderer** 分配材质（Material）



> 🔗 官方文档：
> https://docs.unity3d.com/Manual/class-MeshFilter.html
> [https://docs.unity3d.com/Manual/class-MeshRenderer.html ](https://docs.unity3d.com/Manual/class-MeshRenderer.html)

# 按键控制

```c#
void Update()
    {
        if (Input.GetKeyDown(KeyCode.S))
        {
            //这里填写按键按下后的逻辑
        }
    }
```

# 获取当前工作目录

在 Unity 中，你可以通过 `System.Environment` 或 `Directory.GetCurrentDirectory()` 来**输出当前工作目录（Working Directory）**。

### ✅ 方法一：使用 `Directory.GetCurrentDirectory()`

```c#
using System.IO;
using UnityEngine;

public class PrintWorkingDirectory : MonoBehaviour
{
    void Start()
    {
        string currentDir = Directory.GetCurrentDirectory();
        Debug.Log("当前工作目录: " + currentDir);
    }
}
```

### ✅ 方法二：使用 `System.Environment`

```c#
using UnityEngine;

public class PrintWorkingDirectory : MonoBehaviour
{
    void Start()
    {
        string currentDir = System.Environment.CurrentDirectory;
        Debug.Log("当前工作目录: " + currentDir);
    }
}
```

### 🔍 补充：常用路径对比

| 路径               | 代码                              | 说明                       |
| ------------------ | --------------------------------- | -------------------------- |
| **当前工作目录**   | `Directory.GetCurrentDirectory()` | 项目根目录                 |
| **Assets 目录**    | `Application.dataPath`            | `.../YourProject/Assets`   |
| **持久化数据目录** | `Application.persistentDataPath`  | 平台相关，用于保存用户数据 |
| **临时缓存目录**   | `Application.temporaryCachePath`  | 临时文件                   |