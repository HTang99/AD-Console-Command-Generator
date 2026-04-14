from __future__ import annotations

from pathlib import Path

from ad_ui.app import main


def read_version() -> str:
    version_path = Path(__file__).resolve().parent / "VERSION"
    try:
        return version_path.read_text(encoding="utf-8").strip()
    except OSError:
        return ""


if __name__ == "__main__":
    main(version=read_version())
