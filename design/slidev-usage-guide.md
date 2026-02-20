# Slidev テンプレート利用ガイド

> `proposal-knowhow.md` のノウハウを Slidev のレイアウト・コンポーネントへ対応づけるリファレンス。
> スライド作成者がこのドキュメントを参照しながら `slides.md` を編集することを想定しています。

---

## 1. クイックスタート

```bash
cd design/slidev
npm install
npm run dev
```

- ブラウザで `http://localhost:3030` が自動的に開く
- `slides.md` を編集すると即座にホットリロードされる
- アスペクト比は **16:9 横表示**（`aspectRatio: '16/9'`）
- フォント設定は frontmatter の `fonts.sans` で `Noto Sans JP` を指定済み

### frontmatter の基本構造

```yaml
---
title: 提案書タイトル
theme: default
aspectRatio: '16/9'
canvasWidth: 980
fonts:
  sans: 'Noto Sans JP'
  mono: 'Fira Code'
---
```

---

## 2. スライドの基本構造

ノウハウ集 **3.2 スライドの6構成要素** で定義された要素と、本テンプレートでの実現方法の対応は以下の通り。

```
+--------------------------------------------------+
| [タイトル]                                        |  ... レイアウト名がセクションを示す
| [キーメッセージ]                                   |  ... H2 見出し（完全な文で主張を記述）
|--------------------------------------------------|
|                                                  |
|   ボディ（根拠データ・図表・チャート）                 |  ... default スロット内の Markdown
|                                                  |
|  *1) 脚注                                         |  ... ::footnote:: スロット
|  出所: ...                              Page X/Y  |  ... global-bottom.vue が自動表示
+--------------------------------------------------+
```

| 構成要素 | ノウハウ節 | Slidev での実現方法 |
|---------|-----------|-------------------|
| (1) タイトル | 3.2 | レイアウト名でセクションを区別。cover/section レイアウトで明示 |
| (2) キーメッセージ | 3.2, 3.4 | **H2 見出し**（`## アクションタイトル`）に完全な文で記述 |
| (3) ボディ | 3.2 | default スロット内に Markdown やコンポーネントを配置 |
| (4) 脚注 | 3.2 | `::footnote::` スロット（default / kpi レイアウトで利用可） |
| (5) 出所 | 3.2 | `global-bottom.vue` が `$slidev.configs.title` を自動表示 |
| (6) ページ番号 | 3.2 | `global-bottom.vue` が `currentPage / total` を自動表示 |

> **補足:** cover / section レイアウトでは global-bottom.vue のフッターが非表示になる。

### H2 見出し = アクションタイトルの書き方

ノウハウ 3.4 に従い、**単なるトピックラベルではなく完全な文**で記述する。

```markdown
<!-- NG: トピックラベル -->
## 市場環境分析

<!-- OK: アクションタイトル -->
## 市場は年率5%で縮小しており、早期の対策が不可欠
```

---

## 3. レイアウト一覧（13種）

### 3-1. cover

表紙ページ。ネイビー背景・白文字。global-bottom.vue のフッターは非表示。

| スロット | 内容 |
|---------|------|
| default | メインタイトル（H1） |
| subtitle | サブタイトル（会社名・日付等） |

```markdown
---
layout: cover
---

# 提案書タイトル

::subtitle::

株式会社〇〇 | 2026年2月
```

---

### 3-2. default

最も頻繁に使用する標準レイアウト。1メッセージ + 根拠の構成。

| スロット | 内容 |
|---------|------|
| default | H2 キーメッセージ + ボディ |
| footnote | 脚注テキスト（12px、グレー） |

```markdown
---
layout: default
---

## AIチャットボット導入により、問合せ対応時間を年間2,000時間削減できる

根拠データやテーブル、コンポーネントをここに配置。

::footnote::

出所: 〇〇調査（2025年）
```

---

### 3-3. section

セクション区切りページ。ネイビー背景・白文字。global-bottom.vue のフッターは非表示。

| スロット | 内容 |
|---------|------|
| default | セクション名（H1） |
| label | セクション番号やラベル（大文字・小文字で表示） |

```markdown
---
layout: section
---

ソリューション提案

::label::

PART 3
```

---

### 3-4. agenda

