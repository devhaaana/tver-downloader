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

`Tver-Downloader`는 [tver.jp](https://tver.jp/) 프로그램을 일본 외 지역에서 녹화할 수 있습니다.

## 인덱스
- [인덱스](#인덱스)
- [아키텍처](#아키텍처)
- [경고](#경고)
- [사용 기술](#사용-기술)
- [시작하기](#시작하기)
  - [설치](#설치)
  - [사용 방법](#사용-방법)
- [릴리스 파일](#릴리스-파일)

## 아키텍처

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

## 경고

**이 프로젝트를 상업적인 용도로 사용하지 마십시오. 개인적, 비상업적인 용도로만 사용해 주세요.**

## 사용 기술

- `Python` : 3.12
- `FFmpeg`

## 시작하기

### 설치

- **로컬** 설치
  ```bash
  $ git clone https://github.com/devhaaana/tver-downloader.git
  $ cd tver-downloader
  ```

- 시스템에 **Python**이 설치되어 있는지 확인한 후, 다음 명령어를 실행하여 **필요한 패키지**를 설치하세요.
  ```bash
  $ conda create -n tver_env python=3.12
  $ conda activate tver_env
  $ pip install -r requirements.txt
  ```

### 사용 방법
```bash
python main.py
```

![base-ui](../images/sample/base-ui.png)

## 릴리스 파일

| 파일 | 설명 |
| --- | --- |
| [tver-downloader-1.0.0.zip](https://github.com/devhaaana/tver-downloader/archive/refs/tags/v1.0.0.zip)       | tver-downloader v1.0.0의 전체 소스 코드가 포함된 *ZIP* 파일 |
| [tver-downloader-1.0.0.tar.gz](https://github.com/devhaaana/tver-downloader/archive/refs/tags/v1.0.0.tar.gz) | tver-downloader v1.0.0의 전체 소스 코드가 포함된 *TAR.GZ* 파일 |

<br />

<div align="center">
  
  [![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fdevhaaana%2Ftver-downloader.git&count_bg=%23000000&title_bg=%23000000&icon=github.svg&icon_color=%23FFFFFF&title=GitHub&edge_flat=false)](https://hits.seeyoufarm.com)

</div>