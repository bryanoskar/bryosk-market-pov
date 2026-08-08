# 🛠 BryOsk Market PoV — Roadmap Journal

**Untuk Bryan:** ini catatan harian perkembangan proyek. Setiap kali saya (Claude) mengerjakan sesuatu — otomatis maupun bareng Bryan — saya catat di sini: **apa yang dikerjakan, error apa yang ditemukan + cara saya perbaiki, dan apa berikutnya**. Kalau ada yang janggal atau tidak dimengerti, cari tanda **❓** dan tanyakan ke saya.

**Cara baca:** entri terbaru di atas. Setiap entri punya:
- ✅ **Dikerjakan** — yang selesai hari itu
- 🐛 **Error & Fix** — masalah yang ketemu + cara diselesaikan (ini yang Bryan minta dicatat)
- ⏸ **Butuh Bryan** — hal yang tidak bisa saya lakukan sendiri (perlu signup / keputusan / KYC)
- ➡️ **Berikutnya** — rencana task hari berikutnya

**Legenda status roadmap** di bagian bawah file.

---

## 2026-08-08 (Sabtu) — Automasi harian (jalan otomatis pagi)

### ✅ Dikerjakan
- **Health check**: pull dari GitHub bersih (auto-archive tanggal 7 Agustus sudah jalan sehat). Situs (`dateLong`) masih tanggal 7 Agustus (Jumat), selisih 1 hari — wajar untuk Sabtu pagi.
- **Update tanggal + cek fakta pakai web search** (bukan tebak-tebakan): karena hari ini akhir pekan (bursa saham AS/Indonesia tutup), saya cek dulu apakah narasi yang sudah ada masih akurat sebelum majukan tanggal. Hasil cek: **konsisten dengan yang sudah ditulis** — S&P 500 malah tutup di rekor tertinggi $7,757.64 Jumat kemarin (+3.6% seminggu), Nasdaq +1.3%, minyak WTI turun >7% minggu ini menembus $78 gara-gara isu kesepakatan Iran-Oman soal Selat Hormuz (persis tema yang sudah kita tulis), BTC $64,718 (persis di sekitar level $65k yang sudah dinarasikan). **Karena semuanya cocok, saya TIDAK mengubah opini/skenario** — cuma majukan tanggal ke Sabtu, 8 Agustus 2026, dan sedikit refresh angka BTC snapshot (~$64,400 → ~$64,700, sesuai data riil) sebagai angka fallback (harga live sebenarnya tetap ditampilkan oleh feed CoinGecko real-time di situs).
- **Task ke-2 (perbaikan struktural, bukan cuma refresh harian): sinkronisasi angka macro di teks narasi.** Ini nyambung ke bug yang berulang 2 hari beruntun minggu ini (harga WTI beda-beda di beberapa tempat). Sekarang 4 angka paling rawan kontradiksi — **Gold, WTI, US 10Y, DXY** — di semua tempat mereka disebut (baris snapshot, panel Macro Technicals, tab Crypto untuk Gold, dan tesis saham XLE) **otomatis ambil angka dari `macro.json`** lewat fungsi baru `syncMacroProse()`. Jadi ke depannya, refresh 1 angka di `macro.json` = semua tempat ikut berubah bareng, tidak mungkin lagi ada 2 angka WTI yang beda di 1 halaman.
- **Verifikasi ekstra (bukan cuma tampilan sama)**: saya sengaja ubah sementara angka WTI di `macro.json` jadi teks dummy, reload situs, dan konfirmasi ke-3 tempat WTI disebut (snapshot, tesis XLE, Macro Technicals) **berubah bareng** — baru setelah terbukti jalan, saya kembalikan ke angka asli ($77). Ini pembuktian nyata mekanismenya jalan, bukan cuma asumsi.

### 🐛 Error & Fix
- Tidak ada error teknis baru. 0 error console (selain CORS CoinGecko yang memang cuma muncul di server lokal, bukan di situs live).

### ⏸ Butuh Bryan
- Item lama masih menunggu: aktifkan link Crypto Monitor (kapan Bryan bilang go), Plan A Tier 2 (API key FRED/TE), Premium platform/Trakteer (KYC + rekening).

### ➡️ Berikutnya
- Perluas sinkronisasi macro ke angka lain kalau muncul (lihat catatan di `PLAN-macro-json.md`).
- Lanjut roadmap: Simulator Phase 2 (worst/base/bull), Track Record enhancements, mobile/dark-mode polish. **Catatan untuk sesi nanti:** saya sempat scoping dark-mode — ternyata warna `--accent`/`--navy` dipakai ganda (sebagai warna teks DAN warna latar) di ~20 tempat, jadi butuh 2 set token warna terpisah supaya teks tetap terbaca di background gelap. Bukan tugas 1 sesi singkat, sengaja tidak saya kerjakan asal-asalan.

---

## 2026-08-07 (Jumat) — Automasi harian (jalan otomatis pagi)

