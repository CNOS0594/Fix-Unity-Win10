import sys
import os
import shutil

def patch_dll(file_path):
    print("="*50)
    print(" UnityPlayer.dll 修复工具 (SetThreadDescription)")
    print("="*50)
    
    # 目标字节和替换字节（长度严格保持一致：20字节）
    target = b"SetThreadDescription"
    replacement = b"SetThreadPriority\x00\x00\x00"

    if not os.path.isfile(file_path):
        print(f"[错误] 找不到文件: {file_path}")
        return

    # 1. 自动备份原文件
    backup_path = file_path + ".bak"
    try:
        shutil.copy2(file_path, backup_path)
        print(f"[成功] 原文件已备份至: \n{backup_path}")
    except Exception as e:
        print(f"[错误] 创建备份失败，无法继续操作: {e}")
        return

    # 2. 读取并替换
    try:
        with open(file_path, 'rb') as f:
            content = f.read()

        if target not in content:
            print("[提示] 未在文件中找到 'SetThreadDescription'。")
            print("文件可能已经被修改过，或者不需要修改。")
            return

        # 替换所有匹配的字符串
        new_content = content.replace(target, replacement)

        with open(file_path, 'wb') as f:
            f.write(new_content)

        print("-" * 50)
        print("[大功告成] SetThreadDescription 已成功替换为 SetThreadPriority！")
        print("现在你可以尝试启动游戏了。")
        print("-" * 50)
        
    except PermissionError:
        print("[错误] 权限被拒绝！请确保游戏没有在运行，且文件没有被占用。")
    except Exception as e:
        print(f"[错误] 处理文件时发生未知错误: {e}")

if __name__ == "__main__":
    # sys.argv[0] 是脚本自身，sys.argv[1] 是拖入的文件路径
    if len(sys.argv) < 2:
        print("【用法说明】")
        print("请不要直接双击打开此程序！")
        print("请将需要修改的 UnityPlayer.dll 文件【拖放】到本程序的图标上。")
    else:
        file_path = sys.argv[1]
        patch_dll(file_path)
    
    print("\n")
    input("按回车键退出程序...")