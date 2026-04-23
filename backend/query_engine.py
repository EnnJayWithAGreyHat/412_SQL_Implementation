"""Helpers for compiling named SQL parameters for different adapters."""

from __future__ import annotations

import re
from typing import Any


_PARAM_PATTERN = re.compile(r":([A-Za-z_][A-Za-z0-9_]*)")


def extract_parameter_names(sql: str) -> list[str]:
    """Return placeholders in first-appearance order."""
    seen: set[str] = set()
    ordered: list[str] = []
    for match in _PARAM_PATTERN.finditer(sql):
        name = match.group(1)
        if name not in seen:
            ordered.append(name)
            seen.add(name)
    return ordered


def compile_named_query(
    sql: str,
    params: dict[str, Any] | None = None,
    *,
    dialect: str = "sqlite",
) -> tuple[str, Any]:
    """Compile a named-parameter SQL statement for SQLite or MySQL adapters."""

    params = params or {}
    parameter_names = extract_parameter_names(sql)
    missing = [name for name in parameter_names if name not in params]
    if missing:
        raise ValueError(f"Missing required SQL parameters: {', '.join(missing)}")

    if dialect == "sqlite":
        return sql, {name: params[name] for name in parameter_names}

    if dialect == "mysql":
        ordered_values: list[Any] = []

        def replacer(match: re.Match[str]) -> str:
            name = match.group(1)
            ordered_values.append(params[name])
            return "%s"

        compiled = _PARAM_PATTERN.sub(replacer, sql)
        return compiled, ordered_values

    raise ValueError(f"Unsupported SQL dialect: {dialect}")
