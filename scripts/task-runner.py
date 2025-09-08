#!/usr/bin/env python3

import argparse
import subprocess
import sys


def test():
    """Run tests"""
    subprocess.run(["pytest"], check=True)


def edit():
    """Edit this file"""
    subprocess.run(["vim", __file__], check=True)


def dev():
    """run development server"""
    subprocess.run(["fastapi", "dev", "src/main.py"], check=True)


def lint():
    """Run linter"""
    subprocess.run(["flake8", "."], check=True)


def format_code():
    """Format code"""
    subprocess.run(["black", "."], check=True)


def main():
    parser = argparse.ArgumentParser(description="Task runner for fastapi projects")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Test command
    test_parser = subparsers.add_parser("test", help="Run tests")
    test_parser.set_defaults(func=test)

    # Lint command
    lint_parser = subparsers.add_parser("lint", help="Run linter")
    lint_parser.set_defaults(func=lint)

    # Format command
    fmt_parser = subparsers.add_parser("fmt", help="Format code")
    fmt_parser.set_defaults(func=format_code)

    # Run development server
    fmt_parser = subparsers.add_parser("dev", help="Run dev server")
    fmt_parser.set_defaults(func=dev)

    # Edit this file
    fmt_parser = subparsers.add_parser("edit", help="Edit this file")
    fmt_parser.set_defaults(func=edit)

    args = parser.parse_args()
    args.func()


if __name__ == "__main__":
    main()
