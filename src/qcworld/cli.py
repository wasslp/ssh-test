import argparse


def greet(name: str) -> str:
    return f"你好，{name}！欢迎使用 Claude 开发的程序。"


def main():
    parser = argparse.ArgumentParser(description="问候程序")
    parser.add_argument("--name", help="你的名字")
    args = parser.parse_args()

    name = args.name if args.name else input("请输入你的名字：")
    print(greet(name))


if __name__ == "__main__":
    main()
