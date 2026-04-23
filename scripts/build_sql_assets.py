"""Generate the root SQL assignment files from the canonical backend catalog."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.sql_assets import write_project_sql_assets


def main() -> None:
    written_files = write_project_sql_assets()
    for filename, path in written_files.items():
        print(f"Wrote {filename} -> {path}")


if __name__ == "__main__":
    main()
