---
title: 提案書テンプレート — キッチンシンク
theme: default
aspectRatio: '16/9'
canvasWidth: 980
fonts:
  sans: 'Noto Sans JP'
  mono: 'Fira Code'
highlighter: shiki
drawings:
  persist: false
---

# 提案書スライドテンプレート

キッチンシンクデモ — 全レイアウト・コンポーネント一覧

::subtitle::

株式会社〇〇 | 2026年2月

---
layout: agenda
sections:
  - 'レイアウト'
  - 'コンポーネント'
  - 'データ表示'
  - '図表・チャート'
  - '装飾'
current: 0
---

---
layout: section
---

レイアウトデモ

::label::

PART 1

---
layout: default
---

## defaultレイアウト — 標準的な1メッセージ＋根拠のスライド

このレイアウトは最も頻繁に使用されます。H2見出しがキーメッセージ（アクションタイトル）として機能し、その下にボディ（根拠データ）を配置します。

**ノウハウ対応: §3.2 スライドの6構成要素、§3.4 キーメッセージ**

| 構成要素 | Slidevでの実現方法 |
|---------|------------------|
| タイトル | レイアウト名でセクションを示す |
| キーメッセージ | H2見出し（完全な文で記述） |
| ボディ | defaultスロット内のMarkdownコンテンツ |
| 脚注 | `::footnote::` スロット |
| 出所・ページ番号 | global-bottom.vueで自動表示 |

::footnote::

出所: proposal-knowhow.md §3.2

---
layout: two-cols
---

## 左カラム: 課題認識

two-colsレイアウトは左右2分割で情報を並列表示します。

**典型的な用途:**
- Before / After 比較
- 課題と解決策の対比
- データと解説の並列表示

**ノウハウ対応: §3.9 ボディの5大レイアウトパターン ①並列配置**

::right::

## 右カラム: 解決策

右側には対になる情報を配置します。

<Callout type="info">

`::right::` スロットシュガーで右カラムの内容を記述します。

</Callout>

---
layout: three-cols
---

### 要素A

three-colsレイアウトで3つの要素を並列表示。

カード型レイアウトとの併用が効果的です。

::center::

### 要素B

中央カラムには `::center::` スロットを使用。

3分割は「問題→解決策→効果」のパターンに適しています。

::right::

### 要素C

右カラムには `::right::` スロットを使用。

**ノウハウ対応: §3.6 カード型レイアウト**

---
layout: four-quadrant
---

::q1::

### 高影響・高緊急

最優先で対応すべき課題

::q2::

### 高影響・低緊急

計画的に対応する課題

::q3::

### 低影響・高緊急

迅速に処理する課題

::q4::

### 低影響・低緊急

後回しにできる課題

---
layout: agenda
sections:
  - 'レイアウト'
  - 'コンポーネント'
  - 'データ表示'
  - '図表・チャート'
  - '装飾'
current: 1
---

---
layout: default
---

## SlideHeader / SectionNav — 構造系コンポーネント

<SlideHeader subtitle="スライドのヘッダー領域を統一的に管理するコンポーネント">
  SlideHeaderコンポーネントのデモ
</SlideHeader>

### SectionNavコンポーネント

<SectionNav
  :sections="['背景', '課題', '提案', '体制', '効果']"
  :current="2"
/>

<div class="mt-[24px]">

<Callout type="info">

SectionNavはagendaレイアウトで自動的に使用されますが、defaultレイアウト内でも単独で使えます。**ノウハウ §3.5 アジェンダスライドの戦略的活用** に対応。

</Callout>

</div>

---
layout: default
---

## Card / CardGroup — カード型並列レイアウト

<CardGroup :cols="3">
  <Card title="可用性" icon="🛡️">
    Multi-AZ構成により99.95%以上の可用性を実現
  </Card>
  <Card title="性能" icon="⚡">
    Auto Scalingでピーク時80倍のアクセス増に自動対応
  </Card>
  <Card title="コスト" icon="💰">
    従量課金とGlacier Lifecycleで保管コスト84%削減
  </Card>
</CardGroup>

<div class="mt-[16px]">

**ノウハウ対応: §3.10 カード型レイアウト**

`cols` propで2〜4列を指定可能。各Cardにはicon, titleプロップとslotでの本文を渡します。

</div>

---
layout: agenda
sections:
  - 'レイアウト'
  - 'コンポーネント'
  - 'データ表示'
  - '図表・チャート'
  - '装飾'
current: 2
---

