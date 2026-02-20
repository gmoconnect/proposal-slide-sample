---
title: クラウドネイティブアーキテクチャによるWebサービス基盤刷新のご提案
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

# クラウドネイティブアーキテクチャによるWebサービス基盤刷新のご提案

::subtitle::

株式会社〇〇 | 2026年2月

---
layout: agenda
sections:
  - 'エグゼクティブサマリー'
  - '現状と課題'
  - 'ソリューション'
  - 'コストと効果'
  - '実施上の重要ポイント'
  - '長期戦略'
current: 0
---

---
layout: section
---

エグゼクティブサマリー

::label::

PART 1

---
layout: summary
---

## AWSサーバーレス構成により、5つの課題すべてを解決し運用負荷ゼロを実現する

<Callout type="info">

**評価項目No.5**: 本システム実現のための最適なクラウドアーキテクチャの提案ができているか。次の観点を含むこと。
**性能 / 可用性 / コスト / 拡張性 / セキュリティ / 可視化**

</Callout>

| 現行の課題 | 解決策 | 評価観点 |
|---|---|---|
| ハードウェア故障による可用性低下 | Multi-AZ Fargate + Aurora Serverless v2 | **可用性** |
| 月末アクセス集中とピークコスト | Fargate/Aurora自動スケーリング + CloudFront | **性能・コスト・拡張性** |
| DB拡張性ボトルネック | S3オフロード + Aurora自動拡張 + S3階層化 | **拡張性・コスト・性能** |
| 日々のオペレーション負荷 | マネージドサービス + Go Distroless + CI/CD | **セキュリティ・コスト** |
| KPI可視化の欠如 | S3ログ → Athena → QuickSightダッシュボード | **可視化** |

**提案コンセプト: 「NoOpsでコスト・可用性・性能・セキュリティのバランスをとる」**

---
layout: kpi
---

<h2 class="!text-[16px] !mb-[8px]">6つの評価観点すべてにおいて、現行システムから定量的に大幅改善する</h2>

<div class="grid grid-cols-3 gap-[8px] [&>div]:p-[8px]">
  <KPICard value="~100" unit="倍" label="性能" change="ピーク時レスポンス安定" :positive="true" />
  <KPICard value="99.95" unit="%" label="可用性" change="自動フェイルオーバー" :positive="true" />
  <KPICard value="92" unit="%" label="コスト" change="従量課金+S3階層化" :positive="true" />
  <KPICard value="1TB" unit="" label="拡張性" change="S3容量無制限" :positive="true" />
  <KPICard value="大幅" unit="削減" label="セキュリティ" change="CVE対象削減+監視自動化" :positive="true" />
  <KPICard value="RT" unit="" label="可視化" change="リアルタイムBIダッシュボード" :positive="true" />
</div>

---
layout: agenda
sections:
  - 'エグゼクティブサマリー'
  - '現状と課題'
  - 'ソリューション'
  - 'コストと効果'
  - '実施上の重要ポイント'
  - '長期戦略'
current: 1
---

---
layout: section
---

現状分析と課題

::label::

PART 2

---
layout: default
---

## 現行オンプレミスシステムはハードウェア保守期限を迎え、抜本的な基盤刷新が必要である

<CardGroup :cols="3">
  <Card title="Web層" icon="1">Webサーバー（オンプレミス）</Card>
  <Card title="AP層" icon="2">アプリケーションサーバー（モノリシック構成）</Card>
  <Card title="DB層" icon="3">RDBMS（構造化データ＋バイナリデータを格納）</Card>
</CardGroup>

<div class="mt-[16px]">

**現行の課題:**

- すべてのコンポーネントが単一データセンター内に配置 → **DC障害時にサービス全体が停止**
- バイナリデータ（画像・PDF等）もRDBMSに格納 → Web→AP→DBの全層を経由 → **レスポンス遅延**
- ハードウェア保守期限が到来 → 「同等HW更新」か「クラウド移行」かの判断が必要

</div>

<Callout type="warning">

ハードウェアを新調しても同じアーキテクチャ上の問題は解決しない。抜本的な基盤刷新が必要。

</Callout>

---
layout: default
---

## 現行システムにはインフラ起因の3つの構造的課題がある

<CardGroup :cols="3">
  <Card title="課題1: 可用性低下" icon="1">

単一DC構成のため、HW障害がサービス停止に直結。大規模災害時のBCP対応も必要。
→ **利用者の業務が完全に停止**

  </Card>
  <Card title="課題2: ピークアクセス" icon="2">

