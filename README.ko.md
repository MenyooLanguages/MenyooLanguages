<p align="center"><img src="assets/banner.svg" alt="Menyoo Language Packs — 16 languages, 100% coverage" width="100%"></p>

<div align="center">

# 🌍 Menyoo Language Packs — 한국어

**Menyoo 인터페이스 한국어 번역 — 3164개 문자열, 100% 커버리지.**

[![Coverage](https://img.shields.io/badge/coverage-100%25-brightgreen)](#-pack) [![Strings](https://img.shields.io/badge/strings-3164-blue)](#-pack) [![License](https://img.shields.io/badge/license-MIT-important)](LICENSE) [![GTA V](https://img.shields.io/badge/GTA%20V-Enhanced%20%26%20Legacy-orange)](#-installation)

[English](README.md) · [Русский](README.ru.md) · [Deutsch](README.de.md) · [Español](README.es.md) · [Français](README.fr.md) · [Italiano](README.it.md) · [Português](README.pt.md) · [Polski](README.pl.md) · [Українська](README.uk.md) · [Čeština](README.cs.md) · [Nederlands](README.nl.md) · [Türkçe](README.tr.md) · [日本語](README.ja.md) · [简体中文](README.zh.md) · [繁體中文](README.zh-TW.md) · [한국어](README.ko.md)

</div>

---

## 🚀 설치

```text
1. Language/Korean.json  ->  <GTA V>/menyooStuff/Language/
2. 게임 안에서:  Settings → Language → Korean
3. 게임 안에서:  Settings → Reload Language Files   (또는 게임 재시작)
```

선택 사항: `menyooStuff/menyooConfig.ini` 에 `language = Korean`

## 📦 팩

| 파일 | 키 수 | 커버리지 |
|:--|--:|--:|
| `Korean.json` | 3164 | 100% |

메뉴, 플레이어/차량 토글, 설정, 날씨, 알림까지 UI 전체가 번역되어 있습니다. 모델 이름, FX 이펙트 ID, 애니메이션·컷신 목록은 의도적으로 라틴 문자로 남겨 두었습니다 — 에셋 식별자이지 UI 텍스트가 아닙니다.

## ✅ 검증

```bash
python tools/validate.py Korean
python tools/translate.py --pack Korean --target KO --backend google   # 빈 항목 채우기
```

전체 문서(영어/러시아어): [README.md](README.md) · [README.ru.md](README.ru.md)

## 🏆 크레딧

Menyoo — MAFINS / itsjustcurtis · 번역 및 도구 — MIT ([LICENSE](LICENSE)).

수정 환영: JSON 값만 고쳐서 PR을 보내면 CI가 구조와 마커를 검증합니다.
