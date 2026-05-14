# =============================================================
# CHECKPOINT 5 — PAPUA: DANAU SENTANI
# =============================================================
# CARA PAKAI:
# 1. Taruh file ini di folder /game/ proyekmu
# 2. Atau copy-paste isi file ini ke script.rpy bagian paling bawah
#    (sebelum baris "return" terakhir)
# 3. Dari akhir Checkpoint 4, tambahkan: jump cp5_intro
#
# PLACEHOLDER ASET (ganti dengan file asli saat sudah ada):
#   bg_papua_danau.png       → background Danau Sentani (siang)
#   bg_papua_pulau_asei.png  → background Pulau Asei / dermaga kayu
#   bg_papua_lapangan.png    → background lapangan Barapen (malam, ada api)
#   bg_papua_hutan.png       → background hutan Asmat yang gelap
#   bg_papua_ending_good.png → background ending baik (danau cerah)
#   bg_papua_ending_bad.png  → background ending buruk (gelap/sepi)
#   mama_tita.png            → karakter Mama Tita (perempuan tua Asmat)
#   perempuan_tua_asei.png   → karakter Perempuan Tua Asei (di dermaga)
#   tetua_asei.png           → karakter Tetua Asei (pria tua, pemimpin)
#   warga_papua.png          → karakter warga Papua (generik)
#   garuda_papua.png         → Garuda (pakai asset Garuda yang sudah ada)
# =============================================================

# ── DEKLARASI KARAKTER BARU ──────────────────────────────────
# (taruh ini di bagian atas script.rpy bersama define lainnya,
#  atau biarkan di sini — Ren'Py tetap bisa membacanya)

define perempuan_tua = Character("Perempuan Tua", who_color = "#c8a06a")
define tetua_asei = Character("Tetua Asei", who_color = "#d4a050")
define mama_tita = Character("Mama Tita", who_color = "#8fbf8f")
define warga_papua = Character("Warga", who_color = "#aaaaaa")
define garuda = Character("Garuda", who_color = "#e8c97a")


# ── DEKLARASI IMAGE PLACEHOLDER ──────────────────────────────
# Ganti path string-nya saat aset asli sudah siap.
# Kalau belum ada file-nya, Ren'Py akan error saat scene itu
# dijalankan — jadi buat dulu file PNG kosong dengan nama itu,
# atau pakai solid color sementara.

image bg_papua_danau = Solid("#0a1e2c")   # biru gelap = danau malam
image bg_papua_pulau_asei = Solid("#0d2035")   # biru lebih gelap
image bg_papua_lapangan = Solid("#1a0800")   # merah gelap = api barapen
image bg_papua_hutan = Solid("#060e06")   # hijau hitam = hutan Asmat
image bg_papua_ending_good = Solid("#0a2830")  # teal gelap = danau damai
image bg_papua_ending_bad = Solid("#0a0508")  # hampir hitam

# Karakter placeholder: pakai transform warna solid sampai
# sprite asli ada. Hapus baris image di bawah ini dan ganti
# dengan: image mama_tita = "mama_tita.png"  dll.
image perempuan_tua_asei_sprite = Solid("#c8a06a")
image tetua_asei_sprite = Solid("#d4a050")
image mama_tita_sprite = Solid("#8fbf8f")


# ── TRANSFORM POSISI (sesuaikan dengan yang sudah ada) ───────
transform cp5_center:
    xalign 0.5
    yalign 1.0

transform cp5_left:
    xalign 0.2
    yalign 1.0

transform cp5_right:
    xalign 0.8
    yalign 1.0

transform cp5_char_kiri:
    xalign 0.25
    yalign 0.85
    zoom 0.55

transform cp5_char_kanan:
    xalign 0.75
    yalign 0.85
    zoom 0.55


# ── VARIABEL POIN ─────────────────────────────────────────────
# Jika checkpoint lain sudah punya sistem poin sendiri,
# sesuaikan nama variabel dengan yang dipakai tim.
# Kalau belum ada: variabel ini akan dibuat otomatis saat dipakai.

default poin_papua = 0


