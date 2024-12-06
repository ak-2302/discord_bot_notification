import sys
import discord


def check_python_version():
    version = sys.version
    major = sys.version_info.major
    minor = sys.version_info.minor
    micro = sys.version_info.micro
    print(f"Python バージョン: {version}")
    print(f"バージョン情報: {major}.{minor}.{micro}")


check_python_version()
