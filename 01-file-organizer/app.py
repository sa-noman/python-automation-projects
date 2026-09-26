from __future__ import annotations
import argparse
from pathlib import Path
import shutil

CATEGORIES = {
    'Images': {'.jpg','.jpeg','.png','.gif','.webp','.svg'},
    'Documents': {'.pdf','.doc','.docx','.txt','.md','.csv','.xlsx','.ppt','.pptx'},
    'Audio': {'.mp3','.wav','.flac','.m4a'},
    'Video': {'.mp4','.mkv','.mov','.avi','.webm'},
    'Archives': {'.zip','.rar','.7z','.tar','.gz'},
    'Code': {'.py','.js','.ts','.java','.c','.cpp','.html','.css','.json','.yaml','.yml'},
}

def category_for(path: Path) -> str:
    ext = path.suffix.lower()
    for category, extensions in CATEGORIES.items():
        if ext in extensions:
            return category
    return 'Other'

def unique_destination(dest: Path) -> Path:
    if not dest.exists():
        return dest
    stem, suffix = dest.stem, dest.suffix
    i = 1
    while True:
        candidate = dest.with_name(f"{stem}_{i}{suffix}")
        if not candidate.exists():
            return candidate
        i += 1

def organize(folder: Path, dry_run: bool = False) -> list[tuple[Path, Path]]:
    if not folder.is_dir():
        raise ValueError(f"Not a directory: {folder}")
    moves = []
    for item in sorted(folder.iterdir()):
        if not item.is_file() or item.name.startswith('.'):
            continue
        target_dir = folder / category_for(item)
        target = unique_destination(target_dir / item.name)
        moves.append((item, target))
        if not dry_run:
            target_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(target))
    return moves

def main() -> None:
    parser = argparse.ArgumentParser(description='Organize files into category folders by extension.')
    parser.add_argument('folder', type=Path)
    parser.add_argument('--dry-run', action='store_true', help='Preview changes without moving files')
    args = parser.parse_args()
    try:
        moves = organize(args.folder.expanduser().resolve(), args.dry_run)
    except ValueError as exc:
        raise SystemExit(str(exc))
    if not moves:
        print('No files to organize.')
        return
    for src, dst in moves:
        print(f"{'WOULD MOVE' if args.dry_run else 'MOVED'}: {src.name} -> {dst.parent.name}/{dst.name}")

if __name__ == '__main__':
    main()