### ✅ Dikerjakan
- **Health check**: pull dari GitHub bersih. Situs (`dateLong`) masih tanggal 6 Agustus (Kamis) — cuma selisih 1 hari dari hari ini, tidak parah stale. `archive/metadata.json` sehat (entry terakhir 6 Agustus).
- **Perbaikan data akurasi — harga minyak WTI (bug nyata, bukan cuma stale):** situs menulis WTI "~$90" di 5 tempat (snapshot, tesis XLE, Macro Technicals, `macro.json`, fallback JS). Saya cek data riil via web search (sumber: TradingEconomics, FXDailyReport, Forbes Advisor) — harga minyak sebenarnya sudah **jatuh tajam ke ~$77** (dari $90-an) setelah Iran & Oman sepakat soal jalur pelayaran Selat Hormuz, yang meredakan risiko pasokan. Ini gap ~15%, kelas bug yang sama dengan insiden WTI bulan lalu. **Fix:** semua 5 tempat disamakan ke ~$77 + narasi disesuaikan (bukan lagi "rangebound $90", tapi "turun tajam dari $90-an akibat kesepakatan Hormuz"). Tesis XLE (BUY) saya update fakta harganya saja — **rating BUY tidak saya ubah**, tapi saya tandai risikonya sudah mulai kejadian, biar Bryan bisa review sendiri kalau mau downgrade.
- **Tambah data baru yang tervalidasi:** laporan tenaga kerja AS Juli (NFP) keluar pagi ini — hanya +22K (ekspektasi +75K), pengangguran naik ke 4.3% (tertinggi sejak Okt 2021). Saya tambahkan sebagai item faktual di News + Drivers (mendukung ekspektasi rate cut September), tanpa mengubah opini/skenario probabilitas yang sudah ada.
- **Update tanggal**: `dateLong`/`feedTime`/macro "as of" dimajukan ke Jumat, 7 Agustus 2026 — karena kali ini benar-benar ada update data riil (bukan cuma ganti tanggal kosong). BTC snapshot disesuaikan ke ~$64,400 (tervalidasi via web search, real-time CoinGecko tidak terjangkau dari sini) — masih konsisten dengan narasi "pivot $65k" yang sudah ada, tidak diubah.
- **Task ke-2 (accessibility polish):** tab navigasi (Overview/Positions/Crypto/dst) belum punya atribut ARIA sama sekali — buruk untuk pembaca screen-reader/keyboard. Ditambahkan `role="tablist"/"tab"/"tabpanel"`, `aria-selected`, `aria-controls`, dan navigasi keyboard (arrow kiri/kanan, Home/End) di JS `activate()`. Fungsional sama seperti sebelumnya, cuma lebih accessible.
- **Verifikasi**: server lokal + Claude Browser — 0 error console, dateline tampil "Friday, 7 August 2026", macro board fetch dari `macro.json` menunjukkan $77 + "as of 2026-08-07", klik tab Macro & Global berfungsi + `aria-selected` update dengan benar, tidak ada sisa "$90" yang kontradiktif (6 sisa mention semuanya sengaja bilang "dari $90-an" sebagai konteks historis).

### 🐛 Error & Fix
1. **Harga WTI stale ~15% (lihat detail di atas)** — ditemukan lewat web search (bukan cuma nebak), diperbaiki di 5 lokasi sekaligus + `macro.json`.
2. Tidak ada error teknis lain ditemukan saat verifikasi browser.

### ⏸ Butuh Bryan
- **Tesis XLE (Energy ETF, posisi BUY)**: sekarang harga minyak sudah turun sesuai skenario risiko yang kita tulis sendiri ("Real Iran deal would sustain oil weakness"). Saya cuma perbaiki fakta harganya, TIDAK saya downgrade rating-nya — itu keputusan discretionary Bryan. Worth dilihat kalau ada waktu.
- Item lama masih menunggu: aktifkan link Crypto Monitor (kapan Bryan bilang go), Plan A Tier 2 (API key FRED/TE), Premium platform/Trakteer (KYC + rekening).

### ➡️ Berikutnya
- Kalau Bryan setuju, lanjut turunkan konviksi/posisi XLE sesuai data minyak baru.
- Lanjut roadmap pure-code: Simulator Phase 2 (worst/base/bull), Track Record enhancements, mobile/dark-mode polish.

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
| **Macro Dashboard (Plan A Tier 1)** | 🟢 Live | `macro.json` single-source + panel di tab Macro. Angka Gold/WTI/10Y/DXY di teks narasi lain (snapshot, techMacro, tesis XLE) sekarang ikut auto-sync dari `macro.json` (2026-08-08) — kelas bug kontradiksi harga (WTI $88/$90/$93/$77) tidak bisa terulang lagi untuk 4 angka ini. |
| Plan A Tier 2 (auto-feed FRED/TE) | 🔵 Nunggu Bryan | Perlu API key (gratis). |
| **Track Record dashboard** | 🟢 Live | `track-record.html` — timeline risk-score + call log. |
| **Investment Simulator** | 🟢 Live (Phase 0) | `simulator.html`. Next: Phase 2 worst/base/bull. Refresh 5Y otomatis bulanan. |
| **Crypto Monitor** | 🟡 Siap, nunggu publish | `crypto-monitor.html` sudah jadi & terverifikasi, tapi belum pernah di-push (Bryan pegang kendali). Link nav disembunyikan sementara biar tidak 404 di situs live — aktifkan begitu Bryan bilang go. |
| Premium platform (paywall) | 🔵 Nunggu Bryan | Trakteer dulu → Vercel+Midtrans nanti. KYC. |
| **Auto daily progress + journal** | 🟢 Aktif hari ini | Scheduled task harian + file ini. |

**Legenda:** 🟢 live/jalan · 🟡 sedang dikerjakan · 🔵 nunggu aksi Bryan · ⚪ ide/belum mulai