アジェンダ（ナビゲーション付き目次）。SectionNav コンポーネントを内部で自動使用。

| プロパティ | 型 | 内容 |
|-----------|-----|------|
| sections | Array | セクション名の配列 |
| current | Number | 現在のセクションインデックス（0始まり） |

| スロット | 内容 |
|---------|------|
| default | 追加コンテンツ（任意） |

```markdown
---
layout: agenda
sections:
  - '背景'
  - '課題'
  - '提案'
  - '体制'
  - '効果'
current: 2
---
```

---

### 3-5. two-cols

左右2分割レイアウト。ノウハウ 3.9 の「並列配置」パターンに対応。

| スロット | 内容 |
|---------|------|
| default | 左カラム |
| right | 右カラム |

```markdown
---
layout: two-cols
---

## 左: 現状の課題

- 処理時間: 5日
- エラー率: 15%

::right::

## 右: 導入後の姿

- 処理時間: 2日
- エラー率: 2%
```

---

### 3-6. three-cols

3分割レイアウト。3つの並列要素を表示。

| スロット | 内容 |
|---------|------|
| default | 左カラム |
| center | 中央カラム |
| right | 右カラム |

```markdown
---
layout: three-cols
---

### 課題

現行システムの問題点

::center::

### 解決策

提案するアプローチ

::right::

### 効果

期待される成果
```

---

### 3-7. four-quadrant

2x2 マトリクスレイアウト。ノウハウ 3.9 の「4分割」パターンに対応。

| スロット | 内容 |
|---------|------|
| q1 | 左上（高Y・低X） |
| q2 | 右上（高Y・高X） |
| q3 | 左下（低Y・低X） |
| q4 | 右下（低Y・高X） |

```markdown
---
layout: four-quadrant
---

::q1::

### 高影響・高緊急

最優先で対応

::q2::

### 高影響・低緊急

計画的に対応

::q3::

### 低影響・高緊急

迅速に処理

::q4::

### 低影響・低緊急

後回し可能
```

---

### 3-8. process

プロセスフロー表示用レイアウト。コンテンツ領域が垂直中央揃え。

| スロット | 内容 |
|---------|------|
| default | ProcessFlow コンポーネント等を配置 |

```markdown
---
layout: process
---

## 段階的な移行アプローチでリスクを最小化する

<ProcessFlow :steps="[
  { label: 'Phase 1', description: '現状分析' },
  { label: 'Phase 2', description: '設計・構築' },
  { label: 'Phase 3', description: '移行・検証' },
]" />
```

---

### 3-9. timeline

スケジュール / ロードマップ表示用レイアウト。コンテンツ領域が垂直中央揃え。

| スロット | 内容 |
|---------|------|
| default | TimelineChart コンポーネント等を配置 |

```markdown
---
layout: timeline
---

## 6ヶ月間の段階的実施スケジュール

<TimelineChart
  :months="6"
  :phases="[
    { label: '分析・設計', start: 1, end: 2 },
    { label: '開発', start: 3, end: 4 },
    { label: 'テスト・移行', start: 5, end: 6 },
  ]"
/>
```

---

### 3-10. comparison-table

詳細比較テーブル表示用レイアウト。スクロール可能な overflow 領域を持つ。

| スロット | 内容 |
|---------|------|
| default | ComparisonTable コンポーネント等を配置 |

```markdown
---
layout: comparison-table
---

## 提案構成は全評価軸で現行を上回る

<ComparisonTable
  :headers="['評価軸', '現行', '提案']"
  :rows="[
    ['可用性', '99.5%', '99.95%'],
    ['拡張性', '手動', '自動'],
  ]"
  :highlightCol="2"
/>
```

---

### 3-11. kpi

KPI 数値を大きく表示するレイアウト。コンテンツ領域が中央揃え。

| スロット | 内容 |
|---------|------|
| default | KPICard コンポーネント等を配置 |
| footnote | 脚注テキスト（12px、グレー） |

```markdown
---
layout: kpi
---

<div class="grid grid-cols-3 gap-[16px]">
  <KPICard value="60" unit="%" label="処理時間削減" />
  <KPICard value="3,000" unit="万円" label="年間コスト削減" />
  <KPICard value="99.95" unit="%" label="可用性SLA" />
</div>

::footnote::

出所: 社内試算（2025年12月時点）
```