月間100万アクセスの90%が月末2日間に集中。ピーク/通常比 <Highlight>約100倍</Highlight>。
→ **IT予算を圧迫**

  </Card>
  <Card title="課題3: DB拡張性" icon="3">

現状100GB → 5年後1TB。データの<Highlight>90%がバイナリ</Highlight>。RDBMSへの格納は非効率。
→ **サービス継続困難のリスク**

  </Card>
</CardGroup>

<Callout type="info">

ピーク時: 90万アクセス/8時間 ≒ 31 req/sec、通常時: 約0.3 req/sec。30日超のデータは参照頻度が極めて低いが、法定保存期限の5年間保管が必要。

</Callout>

---
layout: summary
---

## 運用・可視化にも2つの構造的課題があり、クラウドネイティブアーキテクチャへの刷新が必要である

<CardGroup :cols="2">
  <Card title="課題4: オペレーション負荷" icon="4">

セキュリティ監視、CVE確認、OSパッチ適用、ログローテーション、バックアップなど日常的な運用作業が多岐にわたる。
→ **運用チームの工数が定常作業に占有され、改善・新機能開発に充てる余力がない**

  </Card>
  <Card title="課題5: KPI可視化の欠如" icon="5">

システムおよびWebサービスのKPIが可視化されておらず、データに基づく意思決定ができていない。
→ **問題の早期発見ができず、障害の長期化やサービス品質低下を招くリスク**

  </Card>
</CardGroup>

| # | 課題 | 関連する評価観点 |
|---|---|---|
| 1 | ハードウェア故障による可用性低下 | 可用性 |
| 2 | 月末アクセス集中とピークコスト | 性能・コスト・拡張性 |
| 3 | データベースの拡張性ボトルネック | 拡張性・コスト・性能 |
| 4 | 日々のオペレーション負荷 | セキュリティ・コスト |
| 5 | KPI可視化の欠如 | 可視化 |

<Callout type="success">

ハードウェア更新ではなく、**クラウドネイティブアーキテクチャへの刷新**で5つの課題すべてを解決する。

</Callout>

---
layout: agenda
sections:
  - 'エグゼクティブサマリー'
  - '現状と課題'
  - 'ソリューション'
  - 'コストと効果'
  - '実施上の重要ポイント'
  - '長期戦略'
current: 2
---

---
layout: section
---

ソリューション提案

::label::

PART 3

---
layout: default
---

## AWSサーバーレス・マネージドサービスを中心としたクラウドネイティブアーキテクチャで全課題を解決する

<Callout type="info">

**[ ここにアーキテクチャ全体図を挿入 ]**

</Callout>

**図に含めるべき要素:**

- **メインフロー**: ユーザー → CloudFront（CDN + WAF） → ALB（JWT検証） → ECS on Fargate → Aurora Serverless v2
- **認証フロー**: ユーザー ↔ Amazon Cognito（MFA対応）
- **バイナリデータフロー**: ユーザー ↔ S3（Pre-signed URL、アプリ層をバイパス）
- **ダッシュボードフロー**: S3ログ → Athena → QuickSight
- **CI/CDフロー**: CodeCommit → CodeBuild → ECR → CodePipeline → CodeDeploy（Blue/Green）
- **セキュリティ層**: WAF（エッジ）、GuardDuty、CloudTrail
- **可用性**: 全コンポーネントMulti-AZ配置（2〜3 AZ）
- **カラーコード**: コンピュート（青）、ストレージ（緑）、セキュリティ（オレンジ）、監視（紫）

---
layout: default
---

## CloudFront + Fargate自動スケーリングにより、月末ピーク時でもレスポンス劣化なく対応する

<BeforeAfter improvement="従量課金で最適化" beforeLabel="現行（固定構成）" afterLabel="提案（自動スケール）">
  <template #before>
    <ul>
      <li>ピーク性能に合わせたHWを常時稼働</li>
      <li>月の大半はリソースが過剰 → <strong>コスト浪費</strong></li>
      <li>それでもピーク時はリソース不足のリスク</li>
    </ul>
  </template>
  <template #after>
    <ul>
      <li><strong>CloudFront</strong>: 静的コンテンツをエッジキャッシュ</li>
      <li><strong>Fargate</strong>: 2タスク ↔ 20タスク自動スケール</li>
      <li><strong>従量課金</strong>: タスク稼働時間のみ課金</li>
    </ul>
  </template>