# =============================================================
# LABEL UTAMA — ENTRY POINT CHECKPOINT 5
# Panggil dengan: jump cp5_intro
# =============================================================

label cp5_intro:

    $ poin_papua = 0

    scene bg_papua_danau
    with fade

    narrator "Dari ketinggian, Danau Sentani terbentang luas di bawah langit Papua yang gelap. Perahu-perahu kecil tersebar di permukaan air yang tenang."

    narrator "Tapi malam ini, ketenangan itu terasa palsu."

    with vpunch

    narrator "Tiba-tiba — suara teriakan. Kayu beradu. Lima suku di tepi danau sedang beradu mulut soal batas wilayah tangkap ikan."

    wira "Loh, itu ada apa? Aku harus sembunyi sekarang."

    narrator "Wira berlindung di balik pohon besar di tepi danau. Setelah beberapa saat, keadaan sedikit mereda — tapi Garuda masih belum muncul."

    wira "Mana sih Garuda, kok nggak muncul-muncul. Masa aku harus ngelewatin misi ini sendirian?"

    # Garuda muncul dengan cahaya keemasan
    with flash

    show wira sinis at chara_wira_sinis
    with dissolve

    garuda "Halo Wira, selamat datang di misi terakhirmu."

    wira "Terakhir?!"

    garuda "Ada pertikaian antara 5 suku yang tinggal di sekitar Danau Sentani — masalah wilayah tangkap ikan. Kamu adalah satu-satunya kunci agar konflik ini bisa selesai."

    wira "Jadi aku harus apa, Gar? Nemuin mereka satu per satu? Aku orang luar, apa mereka mau dengerin pendapatku?"

    garuda "Pilihan ada di tanganmu seorang. Ingat... caramu mendekati mereka akan menentukan nasib danau ini."

    jump cp5_scene_asei


# =============================================================
# SCENE 2 — PULAU ASEI: PEREMPUAN TUA DI DERMAGA
# =============================================================

label cp5_scene_asei:

    scene bg_papua_pulau_asei
    with dissolve

    narrator "Wira mendayung menuju sebuah pulau kecil — Pulau Asei, hanya seukuran lapangan bola, dipenuhi pepohonan rindang."

    narrator "Di dermaga kayu tua, seorang perempuan tua duduk tenang. Tangannya menenun anyaman sambil menatap permukaan danau."

    wira "Selamat siang, Nenek. Maaf mengganggu."

    perempuan_tua "Kamu orang baru. Perahumu tidak seperti perahu kami."

    wira "Aku dari jauh, Nenek. Aku datang dengan hati yang ingin belajar."

    perempuan_tua "Belajar? Belajar apa? Tidak ada yang menarik di sini."

    wira "Aku ingin belajar tentang danau ini. Tentang suku-suku di sini. Aku dengar... ada konflik? Mungkin aku bisa membantu."

    perempuan_tua "Membantu? Banyak orang datang mau membantu. Semua pergi setelah dapat apa yang mereka mau. Kamu juga akan begitu."

    wira "Tidak, Nek. Aku akan menunjukkan bahwa aku benar-benar berbeda dari mereka."

    narrator "Wira melihat sekeliling. Ada tumpukan daun sagu berat di belakang dermaga yang harus dipindahkan sebelum hujan."

    wira "Tidak apa, Nek. Tunjukkan saja di mana letak daun sagunya."

    narrator "Wira mengangkut daun sagu yang berat, bolak-balik hingga selesai. Peluh membasahi wajahnya. Perempuan tua itu mengamati dalam diam."

    perempuan_tua "Kamu orang asing. Mau bantu kami berdamai? Hati-hati... lima suku ini keras kepala."

    perempuan_tua "Ada yang butuh dibujuk, ada yang butuh dibantu, ada yang butuh dihormati, ada yang butuh ditakuti."

    perempuan_tua "Kamu mau pakai cara apa?"

    menu:
        "A — Mendatangi satu per satu dan mendengarkan mereka":
            $ poin_papua += 25
            jump cp5_pilihan1_a

        "B — Sampaikan pesan batas wilayah lewat pesan, tidak perlu repot":
            $ poin_papua += 0
            jump cp5_pilihan1_b

        "C — Kumpulkan paksa, ancam mereka supaya berhenti bertengkar":
            $ poin_papua -= 25
            jump cp5_pilihan1_c


