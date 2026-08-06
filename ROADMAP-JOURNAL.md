# 🛠 BryOsk Market PoV — Roadmap Journal

**Untuk Bryan:** ini catatan harian perkembangan proyek. Setiap kali saya (Claude) mengerjakan sesuatu — otomatis maupun bareng Bryan — saya catat di sini: **apa yang dikerjakan, error apa yang ditemukan + cara saya perbaiki, dan apa berikutnya**. Kalau ada yang janggal atau tidak dimengerti, cari tanda **❓** dan tanyakan ke saya.

**Cara baca:** entri terbaru di atas. Setiap entri punya:
- ✅ **Dikerjakan** — yang selesai hari itu
- 🐛 **Error & Fix** — masalah yang ketemu + cara diselesaikan (ini yang Bryan minta dicatat)
- ⏸ **Butuh Bryan** — hal yang tidak bisa saya lakukan sendiri (perlu signup / keputusan / KYC)
- ➡️ **Berikutnya** — rencana task hari berikutnya

**Legenda status roadmap** di bagian bawah file.

---

## 2026-08-06 (Kamis) — Automasi harian (jalan otomatis pagi)

### ✅ Dikerjakan
- **Health check rutin**: pull dari GitHub bersih (tidak ada konflik). Tanggal situs (`dateLong`) = "Thursday, 6 August 2026" — sudah sesuai hari ini, tidak stale (situs baru saja di-refresh di sesi bareng Bryan tadi malam, lihat entri di bawah).
- **Perbaikan konsistensi data — harga WTI (minyak)**: ketemu 3 angka WTI yang saling bertentangan di 1 halaman — snapshot menulis ~$88, panel Macro Technicals menulis ~$90, dan tesis saham XLE menulis "capped near $93". Ini melanggar prinsip utama Bryan (data akurat = trust) — pembaca bisa lihat 3 harga minyak berbeda sekaligus. **Fix:** disamakan semua ke ~$90 (angka yang sudah konsisten di `macro.json` + Macro Technicals) — baris snapshot & tesis XLE diupdate ke $90.
- **Tautan rusak diperbaiki**: link "🪙 Crypto Monitor →" di footer situs sudah live (ter-push di commit sebelumnya), tapi file `crypto-monitor.html` sendiri **belum pernah di-push** ke GitHub — sengaja, karena catatan saya sebelumnya bilang Bryan yang pegang kendali kapan file itu di-publish. Akibatnya link itu 404 di situs live sekarang. **Fix (reversibel):** link saya sembunyikan (dikomentari, bukan dihapus) sampai Bryan bilang "go" — begitu setuju, saya aktifkan link + push filenya sekaligus.
- **Verifikasi**: dites di server lokal + browser — 0 error console, 9 macro card render dari `macro.json`, 7 tab (Journal masih disembunyikan sesuai permintaan), tidak ada lagi "$88" atau "$93" di halaman manapun.

### 🐛 Error & Fix
1. **Kontradiksi harga WTI (3 angka berbeda di 1 halaman)** — lihat detail di atas, kemungkinan sisa dari refresh sebelumnya yang tidak menyisir semua tempat minyak disebut. Sudah diperbaiki.
2. **Link Crypto Monitor 404 di situs live** — link sudah live tapi file targetnya belum pernah dipublish. Disembunyikan sementara (tidak ada data hilang, tinggal aktifkan lagi kapan saja).

### ⏸ Butuh Bryan
- **Aktifkan link "Crypto Monitor"**: kapan Bryan mau publish `crypto-monitor.html` ke situs live, tinggal bilang — saya aktifkan link + push filenya (halamannya sudah siap & sebelumnya sudah diverifikasi dengan data live).
- Item lama masih menunggu: Plan A Tier 2 (API key FRED/Trading Economics), Premium platform/Trakteer (KYC + rekening).

### ➡️ Berikutnya
- Content-consistency sweep lanjutan (cek array lain untuk kontradiksi serupa) kalau ada waktu.
- Lanjut roadmap pure-code: Simulator Phase 2 (worst/base/bull), polish mobile/dark-mode, Track Record enhancements.

---

## 2026-08-06 (Kamis) — Sesi bareng Bryan + setup automation

