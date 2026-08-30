# 🛠 BryOsk Market PoV — Roadmap Journal

**Untuk Bryan:** ini catatan harian perkembangan proyek. Setiap kali saya (Claude) mengerjakan sesuatu — otomatis maupun bareng Bryan — saya catat di sini: **apa yang dikerjakan, error apa yang ditemukan + cara saya perbaiki, dan apa berikutnya**. Kalau ada yang janggal atau tidak dimengerti, cari tanda **❓** dan tanyakan ke saya.

**Cara baca:** entri terbaru di atas. Setiap entri punya:
- ✅ **Dikerjakan** — yang selesai hari itu
- 🐛 **Error & Fix** — masalah yang ketemu + cara diselesaikan (ini yang Bryan minta dicatat)
- ⏸ **Butuh Bryan** — hal yang tidak bisa saya lakukan sendiri (perlu signup / keputusan / KYC)
- ➡️ **Berikutnya** — rencana task hari berikutnya

**Legenda status roadmap** di bagian bawah file.

---

## 2026-08-30 (Minggu) — Automasi harian (jalan otomatis pagi)

### ✅ Dikerjakan
- **Health check nemu gap OTOMASI 13 hari — lebih parah dari insiden 5 hari tanggal 16 Agustus.** Commit konten terakhir sebelum hari ini adalah `9197c17` (16 Agustus); sesudah itu cuma ada **satu** commit auto-archive (`e2d9e29`, 17 Agustus) lalu **kosong total 18–29 Agustus**. Saya cek `mcp__scheduled-tasks__list_scheduled_tasks`: task `bryosk-daily-roadmap` masih **enabled**, jadwal normal (`0 10 * * *`), tapi `lastRunAt` cuma menunjukkan run hari ini — dari dalam sesi saya tetap tidak bisa lihat riwayat run 13 hari kemarin (apakah run tapi gagal, run tapi tidak nemu kerjaan, atau memang tidak jalan). ❓ **Ini kedua kalinya kejadian pola yang sama** (pertama 11–15 Agustus, sekarang 18–29 Agustus) — kalau Bryan bisa cek riwayat run dari sisi platform, ini sekarang layak jadi prioritas, bukan cuma catatan sekali jalan.
- **Karena gap 13 hari (bukan cuma "maju tanggal"), saya web-search ekstensif dulu sebelum sentuh narasi** — BTC/ETH, Fed/FOMC + Jackson Hole, WTI/Hormuz, Gold, S&P/Nasdaq, IHSG/rupiah/BBCA, MSCI, dan China/HK — baru refresh setelah semua angka tersumber silang. Hasilnya market bergerak BESAR, bukan cuma basi tanggal:
  1. **Kripto BALIK ARAH TOTAL dari yang kita tulis 16 Agustus** — waktu itu BTC baru saja jebol turun ke shelf $61–63k (skenario bear/base). Ternyata sejak itu BTC justru **melonjak ke ~$78k** (+~25%), dipicu dorongan Trump untuk RUU Clarity Act di kripto + pengumuman buyback obligasi Treasury yang memicu short squeeze ~$2,7 miliar (19 Agustus) + inflow ETF spot $1,9 miliar+. ETH malah lebih kencang lagi (dari high-$1.800an ke ~$2.460+). Sentimen berbalik dari Fear ke Greed. **Catatan penting:** RUU Clarity Act-nya sendiri BELUM disahkan — voting Senat ditunda ke September — jadi katalisnya masih janji, bukan hukum.
  2. **The Fed balik hawkish** — bertahan di 3,50–3,75% (24 Agustus), lalu pidato Jackson Hole Ketua Fed Warsh (27–28 Agustus) memunculkan lagi kekhawatiran inflasi: US 10Y naik ke ~4,73%, dan kemungkinan **kenaikan suku bunga** di FOMC 15–16 September (bukan cuma "tidak turun") jadi nyata — pembalikan dari narasi "menunggu pemotongan" 2 minggu lalu.
  3. **Minyak (Hormuz) mendatar, bukan mereda ataupun makin parah** — WTI di ~$83, nyaris sama dengan ~$82 dua minggu lalu. Standoff blokade AS-Iran masih jalan tanpa kesepakatan (Iran tetap minta blokade dicabut dulu).
  4. **Emas tembus tinggi baru** (~$4.400 → ~$4.600) dari permintaan haven + pembelian bank sentral yang berlanjut.
  5. **Saham AS: rekor lalu koreksi kecil** — S&P 500 sempat rekor intraday 7.814 (12 Agustus), lalu 2 minggu bergejolak (efek minyak Hormuz + jebolnya kripto), baru pekan 24–28 Agustus positif lagi — tapi Jumat 28 Agustus turun lagi karena pidato hawkish Warsh menghantam saham semikonduktor (NVDA, Intel).
  6. **China/HK JUSTRU MELEMAH** dari narasi "leadership confirmed" 16 Agustus — Hang Seng turun dari ~26.700 ke ~25.600 akibat kekhawatiran dilusi dari private placement Alibaba HK$80 miliar, ditambah ketegangan baru AS-China (ancaman tarif 7,5%, wacana sanksi ke bank China terkait transaksi minyak Iran). Tencent justru bertahan lebih baik dari indeksnya (+1,7% pada 28 Agustus). Mainland (Shanghai/CSI 300) juga turun 7–9% dalam 2 minggu.
  7. **Indonesia tetap solid di tengah semua ini** — IHSG naik ke ~6.525 (dari ~6.400), BBCA dapat inflow asing berkelanjutan (Rp2,14 triliun sejak 1 Juli) + pengumuman dividen interim. Review MSCI Agustus (GOTO dikeluarkan, CPIN diturunkan ke indeks Small Cap) **berlaku efektif besok penutupan (31 Agustus)** — jadi ini sekarang isu yang sangat dekat, bukan lagi jauh di depan.
  - **Cakupan refresh menyeluruh**: `bottomLine`, snapshot 14 baris, semua posisi terdampak (BTC, ETH, XLE, BBCA, CPIN, Tencent/HSCEI), `techCrypto`/`techEquity`/`techMacro`, `derivFlow`/`funding` (ketemu masih pakai narasi bear lama — ikut diperbaiki), `stockMarkets`/`hotToday` untuk 3 pasar, `chinaHK`/`drivers`/`news`/`rotation`/`corp`/`watch`/`assetsWatch`, `tilt`, dan ke-5 skenario (probabilitas & narasi disusun ulang untuk fase BERIKUTNYA — Clarity Act & FOMO September — bukan mengulang skenario yang sudah terjadi), plus `macro.json` + `MACRO_FALLBACK` (auto-sebar via `syncMacroProse()`).
  - **Untuk mover per-saham individual** (hotToday/stockMarkets movers seperti BBRI/ASII/AAPL/Alibaba dll.) yang datanya tidak saya verifikasi ulang secara spesifik minggu ini, saya GANTI ke bahasa umum/tematik ("see live", "not independently re-verified") daripada biarkan angka % basi 2 minggu — sesuai prinsip lama "jangan biarkan % harian basi tanpa refresh". BBCA, Tencent, Alibaba, NVDA/INTC saya update dengan fakta yang benar-benar tersumber.
  - **Tanggal**: `dateLong`/`feedTime` dimajukan ke Minggu, 30 Agustus 2026, dengan framing Jumat 28 Agustus sebagai hari perdagangan terakhir (bursa tutup akhir pekan) — konsisten pola sesi Minggu sebelumnya.