</BeforeAfter>

<Callout type="info">

ピーク時: 31 req/sec → Fargateタスク自動増加で対応。通常時: 0.3 req/sec → 最小構成で運用。ピーク/通常比 **約100倍** の差を従量課金で吸収。

</Callout>

---
layout: default
---

## Aurora Serverless v2により、データベースの容量・性能がワークロードに応じて自動調整される

<BeforeAfter improvement="自動スケーリング" beforeLabel="現行DB" afterLabel="Aurora Serverless v2">
  <template #before>
    <ul>
      <li>固定スペックのDBサーバー</li>
      <li>容量拡張は手動（HW増設 or リプレース）</li>
      <li><strong>単一障害点</strong>: DB故障時はサービス全体が停止</li>
    </ul>
  </template>
  <template #after>
    <ul>
      <li><strong>ACU自動スケーリング</strong>: 0.5〜128 ACU、ワークロードに応じて自動調整</li>
      <li><strong>ストレージ自動拡張</strong>: 使用量に応じて自動拡張（最大128TB）</li>
      <li><strong>Multi-AZフェイルオーバー</strong>: 通常30秒以内で自動切替</li>
    </ul>
  </template>
</BeforeAfter>

<Callout type="info">

バイナリデータ（データ全体の90%）をS3にオフロードすることで、Aurora Serverless v2にはメタデータのみを格納。5年後もDBサイズは約100GBに抑制。

</Callout>

---
layout: default
---

## S3 Pre-signed URLによりバイナリデータをオフロードし、アプリケーション負荷とDBボトルネックを同時に解消する

<BeforeAfter improvement="転送量90%削減" beforeLabel="現行フロー" afterLabel="提案フロー">
  <template #before>
    <ul>
      <li>Client → Web → AP → <strong>DB（バイナリ格納）</strong></li>
      <li>全データがアプリケーション層を経由</li>
      <li>DBサイズ肥大化（100GB、うち90GBがバイナリ）</li>
    </ul>
  </template>
  <template #after>
    <ul>
      <li>メタデータ: Client → AP → Aurora（<strong>10%</strong>）</li>
      <li>バイナリ: Client ↔ <strong>S3直接</strong>（<strong>90%</strong>）</li>
      <li>DBサイズ: 約100GB（メタデータのみ）に抑制</li>
    </ul>
  </template>
</BeforeAfter>

<Callout type="success">

AP・DBをバイナリ転送から完全解放。S3は容量無制限のため将来のデータ増にも対応可能。

</Callout>

---
layout: process
---

<div class="w-full">

## S3ライフサイクルポリシーにより、5年間のデータ保管コストを最大92%削減する

<ProcessFlow :steps="[
  { label: 'アップロード', description: 'S3 Standard' },
  { label: '30日後', description: 'Glacier Instant' },
  { label: '1年後', description: 'Deep Archive' },
  { label: '5年保管', description: '法定期限まで' },
]" />

<div class="mt-[24px]">

| ストレージクラス | コスト（GB/月） | 取得時間 |
|---|---|---|
| S3 Standard | $0.025 | ミリ秒 |
| S3 Glacier Instant Retrieval | $0.005 | ミリ秒 |
| S3 Glacier Deep Archive | $0.002 | 12時間以内 |

</div>

<Callout type="success">

S3 Standard → Deep Archive で **約92%のコスト削減**。要件「取り出しに時間がかかっても良い」に完全合致。ライフサイクルポリシーは一度設定すれば自動実行。

</Callout>

</div>

---
layout: comparison-table
---

## Go言語 + Distrolessイメージにより、コンテナの攻撃面を極小化する

<ComparisonTable
  :headers="['項目', '一般的なイメージ（Ubuntu+ランタイム）', 'Go + Distroless']"
  :rows="[
    ['イメージサイズ', '約500MB', '約10〜20MB'],
    ['CVE対象パッケージ数', '100以上（OS, ライブラリ, ツール）', '大幅削減（Go標準ライブラリのみ）'],
    ['シェルアクセス', 'あり（攻撃者に利用されるリスク）', 'なし（シェル非搭載）'],
    ['パッケージマネージャー', 'あり', 'なし'],
    ['rootファイルシステム', '読み書き可能', 'read-only設定'],
  ]"
  :highlightCol="2"
/>

<Callout type="info">

