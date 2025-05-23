<div align="center">

  [![tverpy](../images/banner.svg)](#readme)
  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE "License")
  [![Release version](https://img.shields.io/github/release/devhaaana/tver-downloader.svg?label=Download&style=for-the-badge)](#release-files "Release Files")
  [![Commits](https://img.shields.io/github/commit-activity/y/devhaaana/tver-downloader.svg?label=commits&style=for-the-badge)](https://github.com/devhaaana/tver-downloader/commits "Commit History")
  [![Last Commit](https://img.shields.io/github/last-commit/devhaaana/tver-downloader.svg?label=&style=for-the-badge&display_timestamp=committer)](https://github.com/devhaaana/tver-downloader/pulse/monthly "Last Commit")

</div>

<br />

<div align="center">

[ENGLISH](/README.md)  ·  [한국어](/documents/README-KR.md)  ·  [日本語](/documents/README-JP.md)

</div>

<br />

`Tver-Downloader`は、日本国外でも [tver.jp](https://tver.jp/) の番組を録画できます。

## インデックス

- [インデックス](#インデックス)
- [アーキテクチャ](#アーキテクチャ)
- [警告](#警告)
- [技術](#技術)
- [はじめに](#はじめに)
  - [インストール](#インストール)
  - [使用方法](#使用方法)
- [リリースファイル](#リリースファイル)

## アーキテクチャ

```
tver-downloader
├─ LICENSE
├─ README.md
├─ documents
│  ├─ README-JP.md
│  └─ README-KR.md
├─ images
│  ├─ banner.svg
│  └─ sample
│     └─ base-ui.png
├─ main.py
├─ requirements.txt
├─ tver.py
└─ utils.py
```

## 警告

**このプロジェクトを商業目的で使用しないでください。個人的な非商業的使用のみにご利用ください。**

## 技術

- `Python` : 3.12
- `FFmpeg`

## はじめに

### インストール

- **ローカル**にインストールする方法:

  ```bash
  git clone https://github.com/devhaaana/tver-downloader.git
  cd tver-downloader
  ```
- **Python** がシステムにインストールされていることを確認してください。次に、必要なパッケージを以下のコマンドでインストールします:

  ```bash
  conda create -n tver_env python=3.12
  conda activate tver_env
  pip install -r requirements.txt
  ```
- TVerのDRM追加により、日本の**VPN**または**プロキシサーバー**が必要です。

### 使用方法

```bash
python main.py
```

![base-ui](../images/sample/base-ui.png)

## リリースファイル

| File                                                                                                      | Description                                                    |
| --------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- |
| [tver-downloader-1.0.1.zip](https://github.com/devhaaana/tver-downloader/archive/refs/tags/v1.0.1.zip)       | tver-downloader v1.0.1 のソースコードを含む*ZIP* ファイル    |
| [tver-downloader-1.0.1.tar.gz](https://github.com/devhaaana/tver-downloader/archive/refs/tags/v1.0.1.tar.gz) | tver-downloader v1.0.1 のソースコードを含む*TAR.GZ* ファイル |

<br />