---

### 3-12. team

チーム体制表示用レイアウト。

| スロット | 内容 |
|---------|------|
| default | テーブルや CardGroup でメンバー情報を配置 |

```markdown
---
layout: team
---

## 認定資格保有の専任チームで確実に遂行する

| 役割 | 担当 | 資格 | 責任範囲 |
|------|------|------|----------|
| PM | 〇〇 | PMP | 全体統括 |
| 開発 | 〇〇 | AWS SAP | 設計・開発 |
```

---

### 3-13. summary

エグゼクティブサマリー用レイアウト。本文が **14px** で表示され、情報密度の高いスライドに適する。

| スロット | 内容 |
|---------|------|
| default | サマリーコンテンツ（14px, line-height: relaxed） |

```markdown
---
layout: summary
---

## エグゼクティブサマリー — 提案の骨子

本提案では、AWS マネージドサービスを活用したクラウド移行により、
可用性 99.95% の達成、運用コスト 84% 削減、NoOps 体制の実現を提案します。
```

---

## 4. コンポーネント一覧（19種）

### 構造系コンポーネント

#### SlideHeader

スライド上部のヘッダー領域を統一的に管理する。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| subtitle | String | `''` | サブタイトルテキスト（16px、グレー） |

スロット: default（ヘッダータイトル）

```html
<SlideHeader subtitle="補足説明テキスト">
  セクションの見出し
</SlideHeader>
```

---

#### SlideFooter

スライド下部のフッター領域。出所情報の表示に使用。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| source | String | `''` | 出所テキスト（「出所: 」プレフィックス付き） |

スロット: default（任意のフッターコンテンツ）

```html
<SlideFooter source="総務省統計局（2025年）" />
```

> **補足:** 通常は `::footnote::` スロットや `global-bottom.vue` で十分。明示的にフッターを配置したい場合に使用する。

---

#### SectionNav

セクションナビゲーション。全体の中での現在位置を可視化する。agenda レイアウトでは自動的に使用されるが、default レイアウト内でも単独で使用可能。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| sections | Array | （必須） | セクション名の文字列配列 |
| current | Number | `0` | 現在のセクションインデックス（0始まり） |

```html
<SectionNav
  :sections="['背景', '課題', '提案', '体制', '効果']"
  :current="2"
/>
```

---

#### SlideLabel

スライドのトピック識別子。H2 キーメッセージの直上に配置し、スライドが扱うトピック・評価観点を小さく明示する。ノウハウ 3.2 ①タイトル要素をスライドごとに可視化するためのコンポーネント。

プロパティ: なし（スロットのみ）

スロット: default（ラベルテキスト）

```html
<SlideLabel>2. CloudFront + Fargate 自動スケーリング</SlideLabel>

## CloudFront + Fargate自動スケーリングにより、月末ピーク時でもレスポンス劣化なく対応する
```

> **補足:** 11px / 太字 / 全大文字 / letter-spacing: wider でスタイリングされており、H2 の視認性を妨げない。評価観点番号と短いテーマ名を組み合わせた形式（例: `2. 性能`）が推奨。

---

#### SolutionNav

ソリューション提案セクション内のステップナビゲーション。1セクション内のスライドが6枚以上になる場合に、現在扱っているサブトピックをパンくず形式で可視化する。agenda レイアウトの SectionNav の「セクション内版」にあたるコンポーネント。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| current | Number | `0` | 現在のサブトピックインデックス（0始まり）。-1 を指定するとすべて非アクティブ（概要スライドで使用） |

> **注意:** SolutionNav は `design/slidev/components/SolutionNav.vue` にハードコードされたサブトピック名を持つ。別のセクションに使う場合は `sections` 配列を編集するか、新たなコンポーネントを作成する。

```html
<!-- サブトピック一覧スライド（何も強調しない） -->
<SolutionNav :current="-1" />

## 評価観点ごとに最適なAWSサービスを組み合わせ、6つの課題すべてを解決する

<!-- 個別トピックスライド（インデックス1: 性能を強調） -->
<SolutionNav :current="1" />
<SlideLabel>2. CloudFront + Fargate 自動スケーリング</SlideLabel>

## CloudFront + Fargate自動スケーリングにより、月末ピーク時でもレスポンス劣化なく対応する
```