OS層やミドルウェアがほぼ存在しないため、CVEの検知対象が大幅に減少し攻撃面を極小化する。

</Callout>

---
layout: default
---

## Distroless + read-only FSにより、セキュリティ運用工数を大幅に削減しNoOpsに貢献する

**セキュリティ効果:**

<CardGroup :cols="3">
  <Card title="Distroless" icon="1">OS・シェル非搭載で攻撃面を極小化</Card>
  <Card title="Read-only FS" icon="2">マルウェアの永続化を防止。実行時にファイルを書き込めない</Card>
  <Card title="Multi-Stage Build" icon="3">ビルドツールが本番イメージに含まれない</Card>
</CardGroup>

<div class="mt-[16px]">

**運用効果:**

</div>

<CardGroup :cols="3">
  <Card title="CVE工数削減" icon="4">Go自体の更新のみ対応すればよい</Card>
  <Card title="デプロイ高速化" icon="5">イメージサイズが小さくCI/CDが高速化</Card>
  <Card title="NoOps貢献" icon="6">運用チームをセキュリティ運用から解放</Card>
</CardGroup>

---
layout: comparison-table
---

## WAF・GuardDuty・CloudTrailの多層防御により、エッジからデータ層まで自動的に保護する

<ComparisonTable
  :headers="['防御層', 'サービス', '役割']"
  :rows="[
    ['エッジ層', 'CloudFront + AWS WAF（Managed Rules）', 'DDoS防御、OWASP Top 10対策、不正リクエスト遮断'],
    ['認証層', 'ALB + Cognito JWT検証', '未認証リクエストをアプリケーション到達前に遮断'],
    ['コンピュート層', 'ECS on Fargate（read-only FS、SSHなし）', 'コンテナ内部への侵入・改ざんを防止'],
    ['監視層', 'GuardDuty', '機械学習ベースの脅威検出（不正アクセス、マルウェア通信等）'],
    ['監査層', 'CloudTrail', '全APIコールの記録・監査証跡の保全'],
  ]"
  :highlightCol="1"
/>

<Callout type="info">

すべてマネージドサービスのため、セキュリティ監視の自動化が実現する。外側から内側に向かう多層防御（オニオンモデル）を構成。

</Callout>

---
layout: comparison-table
---

## マネージドサービスにより、セキュリティ運用の大半を自動化しNoOpsを実現する

<ComparisonTable
  :headers="['運用項目', 'Before（手動）', 'After（マネージド）']"
  :rows="[
    ['セキュリティ監視', '24/365の有人監視', 'GuardDutyが自動検出・アラート'],
    ['CVE確認', '手動で定期確認', 'Distrolessで対象大幅削減 + ECRイメージスキャン自動化'],
    ['OSパッチ適用', '手動適用・再起動', 'Fargateはマネージド基盤。OS管理不要'],
    ['ログ管理', '手動ローテーション・保管', 'CloudWatch Logs / S3で自動管理'],
    ['バックアップ', '手動実施', 'Aurora自動バックアップ + S3バージョニング'],
  ]"
  :highlightCol="2"
/>

<Callout type="success">

運用チームは手動のセキュリティ運用から解放され、改善・新機能開発に注力できる。

</Callout>

---
layout: comparison-table
---

## Multi-AZ構成と自動フェイルオーバーにより、99.95%以上の可用性を確保する

<ComparisonTable
  :headers="['コンポーネント', '可用性設計', 'SLA']"
  :rows="[
    ['CloudFront', 'グローバルエッジ、本質的に高可用', '99.9%'],
    ['ALB', 'Multi-AZ自動分散', '99.99%'],
    ['ECS on Fargate', 'タスクをAZ間に分散配置、異常タスク自動置換', '99.99%'],
    ['Aurora Serverless v2', 'Multi-AZフェイルオーバー（通常30秒以内）', '99.99%'],
    ['S3', '99.999999999%の耐久性', '99.99%'],
  ]"
  :highlightCol="2"
/>

**遠隔地バックアップ:**
- **Aurora**: AWS Backupによるクロスリージョンバックアップ
- **S3**: クロスリージョンレプリケーションで別リージョンに自動複製

<Callout type="info">

すべてのコンポーネントをMulti-AZに配置し、単一障害点を完全に排除。遠隔地バックアップでBCP対応も実現。

</Callout>

---
layout: process
---

<div class="w-full">

## Cognito + ALBのJWT検証により、不正リクエストをアプリケーション到達前に遮断する