---
layout: kpi
---

<div class="grid grid-cols-4 gap-[16px]">
  <KPICard value="99.95" unit="%" label="可用性SLA" change="単一拠点→Multi-AZ" :positive="true" />
  <KPICard value="80" unit="倍" label="自動スケーリング" change="固定→自動拡張" :positive="true" />
  <KPICard value="84" unit="%" label="ストレージコスト削減" change="S3 → Glacier" :positive="true" />
  <KPICard value="0" label="日常運用タスク" unit="件" change="NoOps実現" :positive="true" />
</div>

::footnote::

ノウハウ対応: §4.2 定量データの活用 — 抽象的な表現を避け、具体的な数値で語る

---
layout: default
---

## Before/After比較で導入効果を明確に伝える

<BeforeAfter improvement="60%削減" beforeLabel="導入前" afterLabel="導入後">
  <template #before>
    <ul>
      <li>処理時間: <strong>5日</strong></li>
      <li>エラー率: <strong>15%</strong></li>
      <li>年間コスト: <strong>5,000万円</strong></li>
      <li>運用体制: <strong>常駐3名</strong></li>
    </ul>
  </template>
  <template #after>
    <ul>
      <li>処理時間: <strong>2日</strong></li>
      <li>エラー率: <strong>2%</strong></li>
      <li>年間コスト: <strong>2,000万円</strong></li>
      <li>運用体制: <strong>NoOps（自動化）</strong></li>
    </ul>
  </template>
</BeforeAfter>

<div class="mt-[12px] text-[13px]" style="color: var(--color-muted);">

ノウハウ対応: §4.1 Before/After比較 — 同一フォーマットで対比し、改善効果を一目で示す

</div>

---
layout: default
---

## ComparisonTableで詳細な比較データを提示する

<ComparisonTable
  :headers="['評価軸', '現行（オンプレミス）', '提案構成（AWS）']"
  :rows="[
    ['可用性', '単一拠点、HW故障→停止', 'Multi-AZ 99.95%以上'],
    ['性能', 'ピーク固定設計', '自動スケーリング（80倍対応）'],
    ['コスト', '全データ同一ストレージ', 'Glacier Lifecycle（84%削減）'],
    ['拡張性', 'RDB 1TBが限界', 'S3無制限 + Aurora自動拡張'],
    ['セキュリティ', '手動パッチ・監視', '多層防御 + NoOps'],
  ]"
  :highlightCol="2"
/>

<div class="mt-[12px] text-[13px]" style="color: var(--color-muted);">

highlightColプロップで強調する列を指定。ノウハウ §4.2 定量データの活用に対応。

</div>

---
layout: agenda
sections:
  - 'レイアウト'
  - 'コンポーネント'
  - 'データ表示'
  - '図表・チャート'
  - '装飾'
current: 3
---

---
layout: process
---

## 段階的な移行アプローチで、リスクを最小化しながら最適構成へ移行する

<ProcessFlow :steps="[
  { label: 'Phase 1', description: '現状分析・設計' },
  { label: 'Phase 2', description: 'インフラ構築' },
  { label: 'Phase 3', description: 'アプリ移行' },
  { label: 'Phase 4', description: 'データ移行' },
  { label: 'Phase 5', description: 'テスト・検証' },
  { label: 'Phase 6', description: '切替・運用開始' },
]" />

<div class="mt-[24px] text-[13px]" style="color: var(--color-muted);">

ノウハウ対応: §3.10 プロセス図（矢印フロー） — 手順、工程の可視化

</div>

---
layout: timeline
---

## 7ヶ月間の段階的実施スケジュール

<TimelineChart
  :months="7"
  :phases="[
    { label: '現状分析・設計', start: 1, end: 1 },
    { label: 'インフラ構築', start: 2, end: 2 },
    { label: 'アプリ移行', start: 3, end: 4 },
    { label: 'データ移行', start: 5, end: 5 },
    { label: 'テスト・検証', start: 6, end: 6 },
    { label: '切替・運用', start: 7, end: 7 },
  ]"
/>

<div class="mt-[16px] text-[13px]" style="color: var(--color-muted);">

ノウハウ対応: §3.10 タイムライン / ガントチャート — スケジュールの可視化

</div>

---
layout: default
---

## Matrix2x2 — 二軸での分類・ポジショニング

<Matrix2x2 xLabel="実現容易性" yLabel="ビジネスインパクト" xLow="難" xHigh="易" yLow="小" yHigh="大">
  <template #q1>

