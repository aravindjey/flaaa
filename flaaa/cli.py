#!/usr/bin/env python3
"""flaaa CLI - List, view, and export Flutter experiment files."""

import sys
import argparse
from pathlib import Path

try:
    from importlib import resources
except ImportError:
    import importlib_resources as resources  # type: ignore

EXPERIMENTS = [
    (1, "Basic Flutter App", "Welcome screen with Icon, Text, and ElevatedButton"),
    (2, "Responsive UI", "LayoutBuilder adapting UI to screen dimensions"),
    (3, "User Input", "TextField, TextEditingController, and SnackBar feedback"),
    (4, "Image Asset App", "Image.asset rendering with pubspec.yaml asset configuration"),
    (5, "Multi-Screen Navigation", "Screen routing using Navigator.push and MaterialPageRoute"),
    (6, "Animation", "Smooth state animations using AnimatedContainer"),
    (7, "State Management", "Interactive counter with StatefulWidget and setState"),
    (8, "SQLite Database", "Local database storage with sqflite and path packages"),
    (9, "HTTP REST API", "Asynchronous network request using http package"),
    (10, "Flutter CLI & Build", "Terminal commands for doctor, create, run, and build APK"),
]


def _get_experiment_content(num: int) -> str:
    filename = f"exp{num}.txt"
    try:
        if sys.version_info >= (3, 9):
            ref = resources.files("flaaa.experiments").joinpath(filename)
            return ref.read_text(encoding="utf-8")
        else:
            return resources.read_text("flaaa.experiments", filename, encoding="utf-8")
    except Exception:
        # Fallback to relative path lookup
        local_path = Path(__file__).resolve().parent / "experiments" / filename
        if local_path.exists():
            return local_path.read_text(encoding="utf-8")
        root_path = Path(__file__).resolve().parent.parent / filename
        if root_path.exists():
            return root_path.read_text(encoding="utf-8")
        raise FileNotFoundError(f"Could not locate {filename}")


def list_experiments() -> None:
    print("\n" + "=" * 65)
    print("                     FLUTTER EXPERIMENTS")
    print("=" * 65)
    print(f"{'#':<4} {'Title':<26} {'Description'}")
    print("-" * 65)
    for num, title, desc in EXPERIMENTS:
        print(f"[{num:>2}] {title:<26} {desc}")
    print("=" * 65)
    print("Usage tips:")
    print("  flaaa <number>          View code for an experiment (e.g. flaaa 1)")
    print("  flaaa save <number>     Save experiment file locally (e.g. flaaa save 1)")
    print("  flaaa save all          Save all 10 experiment files to current directory")
    print("=" * 65 + "\n")


def show_experiment(num: int) -> None:
    if num < 1 or num > 10:
        print(f"Error: Experiment #{num} not found. Valid range is 1-10.", file=sys.stderr)
        sys.exit(1)

    title = next((t for n, t, _ in EXPERIMENTS if n == num), "")
    content = _get_experiment_content(num)
    print(f"\n--- Experiment {num}: {title} (exp{num}.txt) ---")
    print(content.strip())
    print("-" * 60 + "\n")


def save_experiment(target: str) -> None:
    cwd = Path.cwd()
    if target.lower() == "all":
        for num in range(1, 11):
            content = _get_experiment_content(num)
            out_file = cwd / f"exp{num}.txt"
            out_file.write_text(content, encoding="utf-8")
            print(f"Saved: {out_file.name}")
        print("\nAll 10 experiments saved to current directory.")
    else:
        try:
            num = int(target)
            if num < 1 or num > 10:
                raise ValueError
        except ValueError:
            print(f"Error: Invalid experiment '{target}'. Specify 1-10 or 'all'.", file=sys.stderr)
            sys.exit(1)

        content = _get_experiment_content(num)
        out_file = cwd / f"exp{num}.txt"
        out_file.write_text(content, encoding="utf-8")
        print(f"Saved: {out_file.name}")


def main() -> None:
    args = sys.argv[1:]

    # Default invocation: list all experiments
    if not args or args[0] in ("list", "-l", "--list"):
        list_experiments()
        return

    # Check for direct number shorthand: e.g. "flaaa 1" or "flaaa 10"
    if len(args) == 1 and args[0].isdigit():
        show_experiment(int(args[0]))
        return

    parser = argparse.ArgumentParser(
        prog="flaaa",
        description="CLI tool to list, view, and export Flutter experiments (1-10)."
    )
    subparsers = parser.add_subparsers(dest="command")

    # 'list' subcommand
    subparsers.add_parser("list", help="List all 10 Flutter experiments")

    # 'show' subcommand
    show_parser = subparsers.add_parser("show", help="Display the code of a specific experiment")
    show_parser.add_argument("number", type=int, help="Experiment number (1-10)")

    # 'save' subcommand
    save_parser = subparsers.add_parser("save", help="Save experiment(s) as file(s) in current directory")
    save_parser.add_argument("target", help="Experiment number (1-10) or 'all'")

    parsed = parser.parse_args(args)

    if parsed.command == "list" or not parsed.command:
        list_experiments()
    elif parsed.command == "show":
        show_experiment(parsed.number)
    elif parsed.command == "save":
        save_experiment(str(parsed.target))
    else:
        list_experiments()


if __name__ == "__main__":
    main()