- **Verifikasi menyeluruh**: server lokal `python -m http.server 8137` + Claude Browser — 0 error console di ke-6 tab (Overview/Positions/Crypto/Stocks/Macro/Outlook), 7 tab total (Journal tetap disembunyikan), 14 baris snapshot, 14 poscard, 15 kartu skenario (5×3), 9 kartu macro dari fetch live `macro.json`, 16 sumber. **Live feed CoinGecko ternyata BISA diakses dari lingkungan ini kali ini** (BTC live $78.795, XRP live $1,40) — sangat dekat dengan angka yang saya tulis dari web search ($78.100 / $1,45), jadi saling menguatkan akurasi.

### 🐛 Error & Fix
1. **Gap otomasi 13 hari (18–29 Agustus), kedua kalinya pola ini terjadi** — lihat detail ❓ di atas. Belum ada akar masalah yang bisa saya diagnosis dari dalam sesi; perlu bantuan Bryan cek dari sisi platform.
2. **`derivFlow` dan `funding` (panel Crypto Technicals) masih pakai narasi bear 16 Agustus** ("pivot break lower", "SOL squeeze faded") padahal kripto sudah balik arah total — ketemu saat menyisir seluruh file untuk sisa narasi basi, langsung diperbaiki agar konsisten dengan snapshot/bottomLine yang sudah di-update.