<ProcessFlow :steps="[
  { label: '1. 認証要求', description: 'ID/PW + MFA' },
  { label: '2. JWT発行', description: 'Cognito検証' },
  { label: '3. リクエスト', description: 'JWT付き送信' },
  { label: '4. JWT検証', description: 'ALBで判定' },
  { label: '5. 転送/遮断', description: '有効→Fargate' },
]" />

<div class="mt-[24px]">

- **有効な場合**: ALBがリクエストをFargateに転送 → 正常処理
- **無効な場合**: ALBが403 Forbiddenを返却 → **アプリケーションに到達しない**

</div>

<Callout type="success">

認証されていないリクエストはアプリケーション到達前に遮断される。アプリケーション層の負荷軽減とセキュリティ強化を同時に実現。

</Callout>

</div>

---
layout: default
---

## マネージド認証基盤により、認証の運用負荷ゼロとピーク時のスケーラビリティを両立する

<BeforeAfter improvement="運用ゼロ" beforeLabel="自前認証基盤" afterLabel="Cognito">
  <template #before>
    <ul>
      <li>自前で構築・運用が必要</li>
      <li>認証サーバーの増強が必要</li>
      <li>MFA実装は追加開発が必要</li>
      <li>アプリ層で認証処理</li>
    </ul>
  </template>
  <template #after>
    <ul>
      <li><strong>フルマネージド、運用ゼロ</strong></li>
      <li><strong>自動スケール、ピーク時も対応</strong></li>
      <li><strong>MFA対応が標準機能</strong></li>
      <li><strong>ALBで遮断、アプリ負荷軽減</strong></li>
    </ul>
  </template>
</BeforeAfter>

<Callout type="info">

Cognitoはフルマネージドサービスのため、認証インフラの構築・運用が不要。認証基盤自体がスケーラブルなため、月末ピーク時にも認証がボトルネックにならない。

</Callout>

---
layout: default
---

## QuickSightダッシュボードにより、システムKPIをリアルタイムに可視化する

<ProcessFlow :steps="[
  { label: 'ログ収集', description: 'CloudFront/ALB/App' },
  { label: 'S3集約', description: 'ログストレージ' },
  { label: 'Athena', description: 'サーバーレスSQL' },
  { label: 'QuickSight', description: 'BIダッシュボード' },
]" />

<div class="mt-[24px]">

**可視化KPI例:**

- アクセス数の推移（日次・時間帯別・月末ピーク分析）
- レスポンスタイムの推移
- エラー率の推移
- リソース使用率（Fargate CPU/メモリ、Aurora ACU）
- ストレージ使用量の推移

</div>

<Callout type="success">

サーバー管理不要・クエリ実行時のみ課金のサーバーレス分析基盤で、データに基づく意思決定を実現。

</Callout>

---
layout: agenda
sections:
  - 'エグゼクティブサマリー'
  - '現状と課題'
  - 'ソリューション'
  - 'コストと効果'
  - '実施上の重要ポイント'
  - '長期戦略'
current: 3
---

---
layout: section
---

AWSランニングコストと効果

::label::

PART 4

---
layout: default
---

## 従量課金モデルにより、月額ランニングコストを最適化する

| サービス | 通常時 | ピーク時（月末2日間） | 備考 |
|---|---|---|---|
| ECS on Fargate | 最小タスク構成 | タスク自動増加分のみ追加 | vCPU/メモリ × 稼働秒数 |
| Aurora Serverless v2 | 最小ACU | ACU自動増加分のみ追加 | ACU × 稼働時間 |
| S3 | 格納量に応じた課金 | - | ライフサイクルで階層化済み |
| CloudFront | 転送量に応じた課金 | キャッシュ効果あり | エッジキャッシュ |

**コスト最適化のポイント:**

- Fargate/Aurora: 通常時（月の約93%）は最小構成で稼働 → ピーク構成固定に比べ大幅な削減
- S3ライフサイクル: アーカイブデータは最大92%のストレージコスト削減
- マネージドサービス: 人件費（セキュリティ監視、パッチ適用等）のコスト削減効果

<Callout type="info">

詳細な前提条件・全サービスの内訳は補足資料Cに記載。

</Callout>

---
layout: comparison-table
---

## 6つの評価観点すべてにおいて、提案アーキテクチャにより現行システムから定量的に改善される