> **推奨配置パターン:**
> 1. セクション冒頭に `SolutionNav :current="-1"` + CardGroup でサブトピック一覧スライドを配置
> 2. 各詳細スライドに `SolutionNav :current="N"` + `SlideLabel` を H2 の直前に挿入

---

### レイアウト系コンポーネント

#### CardGroup

カード型並列レイアウトのコンテナ。CSS Grid でカードを配置する。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| cols | Number | `3` | カラム数（2〜4を推奨） |

スロット: default（Card コンポーネントを並べる）

```html
<CardGroup :cols="3">
  <Card title="要素A">内容A</Card>
  <Card title="要素B">内容B</Card>
  <Card title="要素C">内容C</Card>
</CardGroup>
```

---

#### Card

情報カード。CardGroup 内に配置して使用する。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| title | String | `''` | カードタイトル（16px、ネイビー太字） |
| icon | String | `''` | アイコン文字（24px） |

スロット: default（カード本文、14px）

```html
<Card title="可用性" icon="99.95%">
  Multi-AZ構成により高可用性を実現
</Card>
```

---

### データ表示系コンポーネント

#### KPICard

KPI 数値を大きく強調表示する。kpi レイアウトと組み合わせて使用。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| value | String | （必須） | 数値（48px、ネイビー、Arialフォント） |
| label | String | （必須） | ラベル（14px、グレー） |
| unit | String | `''` | 単位（24px、数値の右に表示） |
| change | String | `''` | 変化の説明テキスト（14px） |
| positive | Boolean | `true` | true: 緑色、false: 赤色 |

```html
<KPICard
  value="84"
  unit="%"
  label="コスト削減率"
  change="オンプレ比"
  :positive="true"
/>
```

---

#### ComparisonTable

詳細比較テーブル。ヘッダー行はネイビー背景・白文字。偶数行にはストライプ背景が適用される。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| headers | Array | （必須） | ヘッダー文字列の配列 |
| rows | Array | （必須） | 行データの二次元配列 |
| highlightCol | Number | `-1` | 強調する列のインデックス（太字・ネイビー） |

```html
<ComparisonTable
  :headers="['評価軸', '現行', '提案']"
  :rows="[
    ['可用性', '99.5%', '99.95%'],
    ['コスト', '5,000万', '800万'],
  ]"
  :highlightCol="2"
/>
```

---

#### BeforeAfter

Before/After 比較を同一フォーマットで対比表示する。ノウハウ 4.1 に直接対応。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| beforeLabel | String | `'Before'` | 左側のラベル |
| afterLabel | String | `'After'` | 右側のラベル |
| improvement | String | `''` | 中央に表示する改善率テキスト（赤色で強調） |

| スロット | 内容 |
|---------|------|
| #before | Before 側のコンテンツ |
| #after | After 側のコンテンツ |

```html
<BeforeAfter improvement="60%削減" beforeLabel="導入前" afterLabel="導入後">
  <template #before>

- 処理時間: **5日**
- エラー率: **15%**

  </template>
  <template #after>

- 処理時間: **2日**
- エラー率: **2%**

  </template>
</BeforeAfter>
```

---

### 図表系コンポーネント

#### ProcessFlow

プロセスフロー図。ステップを矢印で接続して横並びに表示する。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| steps | Array | （必須） | ステップオブジェクトの配列 |

steps の各要素:

| キー | 型 | 説明 |
|------|-----|------|
| label | String | ステップ名（14px、白太字） |
| description | String | 説明テキスト（12px、白、任意） |

```html
<ProcessFlow :steps="[
  { label: 'Phase 1', description: '現状分析・設計' },
  { label: 'Phase 2', description: 'インフラ構築' },
  { label: 'Phase 3', description: 'テスト・検証' },
]" />
```

---

#### TimelineChart

ガントチャート風のタイムライン。月単位のスケジュールを可視化する。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| phases | Array | （必須） | フェーズオブジェクトの配列 |
| months | Number | `6` | 表示する月数 |

phases の各要素:

| キー | 型 | 説明 |
|------|-----|------|
| label | String | フェーズ名 |
| start | Number | 開始月（1始まり） |
| end | Number | 終了月（1始まり） |

```html
<TimelineChart
  :months="7"
  :phases="[
    { label: '現状分析', start: 1, end: 1 },
    { label: '設計・構築', start: 2, end: 3 },
    { label: '移行・検証', start: 4, end: 6 },
    { label: '運用開始', start: 7, end: 7 },
  ]"
/>
```

---

#### Matrix2x2

2x2 マトリクス図。二軸での分類・ポジショニングに使用する。ノウハウ 3.10 の「2x2マトリクス」に対応。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| xLabel | String | `''` | X軸ラベル |
| yLabel | String | `''` | Y軸ラベル |
| xLow | String | `'低'` | X軸の低い側のラベル |
| xHigh | String | `'高'` | X軸の高い側のラベル |
| yLow | String | `'低'` | Y軸の低い側のラベル |
| yHigh | String | `'高'` | Y軸の高い側のラベル |

| スロット | 位置 |
|---------|------|
| #q1 | 左上（高Y・低X） |
| #q2 | 右上（高Y・高X） |
| #q3 | 左下（低Y・低X） |
| #q4 | 右下（低Y・高X） |

```html
<Matrix2x2
  xLabel="実現容易性" yLabel="ビジネスインパクト"
  xLow="難" xHigh="易" yLow="小" yHigh="大"
>
  <template #q1>重要だが困難</template>
  <template #q2>Quick Win</template>
  <template #q3>保留</template>
  <template #q4>効率化候補</template>
</Matrix2x2>
```

---

#### LogicTree

ロジックツリー図。課題分解や原因分析を構造的に可視化する。最大3階層（root / children / grandchildren）をサポート。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| tree | Object | （必須） | ツリー構造オブジェクト |

tree オブジェクトの構造:

```
{
  label: String,         // ルートノード名
  children: [            // 第2階層（任意）
    {
      label: String,     // ノード名
      detail: String,    // 補足説明（任意）
      children: [        // 第3階層（任意）
        { label: String }
      ]
    }
  ]
}
```

```html
<LogicTree :tree="{
  label: 'コスト削減',
  children: [
    {
      label: 'インフラ費',
      detail: '従量課金化',
      children: [
        { label: 'Fargate' },
        { label: 'Aurora Serverless' },
      ]
    },
    {
      label: '運用費',
      detail: 'NoOps化',
      children: [
        { label: 'マネージド' },
        { label: 'CI/CD' },
      ]
    },
  ]
}" />
```

---

### 装飾系コンポーネント

#### Callout

注釈・補足情報の吹き出し。左ボーダー付きのボックスで表示。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| type | String | `'info'` | `info`（ネイビー）/ `warning`（赤）/ `success`（緑） |

スロット: default（注釈テキスト）

```html
<Callout type="info">
すべてのチャートにCalloutをつけ、データの意味を明示する
</Callout>

<Callout type="warning">
円グラフは基本的に避ける（ノウハウ §3.10）
</Callout>

<Callout type="success">
定量データの活用で説得力を向上
</Callout>
```

---

#### Arrow

方向矢印。フロー説明やインライン表示に使用。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| direction | String | `'right'` | `right` / `left` / `up` / `down` |
| size | String | `'md'` | `sm`（16px）/ `md`（24px）/ `lg`（36px） |

```html
現状 <Arrow direction="right" size="md" /> 目標
```

---

#### Badge

ラベルバッジ。ステータスや分類の表示に使用。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| color | String | `'primary'` | `primary`（ネイビー）/ `accent`（赤）/ `success`（緑）/ `muted`（グレー背景） |

スロット: default（バッジテキスト）

```html
<Badge color="primary">必須</Badge>
<Badge color="accent">重要</Badge>
<Badge color="success">完了</Badge>
<Badge color="muted">参考</Badge>
```

---

#### DiffArrow

差分矢印ラベル。数値の変化量を視覚的に示す。ノウハウ 3.10 の「差分矢印ラベル」に対応。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| label | String | （必須） | 差分テキスト（例: `"84%削減"`） |
| positive | Boolean | `true` | true: 緑色・上向き三角、false: 赤色・下向き三角 |

