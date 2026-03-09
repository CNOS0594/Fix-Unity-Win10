# UnityPlayer.dll SetThreadDescription 修复工具

## 📝 简介
在使用较旧版本的 Windows 10（如 1507, 1607, LTSB 2015 等）运行较新的 Unity 引擎游戏时，经常会遇到 `UnityPlayer.dll` 崩溃报错，提示找不到 `SetThreadDescription` 入口点。
这是因为该 API 是在 Win10 1607 版本才引入的。本项目通过“十六进制替换”的原理，将引擎调用的 `SetThreadDescription` 无损替换为旧系统自带的 `SetThreadPriority`，从而**完美绕过该限制，无需升级系统即可畅玩游戏！**

## 🚀小白玩家怎么用？(直接下载 EXE)
如果你不懂代码，请直接下载打包好的成品程序：
1. 前往本页面的右侧，找到 **[Releases]** 标签，下载最新的 `UnityDLL_Patcher.exe`。
2. 找到你游戏目录下的 `UnityPlayer.dll` 文件。
3. **用鼠标左键按住它，直接拖拽到 `UnityDLL_Patcher.exe` 图标上松手。**
4. 弹出黑框提示“修改成功”，并在同目录生成一个 `.bak` 备份文件。
5. 重新启动游戏即可！

## 💻 开发者/极客如何自行编译？
如果你不信任现成的 EXE，想要自己从源码编译：
1. 下载本仓库的所有源码。
2. 双击运行 `1_安装环境.bat`（会自动创建 venv 并安装 pyinstaller）。
3. 双击运行 `2_打包EXE.bat`。
4. 在生成的 `dist` 文件夹中即可找到属于你自己的 `UnityDLL_Patcher.exe`。

## ⚠️ 免责声明
本工具仅修改 DLL 中的字符串进行 API 欺骗，绝不涉及游戏逻辑修改。但**如果是带有 EAC、BattlEye 等强反作弊系统的多人联机游戏，请慎用**（反作弊系统可能会校验 DLL 文件完整性导致封号）。单机游戏请放心使用！修改前会自动生成备份文件。