<ComparisonTable
  :headers="['評価観点', 'Before（現行オンプレ）', 'After（AWS提案構成）', '改善ポイント']"
  :rows="[
    ['性能', '固定容量、ピーク時にリスク', 'Fargate/Aurora自動スケール + CloudFront CDN', 'ピーク時もレスポンス安定'],
    ['可用性', '単一DC、手動フェイルオーバー', 'Multi-AZ自動フェイルオーバー', 'SLA 99.95%以上'],
    ['コスト', 'ピーク構成の固定費用', '従量課金 + S3階層化', '通常時コスト大幅削減'],
    ['拡張性', 'DB 100GB上限、バイナリもDB格納', 'S3容量無制限 + Aurora自動拡張', '5年後1TBに対応'],
    ['セキュリティ', '手動監視・手動パッチ', 'マネージドWAF + GuardDuty + Distroless', '運用自動化、CVE大幅削減'],
    ['可視化', 'KPIダッシュボードなし', 'QuickSightリアルタイムダッシュボード', 'データ駆動の意思決定'],
  ]"
  :highlightCol="2"
/>

---
layout: agenda
sections:
  - 'エグゼクティブサマリー'
  - '現状と課題'
  - 'ソリューション'
  - 'コストと効果'
  - '実施上の重要ポイント'
  - '長期戦略'
current: 4
---

---
layout: section
---

実施上の重要ポイント

::label::

PART 5

---
layout: process
---

<div class="w-full">

## CI/CDパイプラインとBlue/Greenデプロイにより、ゼロダウンタイムで安全なリリースを実現する

<ProcessFlow :steps="[
  { label: 'CodeCommit', description: 'ソース管理' },
  { label: 'CodeBuild', description: 'ビルド・テスト' },
  { label: 'ECR', description: 'イメージ保管' },
  { label: 'CodePipeline', description: '手動承認' },
  { label: 'CodeDeploy', description: 'Blue/Green' },
]" />

<div class="mt-[24px]">

**Blue/Greenデプロイ:**
- 新バージョンをGreen環境にデプロイ → TestTrafficで検証 → 本番トラフィックをGreenに切替
- 問題発生 → Blue環境に即時ロールバック（**ダウンタイムゼロ**）
- 手動承認ステップにより本番リリースの統制を維持

</div>

<Callout type="info">

完全自動化されたCI/CDパイプラインで、品質を確保しつつ迅速なリリースサイクルを実現。ロールバックは自動で数分以内に完了。

</Callout>

</div>

---
layout: comparison-table
---

## クラウド移行に伴うリスクを事前に特定し、対策を講じる

<ComparisonTable
  :headers="['リスク', '影響', '対策']"
  :rows="[
    ['データ移行時のデータ不整合', '移行後にデータ欠損・不整合が発生', '移行前後のデータ件数・チェックサム照合。段階的な移行で影響範囲を限定'],
    ['切り替え時のサービス停止', 'ユーザーがサービスを利用できない', 'DNS加重ルーティングによる段階的移行。問題時は即時切り戻し可能'],
    ['運用チームの習熟不足', 'インシデント対応が遅延', '移行前にAWSトレーニング実施。運用手順書の整備。移行後はサポート体制を強化'],
    ['想定外のコスト増', '従量課金の見積もりと実績に乖離', 'AWS Cost Explorerで日次モニタリング。Budgetsアラートで閾値超過を即時検知'],
  ]"
  :highlightCol="2"
/>

<Callout type="info">

主要なリスクを事前に特定し、それぞれに具体的な対策を講じることで移行の成功確率を高める。

</Callout>

---
layout: agenda
sections:
  - 'エグゼクティブサマリー'
  - '現状と課題'
  - 'ソリューション'
  - 'コストと効果'
  - '実施上の重要ポイント'
  - '長期戦略'
current: 5
---

---
layout: section
---

長期戦略

::label::

PART 6

---
layout: default
---

## API設計により、外部システム連携やAIエージェント活用など将来の機能拡張に柔軟に対応する

<LogicTree :tree="{
  label: '提案アーキテクチャの拡張性',
  children: [
    { label: 'フロント・バック分離', detail: 'CloudFront + ALB + Fargate', children: [{ label: 'APIベースの設計' }] },
    { label: 'API公開基盤', detail: '外部システム連携が容易', children: [{ label: '将来的なAPI公開' }] },
    { label: 'AIエージェント連携', detail: 'MCPを通じたシステム利活用', children: [{ label: '新たな活用可能性' }] },
  ]
}" />

