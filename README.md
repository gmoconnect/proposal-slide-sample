# proposal-slide-sample

## 事前準備・前提条件

- Claude Code利用
  - VSCodeに `Claude Code for VS Code` をインストール
  - Model: Opus4.6+Thinking
  - plugin追加
    - context7
    - playwright

## 1. 提案書スライドテンプレートの作成

### 提案書ストーリーのノウハウ作成

- Plan modeで方針を確認した後、作成してもらうこと
- prompt例
  - pprompts/1_template/prompt-template-story.md
- 自社にノウハウがすでにあれば、そちらを活用する方が良い
  - 例: 企画書のテンプレート、チェックリスト、過去の提案書など
    - pptxやpdfや画像(印刷した紙をカメラで撮ったもの含む)などでも可能
- 作成例:
  - design/proposal-knowhow.md

### スライド作成ノウハウの収集

- 新しいChat Sesionで開始。`Ask before edits`
- prompt例
  - prompts/1_template/template-slide1.md
- こちらも自社のノウハウがあれば、そちらを活用する方が良い
- 作成例:
  - design/slide-component-survey.md

### 調査結果を元にslidevテンプレートの作成

- 上記から継続したChat Sessionで、Plan modeで方針を確認した後、作成してもらうこと
- prompt例
  - prompts/1_template/prompt-template-slide2.md
- 作成例:
  - design/slidev-usage-guide.md
  - design/slidev/*

## 2. 提案ストーリーを作成

### ストーリー案の作成

- 評価観点毎に、ストーリーを作成。Plan modeで方針を確認した後、作成してもらうこと
  - `### 提案コンセプト` は、観点毎に最適なものを検討すること
- prompt例
  - prompts/2_story/prompt-story.md
- 作成例:
  - proposal/story-before-review.md

### ストーリー案のレビュー＆修正

- 新しいChat Sesionで開始。`Ask before edits`
- prompt例
  - prompts/2_story/prompt-story-review.md
- 作成例:
  - proposal/story.md
- 何度か新しいChat Sesionでレビューを繰り返すことが望ましい

## 3. Slidev形式のMarkdownに変換

- 新しいChat Sesionで開始。`Plan mode`で方針を確認した後、作成してもらうこと
- prompt例:
  - prompts/3_slidev/prompt-slidev-convert.md
- 作成例:
  - proposal/slides.md
- slidev Markdown作成後、slidevを自分で起動し、Claudeに伝えると表示確認と修正をしてもらえる