label cp5_pilihan1_a:

    garuda "Langkah yang lambat, tapi seringkali paling pasti, Wira."

    narrator "Wira mendatangi rumah adat satu per satu. Duduk bersama warga. Minum teh bersama mereka. Mengangguk mendengarkan setiap keluhan."

    wira "Saya mengerti, Bapak. Batas jaring itu memang penting untuk keluarga Bapak."

    narrator "Semua suku akhirnya merasa dihargai. Mereka setuju untuk berkumpul dan memulai ritual perdamaian."

    jump cp5_scene_barapen


label cp5_pilihan1_b:

    garuda "Efisien. Tapi ingat, Wira, manusia bukan sekadar angka di atas peta."

    narrator "Wira membagikan kertas pembagian wilayah dari atas perahunya, tanpa banyak bicara."

    wira "Ini batasnya. Jangan dilewati. Besok kumpul di tengah danau untuk tanda tangan kesepakatan adat."

    narrator "Semua suku setuju berkumpul — tapi wajah mereka dingin. Tidak ada senyuman. Tidak ada kehangatan."

    jump cp5_scene_barapen


label cp5_pilihan1_c:

    garuda "Wira! Kesombongan hanya akan membakar jembatan yang belum sempat kamu bangun!"

    wira "Kalian ini bodoh sekali! Tinggal bagi saja daerah-daerah perairan di sini, apa susahnya?! Kumpul sekarang atau kalian semua rugi!"

    warga_papua "Hei orang asing! Berani sekali kau mengatur kami di tanah kami sendiri!"

    narrator "Semua suku marah besar. Mereka mengusir Wira — batu dan kayu dilempar ke arah perahunya."

    wira "Aw! Hei! Tunggu dulu!"

    garuda "Sudah kubilang, Wira! Kita gagal!"

    narrator "Wira terpaksa mundur. Konflik tidak selesai, bahkan memburuk."

    jump cp5_ending_bad


# =============================================================
# SCENE 3 — BARAPEN: RITUAL BAKAR BATU
# =============================================================

label cp5_scene_barapen:

    scene bg_papua_lapangan
    with dissolve

    narrator "Lapangan terbuka di tepi danau. Batu-batu membara kemerahan. Asap mengepul ke langit malam."

    narrator "Kelima perwakilan suku sudah duduk melingkar dalam lingkaran yang dibentuk oleh api dan batu."

    garuda "Sekarang sudah saatnya mereka melakukan ritual perdamaian Barapen — bakar batu. Kamu diminta untuk menjadi pemimpin upacaranya. Ini simbol penyatuan."

    wira "Tapi aku tidak tahu caranya, Gar! Aku hanya diberi tahu sedikit tentang upacara ini!"

    garuda "Tenang saja, ikuti intuisimu. Mereka akan mengarahkanmu lewat isyarat."

    tetua_asei "Nak Wira. Kamu yang menyatukan mereka. Sekarang kamu yang memimpin Barapen."

    tetua_asei "Batu dari utara, selatan, timur, barat, dan tengah sudah siap. Doa sudah siap. Makanan sudah siap."

    tetua_asei "Sekarang... bagaimana cara kamu memimpin? Apakah kamu akan mengikuti adat dengan benar? Atau kamu punya cara sendiri?"

    menu:
        "A — Mulai dari batu Timur, memutar, akhiri batu Tengah sebagai penyatu":
            $ poin_papua += 25
            jump cp5_pilihan2_a

        "B — Tumpuk semua batu di tengah sekaligus, yang penting cepat selesai":
            $ poin_papua += 0
            jump cp5_pilihan2_b

        "C — Ambil tiga batu saja, skip doa, langsung masak":
            $ poin_papua -= 25
            jump cp5_pilihan2_c


