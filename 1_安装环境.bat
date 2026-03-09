@echo off
:: 设置控制台编码为UTF-8，防止中文乱码
chcp 65001 >nul
title 初始化 Python 虚拟环境

echo ========================================
echo 正在创建 Python 虚拟环境 (venv)...
echo ========================================
python -m venv venv

if not exist "venv\Scripts\activate.bat" (
    echo [错误] 虚拟环境创建失败，请检查是否正确安装了 Python 并添加到了环境变量！
    pause
    exit
)

echo.
echo ========================================
echo 正在激活虚拟环境并安装 PyInstaller...
echo ========================================
call venv\Scripts\activate
pip install -i https://pypi.tuna.tsinghua.edu.cn/simple pyinstaller

echo.
echo ========================================
echo 环境配置完成！你可以运行下一个打包脚本了。
echo ========================================
pause