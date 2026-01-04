import os
import subprocess
import sys
from datetime import datetime
from pathlib import Path

# プロジェクト作成
# @param    プロジェクト名
# @returns  none
def create_project(project_name):
    project_path = Path.cwd() / project_name
    if project_path.exists():
        print(f"エラー: フォルダ '{project_name}' は既に存在します。")
        return

    print(f"🚀 プロジェクト '{project_name}' を作成中...")
    project_path.mkdir(parents=True)

    # --- Git初期化 ---
    subprocess.run(["git", "init"], cwd=project_path, check=True, capture_output=True)

    # --- venvの作成（追加機能） ---
    print("📦 仮想環境(venv)を作成中...")
    subprocess.run([sys.executable, "-m", "venv", "venv"], cwd=project_path, check=True)

    # --- 雛形ファイル作成 ---
    (project_path / "main.py").write_text('print("Hello!")', encoding="utf-8")
    
    # .gitignore に venv/ を追加して、仮想環境をGit管理から外す
    gitignore_content = "venv/\n__pycache__/\n.env\n"
    (project_path / ".gitignore").write_text(gitignore_content, encoding="utf-8")

    print(f"✅ すべての準備が整いました！")
    print(f"\n💡 使い方:")
    print(f"  cd {project_name}")
    print(f"  source venv/bin/activate  # 環境を有効化")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        name = sys.argv[1]
    else:
        name = input("プロジェクト名を入力してください: ").strip()
    
    if name:
        create_project(name)
    else:
        print("プロジェクト名が入力されませんでした。")