label cp5_pilihan2_a:

    wira "(dalam hati) Aku harus berhati-hati. Utamakan persatuan."

    wira "Mari kita mulai dari batu Timur — tempat matahari terbit. Lalu memutar... dan terakhir batu Tengah, yang menyatukan kita semua di danau ini."

    narrator "Wira menyusun batu dengan penuh penghormatan. Asap membubung tinggi membentuk siluet indah di langit malam."

    tetua_asei "Leluhur kita tersenyum hari ini. Kau menghormati arah, kau menghormati kehidupan."

    narrator "Para suku terharu. Mereka makan bersama sambil berbincang tentang masa lalu yang indah sebelum konflik. Suasana hangat dan penuh harapan."

    jump cp5_scene_asmat


label cp5_pilihan2_b:

    wira "(dalam hati) Yang penting batunya panas dan makanannya matang."

    wira "Baiklah, tumpuk semua batunya di tengah sekalian, taruh daun dan dagingnya. Mari kita masak."

    narrator "Ritual berjalan biasa saja. Tidak ada yang salah, tapi tidak ada maknanya."

    warga_papua "Makanannya matang... tapi rasanya ada yang kurang."

    narrator "Perdamaian tertulis tercapai, namun tidak ada suasana kekeluargaan. Dingin — seolah masing-masing tidak mengakui keberadaan suku lain."

    jump cp5_scene_asmat


label cp5_pilihan2_c:

    wira "(dalam hati) Panas sekali di sini, aku ingin cepat selesai."

    wira "Ambil tiga batu saja, itu sudah cukup panas! Tidak usah repot-repot berdoa panjang lebar, kita semua lapar. Masukkan umbinya sekarang!"

    narrator "Batu susunan Wira runtuh. Makanan tidak matang sempurna. Warga berdiri dengan marah."

    tetua_asei "Ini penghinaan! Batu dari selatan kau buang, doa kau lupakan! Kau tidak menghargai roh nenek moyang kami!"

    narrator "Beberapa ketua marah dan meninggalkan lapangan. Barapen dianggap tidak sah. Perdamaian hancur berantakan."

    garuda "Sudah kubilang, Wira!"

    jump cp5_ending_bad


# =============================================================
# SCENE 4 — HUTAN ASMAT: UKIRAN & AIR SUCI
# =============================================================

label cp5_scene_asmat:

    scene bg_papua_hutan
    with dissolve

    narrator "Garuda membawa Wira menuju wilayah Asmat — hutan lebat di selatan danau. Pohon-pohon menjulang tinggi, cahaya bulan hampir tidak tembus ke lantai hutan."

    narrator "Di depan sebuah pondok tua, seorang perempuan tua berdiri dengan tongkat kayu berukir. Tatapannya tajam seperti elang."

    mama_tita "Kamu. Orang asing. Dari mana?"

    wira "(menunduk hormat) Dari Danau Sentani, Mama. Aku Wira."

    mama_tita "Sentani? Jauh. Apa yang kamu cari di sini?"

    wira "Air Suci, Mama. Kami butuh air suci untuk menyempurnakan perdamaian di Sentani."

    narrator "Perempuan tua itu tertawa kecil. Tawanya pahit."

    mama_tita "Air Suci. Banyak yang cari. Tiga orang sebelum kamu. Dua gila. Satu mati."

    mama_tita "Kamu yakin mau coba?"

    wira "(menggigil, tapi mengangguk) Aku yakin, Mama."

    mama_tita "Aku Tetua Asmat. Panggil Mama Tita. Kalau kamu mau cari Air Suci... kamu harus pecahkan teka-teki ukiran ini dulu."

    narrator "Mama Tita mengulurkan sebatang kayu ukiran sepanjang lengan. Motifnya berlapis-lapis — binatang di bawah, manusia di tengah, lalu lingkaran kosong di ujung atas."

    mama_tita "Ukiran ini bicara. Tapi dia hanya bicara pada yang mau mendengar. Bukan dengan telinga... tapi dengan hati dan ingatan."

    mama_tita "Bawa ini. Pecahkan maknanya. Kalau sudah tahu... kembali padaku."

    menu:
        "A — Duduk tenang berjam-jam, renungkan semua pelajaran dari suku-suku sebelumnya":
            $ poin_papua += 25
            jump cp5_pilihan3_a

        "B — Keliling desa, tanya orang-orang yang lewat sambil bawa ukiran":
            $ poin_papua += 0
            jump cp5_pilihan3_b

        "C — Lempar ukiran, paksa Mama Tita tunjukkan airnya sekarang":
            $ poin_papua -= 25
            jump cp5_pilihan3_c