### ⏸ Butuh Bryan
- **❓ PENTING — cek riwayat run scheduled task `bryosk-daily-roadmap` 18–29 Agustus** dari sisi platform/dashboard. Ini kedua kalinya gap panjang terjadi (5 hari lalu, sekarang 13 hari) — kalau pola ini terus berulang, mungkin perlu penyesuaian jadwal atau notifikasi kegagalan yang bisa saya lihat dari sesi berikutnya.
- **❓ Tesis XLE (Energy ETF)** — masih dua sisi seperti dicatat 16 Agustus: minyak mendatar ~$83, standoff Hormuz belum selesai. Belum ada keputusan baru diperlukan, tapi masih menunggu review Bryan kalau mau ambil sikap lebih jelas.
- Item lama masih menunggu: aktifkan link Crypto Monitor (kapan Bryan bilang go), Plan A Tier 2 (API key FRED/TE), Premium platform/Trakteer (KYC + rekening).

### ➡️ Berikutnya
- Karena skala refresh hari ini besar (gap 13 hari + pembalikan arah besar di kripto/Fed/China), saya sengaja TIDAK menambah task kode kedua hari ini (prinsip "kualitas di atas kuantitas", sama seperti sesi 16 Agustus).
- Pantau ketat apakah gap otomasi 13 hari ini berulang lagi — kalau iya untuk ketiga kalinya, ini perlu jadi prioritas diagnosis serius, bukan cuma dicatat.
- Lanjut roadmap besok kalau tidak ada gap lagi: Simulator Phase 2 (worst/base/bull), Track Record enhancements, dark-mode (sudah di-scope, butuh sesi khusus), atau content-consistency sweep lanjutan.

---

## 2026-08-16 (Minggu) — Automasi harian (jalan otomatis pagi)