<div class="mt-[16px]">

**AWSマネージドサービスの継続的進化:**
- AWSが継続的にサービスを改善・機能追加
- 最新のセキュリティパッチが自動適用
- 新機能の追加はサービス設定の変更のみで対応可能

</div>

<Callout type="success">

フロントエンドとバックエンドが明確に分離されたAPI構成により、将来的な外部システム連携やAIエージェント活用にも柔軟に対応。

</Callout>

---
layout: default
---

## IaCによりインフラ構成をコード管理し、環境の再現性と変更管理を確保する

<BeforeAfter improvement="コード管理" beforeLabel="手動管理" afterLabel="IaC（Infrastructure as Code）">
  <template #before>
    <ul>
      <li>手動で個別構築、手順書依存</li>
      <li>変更履歴が不明確</li>
      <li>手動変更が蓄積し構成が不明に</li>
      <li>手順書に基づく手動復旧</li>
    </ul>
  </template>
  <template #after>
    <ul>
      <li><strong>同一コードから開発・ステージング・本番を構築</strong></li>
      <li><strong>コードレビュー + CI/CDで統制</strong></li>
      <li><strong>ドリフト検知で差分を自動検出・是正</strong></li>
      <li><strong>コードから環境を再構築</strong></li>
    </ul>
  </template>
</BeforeAfter>

<Callout type="info">

CloudFormation / CDKでインフラ構成を定義し、CI/CDパイプラインと連携してインフラ変更も自動テスト・デプロイ。

</Callout>

---
layout: section
---

まとめ

---
layout: summary
---

## 評価項目No.5に対する回答の総括 — AWSサーバーレス構成で6つの評価観点すべてを満たす

<Callout type="info">

**評価項目No.5**: 本システム実現のための最適なクラウドアーキテクチャの提案ができているか。次の観点を含むこと。
**性能 / 可用性 / コスト / 拡張性 / セキュリティ / 可視化**

</Callout>

| 評価観点 | 本提案での回答 | 該当スライド |
|---|---|---|
| **性能** | Fargate/Aurora自動スケール + CloudFront CDNでピーク約100倍でも安定。S3オフロードで転送量90%削減 | 7, 8, 9 |
| **可用性** | 全層Multi-AZ + 自動フェイルオーバーでSLA 99.95%以上。クロスリージョンバックアップ対応 | 15, 21 |
| **コスト** | 従量課金で通常時コスト大幅削減。S3階層化で保管コスト最大92%削減 | 7, 10, 19 |
| **拡張性** | S3容量無制限 + Aurora自動拡張。バイナリオフロードでDB 1/10。5年後1TB対応 | 8, 9, 10 |
| **セキュリティ** | WAF + GuardDuty + CloudTrailの多層防御。Distroless + read-only FSでCVE大幅削減 | 11-14, 16 |
| **可視化** | S3ログ → Athena → QuickSightでリアルタイムBIダッシュボードを構築 | 18 |

**本提案のAWSサーバーレス・マネージドサービス構成は、評価項目No.5が求める「本システム実現のための最適なクラウドアーキテクチャ」を、6つの評価観点すべてにおいて実現する。**

---
layout: section
---

補足資料（Appendix）

---
layout: default
---

## 補足A: AWS各サービスのSLA一覧

| サービス | SLA（月間稼働率） | 補足 |
|---|---|---|
| Amazon CloudFront | 99.9% | グローバルエッジネットワーク |
| Elastic Load Balancing (ALB) | 99.99% | Multi-AZ自動分散 |
| Amazon ECS on Fargate | 99.99% | Multi-AZタスク配置 |
| Amazon Aurora | 99.99% | Multi-AZフェイルオーバー |
| Amazon S3 | 99.99%（可用性）/ 99.999999999%（耐久性） | イレブンナインの耐久性 |
| Amazon Cognito | 99.9% | マネージド認証 |
| AWS WAF | CloudFrontまたはALBのSLAに準ずる | - |
| Amazon GuardDuty | リージョン内の高可用性 | マネージド脅威検出 |

---
layout: default
---

## 補足B: S3ストレージクラス別コスト詳細

