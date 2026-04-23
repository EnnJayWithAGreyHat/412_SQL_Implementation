"""Generate output.txt from the backend verification runner."""

from __future__ import annotations

import sys
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from backend.output_generator import write_output_file


def main() -> None:
    output_path = write_output_file()
    print(f"Wrote output transcript -> {output_path}")


if __name__ == "__main__":
    main()
