# QCWorld

一个简单的 Python 问候程序命令行工具。

## 环境要求

- Python 3.8+

## 安装

1. 克隆项目：
   ```bash
   git clone <repository-url>
   cd ssh-test
   ```

2. 创建并激活虚拟环境：
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # macOS/Linux
   # 或 .venv\Scripts\activate  # Windows
   ```

3. 安装为命令行工具（开发模式）：
   ```bash
   pip install -e .
   ```

## 运行

安装后可直接使用 `qcworld` 命令：

```bash
# 使用 --name 参数
qcworld --name "张三"

# 交互模式
qcworld

# 查看帮助
qcworld --help
```

## 项目结构

```
ssh-test/
├── README.md
├── pyproject.toml        # 项目配置与入口点声明
├── requirements.txt
└── src/
    └── qcworld/
        ├── __init__.py
        └── cli.py        # 命令行入口
```