| ストレージクラス | 保管コスト（GB/月） | 取得コスト | 最低保管期間 | 取得時間 |
|---|---|---|---|---|
| S3 Standard | $0.025 | 無料 | なし | ミリ秒 |
| S3 Standard-IA | $0.0138 | $0.01/GB | 30日 | ミリ秒 |
| S3 Glacier Instant Retrieval | $0.005 | $0.03/GB | 90日 | ミリ秒 |
| S3 Glacier Flexible Retrieval | $0.0045 | $0.01/GB（標準） | 90日 | 数分〜数時間 |
| S3 Glacier Deep Archive | $0.002 | $0.02/GB（標準） | 180日 | 12時間以内 |

::footnote::

料金は東京リージョン（ap-northeast-1）の参考値。最新の料金はAWS公式サイトを参照。

---
layout: summary
---

## 補足C: AWSランニングコスト試算の前提条件と全サービス内訳

**前提条件:**
- リージョン: 東京（ap-northeast-1）
- 月間アクセス数: 100万リクエスト
- データ量: 初年度100GB、5年後1TB
- バイナリデータ比率: 90%
- ピーク時トラフィック: 月末2営業日の営業時間（8時間）に月間アクセスの90%が集中

| サービス | サイジング前提 | 概算月額 |
|---|---|---|
| ECS on Fargate | 通常時: 0.5vCPU/1GBメモリ × 2タスク、ピーク時: × 10〜20タスク | [要見積] |
| Aurora Serverless v2 | 通常時: 0.5 ACU、ピーク時: 4〜8 ACU | [要見積] |
| S3 | 初年度: 100GB（Standard + ライフサイクル移行） | [要見積] |
| CloudFront | 月間データ転送量に依存 | [要見積] |
| ALB | 固定費 + LCU課金 | [要見積] |
| Cognito | MAU課金。50,000 MAUまで無料枠 | [要見積] |
| WAF | WebACL + ルール数 + リクエスト数 | [要見積] |
| GuardDuty | 分析データ量に応じた課金 | [要見積] |
| QuickSight | ユーザー数課金 | [要見積] |
| CodePipeline/Build/Deploy | パイプライン実行回数課金 | [要見積] |

::footnote::

詳細な見積もりはAWS Pricing Calculatorを用いて別途算出する。

---
layout: summary
---

## 補足D: セキュリティ対策の詳細マッピング

| 脅威カテゴリ | 対策 | AWSサービス |
|---|---|---|
| DDoS攻撃 | エッジでの遮断、レート制限 | CloudFront + AWS Shield Standard |
| SQLインジェクション / XSS | WAFルールによる検知・遮断 | AWS WAF（Managed Rules） |
| 不正アクセス | JWT認証、MFA | Cognito + ALB |
| コンテナへの侵入 | read-only FS、シェルなし、SSHなし | Fargate + Distroless |
| 内部脅威・異常行動 | 機械学習ベースの異常検知 | GuardDuty |
| 監査証跡 | 全APIコールの記録 | CloudTrail |
| データ暗号化 | 保管時・転送時の暗号化 | S3 SSE、Aurora暗号化、ACM(TLS) |
| 脆弱性管理 | コンテナイメージスキャン | ECRイメージスキャン |

**WAF SOCオプション:**
AWS Managed Rulesで主要な攻撃パターンに対応。より高度なWAF運用（カスタムルール管理、24/365監視、インシデント対応）が必要な場合、WafCharm等のSOCサービスの導入を検討。

---
layout: default
---

## 補足E: Go + Distrolessのベンチマーク比較

**コンテナイメージサイズ比較:**

| ベースイメージ | イメージサイズ | 備考 |
|---|---|---|
| Ubuntu 22.04 + Go runtime | 約800MB | フルOS + ツール群 |
| Alpine + Go runtime | 約300MB | 軽量Linux |
| golang:alpine (multi-stage) | 約15MB | ビルドステージ分離 |
| **gcr.io/distroless/static** | **約10MB** | **OS/シェルなし、最小構成** |

**Multi-Stage Buildフロー:**

```
Stage 1 (Builder): golang:alpine → ソースコード取得 → go build → 単一バイナリ生成
Stage 2 (Production): gcr.io/distroless/static → 単一バイナリのみコピー → 最終イメージ
```

**セキュリティ比較（CVE検知数の目安）:**

| ベースイメージ | 一般的なCVE検知数 | 備考 |
|---|---|---|
| Ubuntu 22.04 | 50〜200件 | OS・ライブラリの脆弱性を含む |
| Alpine | 10〜30件 | 軽量だがmusl libc等の脆弱性 |
| **Distroless** | **極少** | **OS層の脆弱性がほぼゼロ** |