### ✅ Dikerjakan
- **Health check nemu gap 6 hari:** commit terakhir yang mengubah konten (`d7084d2`, 10 Agustus) diikuti cuma oleh auto-archive (`f3a1552`, 11 Agustus) — automasi harian ini sendiri **tidak jalan/tidak nge-commit apa pun dari 11–15 Agustus**. Saya cek `mcp__scheduled-tasks__list_scheduled_tasks`: task `bryosk-daily-roadmap` masih **enabled** dan jadwalnya normal, `lastRunAt` cuma menunjukkan run hari ini — tidak ada log kegagalan yang bisa saya lihat dari sini untuk tahu PERSIS kenapa 5 hari kemarin kosong (kemungkinan: sesi run tapi tidak menemukan apa pun untuk dikerjakan, atau ada masalah infra di luar kendali saya). **Auto-archive tetap sehat** (`archive/metadata.json` konsisten sampai 10 Agustus, tidak ada lompatan tanggal). ❓ **Perlu Bryan cek:** kalau Bryan bisa lihat riwayat run scheduled task dari sisi platform, tolong konfirmasi apakah task ini benar-benar jalan tiap hari minggu ini — saya tidak punya visibilitas ke situ dari dalam sesi.
- **Karena gap 6 hari itu, saya cross-check dulu via web search sebelum menyentuh narasi (bukan asal majukan tanggal)** — dan ternyata pasar bergerak signifikan, dengan 2 dari 3 skenario yang SUDAH kita tulis sendiri di tab Outlook ternyata yang kejadian, bukan skenario bull:
  1. **BTC beneran kehilangan pivot $65k** — bukan naik ke $68–72k seperti skenario bull, tapi turun ke shelf $61–63k (persis skenario base/bear yang sudah kita tulis) akibat 2 hari beruntun outflow ETF spot + progres regulasi tokenisasi kripto yang mandek di Washington (sumber: CoinDesk, Fortune) — BUKAN karena Fed hawkish.
  2. **Cerita minyak/Hormuz BALIK ARAH TOTAL** — minggu lalu kita tulis "kesepakatan Iran-Oman meredakan risiko pasokan, WTI turun ke ~$77". Ternyata kesepakatan itu **bubar**, AS sekarang mengancam blokade laut Iran **tanpa batas waktu** (ada halaman Wikipedia sendiri: "2026 Strait of Hormuz crisis" / "2026 United States naval blockade of Iran"), dan WTI justru **naik lagi ke ~$82** (Brent ~$88.50) — kebalikan 180° dari yang kita tulis sebelumnya. Ini kelas bug yang sama pentingnya dengan insiden WTI bulan lalu, cuma kali ini arahnya terbalik.
  3. **US 10Y naik lagi** ke ~4.68% (sempat 19-bulan tertinggi ~4.75% di tengah minggu), bukan makin turun seperti narasi lama.
  4. **Indonesia**: IHSG masih di kisaran ~6.400 (relatif stabil), TAPI review MSCI bulan Agustus mengeluarkan 11 saham IDX dari indeks utama (efektif setelah 31 Agustus) — headwind baru yang belum ada di narasi "recovery matured" kita. Saya TIDAK downgrade rating BBCA/tesis Indonesia — cuma tambahkan sebagai watch-item baru yang sudah tervalidasi, sesuai prinsip "jangan ubah opini sendiri, cukup perbaiki fakta + tandai."
  - Refresh MENYELURUH hari ini (bukan cuma 1-2 angka): `bottomLine`, snapshot BTC/ETH/Gold/10Y/WTI/IHSG, posisi BTC/ETH/XLE/BBCA, `techCrypto`/`techEquity`/`techMacro`, `drivers`/`news`/`rotation`/`corp`/`watch`/`assetsWatch`, `tilt`, dan ke-5 skenario (`overview/crypto/stocks/macro/outlook` — probabilitas base/bear digeser naik sedikit mengikuti apa yang benar-benar terjadi, BUKAN ditambah spekulasi baru), plus `macro.json` (single source untuk Gold/WTI/US10Y/DXY — otomatis menyebar ke semua tempat via `syncMacroProse()`).
  - **Tesis XLE (Energy ETF, posisi BUY) saya tandai ❓ untuk Bryan** — sebelumnya risk case-nya adalah "harga minyak makin turun", sekarang minyak justru MELONJAK karena krisis geopolitik yang sama. Ini bikin thesis XLE jadi dua-sisi (bisa untung dari harga minyak naik, tapi juga risiko demand-destruction/risk-off kalau krisis makin parah) — saya cuma perbaiki fakta, TIDAK saya upgrade/downgrade rating-nya sendiri.
  - **Tanggal**: `dateLong`/`feedTime` dimajukan ke Minggu, 16 Agustus 2026, dengan framing jujur "Jumat 14 Agustus" sebagai hari perdagangan terakhir (bursa tutup akhir pekan) — sama seperti pola sesi-sesi Minggu sebelumnya.

