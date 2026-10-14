"""Validate and synchronize the repository's installed portable SEO skills."""
from __future__ import annotations

import argparse
import hashlib
import json
import shutil
from pathlib import Path
from urllib.request import urlopen


def git_hash(data: bytes) -> str:
    return hashlib.sha1(b"blob " + str(len(data)).encode("ascii") + b"\0" + data).hexdigest()


def within(root: Path, relative: str) -> Path:
    root = root.resolve()
    target = (root / relative).resolve()
    if not target.is_relative_to(root):
        raise ValueError("Path escapes workspace: " + relative)
    return target


def check(root: Path, manifest: dict) -> list[str]:
    errors = []
    for item in manifest["files"]:
        path = within(root, item["path"])
        if not path.is_file():
            errors.append("missing source: " + item["path"])
        elif git_hash(path.read_bytes()) != item["git_blob_sha"]:
            errors.append("source hash mismatch: " + item["path"])
    ids = [skill["id"] for skill in manifest["skills"]]
    if len(ids) != len(set(ids)):
        errors.append("duplicate skill ids")
    for skill in manifest["skills"]:
        source = within(root, skill["local_path"])
        if not source.is_file():
            errors.append("missing workflow: " + skill["local_path"])
        canonical = within(root, manifest["agents"]["generic"] + "/" + skill["id"] + "/SKILL.md")
        for agent, folder in manifest["agents"].items():
            path = within(root, folder + "/" + skill["id"] + "/SKILL.md")
            if not path.is_file():
                errors.append("missing adapter: " + str(path.relative_to(root)))
                continue
            text = path.read_text(encoding="utf-8")
            if "name: " + skill["id"] + "\n" not in text or skill["local_path"] not in text:
                errors.append("invalid adapter: " + str(path.relative_to(root)))
            if canonical.is_file() and path.read_bytes() != canonical.read_bytes():
                errors.append("adapter differs from canonical: " + agent + "/" + skill["id"])
    for asset in manifest.get("optional_assets", []):
        path = within(root, asset["path"])
        if path.is_file() and git_hash(path.read_bytes()) != asset["git_blob_sha"]:
            errors.append("optional asset hash mismatch: " + asset["path"])
    return errors


def sync(root: Path, manifest: dict, agents: list[str]) -> None:
    for agent in agents:
        folder = manifest["agents"][agent]
        if agent == "generic":
            continue
        for skill in manifest["skills"]:
            source = within(root, manifest["agents"]["generic"] + "/" + skill["id"] + "/SKILL.md")
            target = within(root, folder + "/" + skill["id"] + "/SKILL.md")
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(source, target)


def fonts(root: Path, manifest: dict) -> None:
    for asset in manifest.get("optional_assets", []):
        if not asset["url"].startswith("https://raw.githubusercontent.com/"):
            raise ValueError("Unexpected asset host")
        target = within(root, asset["path"])
        if target.is_file() and git_hash(target.read_bytes()) == asset["git_blob_sha"]:
            continue
        with urlopen(asset["url"], timeout=30) as response:
            data = response.read(asset["bytes"] + 1)
        if len(data) != asset["bytes"] or git_hash(data) != asset["git_blob_sha"]:
            raise ValueError("Downloaded font failed integrity check: " + asset["path"])
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
        print("Downloaded verified font:", asset["path"])


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=["check", "list", "sync", "fonts"])
    parser.add_argument("--agents", nargs="+", choices=["claude", "cursor", "gemini", "copilot"])
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    manifest = json.loads((root / "skills-lock.json").read_text(encoding="utf-8"))
    if args.command == "list":
        for skill in manifest["skills"]:
            print(skill["id"], "->", skill["local_path"])
        return 0
    if args.command == "sync":
        sync(root, manifest, args.agents or [a for a in manifest["agents"] if a != "generic"])
    elif args.command == "fonts":
        fonts(root, manifest)
    errors = check(root, manifest)
    for error in errors:
        print("ERROR:", error)
    if not errors:
        print("OK:", len(manifest["skills"]), "skills;", len(manifest["agents"]), "agent layouts; pinned sources intact.")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