```html
<DiffArrow label="84%削減" :positive="true" />
<DiffArrow label="15%増加" :positive="false" />
```

---

#### Highlight

テキスト強調。インラインで特定の文字列を色付きで強調する。

| プロパティ | 型 | デフォルト | 説明 |
|-----------|-----|-----------|------|
| color | String | `'accent'` | `primary`（ネイビー）/ `accent`（赤）/ `success`（緑） |

スロット: default（強調テキスト）

```html
処理時間を<Highlight>60%短縮</Highlight>し、
<Highlight color="success">年間3,000万円</Highlight>のコスト削減を実現
```

---

## 5. デザイントークン

すべてのデザイントークンは `styles/index.css` の CSS カスタムプロパティとして定義されている。

### カラーパレット

| トークン | 値 | 用途 |
|---------|-----|------|
| `--color-primary` | `#1B3A5C` | タイトル、見出し、主要要素（ネイビー） |
| `--color-secondary` | `#666666` | 補足テキスト、サブラベル |
| `--color-accent` | `#E63946` | 強調、警告、重要数値のハイライト |
| `--color-success` | `#2D9C4F` | 正の効果、改善指標 |
| `--color-bg` | `#FFFFFF` | 背景色 |
| `--color-text` | `#333333` | 本文テキスト |
| `--color-muted` | `#999999` | 脚注、ページ番号 |
| `--color-light-bg` | `#F5F7FA` | テーブルストライプ、カード背景 |
| `--color-border` | `#E0E0E0` | ボーダー、区切り線 |

### フォント

| トークン | 値 | 用途 |
|---------|-----|------|
| `--font-heading` | `'Noto Sans JP', 'メイリオ', sans-serif` | 見出し |
| `--font-body` | `'Noto Sans JP', 'メイリオ', sans-serif` | 本文 |
| `--font-number` | `'Arial', 'Segoe UI', sans-serif` | 数値、ページ番号 |

### フォントサイズ

| トークン | 値 | 用途 |
|---------|-----|------|
| `--font-size-title` | `28px` | スライドタイトル（cover, agenda の H2） |
| `--font-size-subtitle` | `20px` | H2 キーメッセージ |
| `--font-size-body` | `16px` | 本文 |
| `--font-size-caption` | `12px` | 脚注、出所 |
| `--font-size-kpi` | `48px` | KPI 数値 |

### スペーシング

| トークン | 値 | 用途 |
|---------|-----|------|
| `--slide-padding` | `40px` | スライド外周のパディング |
| `--section-gap` | `24px` | セクション間のギャップ |
| `--element-gap` | `16px` | 要素間のギャップ |
| `--line-height` | `1.5` | 本文の行間 |

---

## 6. ノウハウとの対応表

`proposal-knowhow.md` の各セクションに対して、本テンプレートでどのレイアウト・コンポーネントを使うかの対応表。

