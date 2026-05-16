from __future__ import annotations

import shutil
import subprocess
import tempfile
from contextlib import contextmanager
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
FIXTURES = ROOT / "tests" / "compliance" / "fixtures"


@dataclass(frozen=True)
class FixtureWorkspace:
    root: Path
    outside_secret: Path


@contextmanager
def workspace_from_fixture(name: str, *, git: bool = True):
    with tempfile.TemporaryDirectory(prefix=f"codex-mcp-{name}-") as tmp:
        parent = Path(tmp)
        source = FIXTURES / name
        if not source.exists():
            raise AssertionError(f"Unknown compliance fixture: {name}")
        root = parent / name
        shutil.copytree(source, root, symlinks=True)
        outside_secret = parent / "outside-secret.txt"
        outside_secret.write_text((ROOT / "tests" / "compliance" / "outside-secret.txt").read_text(), encoding="utf-8")
        materialize_runtime_files(root, outside_secret, name)
        if git:
            init_git(root)
        yield FixtureWorkspace(root=root, outside_secret=outside_secret)


def materialize_runtime_files(root: Path, outside_secret: Path, name: str) -> None:
    (root / ".reference").mkdir(exist_ok=True)
    (root / ".reference" / "cache.txt").write_text("reference cache must be excluded\n", encoding="utf-8")
    (root / "node_modules" / "leftpad").mkdir(parents=True, exist_ok=True)
    (root / "node_modules" / "leftpad" / "index.js").write_text("module.exports = 1;\n", encoding="utf-8")
    (root / "dist").mkdir(exist_ok=True)
    (root / "dist" / "bundle.js").write_text("bundle output must be excluded\n", encoding="utf-8")
    (root / "ignored.log").write_text("ignored by fixture gitignore\n", encoding="utf-8")

    if name == "tiny-js-project":
        (root / "assets").mkdir(exist_ok=True)
        (root / "assets" / "raw.bin").write_bytes(b"\x00\xff\x00binary\x00")
        (root / "src" / "large.txt").write_text("0123456789abcdef\n" * 256, encoding="utf-8")
        (root / "search").mkdir(exist_ok=True)
        for index in range(12):
            (root / "search" / f"bulk_{index:02}.txt").write_text(
                f"common-token bulk line {index}\n", encoding="utf-8"
            )

    if name == "malicious-project":
        link = root / "outside-link.txt"
        if link.exists() or link.is_symlink():
            link.unlink()
        link.symlink_to(outside_secret)


def init_git(root: Path) -> None:
    run(["git", "init", "-q"], root)
    run(["git", "config", "user.email", "compliance@example.invalid"], root)
    run(["git", "config", "user.name", "Compliance Runner"], root)
    run(["git", "add", "-A"], root)
    run(["git", "commit", "-q", "-m", "baseline fixture"], root)


def run(cmd: list[str], cwd: Path) -> None:
    completed = subprocess.run(cmd, cwd=str(cwd), text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if completed.returncode != 0:
        raise AssertionError(
            f"Fixture command failed: {' '.join(cmd)}\nstdout={completed.stdout}\nstderr={completed.stderr}"
        )
