# SSH Test

一个简单的 Python 问候程序。

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

3. 安装依赖（如有）：
   ```bash
   pip install -r requirements.txt
   ```

## 运行

```bash
python src/main.py
```

程序会提示你输入名字，然后输出问候语。

## 项目结构

```
ssh-test/
├── README.md
├── src/
│   └── main.py      # 程序入口
└── .venv/           # 虚拟环境
```