| ノウハウ節 | 内容 | 対応するレイアウト / コンポーネント |
|-----------|------|----------------------------------|
| **3.2** スライドの6構成要素 | タイトル、キーメッセージ、ボディ、脚注、出所、ページ番号 | **default** レイアウトの構造そのもの。H2 = キーメッセージ、`::footnote::` = 脚注、`global-bottom.vue` = 出所・ページ番号 |
| **3.4** キーメッセージ | アクションタイトル（完全な文で主張を記述） | 全レイアウト共通: **H2 見出し**に完全な文で記述する |
| **3.5** アジェンダの戦略的活用 | セクション間のナビゲーション、現在位置の可視化 | **agenda** レイアウト + **SectionNav** コンポーネント |
| **3.5** セクション内ステップナビゲーション | 1セクション内のスライドが6枚以上の場合の現在位置の可視化 | **SolutionNav** コンポーネント（セクション冒頭に一覧スライド + 各スライドにナビ） + **SlideLabel** でトピック識別子を併用 |
| **3.2** ①タイトル要素（スライドトピック識別子） | スライドごとの評価観点・テーマをH2の上で小さく明示 | **SlideLabel** コンポーネント（11px・上部配置） |
| **3.9** ボディの5大レイアウトパターン | 並列、順序、分割、複合、4分割 | **two-cols**（並列）、**three-cols**（3並列）、**four-quadrant**（4分割）、**process**（順序）。分割・複合は **LogicTree** で対応 |
| **3.10** 図表・チャートの活用 | プロセス図、タイムライン、2x2マトリクス、テーブル、カード、ロジックツリー | **ProcessFlow**、**TimelineChart**、**Matrix2x2**、**ComparisonTable**、**CardGroup + Card**、**LogicTree** |
| **3.10** グラフの補助テクニック | Callout 注釈、差分矢印ラベル | **Callout**、**DiffArrow** |
| **4.1** Before/After 比較 | 導入前後の対比表示 | **BeforeAfter** コンポーネント |
| **4.2** 定量データの活用 | 具体的な数値での訴求 | **KPICard**、**DiffArrow**、**Highlight** |
| **5.1** 配色 | ネイビー、グレー、アクセントカラー | `styles/index.css` の CSS カスタムプロパティ |
| **5.2** フォント | ゴシック体、サイズ階層 | `--font-heading`, `--font-body`, `--font-number` トークン |
| **5.4** Data-Ink Ratio | 装飾を排除しデータを際立たせる | テンプレート全体のミニマルデザイン、ヘアライン罫線 |
| **6.1** 官公庁特有の注意点 | 図には必ず説明文を添える | Markdown テキストをコンポーネントと併用して記述 |
| **7.1** McKinsey スライド構造 | Action Title + Body + Source Line | default レイアウトの H2 + ボディ + global-bottom.vue |
| **8** 推奨9セクション構成 | エグゼクティブサマリー〜補足資料 | **summary**（サマリー）、**section**（セクション区切り）、**agenda**（ナビゲーション）を組み合わせて構成 |

---

## 7. レイアウト選択ガイド

スライドの内容に応じて、以下の判断フローでレイアウトを選択する。

```
スライドの役割は？
|
+-- 表紙 / 終了ページ ..................... cover
|
+-- セクション区切り ...................... section
|
+-- ナビゲーション / 目次 ................. agenda
|
+-- 内容スライド
    |
    +-- 標準的な 1メッセージ + 根拠 ....... default
    |
    +-- 左右の比較 / 対比 ................ two-cols
    |
    +-- 3つの並列要素 .................... three-cols
    |
    +-- 2x2 分類 / マトリクス ............ four-quadrant
    |
    +-- ステップ / プロセスフロー ......... process
    |
    +-- スケジュール / ロードマップ ....... timeline
    |
    +-- 詳細な比較テーブル ................ comparison-table
    |
    +-- KPI 数値の強調 ................... kpi
    |
    +-- チーム体制の紹介 ................. team
    |
    +-- 情報密度の高いサマリー ............ summary
```

### よくあるパターンの組み合わせ

| 場面 | レイアウト | 主要コンポーネント |
|------|-----------|------------------|
| 表紙 | cover | -- |
| アジェンダ（各セクション前） | agenda | SectionNav（自動） |
| スライドトピック識別子（各コンテンツスライド） | default / process 等 | SlideLabel（H2直上に配置） |
| 大規模セクションの内部ナビ（6スライド以上） | default | SolutionNav + SlideLabel（冒頭に一覧スライド、各詳細スライドにナビ） |
| 課題と解決策の対比 | two-cols | Callout、BeforeAfter |
| 3つの提案ポイント | default / three-cols | CardGroup + Card |
| 効果の定量表示 | kpi | KPICard、DiffArrow |
| 導入前後の比較 | default | BeforeAfter |
| 実施スケジュール | timeline | TimelineChart |
| 移行プロセス | process | ProcessFlow |
| 技術比較 | comparison-table | ComparisonTable |
| 課題の構造分解 | default | LogicTree |
| 優先度マトリクス | four-quadrant / default | Matrix2x2 |
| チーム体制 | team | テーブル |
| エグゼクティブサマリー | summary | SlideHeader、CardGroup |

---

> 本ガイドは `proposal-knowhow.md`（2026年2月版）および `design/slidev/` 配下の実装に基づいています。
> レイアウトやコンポーネントの追加・変更があった場合は、本ドキュメントも合わせて更新してください。