label cp5_pilihan3_a:

    wira "Aku butuh waktu untuk memahami ini, Gar."

    narrator "Wira duduk bersila di bawah pohon besar. Menutup mata. Mengusap permukaan ukiran itu perlahan."

    wira "(dalam hati) Binatang... manusia... bersatu. Tapi kenapa di ujungnya kosong? Kosong... tempat yang tidak ada di peta para suku Sentani tadi."

    narrator "Wira mengingat semua yang dia pelajari — batas wilayah, rawa-rawa, cerita para tetua. Lalu dia sadar."

    wira "Lingkaran kosong itu... rawa tanpa nama di belakang desa lama. Wilayah netral yang tak bertuan!"

    narrator "Wira berlari ke sana. Menyelam ke dasar rawa yang dingin. Di balik bebatuan tersembunyi sebuah gua kristal kecil."

    narrator "Wira keluar dari gua membawa botol bambu. Air di dalamnya memancarkan cahaya biru yang lembut dan jernih."

    garuda "Luar biasa, Wira! Auranya sangat murni!"

    narrator "Dengan air ini, perdamaian di Sentani akan abadi — mengikat jiwa semua suku dalam harmoni."

    jump cp5_ending_good


label cp5_pilihan3_b:

    wira "(menggaruk kepala) Aduh, aku paling tidak bisa teka-teki sastra begini."

    narrator "Wira keliling desa menanyai orang-orang yang lewat sambil membawa ukiran itu. Tidak sabar duduk lama."

    narrator "Akhirnya, saat lelah dan bersandar di dinding batu, Wira terpeleset — dan menemukan gua di balik air terjun kecil di pinggir desa."

    narrator "Wira keluar membawa air yang warnanya abu-abu keruh. Tidak ada cahaya."

    garuda "Wira... air apa ini? Mengapa rasanya hampa?"

    narrator "Air sucinya keruh. Terkutuk oleh kelalaian. Jika digunakan, perdamaian di Sentani hanya akan bertahan seumur jagung sebelum perang pecah kembali."

    jump cp5_ending_mid


label cp5_pilihan3_c:

    narrator "Wira melempar ukiran itu ke tanah dengan kesal."

    wira "Ini tidak masuk akal! Ukiran kayu kok disuruh bicara?! Katakan padaku di mana air sucinya, Nenek tua! Jangan buang waktuku atau aku akan menghancurkan ukiran kesayanganmu ini!"

    mama_tita "(menatap tajam, lalu menghela napas panjang) Orang sombong selalu menemukan jalannya sendiri menuju kehancuran."

    narrator "Mama Tita membawa Wira ke sebuah gua kecil yang gelap di kaki bukit. Lalu meninggalkan Wira sendirian."

    narrator "Tangan Wira gemetar saat menciduk air. Air itu hitam pekat, kental, dan mengeluarkan asap berbau busuk."

    wira "(terbatuk-batuk) Uhuk! Bau sekali seperti darah dan bangkai ikan!"

    garuda "Wira, buang itu! Itu kutukan rawa mati!"

    narrator "Air suci yang didapat berwarna hitam pekat. Sangat terkutuk. Jika dibawa kembali, ini akan membawa wabah penyakit bagi 5 suku di Danau Sentani."

    jump cp5_ending_bad


# =============================================================
# ENDING BAIK — Skor tinggi (≥ 50)
# =============================================================

