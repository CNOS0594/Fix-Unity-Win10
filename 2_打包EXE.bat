@echo off
:: 设置控制台编码为UTF-8
chcp 65001 >nul
title 打包 EXE 程序

if not exist "venv\Scripts\activate.bat" (
    echo [错误] 找不到虚拟环境！请先运行 "1_安装环境.bat"。
    pause
    exit
)

echo ========================================
echo 正在激活虚拟环境并开始打包...
echo ========================================
call venv\Scripts\activate

:: --onefile 意思是打包成单文件
:: --name 指定生成的 exe 名字
pyinstaller --onefile --name UnityDLL_Patcher patcher.py

echo.
echo ========================================
echo 打包完成！
echo ========================================
echo 请在当前目录下的 【dist】 文件夹中查找生成的 UnityDLL_Patcher.exe
echo.
pause