---
name: generate-illustration
description: Generates or edits illustrations using Nano Banana Pro (Gemini image generation API). Use when the user asks to create, generate, draw, edit, modify, or refine illustrations, diagrams, charts, or images using Nano Banana Pro or Gemini image generation.
argument-hint: "[prompt or file reference + instructions]"
---

# Generate / Edit Illustration with Nano Banana Pro

Nano Banana Pro（Gemini `gemini-3-pro-image-preview`）を使って画像の生成・編集を行う。

## Usage

```
/generate-illustration <プロンプト or ファイル参照 + 指示>
```

**新規生成の例:**
```
/generate-illustration AWS構成図を生成。CloudFront→ALB→ECS→Aurora。出力先: architecture.png
/generate-illustration proposal/illustration-request.md の ill-01 を生成して
```

**既存画像の編集の例:**
```
/generate-illustration ill-01 のラベルのフォントサイズを大きくして
/generate-illustration ill-01 の CI/CD フローの色をもっと薄くして
```

## Workflow

### Step 1: Interpret arguments

`$ARGUMENTS` を解釈し、**新規生成** か **既存画像の編集** かを判断する:

- **新規生成**: 直接プロンプト、またはファイル参照＋指示から新しい画像を生成
- **画像編集**: 既存画像への修正指示（「ラベルを大きく」「色を変えて」「要素を追加」など）
  - 対象画像のパスを特定する（ファイル名やイラスト番号から推測）
  - 編集指示をプロンプトとして構築する
- **出力先**: 「出力先:」「output:」の後のパスを出力先とする。編集時は元ファイルを上書き（未指定の場合）

### Step 2: Build prompt for Gemini

ユーザーの指示から Gemini 向けの画像生成プロンプトを構築する。

**プロンプト構築のポイント:**
- 日本語の指示は英語に変換する（Gemini の画像生成は英語プロンプトが最も効果的）
- レイアウト、色（hex 値）、スタイル、テキストラベルを具体的に記述する
- 画像の用途・コンテキストを含める
- 仕様書参照の場合は、共通デザイン指示 + 個別イラスト仕様の両方を含める

### Step 3: Generate or edit image

スクリプトを実行して画像を生成・編集する。

**新規生成:**
```bash
.venv/bin/python .claude/skills/generate-illustration/scripts/generate_image.py \
  --prompt "constructed prompt here" \
  --output "output_path.png" \
  --aspect-ratio "16:9" \
  --image-size "2K"
```

**既存画像の編集（`--input` で元画像を指定）:**
```bash
.venv/bin/python .claude/skills/generate-illustration/scripts/generate_image.py \
  --prompt "editing instructions here" \
  --input "path/to/existing_image.png" \
  --output "output_path.png"
```

> `.venv` が存在しない場合は `python3 -m venv .venv && .venv/bin/pip install google-genai Pillow` で作成する。

**Parameters:**
- `--prompt`: 構築した英語プロンプト（生成指示または編集指示）
- `--output`: 出力ファイルパス（PNG）
- `--input`: 編集元の画像パス（複数指定可、編集モード時のみ）
- `--aspect-ratio`: アスペクト比（デフォルト: `16:9`、他: `1:1`, `4:3`, `3:4`, `9:16`）
- `--image-size`: 画像サイズ（`1K`, `2K`, `4K`、デフォルト: `2K`）

### Step 4: Verify and report

1. 生成された画像ファイルの存在とサイズを確認する
2. Read ツールで画像を表示してユーザーに見せる
3. ファイルパスとサイズを報告する

## Dependencies

`google-genai` と `Pillow` が必要。未インストールの場合:

```bash
python3 -m venv .venv && .venv/bin/pip install google-genai Pillow
```

## Error Handling

- **API キーが見つからない**: `.env` に `GEMINI_API_KEY=...` を設定するよう案内する
- **パッケージ未インストール**: `pip install google-genai Pillow` を実行する
- **画像が生成されない**: プロンプトを調整して再試行する。安全フィルタに引っかかった可能性がある
- **API エラー**: エラーメッセージを報告し、対処法を提案する