label cp5_ending_good:

    scene bg_papua_ending_good
    with dissolve

    narrator "Semua suku berkumpul di tengah Danau Sentani untuk terakhir kalinya malam itu."

    narrator "Air suci dari botol bambu dituangkan perlahan ke permukaan danau. Cahaya biru menyebar seperti bintang yang jatuh."

    narrator "Dalam diam yang khidmat, kelima tetua berdiri, saling bergenggaman tangan untuk pertama kalinya dalam bertahun-tahun."

    garuda "Checkpoint Papua selesai, Wira. Total poinmu: [poin_papua]."

    if poin_papua >= 60:
        garuda "Kamu tidak hanya menyelesaikan konflik. Kamu baru saja belajar bahwa perdamaian yang nyata tidak bisa dibeli, dipaksa, atau disingkat. Ia hanya bisa dihadirkan oleh mereka yang berani duduk bersama dan menaruh hati di tempat yang tepat."
    else:
        garuda "Kamu sudah mencoba, Wira. Ada momen di mana kamu menunjukkan niat yang baik. Bawa itu ke perjalanan berikutnya."

    narrator "..."

    wira "Garuda... gue mulai ngerti kenapa lo bawa gue ke tempat-tempat ini."

    garuda "Belum sepenuhnya. Tapi kamu sudah di jalan yang benar."

    narrator "{i}Kearifan sejati tidak hanya mendamaikan dunia luar... melainkan juga mempertemukan kita kembali dengan bagian diri kita yang paling murni.{/i}"

    jump cp5_closing


# =============================================================
# ENDING SEDANG — Skor tengah (0–49, pilihan 3B)
# =============================================================

label cp5_ending_mid:

    scene bg_papua_ending_good
    with dissolve

    narrator "Danau Sentani kembali tenang. Namun entah untuk berapa lama."

    narrator "Air keruh yang Wira bawa disebarkan ke danau dengan tata cara seadanya. Para tetua suku mengangguk pelan — mereka menerima, meski tanpa antusias."

    garuda "Checkpoint Papua selesai, Wira. Total poinmu: [poin_papua]."

    garuda "Kamu sudah mencoba, Wira. Dan di sebagian besar perjalanan ini, kamu menunjukkan niat yang baik. Tapi ada momen di mana kamu berhenti di tepi, padahal satu langkah lagi bisa membuat segalanya berbeda."

    garuda "Papua tidak menghukummu. Ia hanya bertanya: apakah lain kali kamu akan berani lebih dalam?"

    jump cp5_closing


# =============================================================
# ENDING BURUK — Skor rendah (< 0)
# =============================================================

label cp5_ending_bad:

    scene bg_papua_ending_bad
    with dissolve

    narrator "Danau Sentani kembali sunyi dalam ketegangan."

    narrator "Perahu-perahu suku yang berbeda tidak lagi saling menyapa. Air danau tetap gelap, menyimpan amarah yang belum selesai."

    narrator "Garuda menatap Wira dalam diam yang panjang."

    garuda "Checkpoint Papua selesai, Wira. Total poinmu: [poin_papua]."

    garuda "Wira... kamu melewati tanah leluhur dengan tangan yang kosong. Bukan karena kamu tidak mampu — tapi karena kamu memilih untuk tidak hadir sepenuhnya."

    garuda "Danau Sentani masih menunggu. Pertanyaannya: kapan kamu siap untuk benar-benar mendengar?"

    narrator "{i}Ketika kita memaksa dunia untuk tunduk pada keegoisan kita... kita hanya akan mewariskan kehancuran — baik di tanah orang lain, maupun di rumah kita sendiri.{/i}"

    jump cp5_closing


# =============================================================
# PENUTUP — Kembali ke rumah Nenek
# Sambungkan ke scene closing yang sudah ada di script.rpy
# Ganti jump di bawah dengan label closing yang sesuai
# =============================================================

label cp5_closing:

    scene black
    with dissolve

    narrator "..."

    narrator "Cahaya keemasan menyelimuti Wira. Danau Sentani memudar di kejauhan."

    narrator "Garuda mengepakkan sayap untuk terakhir kalinya."

    garuda "Perjalanan sudah selesai, Wira. Saatnya pulang."

    # ── Sambungkan ke scene closing / epilog yang sudah ada ──
    # Ganti baris di bawah dengan label epilog kalian, misalnya:
    # jump epilog_rumah_nenek
    # atau jika langsung ke ending:
    # jump good_ending / bad_ending

    jump closing   # <-- GANTI dengan label closing yang benar di script.rpy kalian

