# Gist エンドポイントに関連するコンポーネント一覧

## 1. パラメータコンポーネント

### `#/components/parameters/since`
- **説明**: `since` パラメータは、特定の日時以降の情報を取得するための条件として使用されます。これにより、クライアントは過去の指定日時以降に更新されたGistの情報のみを取得できます。

### `#/components/parameters/per-page`
- **説明**: `per-page` パラメータは、1ページに表示されるアイテムの数を指定します。ページネーションに関連し、クライアントは必要なデータの量を調整することが可能です。

### `#/components/parameters/page`
- **説明**: `page` パラメータは、ページネーションを実現するために特定のページ番号を指定します。これにより、クライアントは複数ページに分かれたデータから必要なページのデータを取得できます。

### `#/components/parameters/gist-id`
- **説明**: `gist-id` パラメータは、操作対象のGistを特定するために使用されます。各Gistには固有のIDが付与されており、このIDを使って操作を行います。

### `#/components/parameters/comment-id`
- **説明**: `comment-id` パラメータは、特定のコメントを特定するために使用されます。Gistに対するコメント操作を行う際に、特定のコメントを参照するためのIDです。

## 2. スキーマコンポーネント

### `#/components/schemas/base-gist`
- **説明**: Gistの基本情報を定義するスキーマです。このスキーマにはGistの概要、ファイルリスト、作者情報などが含まれます。

### `#/components/schemas/gist-comment`
- **説明**: Gistコメントを定義するスキーマです。コメントの本文、作者、タイムスタンプなどの詳細が含まれます。

### `#/components/schemas/gist-commit`
- **説明**: Gistのコミット情報を定義するスキーマです。特定のGistに対する変更履歴を示し、誰がいつ変更を加えたかなどの情報を含みます。

### `#/components/schemas/gist-simple`
- **説明**: シンプルなGist情報を定義するスキーマです。このスキーマは通常のGistの要約情報を提供し、より詳細な情報は別のスキーマに含まれます。

## 3. レスポンスコンポーネント

### `#/components/responses/not_modified`
- **説明**: リクエストに変更がない場合に使用されるレスポンスです。クライアントが最後に受け取った状態と変わらない場合に `304 Not Modified` が返されます。

### `#/components/responses/forbidden`
- **説明**: リクエストが許可されていない場合に返されるレスポンスです。クライアントに適切な認証や権限がない場合に使用されます。

### `#/components/responses/not_found`
- **説明**: リクエストしたリソースが見つからない場合に返されるレスポンスです。存在しないGistやコメントなどを参照した際に `404 Not Found` が返されます。

### `#/components/responses/forbidden_gist`
- **説明**: 特定のGistへのアクセスが許可されていない場合に使用されるレスポンスです。プライベートGistなどに対して不正なアクセスが行われた場合に返されます。

### `#/components/responses/validation_failed`
- **説明**: リクエストのバリデーションに失敗した場合に使用されるレスポンスです。入力データの形式や内容に不備がある場合に `422 Unprocessable Entity` が返されます。

### `#/components/responses/requires_authentication`
- **説明**: 認証が必要なリクエストに対して、認証が行われていない場合に返されるレスポンスです。 `401 Unauthorized` が返されます。

## 4. ヘッダーコンポーネント

### `#/components/headers/link`
- **説明**: ページネーションなどで複数ページにまたがるリソースを参照する際に使用されるリンクヘッダーです。次や前のページのURLを示します。

## 5. 例コンポーネント

### `#/components/examples/base-gist-items`
- **説明**: Gistの基本情報の例を提供するコンポーネントです。クライアントがリクエストやレスポンスの理解を深めるために使用されます。

### `#/components/examples/gist-comment`
- **説明**: Gistコメントの例を提供するコンポーネントです。コメントの内容やフォーマットを示します。

### `#/components/examples/gist-comment-items`
- **説明**: 複数のGistコメントの例を提供します。複数コメントのレスポンスの形式を示すために使用されます。

### `#/components/examples/gist-commit-items`
- **説明**: Gistコミットの例を提供します。変更履歴がどのような形式で提供されるかを示します。

### `#/components/examples/gist-fork-items`
- **説明**: Gistのフォーク例を提供します。フォークされたGistの情報のレスポンス形式を示すために使用されます。

### `#/components/examples/base-gist`
- **説明**: 基本的なGistの例を提供します。新規作成や取得したGistの典型的なデータ形式を示します。

### `#/components/examples/gist`
- **説明**: Gistの具体的な例です。特定のリクエストやレスポンスの理解を補助するために使用されます。

### `#/components/examples/delete-gist-file`
- **説明**: Gistファイルを削除する際のリクエスト例です。削除操作の理解を補助するために提供されます。

### `#/components/examples/rename-gist-file`
- **説明**: Gistファイルの名前を変更する際のリクエスト例です。ファイル名変更操作の理解を補助します。