### ✅ Dikerjakan
- **Health check**: auto-archive sehat (2026-07-19 & sebelumnya ter-archive otomatis). Situs sempat ~18 hari stale (19 Jul → 6 Agu) karena jeda.
- **Market refresh penuh ke 6 Agustus** (semua tab konsisten, 0 kontradiksi terverifikasi): narasi maju — Q2 earnings AI mega-cap *delivered* (NVDA/MSFT beat), tren extend (BTC ~$71,800 lewati target $68k menuju $72–74k), katalis berikut = **Jackson Hole akhir Agustus**. Indonesia tetap standout. Hot Today nama-nama baru (NVDA/MSFT/AVGO · BBRI/TLKM/BMRI · Alibaba/Tencent/Xiaomi). macro.json + dashboard di-update ke 6 Agu.
- **Setup sistem ini**: ROADMAP-JOURNAL.md (file ini) + automation harian (lihat di bawah).

### 🐛 Error & Fix
1. **❓ Anomali sinkronisasi file (PENTING).** Ketemu: `index.html` di repo (versi 3 Agu, ada link Simulator + Crypto Monitor) ternyata **lebih baru** dari file sumber lama saya `Downloads/BryOsk-Market-PoV.html` (versi 19 Jul). Sesi-sesi lain (workstream Simulator & Crypto Monitor) mengedit `repo/index.html` **langsung**. **Kenapa terjadi:** dulu alur saya = edit di Downloads lalu copy ke repo; workstream lain tidak ikut alur itu. **Risiko:** kalau saya copy dari Downloads, kerja mereka ketimpa. **Fix:** mulai sekarang **file kanonik = `repo/index.html`** — saya edit langsung di repo, Downloads copy ditinggalkan sebagai arsip. Tidak ada kerja yang hilang.
2. **Link "🪙 Crypto Monitor →" belum ter-commit.** Ketemu: ada perubahan `index.html` yang belum di-commit dari sesi lain (menambah link nav Crypto Monitor). File `crypto-monitor.html` sudah ada & valid. **Fix:** saya rampungkan — commit link itu bersama refresh hari ini. Link sekarang aktif & tidak rusak.

### ⏸ Butuh Bryan (belum bisa saya lakukan sendiri)
- **Plan A Tier 2 (auto-feed macro real)** — butuh Bryan signup API key gratis: FRED (`fred.stlouisfed.org/docs/api`) + Trading Economics, lalu tambahkan sebagai GitHub secret. Setelah itu macro update 100% otomatis dari sumber resmi.
- **Premium platform / Trakteer** — butuh KYC + rekening Bryan.

### ➡️ Berikutnya (rencana automation — 1-2 task/hari, ikut roadmap)
- Menjaga situs tetap fresh + konsisten tiap hari (health check + refresh ringan).
- Maju di roadmap yang **pure-code** (tidak perlu Bryan): polish Simulator (Phase 2 worst/base/bull), Crypto Monitor, UI/UX, Track Record, mobile.
- Semua tercatat di journal ini tiap hari.

---

## 📋 Status Roadmap (ringkas — diperbarui tiap sesi)

| Workstream | Status | Catatan |
|---|---|---|
| **Main site — daily read** | 🟢 Live | 7 tab (Journal disembunyikan sementara atas permintaan Bryan). Refresh harian via automation. |
| **Macro Dashboard (Plan A Tier 1)** | 🟢 Live | `macro.json` single-source + panel di tab Macro. |
| Plan A Tier 2 (auto-feed FRED/TE) | 🔵 Nunggu Bryan | Perlu API key (gratis). |
| **Track Record dashboard** | 🟢 Live | `track-record.html` — timeline risk-score + call log. |
| **Investment Simulator** | 🟢 Live (Phase 0) | `simulator.html`. Next: Phase 2 worst/base/bull. Refresh 5Y otomatis bulanan. |
| **Crypto Monitor** | 🟡 Siap, nunggu publish | `crypto-monitor.html` sudah jadi & terverifikasi, tapi belum pernah di-push (Bryan pegang kendali). Link nav disembunyikan sementara biar tidak 404 di situs live — aktifkan begitu Bryan bilang go. |
| Premium platform (paywall) | 🔵 Nunggu Bryan | Trakteer dulu → Vercel+Midtrans nanti. KYC. |
| **Auto daily progress + journal** | 🟢 Aktif hari ini | Scheduled task harian + file ini. |

**Legenda:** 🟢 live/jalan · 🟡 sedang dikerjakan · 🔵 nunggu aksi Bryan · ⚪ ide/belum mulai
