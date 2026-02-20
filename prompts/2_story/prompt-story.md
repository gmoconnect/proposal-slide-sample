requirements/requirements_sample.md の提案依頼に対し、ストーリーをまずは作成したい。

- ストーリーは提案ノウハウに従う
  - design/proposal-knowhow.md
- まだslidevにはせず、普通のMarkdownで記載する。（ストーリーなど内容レビューの後、slidev化）
- 複雑な図は、別途デザイナーにて作成するので、絵に含めたい内容をテキストでまとめる。

### 提案コンセプト

AWSのサーバーレス構成＆マネージドサービスで、NoOpeでコスト・可用性・性能・セキュリティのバランスをとる。

- 認証: Cognito
- CloudFront
  --> ALB(Cognito JWT verify)
  --> ECS on Fargate
  --> Aurora Serverless v2
- ダッシュボード: S3 --> Athena --> QuickSight
- CI/CD: codecommit --> CodeBuild --> ECR image
  - codepipeline(必要に応じ手動承認) --> CodeDeploy ECS Blue/Green(TestTrafficあり)
- バイナリデータはS3 pre-signed URLを利用して、クライアントから直接読み書きすることで、通信・処理負荷をオフロード
- Fargete Imageは、golang予定
  - 単一バイナリでImageSize最小
  - Multi-Stage build+distrolessなど軽量OSベースで、ImageSize最小化。不要なpackage無しによるCVE検知の減少
  - rootFileSystem readonlyによりセキュア化
- WAFはAWS ManagedRuleの利用を想定
  - WAFのSOCが必要な場合、WafCharmなどのSOCサービスの導入を検討
- Security
  - GuardDuty, CloudTrailなど