**Quick Win以外の重要施策**

長期的に取り組む戦略課題

  </template>
  <template #q2>

**Quick Win**

最優先で着手すべき施策

  </template>
  <template #q3>

**保留**

現時点では着手不要

  </template>
  <template #q4>

**効率化候補**

自動化等で対応可能

  </template>
</Matrix2x2>

---
layout: default
---

## LogicTree — 課題の構造的分解

<LogicTree :tree="{
  label: 'コスト削減',
  children: [
    { label: 'インフラ費', detail: '従量課金化', children: [{ label: 'Fargate' }, { label: 'Aurora Serverless' }] },
    { label: 'ストレージ費', detail: 'Lifecycle最適化', children: [{ label: 'S3' }, { label: 'Glacier' }] },
    { label: '運用費', detail: 'NoOps化', children: [{ label: 'マネージド' }, { label: 'CI/CD' }] },
  ]
}" />

<div class="mt-[24px] text-[13px]" style="color: var(--color-muted);">

ノウハウ対応: §3.10 ロジックツリー — 課題分解、原因分析。§2.8 MECE原則の可視化にも有効。

</div>

---
layout: agenda
sections:
  - 'レイアウト'
  - 'コンポーネント'
  - 'データ表示'
  - '図表・チャート'
  - '装飾'
current: 4
---

---
layout: default
---

## 装飾コンポーネント一覧

### Badge（バッジ）

<Badge color="primary">必須</Badge> <Badge color="accent">重要</Badge> <Badge color="success">完了</Badge> <Badge color="muted">参考</Badge>

### DiffArrow（差分矢印ラベル）

<DiffArrow label="84%削減" :positive="true" /> &nbsp;&nbsp; <DiffArrow label="15%増加" :positive="false" />

### Highlight（テキスト強調）

通常テキストに<Highlight>アクセントカラー</Highlight>で強調。<Highlight color="success">成功指標</Highlight>や<Highlight color="primary">重要項目</Highlight>にも対応。

### DirectionArrow（方向矢印）

<DirectionArrow direction="right" size="sm" /> Small &nbsp;&nbsp; <DirectionArrow direction="right" size="md" /> Medium &nbsp;&nbsp; <DirectionArrow direction="right" size="lg" /> Large

### Callout（注釈）

<Callout type="info">情報: すべてのチャートにCalloutをつけ、データの意味を明示する（§3.10）</Callout>

<Callout type="warning">警告: 円グラフは基本的に避ける。棒グラフの方が正確に比較できる（§3.10）</Callout>

<Callout type="success">成功: 定量データを活用し、具体的な数値で語る（§4.2）</Callout>

---
layout: team
---

## AWS認定資格保有のクラウドアーキテクトを中心に確実に遂行する

| 役割 | 担当 | 資格・経験 | 責任範囲 |
|------|------|-----------|----------|
| **PM** | 〇〇 | PMP | 全体統括、進捗管理 |
| **アーキテクト** | 〇〇 | AWS SAP | アーキテクチャ設計 |
| **開発** | 〇〇 | Golang 5年 | アプリケーション開発 |
| **インフラ** | 〇〇 | AWS DevOps | 環境構築、CI/CD |
| **データ** | 〇〇 | DBスペシャリスト | データ移行 |
| **品質** | 〇〇 | JSTQB-AL | テスト計画・実行 |

<div class="mt-[16px]">

**体制の特長:** 全メンバーがAWS認定資格を保有。週次進捗報告でリスクの早期検知を実現。

</div>

---
layout: summary
---

## エグゼクティブサマリー — 提案の骨子

<SlideHeader subtitle="summaryレイアウトは情報密度の高いスライドに適しています（本文14px）">
  テンプレート機能のまとめ
</SlideHeader>

**利用可能なレイアウト（13種）:** cover, default, section, agenda, two-cols, three-cols, four-quadrant, process, timeline, comparison-table, kpi, team, summary

**利用可能なコンポーネント（17種）:**

<CardGroup :cols="4">
  <Card title="構造系">SlideHeader, SlideFooter, SectionNav</Card>
  <Card title="レイアウト系">CardGroup, Card</Card>
  <Card title="データ表示系">KPICard, ComparisonTable, BeforeAfter</Card>
  <Card title="図表・装飾系">ProcessFlow, TimelineChart, Matrix2x2, LogicTree, Callout, Arrow, Badge, DiffArrow, Highlight</Card>
</CardGroup>
