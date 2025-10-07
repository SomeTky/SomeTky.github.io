import os
import json
from pathlib import Path
from datetime import datetime

def build_directory_structure(base_path: str, ignore_paths=None) -> dict:
    """
    递归构建目录结构的 JSON 表示，并忽略指定路径。
    
    Args:
        base_path (str): 要扫描的根目录路径
        ignore_paths (list[str], optional): 要忽略的文件/文件夹路径列表（相对或绝对）
    
    Returns:
        dict: 符合规范的 JSON 目录结构
    """
    if ignore_paths is None:
        ignore_paths = []

    base = Path(base_path).resolve()
    if not base.is_dir():
        raise ValueError(f"路径 {base_path} 不是一个有效的目录")

    # 将忽略路径统一转换为绝对路径的 set，便于快速查找
    ignore_set = set()
    for ip in ignore_paths:
        ip_path = Path(ip)
        if not ip_path.is_absolute():
            ip_path = base / ip_path
        try:
            resolved = ip_path.resolve()
            ignore_set.add(resolved)
        except Exception:
            # 如果路径不存在，仍然加入（防止动态生成的路径被遗漏）
            ignore_set.add(ip_path.resolve(strict=False))

    def _scan(current_path: Path) -> dict:
        result = {}
        try:
            for item in current_path.iterdir():
                # 获取绝对路径用于比较
                item_abs = item.resolve()

                # 检查是否在忽略列表中
                if item_abs in ignore_set:
                    print(f"ⓘ 忽略: {item}")
                    continue

                # 获取文件/文件夹名
                name = item.name

                # 验证名称（不应包含路径分隔符）
                if '/' in name or '\\' in name:
                    print(f"⚠️ 警告：跳过非法名称的条目 '{name}'")
                    continue

                rel_path = item.relative_to(base)
                url = 'https://sometky.github.io/notes/' + str(rel_path).replace(os.sep, '/') # 这里是文件的url，正式环境记得更改为github路径

                if item.is_dir():
                    # 递归扫描子目录
                    sub_content = _scan(item)
                    # 只有当子目录内容不为空时才添加
                    if sub_content:
                        result[name] = {
                            "type": "fold",
                            "content": sub_content
                        }
                elif item.is_file():
                    # 只处理txt文件
                    if name.lower().endswith('.txt'):
                        # 获取文件修改时间并格式化为年月日
                        mtime = os.path.getmtime(item_abs)
                        formatted_time = datetime.fromtimestamp(mtime).strftime('%Y%m%d')
                        result[name] = {
                            "type": "file",
                            "url": url,
                            "time": formatted_time
                        }
                # 忽略其他类型（如符号链接、设备文件等）
        except PermissionError:
            print(f"⚠️ 权限不足，无法读取目录: {current_path}")
            result = {}  # 视为空文件夹

        return result

    return _scan(base)


def main():
    # ========== 配置区 ==========
    base_path = "C:/Users/qiuyy/Desktop/SomeTky.github.io/notes"

    # 👇 在这里添加要忽略的路径（相对于 base_path 或绝对路径）
    ignore_paths = [
        '.git'
    ]
    # ==========================

    output_file = "../tkyblog/src/content/directory_structure.json"

    if not base_path:
        print("❌ 错误：未提供有效路径")
        return

    try:
        structure = build_directory_structure(base_path, ignore_paths)
        json_output = json.dumps(structure, indent=2, ensure_ascii=False)

        # 输出到控制台
        print("\n✅ 生成的 JSON 结构：\n")
        print(json_output)

        # 保存到文件
        with open(output_file, 'w+', encoding='utf-8') as f:
            f.write(json_output)
        print(f"\n✅ 已保存到 {output_file}")

    except Exception as e:
        print(f"❌ 发生错误: {e}")
        print('当前路径是：', os.getcwd())

if __name__ == "__main__":
    print("开始生成目录结构...")
    main()