### 🐛 Error & Fix
1. **Narasi minyak/Hormuz jadi kontradiksi besar dengan realita** (lihat detail #2 di atas) — arah ceritanya terbalik total, bukan cuma angka basi. Diperbaiki di 6+ lokasi (snapshot, posisi XLE, techMacro, drivers, news, assetsWatch, macro.json, MACRO_FALLBACK) sekaligus, semua bersumber dari web search (Yahoo Finance, CNN, TradingEconomics-adjacent).
2. **BTC/ETH fallback + narasi pivot basi 6 hari** — situs masih bilang "range-bound di $65k menunggu weekly close" padahal BTC sudah tembus turun ke shelf $61-63k. Diperbaiki di semua tempat (bottomLine, snapshot, posisi, techCrypto, drivers, news, tilt, scenarios, assetsWatch).
3. **Gap automasi 5 hari (11-15 Agustus) belum diketahui akar masalahnya** — lihat catatan ❓ di atas, perlu bantuan Bryan untuk cek dari sisi platform.

### ⏸ Butuh Bryan
- **❓ Tolong cek riwayat run scheduled task `bryosk-daily-roadmap` 11-15 Agustus** (dari sisi platform/dashboard Anda) — saya tidak bisa lihat kenapa 5 hari itu tidak ada commit. Kalau ini keseringan terjadi, mungkin perlu penyesuaian jadwal/monitoring.
- **❓ Tesis XLE (Energy ETF)** — minyak sekarang naik karena krisis Hormuz yang lebih serius (ancaman blokade tanpa batas waktu AS-Iran), bukan lagi turun karena "deal damai". Perlu Bryan putuskan: tetap BUY dengan alasan baru (leverage ke harga minyak naik), atau re-evaluasi risk/conviction-nya. Saya tidak mengubah rating sendiri.
- **❓ Ambang skenario Macro (Outlook tab)** dari 10 Agustus masih menunggu review Bryan (10Y sekarang malah lebih tinggi lagi dari catatan sebelumnya, ~4.68% vs ambang lama 4.35-4.55%) — makin relevan untuk direfresh sekarang.
- Item lama masih menunggu: aktifkan link Crypto Monitor (kapan Bryan bilang go), Plan A Tier 2 (API key FRED/TE), Premium platform/Trakteer (KYC + rekening).

### ➡️ Berikutnya
- Kalau Bryan setuju, putuskan sikap XLE + refresh ambang skenario Macro sekalian.
- Karena hari ini fokus penuh ke refresh data-akurasi (skala besar, 6 hari gap), saya sengaja TIDAK menambah task kode kedua hari ini (prinsip "kualitas di atas kuantitas"). Lanjut roadmap besok: Simulator Phase 2 (worst/base/bull), Track Record enhancements, dark-mode (sudah di-scope, butuh sesi khusus).
- Pantau apakah gap automasi 11-15 Agustus terulang — kalau ya, ini jadi prioritas untuk didiagnosis lebih lanjut.

---

## 2026-08-10 (Senin) — Automasi harian (jalan otomatis pagi)

### ✅ Dikerjakan
- **Health check nemu bug pipeline yang cukup serius (bukan cuma stale tanggal):** `archive/metadata.json` mandek di tanggal 7 Agustus padahal commit harian tetap jalan sampai 9 Agustus — artinya sistem auto-archive (GitHub Action) **diam-diam berhenti 2 hari**. **Akar masalahnya:** GitHub Action auto-archive jalan di jam tetap (00:10 UTC = 07:10 WIB) dan skrip-nya (`scripts/daily-archive.py`) punya aturan "cuma archive kalau tanggal di halaman = tanggal hari ini (UTC)". Ternyata jam saya (automasi harian ini) jalan makin larut tiap hari (01:07 WIB tgl 6 Agu → 09:28 WIB tgl 7 → **23:33 WIB tgl 8** → **20:34 WIB tgl 9**) — begitu saya update tanggal SETELAH jam 07:10 WIB, jam archive keburu jalan duluan lihat tanggal "kemarin", skip, dan pola ini **terus berulang selamanya** karena kedua jadwal (automasi saya vs archive cron) tidak akan pernah balik sinkron sendiri.
- **Fix struktural (bukan tambal sementara):** saya ubah logika `scripts/daily-archive.py` — sekarang archive disimpan berdasarkan **tanggal yang tertulis DI konten halaman itu sendiri** (bukan dibandingkan ke jam UTC saat cron jalan), dan cek "sudah pernah diarsipkan belum" juga berdasarkan tanggal itu, bukan "hari ini". Ini tetap mencegah bug asli yang pernah kejadian 31 Mei (konten basi tersimpan dengan nama file yang salah/lebih baru), tapi TIDAK lagi butuh 2 jadwal berbeda selalu pas bareng. Saya tes langsung: jalankan skrip yang sudah diperbaiki terhadap `index.html` hari ini (9 Agustus saat itu) — berhasil archive dengan benar.
- **Backfill 2 hari yang hilang:** ambil isi asli commit tanggal 8 Agustus dari git history, arsipkan sebagai `archive/2026-08-08.html` + entry metadata (risk 49/100), dan arsipkan juga 9 Agustus dari isi terbaru. Sekarang metadata lengkap lagi berurutan (10, 9, 8, 7, 6, 19 Jul, ...) tanpa lompatan.
- **Task ke-2: perbaikan data akurasi macro (bukan cuma refresh tanggal).** Saya cek lewat web search 4 angka macro yang sudah di-auto-sync (`Gold`, `DXY`, `US 10Y`, `WTI`) — 3 dari 4 ternyata SALAH/basi cukup jauh dari harga riil:
  - **Gold**: tertulis ~$4,560, harga riil ~$4,345 (Jumat naik 2%+ ke level tertinggi sejak pertengahan Juni, +~7% seminggu, dipicu data lapangan kerja lemah yang mendorong ekspektasi pemotongan suku bunga Fed) — beda ~5%.
  - **DXY (Dollar Index)**: tertulis ~98.4 dengan narasi "softer, sub-98 break", padahal riil ~99.6–99.7 — **arahnya kebalik**, dolar masih di atas 98 bukan menembus ke bawah.
  - **US 10Y Treasury**: tertulis ~4.35%, riil ~4.60% (turun 7bp hari Jumat tapi levelnya tetap lebih tinggi dari yang tertulis) — beda 25bp.
  - **WTI**: tertulis ~$77, riil ~$78 — beda tipis, masih dalam toleransi, tapi saya samakan juga sekalian karena sedang membenahi file yang sama.
  - Semua 4 angka + catatan kualitatifnya saya update di `macro.json` (satu sumber kebenaran) — otomatis menyebar ke semua tempat yang pakai `data-mref` (baris snapshot, panel Macro Technicals, tesis saham XLE) lewat mekanisme `syncMacroProse()` yang sudah dibangun sebelumnya. Saya juga update fallback JS (`MACRO_FALLBACK`) dan 1 sisa mention manual (`10Y ~4.35%` di kartu Corporate/Jackson Hole) yang tidak ke-cover oleh mekanisme auto-sync.
  - **Kenapa ini penting:** persis prinsip #1 Bryan (data akurat = trust) — pembaca yang cek Gold/DXY/10Y hari ini akan lihat angka yang jauh dari kenyataan kalau tidak diperbaiki.
- **Update tanggal**: `dateLong`/`feedTime` dimajukan ke Senin, 10 Agustus 2026. BTC snapshot fallback (~$64,900) sudah cocok dengan harga riil ($64,895.75) — tidak perlu diubah.
- **Verifikasi**: server lokal + Claude Browser — 0 error console (selain 429 CoinGecko yang memang cuma muncul di server lokal karena rate limit, bukan bug), dateline tampil "Monday, 10 August 2026", 7 tab, 16 kartu posisi, dan semua 4 `data-mref` (gold/us10y/wti/dxy) terbukti terisi angka baru yang benar langsung dari `macro.json` (bukan angka lama).

### 🐛 Error & Fix
1. **Auto-archive GitHub Action diam-diam berhenti 2 hari (8 & 9 Agustus)** — lihat detail akar masalah di atas. Diperbaiki secara struktural + 2 hari yang hilang di-backfill dari git history.
2. **3 angka macro (Gold, DXY, US 10Y) basi/salah cukup jauh dari harga riil** — ditemukan lewat web search, diperbaiki di `macro.json` + fallback + 1 mention manual yang tidak ke-cover auto-sync.

### ⏸ Butuh Bryan
- **❓ Perlu direview:** ambang skenario Macro di tab Outlook (`scenarios.macro`) masih menulis "bull = 10Y di bawah 4.35%" dan "base = 10Y 4.35–4.55%" — sekarang 10Y riil sudah di ~4.60%, di ATAS kedua ambang itu, padahal alasannya dovish (bukan "sticky inflation" seperti skenario bear). Saya **tidak mengubah probabilitas/ambang skenario ini sendiri** karena itu keputusan discretionary Bryan (sama seperti kasus XLE bulan lalu) — hanya menandai di sini biar Bryan bisa lihat & putuskan apakah ambangnya perlu di-refresh.
- Item lama masih menunggu: aktifkan link Crypto Monitor (kapan Bryan bilang go), Plan A Tier 2 (API key FRED/TE), Premium platform/Trakteer (KYC + rekening).
- **Catatan jadwal:** jam automasi harian ini sendiri makin larut & tidak konsisten (pernah jam 1 pagi, pernah jam 11 malam) — di luar kendali saya dari sisi kode, tapi kalau Bryan punya kontrol atas jadwal cron automasi-nya, menstabilkan jamnya (misal selalu sebelum jam 7 pagi WIB) akan bikin situs ter-refresh lebih pagi & konsisten setiap hari.

### ➡️ Berikutnya
- Kalau Bryan setuju, refresh ambang skenario Macro (Outlook tab) supaya konsisten dengan level 10Y riil saat ini.
- Lanjut roadmap: Simulator Phase 2 (worst/base/bull), Track Record enhancements, dark-mode (sudah di-scope minggu lalu, butuh sesi khusus).

---

## 2026-08-09 (Minggu) — Automasi harian (jalan otomatis pagi)

### ✅ Dikerjakan
- **Health check**: pull dari GitHub bersih (auto-archive kemarin sehat, commit `87139eb` sudah live). Situs (`dateLong`) masih tanggal 8 Agustus (Sabtu), selisih 1 hari — wajar untuk Minggu pagi (bursa saham tutup akhir pekan).
- **Cek fakta pakai web search dulu sebelum ubah apa pun** (sesuai prinsip data akurat = trust): karena akhir pekan, saya cek apakah narasi yang sudah ada (BTC ~$65k range-bound, WTI ~$77 pasca kesepakatan Hormuz, S&P 500 rekor $7,757.64 +3.6% minggu ini) masih cocok dengan data riil. Hasil: **semua cocok** — BTC $64,895 (persis di kisaran $65k yang sudah ditulis), WTI $78.18 di hari perdagangan terakhir (dalam toleransi "~$77" yang sudah ada), S&P 500 dan Nasdaq tidak ada data baru (bursa AS/Indonesia libur akhir pekan, closing Jumat tetap berlaku). **Karena tidak ada kontradiksi, saya TIDAK mengubah opini/skenario** — cuma majukan tanggal ke Minggu, 9 Agustus 2026, dan refresh angka BTC snapshot fallback (~$64,700 → ~$64,900, sesuai harga live yang dikonfirmasi).
- **Task ke-2 (fitur baru, bukan cuma refresh): sparkline mini-chart di kartu Posisi (poscard) untuk BTC & ETH.** Ini bagian dari item roadmap "position-card sparklines" yang sudah lama di backlog. Sebelumnya sparkline 7-hari cuma ada di baris Snapshot (Cross-Asset), sekarang ditambahkan juga di kartu Posisi BTC & ETH di tab Positions — **memakai data live CoinGecko yang SAMA yang sudah di-fetch** untuk Snapshot (`liveMarkets()`), jadi tidak ada panggilan API baru/tambahan. **Kenapa cuma BTC & ETH dulu, tidak semua posisi:** untuk saham (NVDA, BBCA, dst.) belum ada sumber data harga historis gratis & bebas-CORS dari lingkungan ini (masalah yang sama persis yang ditemukan di riset Simulator — lihat `simulator-roadmap`) — jadi saya TIDAK memaksakan/mengarang data harga saham. Jujur diselesaikan sebagian (crypto dulu), sisanya (saham) menunggu proxy/backend data seperti direncanakan di Simulator Phase 1.
- **Verifikasi**: server lokal + Claude Browser — 0 error console, tanggal tampil "Sunday, 9 August 2026", 7 tab & panel utuh, 14 kartu posisi render, 9 kartu macro board render dari `macro.json`, live BTC snapshot menunjukkan $64,997 (dekat dengan fallback $64,900 yang saya set — konsisten), DAN kedua sparkline poscard (BTC & ETH) berhasil terisi SVG dari data live 7-hari yang sama.

### 🐛 Error & Fix
- Tidak ada error teknis baru. 0 error console.

### ⏸ Butuh Bryan
- Item lama masih menunggu: aktifkan link Crypto Monitor (kapan Bryan bilang go), Plan A Tier 2 (API key FRED/TE), Premium platform/Trakteer (KYC + rekening).
- Sparkline untuk posisi SAHAM (non-crypto) butuh sumber data historis — perlu proxy/backend (sama seperti kebutuhan Simulator Phase 1), bukan sesuatu yang bisa saya selesaikan sendiri dari sini.

### ➡️ Berikutnya
- Kalau ada waktu: lanjutkan sparkline ke instrumen lain begitu ada sumber data (nyambung ke Simulator Phase 1 — live data layer/proxy).
- Lanjut roadmap: Simulator Phase 2 (worst/base/bull), Track Record enhancements, dark-mode (sudah di-scope, butuh sesi khusus — lihat catatan 8 Agustus).

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
| **Main site — daily read** | 🟢 Live | 7 tab (Journal disembunyikan sementara atas permintaan Bryan). Refresh harian via automation. Kartu Posisi BTC/ETH sekarang punya mini-sparkline 7D live (2026-08-09); saham menunggu sumber data. |
| **Macro Dashboard (Plan A Tier 1)** | 🟢 Live | `macro.json` single-source + panel di tab Macro. Angka Gold/WTI/10Y/DXY di teks narasi lain (snapshot, techMacro, tesis XLE) sekarang ikut auto-sync dari `macro.json` (2026-08-08) — kelas bug kontradiksi harga (WTI $88/$90/$93/$77) tidak bisa terulang lagi untuk 4 angka ini. |
| Plan A Tier 2 (auto-feed FRED/TE) | 🔵 Nunggu Bryan | Perlu API key (gratis). |
| **Track Record dashboard** | 🟢 Live | `track-record.html` — timeline risk-score + call log. |
| **Investment Simulator** | 🟢 Live (Phase 0) | `simulator.html`. Next: Phase 2 worst/base/bull. Refresh 5Y otomatis bulanan. |
| **Crypto Monitor** | 🟡 Siap, nunggu publish | `crypto-monitor.html` sudah jadi & terverifikasi, tapi belum pernah di-push (Bryan pegang kendali). Link nav disembunyikan sementara biar tidak 404 di situs live — aktifkan begitu Bryan bilang go. |
| Premium platform (paywall) | 🔵 Nunggu Bryan | Trakteer dulu → Vercel+Midtrans nanti. KYC. |
| **Auto daily progress + journal** | 🟡 Aktif tapi ada gap berulang | Scheduled task harian + file ini. GitHub Action auto-archive sehat. Task `bryosk-daily-roadmap` sendiri sudah 2× tidak jalan/tidak commit berhari-hari (11-15 Agustus, lalu 18-29 Agustus 2026) — penyebabnya belum diketahui dari sisi kode, perlu Bryan cek riwayat run dari sisi platform, lihat catatan ❓ 30 Agustus. |

**Legenda:** 🟢 live/jalan · 🟡 sedang dikerjakan · 🔵 nunggu aksi Bryan · ⚪ ide/belum mulai
