# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator =  Character("???", who_color = "#000000")
define wira = Character("Wira", who_color = "#ffffff")
define ibu = Character("Ibu", who_color = "#ffacc2")
define ayah = Character("Ayah", who_color = "#b5e5ff")
define garuda = Character("Garuda", who_color = "#ffd978")
define narasi = Character(None, what_italic = True)
define made = Character("Made", who_color = "#ffffff")
define nyoman = Character("Bu Nyoman", who_color = "#ffffff")
define bima = Character("Bima", who_color = "#ffffff")
define pekaseh = Character("Pekaseh Wayan", who_color = "#ffffff", size=37)

# DAERAH 4 : TORAJA   CHARACTER DEFINITIONS
define aldi = Character("Aldi", who_color = "#ffffff")
define paman_darius = Character("Paman Darius", who_color = "#ffffff", size=37)
define nenek_rante = Character("Nenek Rante", who_color = "#ffffff", size=37)
define rena = Character("Rena", who_color = "#ffffff")

image black = "black-bg.jpg"


# =============================================================
# PROLOG / TERAS PAGI
# =============================================================
image wira_ceria = "wira_ceria.png"
image bg_prolog_teras_pagi = "prolog_teras_pagi.png"
image pipit standing = "pipit_standing.png"
image pipit terbang = "pipit_terbang.png"
image wiranpipit = "wira_dan_pipit.png"
image wiranpipit serius = "wira_dan_pipit_serius.png"
image wiranpipit nunduk = "wira_dan_pipit_nunduk.png"
image wiranpipit terharu = "wira_dan_pipit_terharu.png"

transform pipit_initial:
    xalign 0.4
    yalign 0.495
    zoom 0.13

transform wleft_small:
    xalign 0.23
    yalign 0.65
    zoom 0.6


transform teras:
    xalign 0.5
    yalign 0.72
    zoom 0.6


transform terasnew:
    xalign 0.5
    yalign 0.72
    zoom 0.65


# =============================================================
# PROLOG / TAMAN KOTA SORE
# =============================================================
image taman = im.Scale("prolog_taman_kota_sore.png",1920,1080)
image wira megang sangkar = "wira_megang_sangkar.png"
image wira duduk sangkar = "wira_duduk_sangkar.png"
image wira ketiup angin =  "Wira ketiup angin kenceng.png"
image pipit hinggap di sangkar = "pipit hinggap di sangkar.png"
image pipit terbang = "pipit_terbang.png"
image wira ngejar = "wira_ngejar.png"
image sangkar = "sangkar.png"
image wira sedih = "wira sedih.png"


transform wira_megang_sangkar:
    xalign 0.35
    yalign 0.6
    zoom 0.3

transform wira_duduk_sangkar:
    xalign 0.38
    yalign 0.6
    zoom 0.3

transform wira_ketiup_angin:
    xalign 0.42
    yalign 0.6
    zoom 0.3

transform wira_sedih:
    xalign 0.42
    yalign 0.6
    zoom 0.4

transform pipit_sangkar:
    xalign 0.32
    yalign 0.67
    zoom 0.3

transform pipit_terbang:
    xalign 0.2
    yalign 0.3
    zoom 0.2

transform pipit_leaving:
    xalign 0
    yalign 0
    zoom 0.2

transform sangkar_kosong:
    xalign 0.34
    yalign 0.64
    zoom 0.2

transform atas_sangkar:
    xalign 0.34
    yalign 0.6
    zoom 0.15



# =============================================================
# PROLOG / KAMAR WIRA
# =============================================================
image kamarwira = "prolog_kamar_wira.png"
image wira sinis = "wira dewasa sinis.png"
image wira bingung = "wira dewasa bingung.png"

transform chara_wira_sinis :
    xalign 0.7
    yalign 1.0


# =============================================================
# SCENE 5-8 PLACEHOLDER ASSETS
# Ganti placeholder di bawah ini dengan asset final saat sudah dibuat.
# =============================================================

# TODO IMAGE: Background gudang tua pengap, tumpukan barang tua ditutupi kain putih.
image bg_gudang_nenek = im.Scale("bg_gudang_nenek.png",1920,1080)

# TODO IMAGE: Kotak kuningan tua berkilau misterius, ukiran "Petualangan Nusantara".
image kotak_petualangan_nusantara = "kotak_petualangan_nusantara.png"

# TODO IMAGE: Wira dewasa ekspresi murung, mengusap debu di hidungnya.
image wira murung = "wira_murung.png"

# TODO IMAGE: Wira berlutut di depan kotak, ekspresi penasaran.
image wira berlutut = "wira_berlutut.png"
# TODO IMAGE: Wira panik, tangan menutupi wajah.
image wira panik = "wira_panik.png"

# TODO IMAGE/VFX: Cahaya keemasan warna Pipit meledak dari kotak.
image vfx_cahaya_kotak = "vfx_cahaya_kotak.png"

# TODO IMAGE/VFX: Golden vortex, partikel cahaya berputar kencang.
image vfx_golden_vortex = "vfx_golden_vortex.png"

# TODO IMAGE/VFX:
image vfx_wira_data = "vfx_wira_data.png"

# TODO IMAGE: Pulau terapung di atas awan, langit biru-ungu, siluet 5 checkpoint.
image bg_pulau_terapung = im.Scale("bg_pulau_terapung.png",1920,1080)

# TODO IMAGE: Garuda raksasa megah, bulu putih keemasan, kalung permata tradisional.
image garuda megah = "garuda_default.png"

# TODO IMAGE: UI/HUD poin karakter hijau-merah dan peta Nusantara Checkpoint.


transform center_placeholder:
    xalign 0.5
    yalign 0.5

transform left_placeholder:
    xalign 0.24
    yalign 0.72

transform right_placeholder:
    xalign 0.76
    yalign 0.72

transform lower_center_placeholder:
    xalign 0.5
    yalign 0.82

transform garuda_stage:
    xalign 0.82
    yalign 0.95
    zoom 0.75

transform hud_stage:
    xalign 0.5
    yalign 0.15


# DAERAH 3 : BALI
image bg_bali_pematang_sore = "bali_pematang_subak_sore.png"
image bg_bali_hilir = im.Scale("bali_sawah_hilir_kering.png", 1920, 1080)
image bg_bali_terasering_pagi = "bali_terasering_jatiluwih_pagi.png"
image bg_bali_terasering_sore = "bali_terasering_jatiluwih_sore.png"
image bg_bali_pura = "bali_pura_ulun_carik.png"
image bg_bali_pematang = "bali_pematang_subak.png"

image garuda_default = "garuda_default.png"
image garuda_terbang = "garuda_terbang.png"
image garuda_berbicara = "garuda_berbicara.png"
image wira_dewasa_default = "wira_dewasa_default.png"
image wira_dewasa_bingung = "wira_dewasa_bingung.png"
image wira_dewasa_sinis = "wira_dewasa_sinis.png"
image wira_dewasa_terharu = "wira_dewasa_terharu.png"
image wira_dewasa_terkejut = "wira_dewasa_terkejut.png"
image bali_bima_normal = "bali_bima.png"
image bali_bima_persuasif = "bali_bima_persuasif.png"
image bali_bu_nyoman = "bali_bu_nyoman.png"
image bali_bu_nyoman_tegas = "bali_bu_nyoman_tegas.png"
image bali_bu_nyoman_terluka = "bali_bu_nyoman_kecewa.png"
image bali_bu_nyoman_lega = "bali_bu_nyoman_lega.png"
image bali_pak_made_normal = "bali_pak_made.png"
image bali_pak_made_bekerja = "bali_pak_made_bekerja.png"
image bali_pak_made_defensif = "bali_pak_made_defensif.png"
image bali_pak_made_frustasi = "bali_pak_made_frustasi.png"
image bali_pekaseh_wayan_normal = "bali_pekaseh_wayan.png"
image bali_pekaseh_bijaksana = "bali_pekaseh_bijaksana.png"

image peta_bali = "peta_bali.png"


transform terasering_wira:
    xalign 0.18
    yalign 0.79
    zoom 0.58

transform terasering_garuda:
    xalign 0.8
    yalign 0.98
    zoom 0.53

transform pematang_wira:
    xalign 0.32
    yalign 0.92
    zoom 0.56

transform pematang_garuda:
    xalign 0.07
    yalign 0.95
    zoom 0.5

transform pematang_made:
    xalign 0.75
    yalign 0.70
    zoom 0.45

transform hilir_wira:
    xalign 0.3
    yalign 0.75
    zoom 0.55

transform hilir_nyoman:
    xalign 0.6
    yalign 0.72
    zoom 0.56

transform hilir_bima:
    xalign 0.75
    yalign 0.70
    zoom 0.50

transform pura_wira:
    xalign 0.1
    yalign 0.92
    zoom 0.56

transform pura_garuda:
    xalign 0.9
    yalign 0.94
    zoom 0.5

transform pura_made:
    xalign 0.4
    yalign 0.65
    zoom 0.50

transform pura_nyoman:
    xalign 0.6
    yalign 0.65
    zoom 0.50

transform pura_pekaseh:
    xalign 0.5
    yalign 0.75
    zoom 0.58

default bali_points = 0
default scene1_choice = None
default scene2_choice = None
default scene3_choice = None

# DAERAH 4 : TORAJA

image toraja_aldi_normal = "toraja_aldi.png"
image toraja_nenek_rante = "toraja_nenek_rante.png"
image toraja_paman_darius = "toraja_paman_darius.png"
image toraja_rena = "toraja_rena.png"
image toraja_tautau = "toraja_tautau.png"

# BACKGROUND TORAJA
image bg_toraja_lembah = im.Scale("toraja_lembah_tongkonan.png", 1920, 1080)
image bg_toraja_kamar1 = im.Scale("toraja_kamar1.png", 1920, 1080)
image bg_toraja_kamar2 = im.Scale("toraja_kamar2.png", 1920, 1080)
image bg_toraja_kamar3 = im.Scale("toraja_kamar3.png", 1920, 1080)
image bg_toraja_kamar4 = im.Scale("toraja_Kamar4.png", 1920, 1080)
image bg_toraja_lembah_berkabut = im.Scale("toraja_lembah_berkabut.png", 1920, 1080)
image bg_toraja_lembah_tongkonan = im.Scale("toraja_lembah_tongkonan.png", 1920, 1080)
image bg_toraja_tongkonan_luar = im.Scale("toraja_tongkonan_luar.png", 1920, 1080)
image bg_toraja_lembah_tongkonan_sore = im.Scale("toraja_lembah_tongkonan_sore.png", 1920, 1080)

# GARUDA VARIANTS
image wira_dewasa_merinding = "wira_dewasa_merinding.png"

# CHARACTER EXPRESSIONS TORAJA
image toraja_aldi_heran = "toraja_aldi_heran.png"
image toraja_aldi_mencibir = "toraja_aldi_mencibir.png"
image toraja_paman_darius_uji = "toraja_paman_darius_uji.png"
image toraja_paman_darius_tegas = "toraja_paman_darius_tegas.png"
image toraja_paman_darius_hormat = "toraja_paman_darius_hormat.png"
image toraja_rena_bingung = "toraja_rena_bingung.png"
image toraja_rena_terharu = "toraja_rena_terharu.png"

transform lembah_wira:
    xalign 0.3
    yalign 0.93
    zoom 0.61

transform lembah_garuda:
    xalign 0.75
    yalign 0.9
    zoom 0.6

# Gerbang Tongkonan   Scene 1
transform gerbang_wira:
    xalign 0.25
    yalign 0.94
    zoom 0.55

transform gerbang_aldi:
    xalign 0.85
    yalign 0.95
    zoom 0.56

transform gerbang_paman_darius:
    xalign 0.65
    yalign 0.95
    zoom 0.6

transform gerbang_nenek_rante:
    xalign 1.03
    yalign 0.97
    zoom 0.56

transform gerbang_garuda:
    xalign 0.075
    yalign 0.95
    zoom 0.45

# Ruang Musyawarah   Scene 3
transform musyawarah_wira:
    xalign 0.25
    yalign 0.82
    zoom 0.57

transform musyawarah_aldi:
    xalign 0.56
    yalign 0.82
    zoom 0.54

transform musyawarah_paman_darius:
    xalign 0.74
    yalign 0.82
    zoom 0.54

transform musyawarah_nenek_rante:
    xalign 0.88
    yalign 0.82
    zoom 0.56

transform musyawarah_rena:
    xalign 1.01
    yalign 0.88
    zoom 0.56

transform musyawarah_garuda:
    xalign 0.1
    yalign 0.82
    zoom 0.45

transform kamar_leluhur_wira:
    xalign 0.15
    yalign 0.87
    zoom 0.58

transform kamar_leluhur_paman_darius:
    xalign 0.9
    yalign 0.86
    zoom 0.6

transform kamar_leluhur_garuda:
    xalign 0.03
    yalign 0.86
    zoom 0.45

transform kamar_leluhur_tautau:
    xalign 0.5
    yalign 0.78
    zoom 0.18

default toraja_points = 0

label start:

    # # ==========================================================================================================================
    # # PROLOG / TERAS PAGI
    # # ==========================================================================================================================
    # scene bg_prolog_teras_pagi
    # show pipit standing at pipit_initial
    # with fade

    # narrator "Pada suatu hari..."

    # show wira_ceria at wleft_small
    # with dissolve

    # # These display lines of dialogue.
    # wira "Wah... hari ini cerah sekali ya!"

    # window hide
    # show wira_ceria at teras
    # with ease
    # pause 0.5
    # window show

    # wira "Pipit... lihat deh. Matahari pagi ini bagus banget, kan?"

    # window hide

    # pause 0.3
    # show pipit terbang at pipit_initial with dissolve
    # pause 0.5

    # scene bg_prolog_teras_pagi
    # show wiranpipit at teras
    # with dissolve
    # window show

    # narrator "Wira Terkekeh geli, matanya semakin berbinar"
    # wira "Ih, geli! Kamu suka ya aku elus elus?"
    # narrator "Bagi WIRA, dunia luar penuh dengan suara bising dan kebingungan. Namun, di teras ini, bersama Pipit... semuanya terasa benar."

    # window hide
    # show wiranpipit serius at teras
    # with dissolve
    # pause 0.5
    # window show

    # wira "Pipit... kalau nanti sayapmu sudah kuat... kalau kamu sudah bisa terbang jauh sampai ke awan..."

    # window hide
    # show wiranpipit nunduk at terasnew
    # with dissolve
    # pause 1.5
    # show wiranpipit terharu at teras
    # with dissolve
    # pause 1.5
    # window show

    # wira "...jangan tinggalin aku ya? Janji?"

    # narrator "Di teras rumah itu, WIRA Kecil mengunci separuh hatinya pada seekor burung peliharaan, menjadikannya satu satunya dunia kecil yang dia miliki."

    # window hide

    # # ==========================================================================================================================
    # # PROLOG / TAMAN KOTA SORE
    # # ==========================================================================================================================

    # scene taman
    # with dissolve

    # show wira megang sangkar at wira_megang_sangkar
    # with dissolve
    # pause 1.0

    # window show
    # wira "Kita sudah sampai, Pipit! Lihat, di sini jauh lebih luas daripada kamar aku."
    # window hide
    # pause 0.5

    # show wira duduk sangkar at wira_duduk_sangkar
    # with dissolve

    # pause 1.0
    # window show
    # wira "Aku buka ya pintunya? Tapi kamu jangan terbang tinggi tinggi... aku takut nggak bisa liat kamu lagi."
    # wira "Ayo... keluar sebentar..."

    # window hide
    # pause 0.5

    # show wira ketiup angin at wira_ketiup_angin
    # show pipit hinggap di sangkar at pipit_sangkar
    # with dissolve


    # pause 1.0

    # window show

    # wira "Pipit?! Tunggu!"

    # window hide
    # pause 0.5
    # show sangkar at sangkar_kosong
    # show wira ngejar at wira_ketiup_angin
    # show pipit terbang at atas_sangkar
    # with dissolve
    # pause 0.5

    # show pipit terbang at pipit_leaving
    # with ease

    # hide pipit terbang

    # pause 0.5
    # window show
    # wira "JANGAN TINGGALIN AKU! PIPIT!!!"
    # pause 1.0
    # window hide
    # scene taman
    # show wira sedih at wira_ketiup_angin
    # with dissolve

    # pause 2.0

    # scene black
    # with dissolve
    # narrator "...."
    # narrator "Pipit terbang.... entah kemana..."

    # =============================================================
    # PROLOG : KAMAR WIRA
    # =============================================================

    # scene kamarwira
    # with dissolve

    # show wira sinis at chara_wira_sinis
    # narrator "(Telepon berdering)"
    # show wira bingung at chara_wira_sinis
    # with dissolve
    # wira "Halo?"
    # ibu "Wira, besok kamu ke desa Nenek ya. Sudah Ibu siapkan semuanya."
    # # wira "(Mendengus)"
    # show wira sinis at chara_wira_sinis
    # with dissolve
    # wira "Ma, aku bukan anak kecil lagi yang bisa disuruh suruh ke desa nggak jelas gitu. Males."

    # ayah "Wira! Turuti kata Ibu! Kamu terlalu banyak membuang waktu dengan hal hal nggak berguna di sana."
    # ayah "Kalau besok kamu tidak berangkat, Papa potong uang jajan dan sita semua peralatan game mu!"
    # show wira bingung at chara_wira_sinis
    # # wira "(Mengepalkan tangan, ekspresi kesal)"
    # wira "Apa-apaan sih? Kok jadi ngancem gitu?!"
    # ibu "Ini untuk kebaikanmu, Sayang. Besok berangkat ya. Dadah!"
    # # wira "(Membanting HP ke kasur)"
    # wira "Males deh, selalu aja kayak gini."

    # =============================================================
    # SCENE 5: GUDANG NENEK - KOTAK "PETUALANGAN NUSANTARA"
    # =============================================================

    scene bg_gudang_nenek
    show wira murung at left_placeholder
    with fade

    wira "Nenek kira gue kuli apa... baru nyampe udah disuruh bongkar gudang."

    # TODO IMAGE: Senter Wira menyorot kotak kuningan tua di pojok bawah gudang.
    show kotak_petualangan_nusantara at lower_center_placeholder
    with dissolve

    show wira berlutut at left_placeholder
    with dissolve

    wira "Kotak apaan nih? 'Petualangan Nusantara'?"

    # TODO IMAGE: Close-up tangan Wira menyentuh ukiran tutup kotak yang terasa hangat.
    wira "Tapi... kenapa rasanya kayak nggak asing ya?"

    # TODO IMAGE: Wira membuka tutup kotak.
    # TODO SFX: Suara logam tua/engsel kotak terbuka.
    hide kotak_petualangan_nusantara
    show vfx_cahaya_kotak
    with Dissolve(0.4)

    # TODO VFX: Cahaya keemasan warna Pipit meledak dan menelan sosok Wira.
    pause 0.6

    # =============================================================
    # SCENE 6: TRANSISI - TERSEDOT KE DUNIA GAME
    # =============================================================

    scene bg_gudang_nenek
    show vfx_golden_vortex at center_placeholder
    show wira panik at center_placeholder
    with Fade(0.2, 0.3, 0.6)

    # TODO SFX: Angin menderu, gesekan logam ajaib, sayap mengepak sangat keras.
    wira "H-hei! Apa-apaan ini?! Lantainya... lantainya ilang?!"

    # TODO VFX: Tubuh Wira transparan lalu berubah menjadi butiran data/cahaya.
    hide wira panik
    show vfx_wira_data at center_placeholder
    with dissolve

    pause 1.0

    scene black
    with fade

    narasi "Beberapa pintu dibuka untuk melarikan diri... tapi kotak ini dibuka untuk membuatmu kembali."

    # =============================================================
    # SCENE 7: DUNIA GAME - PERTEMUAN GARUDA
    # =============================================================

    scene bg_pulau_terapung
    show wira bingung at left_placeholder
    with fade

    wira "Gue... gue di mana? Barusan tadi... gue di gudang..."
    wira "Gue masuk ke dalem game?! Gak mungkin, ini pasti gara-gara gue kurang tidur..."

    # TODO SFX: Kepakan sayap besar mendarat tepat di belakang Wira.
    show garuda megah at garuda_stage
    with vpunch

    garuda "Kau akhirnya kembali... meski kau lupa bagaimana kau kehilangan."

    show wira sinis at left_placeholder
    with dissolve

    wira "WOW! Burung apaan lo?! Bisa ngomong?!"
    wira "Jangan deket-deket! Gue nggak kenal lo, ya! Gue mau pulang sekarang!"

    garuda "Justru itu masalahnya, Wira. Kamu menutup hatimu begitu rapat sampai kamu tidak mengenali siapa yang berada di depanmu."

    wira "Nggak usah sok puitis. Gue nggak punya urusan sama burung mitos hasil CGI kayak lo."

    garuda "Aku adalah pemandumu. Tujuan permainannya sederhana: 'Pulang'. Tapi untuk pulang, kau harus belajar kembali cara 'menjaga'."

    # =============================================================
    # SCENE 8: PENJELASAN MEKANISME
    # =============================================================

    scene bg_pulau_terapung
    show garuda megah at garuda_stage
    show wira sinis at left_placeholder
    with dissolve

    # TODO IMAGE/UI: Dua bar poin di depan Wira dan peta checkpoint Nusantara.
    garuda "Setiap langkahmu di sini adalah cerminan prinsipmu. Apa yang kau pilih akan menentukan akhir dari kisahmu."

    wira "Poin? Pilihan? Oke, apa pun lah asal gue bisa keluar dari sini."

    garuda "Ayo, naiklah ke punggungku. Kita lihat, apakah amarahmu itu memang tameng, atau hanya beban yang menghambatmu."

    # TODO SFX: Wings flapping, kepakan sayap besar yang berwibawa.
    wira "Hah?! Naik ke punggung lo?! Ogah! Gue gak mau jadi penunggang burung!"
    wira "Jangan mimpi! Gue gak sudi! Balikin gue sekarang!"

    garuda "Naiklah. Waktu terus berjalan, hanya ada satu jalan keluar. Tunjukkan nilaimu melalui lima gerbang Nusantara dan pilihan pertamamu sudah menanti di Minangkabau."

    wira "Ck! Selalu aja maksa. Oke, fine! Tapi jangan macem-macem ya!"

    # TODO IMAGE: Wira berjalan ke Garuda. Garuda merendahkan tubuh agar Wira bisa naik.
    # TODO IMAGE: Wira memanjat ke punggung Garuda dengan canggung.
    show wira panik at left_placeholder
    with dissolve

    wira "Pegangan kencang! Jangan sampe jatoh!"

    garuda "Tenanglah, Wira. Aku akan menjagamu... sampai kau ingat siapa aku, dan siapa dirimu yang sebenarnya."

    # TODO SFX: Takeoff, kepakan sayap besar dan angin menderu.
    # TODO IMAGE: Garuda terbang tinggi membawa Wira menuju checkpoint pertama.
    scene bg_pulau_terapung
    show garuda megah at center_placeholder
    with Fade(0.2, 0.4, 0.8)

    pause 1.0

    # =============================================================
    # FEEDBACK GARUDA - PREVIEW MEKANISME POIN
    # =============================================================
    # Variabel contoh untuk sistem poin. Nanti bisa diubah oleh pilihan pemain.
    $ poin_karakter = 50

    if poin_karakter >= 65:
        garuda "Kamu mulai memahami bahwa demokrasi yang sesungguhnya bukan tentang suara terbanyak. Ini tentang keselarasan semua unsur dan bahwa prinsip bukan penghalang kemajuan, ini adalah kompas yang memastikan kita tidak tersesat di tengah perjalanan."
    elif poin_karakter >= 25:
        garuda "Ada momen di mana kamu membuka matamu dan momen di mana kamu masih memilih jalan yang mudah. Nagari ini mengajarkan bahwa setengah hadir lebih berbahaya dari tidak hadir sama sekali."
    else:
        garuda "Wira... di setiap pilihan yang kamu anggap pragmatis, kamu sebenarnya sedang membiarkan sesuatu yang orang lain jaga dengan nyawa mereka selama berabad-abad runtuh perlahan. Adat bukan museum."

    # Continue to the next merged checkpoint.
    jump bali_intro

# DAERAH 3 : BALI
label bali_intro:
    # BALI INTRODUCTION   JATILUWIH & SUBAK
    scene bg_bali_terasering_sore
    with fade
    pause 0.5

    show wira_dewasa_terkejut at terasering_wira
    with dissolve
    pause 0.8
    window show

    wira "Ini... sawahnya beda banget. Kok bisa rapi gini bertingkat tingkat?"

    window hide
    show garuda_terbang at terasering_garuda
    with ease
    pause 0.8
    hide garuda_terbang
    show garuda_berbicara at terasering_garuda
    with dissolve
    pause 1.0
    window show

    garuda "Selamat datang di Jatiluwih, WIRA. Ini bukan sekadar sawah biasa."

    window hide
    hide wira_dewasa_terkejut
    show wira_dewasa_bingung at terasering_wira
    with dissolve
    hide garuda_terbang
    hide garuda_berbicara
    show garuda_default at terasering_garuda
    with dissolve
    pause 0.6
    window show

    wira "Maksudnya?"

    window hide
    hide garuda_default
    show garuda_berbicara at terasering_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Yang kamu lihat di hadapanmu ini adalah bukti nyata bahwa manusia bisa hidup selaras dengan alam, sudah lebih dari seribu tahun. Namanya Subak"

    window hide
    hide garuda_berbicara
    show garuda_default at terasering_garuda
    with dissolve
    hide wira_dewasa_bingung
    show wira_dewasa_default at terasering_wira
    with dissolve
    pause 0.5
    window show

    wira "Subak? kayak nama orang?"

    window hide
    hide garuda_default
    show garuda_berbicara at terasering_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Subak adalah sistem pengairan sawah tradisional Bali. Dikelola bersama oleh para petani, berdasarkan hukum adat, gotong royong, dan filosofi leluhur. UNESCO mengakuinya sebagai Warisan Budaya Dunia sejak 2012."

    window hide
    hide garuda_berbicara
    show garuda_default at terasering_garuda
    with dissolve
    hide wira_dewasa_default
    show wira_dewasa_sinis at terasering_wira
    with dissolve
    pause 0.5
    window show

    wira "Diakui dunia? Cuma urusan ngatur air?"

    window hide
    hide garuda_default
    show garuda_berbicara at terasering_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Bukan 'cuma'. Sistem ini menyangga kehidupan ribuan keluarga selama berabad abad. Dan sekarang... ia sedang dalam bahaya."

    window hide
    hide garuda_berbicara
    hide wira_dewasa_sinis
    show peta_bali
    with dissolve
    window show

    garuda "Inilah misimu di Bali, Wira. Sistem subak di desa ini sedang terganggu. Para petani mulai bertengkar, masing masing ingin lebih banyak air untuk lahannya sendiri, tanpa peduli petani lain di hilir."

    window hide
    hide peta_bali
    with dissolve
    hide garuda_berbicara
    show garuda_default at terasering_garuda
    with dissolve
    hide wira_dewasa_sinis
    show wira_dewasa_bingung at terasering_wira
    with dissolve
    pause 0.5
    window show

    wira "Terus gua harus ngapain?"

    window hide
    hide garuda_default
    show garuda_berbicara at terasering_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Kamu akan menemui tiga petani, menghadapi konflik nyata, dan membuat keputusan. Setiap pilihanmu mencerminkan siapa dirimu, apakah kamu bisa melihat nilai kebersamaan, atau hanya melihat kepentingan satu pihak saja."

    window hide
    hide garuda_berbicara
    show garuda_default at terasering_garuda
    with dissolve
    hide wira_dewasa_bingung
    show wira_dewasa_terkejut at terasering_wira
    with dissolve
    pause 0.5
    window show

    narrator "WIRA menghela napas panjang, merasakan beban tanggung jawab."

    window hide
    pause 0.3
    window show

    wira "Oke mulai dari mana?"

    window hide
    hide garuda_default
    show garuda_berbicara at terasering_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Ikuti aliran air. Mulai dari hulu."

    window hide
    hide garuda_berbicara
    show garuda_default at terasering_garuda
    with dissolve
    pause 0.5

    jump bali_scene1


label bali_scene1:
    # SCENE 1 : PERTEMUAN DI HULU: PAK MADE DAN KONFLIK AIR
    scene bg_bali_pematang
    with fade
    pause 0.8

    window show
    narrator "WIRA dan GARUDA berjalan menyusuri pematang sawah yang sempit. Di sisi kiri mengalir saluran irigasi dari bambu dan batu, namun aliran air terlihat mulai terganggu."
    window hide
    with dissolve
    window show
    narrator "Di ujung pematang, seorang lelaki paruh baya bertubuh kekar muncul MADE SUJANA, kulit coklat terbakar matahari, sedang dengan tekun memperluas saluran airnya menggunakan cangkul."
    window hide
    with dissolve
    window show
    narrator "Udeng putih di kepalanya mewakili status pekerja keras Bali. Di wajahnya tampak lelah dan tekad yang keras kepala."

    window hide
    pause 1.0

    show wira_dewasa_default at pematang_wira
    with dissolve
    show garuda_default at pematang_garuda
    with dissolve
    pause 0.5
    show bali_pak_made_bekerja at pematang_made
    with dissolve
    pause 0.8
    window show

    made "Siapa kamu? Anak kota mana yang nyasar ke sawah orang?"

    window hide
    hide wira_dewasa_default
    show wira_dewasa_bingung at pematang_wira
    with dissolve
    pause 0.4
    window show

    wira "Gue Wira. Ini... teman gue, GARUDA."

    window hide
    hide bali_pak_made_bekerja
    show bali_pak_made_normal at pematang_made
    with dissolve
    pause 0.5
    window show

    made "GARUDA... hmm. Sudah lama tidak ada yang membawa nama itu ke sini."

    window hide
    hide bali_pak_made_normal
    show bali_pak_made_bekerja at pematang_made
    with dissolve
    pause 0.3
    window show

    made "Mau apa? Saya sibuk."

    window hide
    hide wira_dewasa_bingung
    show wira_dewasa_default at pematang_wira
    with dissolve
    pause 0.4
    window show

    wira "Itu salurannya... lagi diperbesar ya, Pak?"

    window hide
    hide bali_pak_made_bekerja
    show bali_pak_made_defensif at pematang_made
    with dissolve
    pause 0.5
    window show

    made "Iya. Sawah saya kekeringan tiga musim berturut turut. Sementara sawah si Nyoman di bawah sana malah kelebihan air. Tidak adil!"

    window hide
    hide garuda_default
    show garuda_berbicara at pematang_garuda
    with dissolve
    pause 0.5
    window show

    narrator "GARUDA berbisik pelan ke telinga WIRA, menjelaskan masalah sesungguhnya dengan suara yang hanya terdengar oleh WIRA."
    window hide
    window show
    garuda "Ini masalah utamanya. Made memperlebar salurannya sendiri untuk mengambil lebih banyak air dari jalur utama, tapi itu melanggar kesepakatan subak. Petani di hilir akan kekurangan air."

    window hide
    hide wira_dewasa_default
    show wira_dewasa_bingung at pematang_wira
    with dissolve
    pause 0.4
    window show

    wira "Terus kenapa dia bisa kekeringan?"

    window hide
    hide garuda_berbicara
    show garuda_default at pematang_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Karena ada dua kemungkinan: salurannya bocor, atau rotasi tanam yang tidak sinkron. Tapi Made lebih memilih solusi egois daripada bermusyawarah."

    window hide
    hide bali_pak_made_defensif
    show bali_pak_made_frustasi at pematang_made
    with dissolve
    pause 0.5
    window show

    made "Sudah tiga kali saya bicara ke Pekaseh (pemimpin subak kami) tapi tidak ada yang berubah. Istri saya sakit, anak saya sekolah mahal. Kalau panen gagal lagi, kami bisa kelaparan!"

    window hide
    hide wira_dewasa_bingung
    show wira_dewasa_terkejut at pematang_wira
    with dissolve
    pause 0.5
    window show

    narrator "WIRA merasakan dilema mendalam. Di satu sisi, keputusasaan Made sangat nyata. Di sisi lain, tindakannya melanggar kesepakatan bersama."

    window hide
    hide garuda_default
    show garuda_berbicara at pematang_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Wira, Made butuh didengar. Tapi saluran yang dia perlebar bisa merusak sistem untuk semua. Apa yang kamu katakan?"

    window hide
    pause 1.0

    # PILIHAN 1   SCENE 1
    menu:
        "Pak Made, saya ngerti kondisinya berat. Tapi kalau saluran ini diperlebar tanpa izin, petani lain di bawah juga akan susah. Gimana kalau kita lapor bareng ke Pekaseh, minta solusi yang adil untuk semua?":
            $ bali_points += 20
            $ scene1_choice = "A"
            jump scene1_ending_a

        "Yaudah sih, Pak. Mungkin emang perlu dibesarin biar cukup airnya.":
            $ bali_points  = 5
            $ scene1_choice = "B"
            jump scene1_ending_b

        "Pak Made berhak dong ambil lebih banyak air, itu sawah Bapak. Urusan yang di bawah, terserah mereka aja.":
            $ bali_points  = 20
            $ scene1_choice = "C"
            jump scene1_ending_c


label scene1_ending_a:
    window show
    window hide
    hide bali_pak_made_frustasi
    show bali_pak_made_normal at pematang_made
    with dissolve
    pause 0.5
    window show

    made "Kamu... beda dari anak kota yang biasanya. Baiklah. Ajak saya ke Pekaseh."

    window hide
    window show

    garuda "Bagus. Kamu baru saja menjaga inti dari Subak, bahwa air bukan milik satu orang, tapi milik bersama."

    window hide
    pause 1.0
    jump bali_scene2


label scene1_ending_b:
    window show
    window hide
    hide bali_pak_made_frustasi
    show bali_pak_made_bekerja at pematang_made
    with dissolve
    pause 0.5
    window show

    narrator "Made mengangguk puas, langsung melanjutkan mencangkul semakin dalam. Di kejauhan, saluran air hilir tampak mulai sedikit surut."
    window hide
    window show
    made "Nah, itu baru masuk akal. Anak muda yang ngerti situasi."

    window hide
    window show

    garuda "Kamu tidak salah sepenuhnya, Wira. Tapi diam dalam situasi ini sama saja dengan memilih satu pihak. Made merasa tindakannya dibenarkan, sementara petani di hilir akan semakin sulit. Keadilan butuh suara, bukan kebisuan."

    window hide
    hide wira_dewasa_terkejut
    show wira_dewasa_bingung at pematang_wira
    with dissolve
    pause 0.3
    window show

    wira "Tapi... gue kan nggak tahu siapa yang bener."

    window hide
    hide garuda_berbicara
    show garuda_default at pematang_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Itu alasan untuk bertanya dan mencari tahu, bukan untuk diam. Ayo kita terus."

    window hide
    pause 1.0
    jump bali_scene2


label scene1_ending_c:
    window show
    window hide
    hide bali_pak_made_frustasi
    show bali_pak_made_bekerja at pematang_made
    with dissolve
    pause 0.5
    window show

    narrator "Made tersenyum sinis, melanjutkan mencangkul. Di bawah, terlihat sawah Nyoman mulai mengering."
    window hide
    window show
    garuda "Wira... kamu baru saja membenarkan rantai kerusakan. Ketika satu petani mengambil terlalu banyak, sistem seluruhnya bisa runtuh. Itu yang terjadi ketika gotong royong digantikan ego."

    window hide
    pause 1.5
    jump bali_ending

# SCENE 2   PERTEMUAN DI HILIR
label bali_scene2:
    scene bg_bali_hilir
    with fade
    pause 1.0

    narrator "Wira, GARUDA, dan Made berjalan ke hilir. Mereka tiba di sawah yang lebih kering, tanah sedikit retak, padi menguning terlalu cepat."
    window hide
    window show
    narrator"Di sana berdiri BU NYOMAN SARI, wajah lelah tapi tatapan tajam, memakai kebaya sederhana dan kain batik. Ia sedang berdebat dengan seorang pria berpakaian kasual modern yang membawa tablet, BIMA, seorang pengembang properti muda."

    window hide
    pause 1.0

    show wira_dewasa_default at hilir_wira
    with dissolve
    show bali_bu_nyoman_tegas at hilir_nyoman
    with dissolve
    show bali_bima_normal at hilir_bima
    with dissolve
    show garuda_default at pematang_garuda
    with dissolve
    pause 0.8
    window show

    bima "Bu Nyoman, ini hitungannya jelas. Saya beli lahan ini dua kali lipat harga pasaran. Bisa untuk vila premium. Wisatawan mancanegara sudah antre. Anak ibu bisa kuliah di Denpasar!"

    window hide
    pause 0.3
    window show

    nyoman "Tidak. Lahan ini sudah ada sejak kakek buyut saya. Ini bukan hanya soal harga."

    window hide
    hide bali_bima
    show bali_bima_persuasif at hilir_bima
    with dissolve
    pause 0.3
    window show

    bima "Hei, siapa kalian?"

    window hide
    hide wira_dewasa_default
    show wira_dewasa_bingung at hilir_wira
    with dissolve
    pause 0.3
    window show

    wira "Cuma numpang lewat."

    window hide
    show bali_bu_nyoman_tegas at hilir_nyoman
    with dissolve
    pause 0.3
    window show

    nyoman "Anak muda, kamu lihat sendiri. Sawah ini kering karena air sudah diambil dari hulu. Sekarang ada yang mau beli lahannya dan jadikan vila. Kalau saya jual, sistem Subak di sini hancur, tidak ada lagi sawah, tidak ada lagi aliran air bersama."

    window hide
    hide garuda_default
    show garuda_berbicara at pematang_garuda
    with dissolve
    pause 0.3
    window show

    narrator "GARUDA berbisik ke Wira dengan penuh perhatian."
    window hide
    window show
    garuda "Ini pertarungan antara modernisasi dan kelestarian. Subak bukan hanya soal irigasi, ia adalah urat nadi kehidupan sosial dan budaya Bali. Kalau sawah ini dijual dan diubah jadi vila, rantai subak di daerah ini putus."

    window hide
    window show

    wira "Tapi kondisi Bu Nyoman juga susah karena kekeringan..."

    window hide
    hide garuda_berbicara
    show garuda_default at pematang_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Tepat sekali. Dan itu kenapa masalah di hulu harus diselesaikan dulu. Keduanya terhubung."

    window hide
    show bali_bima_persuasif at hilir_bima
    with dissolve
    pause 0.3
    window show

    narrator "Bima menunggu jawaban. Nyoman menatap Wira dengan harapan."

    bima "Kamu seperti teman Nyoman. Apa pendapatmu tentang ini?"

    window hide
    pause 1.0

    # PILIHAN 2   SCENE 2
    menu:
        "Bu Nyoman, saya setuju dengan Ibu. Subak ini Warisan Dunia, sekali dirusak, tidak bisa dikembalikan. Pak Bima, banyak wisatawan justru datang ke Bali karena pemandangan sawah ini. Kalau hilang, nilai wisatanya juga hilang.":
            $ bali_points += 20
            $ scene2_choice = "A"
            jump scene2_ending_a

        "Hmm... ini susah. Dua duanya ada benarnya juga sih.":
            $ bali_points += 0
            $ scene2_choice = "B"
            jump scene2_ending_b

        "Mending jual aja, Bu. Duitnya lebih pasti daripada nunggu panen.":
            $ bali_points  = 20
            $ scene2_choice = "C"
            jump scene2_ending_c


label scene2_ending_a:
    window show
    window hide
    hide bali_bu_nyoman
    show bali_bu_nyoman_lega at hilir_nyoman
    with dissolve
    pause 0.5
    window show

    nyoman "Terima kasih, anak. Tidak banyak anak muda yang masih peduli soal ini."

    window hide
    hide bali_bima
    show bali_bima_normal at hilir_bima
    with dissolve
    pause 0.5
    window show

    narrator "Bima terlihat keberatan tapi diam, kemudian pergi sambil bergumam."

    bima "Bisa negosiasi lagi kapan kapan..."

    window hide
    hide garuda_default
    show garuda_berbicara at pematang_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Kamu baru saja memahami bahwa menjaga budaya juga berarti menjaga ketahanan pangan dan ekonomi masyarakat. Warisan leluhur adalah modal, bukan beban."

    window hide
    pause 1.0
    jump bali_scene3


label scene2_ending_b:
    window show
    window hide
    hide bali_bima
    show bali_bima_normal at hilir_bima
    with dissolve
    pause 0.5
    window show

    narrator "Bima tersenyum kecil, mencium peluang dari kebimbangan Wira."
    window hide
    window show
    bima "Nah, berarti kamu juga setuju kalau ini bisa didiskusikan lagi, kan? Bu Nyoman, kita bisa duduk lagi"

    window hide
    show bali_bu_nyoman_tegas at hilir_nyoman
    with dissolve
    pause 0.3
    window show

    nyoman "Tidak. Jawaban saya tetap sama."
    window hide
    window show
    narrator "Nyoman menatap Wira dengan ekspresi sedikit kecewa."
    window hide
    window show
    nyoman "Anak muda, di sini tidak ada yang namanya 'dua duanya benar' kalau salah satunya menghancurkan yang lain. Tapi... terima kasih sudah mendengarkan."

    window hide
    hide garuda_default
    show garuda_berbicara at pematang_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Kompromis itu bijak dalam banyak situasi. Tapi ada momen di mana diam di tengah berarti membiarkan yang lebih keras suaranya menang. Bima hampir memanfaatkan keraguanmu. Untung Nyoman cukup kuat berdiri sendiri hari ini."

    window hide
    pause 1.0
    jump bali_scene3


label scene2_ending_c:
    window show
    window hide
    hide bali_bima
    show bali_bima_normal at hilir_bima
    with dissolve
    pause 0.5
    window show

    narrator "Bima langsung tersenyum lebar dan menepuk bahu Wira."
    window hide
    window show
    bima "Nah, ini baru anak muda yang realistis! Bu Nyoman, dengarkan teman kamu ini"

    window hide
    hide bali_bu_nyoman
    show bali_bu_nyoman_terluka at hilir_nyoman
    with dissolve
    pause 1.0
    window show

    narrator "Nyoman menatap Wira dengan tatapan terluka, lalu perlahan berbalik memunggungi mereka. Langit yang tadinya hangat mulai meredup."
    window hide
    window show
    nyoman "Keluar dari lahan saya. Semua."

    window hide
    pause 0.8
    window show
    garuda "Wira... kamu baru saja menyuruh seorang perempuan menjual tanah leluhurnya. Dan kamu belum tahu bahwa sawah itu adalah bagian dari sistem yang menghidupi puluhan keluarga lain."
    window hide
    window show
    garuda "Modernisasi bukan musuh. Tapi pembangunan yang mengorbankan akar budaya tanpa pertimbangan adalah kehilangan yang tidak bisa dibeli kembali, seberapapun mahal harganya."

    window hide
    pause 1.5
    jump bali_ending

# SCENE 3   MUSYAWARAH SUBAK: HADAPAN PEKASEH
label bali_scene3:
    window hide
    pause 1.0

    scene bg_bali_pura
    with fade
    pause 1.0

    narrator "Wira, GARUDA, Made, dan Nyoman berjalan menuju Pura Ulun Carik, tempat suci kecil di tengah sawah yang digunakan untuk pertemuan subak. Bangunan sederhana dari batu dengan atap jerami, dikelilingi bunga bunga sesajen."
    window hide
    window show
    narrator "PEKASEH WAYAN DHARMA, berusia 60an tahun, rambut putih, wajah bijaksana, memakai pakaian adat Bali putih kuning, duduk bersila di atas tikar."

    window hide
    pause 1.2

    show wira_dewasa_default at pura_wira
    with dissolve
    show garuda_default at pura_garuda
    with dissolve
    show bali_pak_made_normal at pura_made
    with dissolve
    show bali_bu_nyoman at pura_nyoman
    with dissolve
    show bali_pekaseh_bijaksana at pura_pekaseh
    with dissolve
    pause 1.0
    window show

    narrator "Suasana pura yang khidmat terasa berat dengan makna."

    pekaseh "Air adalah nadi kehidupan. Subak ini berdiri di atas tiga pilar: hubungan manusia dengan sesama, hubungan manusia dengan alam, dan hubungan manusia dengan Sang Pencipta. Ini yang kami sebut Tri Hita Karana."

    window hide
    hide wira_dewasa_default
    show wira_dewasa_bingung at pura_wira
    with dissolve
    pause 0.3
    window show

    wira "Tri Hita Karana... itu apa?"

    window hide
    hide garuda_default
    show garuda_berbicara at pura_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Filosofi Hindu Bali. Tiga penyebab kebahagiaan: keselarasan dengan sesama manusia, keselarasan dengan alam, dan keselarasan dengan Tuhan. Subak adalah penerapan nyata dari filosofi itu dalam pertanian."

    window hide
    # show bali_pekaseh_bijaksana at pura_pekaseh
    # with dissolve
    # pause 0.5
    window show

    pekaseh "Hari ini ada dua masalah. Pertama, saluran air yang diubah tanpa izin. Kedua, ancaman pengalihan fungsi lahan. Keduanya mengancam keharmonisan kita. Siapa yang bisa memberi jalan keluar?"

    window hide
    pause 0.5

    narrator "Semua mata beralih ke Wira."

    window hide
    show garuda_berbicara at pura_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Wira, ini saat menentukan. Pekaseh memintamu berbicara. Bagaimana kamu merespons?"

    window hide
    pause 1.0

    # PILIHAN 3   SCENE 3
    menu:
        "Menurut saya, sistem subak harus dikembalikan ke jalurnya, semua saluran air dikembalikan ke kondisi awal, lalu ada jadwal rotasi yang disepakati bersama. Untuk masalah lahan, desa bisa mengajukan status perlindungan budaya agar tidak bisa dijual sembarangan. Semua keputusan lewat musyawarah, bukan sepihak.":
            $ bali_points += 30
            $ scene3_choice = "A"
            jump scene3_ending_a

        "Mungkin bisa dibagi bagi airnya secara merata? Tapi soal lahan terserah Bu Nyoman sendiri aja.":
            $ bali_points  = 5
            $ scene3_choice = "B"
            jump scene3_ending_b

        "Ini urusan bapak bapak petani sendiri. Saya nggak tahu apa apa soal pertanian.":
            $ bali_points  = 15
            $ scene3_choice = "C"
            jump scene3_ending_c


label scene3_ending_a:
    window show
    window hide
    # show bali_pekaseh_bijaksana at pura_pekaseh
    # with dissolve
    # pause 0.5
    window show

    narrator "Pekaseh Wayan tersenyum dalam, mengangguk perlahan."
    window hide
    window show
    pekaseh "Anak ini... berbicara dengan kebijaksanaan leluhur, meski ia baru mengenalnya. Subak tidak bertahan seribu tahun karena keberuntungan, ia bertahan karena musyawarah. Karena tidak ada yang merasa paling berhak."

    window hide
    # show bali_pak_made_normal at pura_made
    # with dissolve
    # pause 0.3
    window show

    made "Maaf, tadi saya terlalu egois. Terima kasih sudah mengingatkan."

    window hide
    hide bali_bu_nyoman
    show bali_bu_nyoman_lega at pura_nyoman
    with dissolve
    pause 0.3
    window show

    nyoman "Subak akan tetap hidup, selama ada yang peduli seperti kamu."

    window hide
    show garuda_berbicara at pura_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Kamu baru saja memahami sesuatu yang sangat penting, bahwa ketahanan budaya dimulai dari keberanian untuk bermusyawarah. Bukan dari kekuatan satu orang."

    window hide
    pause 1.0
    jump bali_ending


label scene3_ending_b:
    window show
    window hide
    # show bali_pekaseh_bijaksana at pura_pekaseh
    # with dissolve
    # pause 0.5
    window show

    narrator "Pekaseh Wayan mengangguk pelan, ekspresi bijaksana tapi sedikit menggantung."
    window hide
    window show
    pekaseh "Pikiran yang tidak buruk. Pembagian air yang merata memang salah satu fondasi subak. Tapi soal lahan... itu bukan keputusan yang bisa diserahkan seorang diri. Setiap tanah di sini terhubung dengan sistem kita bersama."

    window hide
    # show bali_pak_made_normal at pura_made
    # with dissolve
    # pause 0.3
    window show

    made "Baiklah. Saya mau coba ikuti rotasi baru. Tapi saya harap ini benar benar adil."

    window hide
    # show bali_bu_nyoman at pura_nyoman
    # with dissolve
    # pause 0.3
    window show

    narrator "Nyoman menatap Wira, nada campuran antara terima kasih dan kekhawatiran."

    nyoman "Kamu sudah berusaha. Tapi masalah lahanku... aku masih harus pikirkan sendiri. Semoga ada jalan."

    window hide
    hide garuda_default
    show garuda_berbicara at pura_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Kamu sudah melihat satu bagian dari masalah, tapi belum semuanya. Subak adalah satu kesatuan, Wira. Solusi yang hanya menyentuh setengah masalah hanya menunda, bukan menyelesaikan. Tapi ini lebih baik dari diam."

    window hide
    pause 1.0
    jump bali_ending


label scene3_ending_c:
    window show
    window hide
    # show bali_pekaseh_bijaksana at pura_pekaseh
    # with dissolve
    pause 1.0
    window show

    narrator "Suasana pura yang tadinya khidmat menjadi hening yang canggung. Pekaseh Wayan menatap Wira lama, lalu mengangguk pelan dengan ekspresi yang sulit dibaca."
    window hide
    window show
    pekaseh "Tidak tahu... adalah titik awal yang jujur. Tapi tidak mau tahu... adalah pilihan yang berbeda."

    window hide
    pause 0.8

    narrator "Hening sejenak."
    window show
    window hide
    pekaseh "Kami akan musyawarahkan ini sendiri."

    window hide
    hide garuda_default
    show garuda_berbicara at pura_garuda
    with dissolve
    pause 0.3
    window show

    narrator "GARUDA mengisyaratkan Wira untuk pergi."
    window hide
    window show
    garuda "Ayo, Wira."

    window hide
    pause 0.5

    scene bg_bali_terasering_sore
    with fade
    pause 0.8

    show wira_dewasa_bingung at terasering_wira
    with dissolve
    show garuda_default at terasering_garuda
    with dissolve
    pause 0.5
    window show

    wira "Gue emang nggak tahu apa apa soal pertanian, Gar. Ngapain gue sok ngomong."

    window hide
    show garuda_berbicara at terasering_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Kamu tidak perlu tahu segalanya untuk berani berpendapat. Kamu sudah melihat Made yang terlalu egois. Kamu sudah melihat Nyoman yang terancam. Kamu sudah mendengar Pekaseh menjelaskan Tri Hita Karana. Semua itu cukup. Yang kurang bukan pengetahuanmu, tapi keberanianmu untuk peduli."

    window hide
    pause 1.0
    jump bali_ending


label bali_ending:
    window hide
    pause 1.0

    scene bg_bali_terasering_sore
    with fade
    pause 1.0

    narrator "Langit berubah jingga keemasan. Sawah terasering bersinar indah dalam cahaya senja. GARUDA mengepakkan sayap dan terbang melayang di hadapan Wira."

    show wira_dewasa_terkejut at terasering_wira
    with dissolve
    show garuda_berbicara at terasering_garuda
    with dissolve
    pause 0.8
    window show

    garuda "Checkpoint Bali selesai, Wira. Mari kita lihat hasil perjalananmu di sini."

    window hide
    pause 1.0

    if bali_points >= 0:
        window show
        garuda "Total poinmu di Bali: [bali_points]"
    else:
        window show
        garuda "Total poinmu di Bali: Minus [ -1 * bali_points]"

    window hide
    pause 0.5

    if bali_points >= 60:
        window show
        garuda "Kamu mulai melihat sesuatu yang dulu kamu anggap tidak relevan. Kearifan lokal bukan sekadar tradisi kuno, ia adalah teknologi hidup yang bertahan ribuan tahun karena benar benar bekerja."
    elif bali_points >= 20:
        window show
        garuda "Kamu sudah mencoba, Wira. Dan mencoba itu tidak kecil. Tapi ada momen momen di mana kamu berhenti di tepi, padahal satu langkah lagi bisa membuat perbedaan. Bawa itu bersamamu ke perjalanan berikutnya."
    else:
        window show
        garuda "Wira... kamu masih menutup mata. Di setiap pilihan yang kamu anggap 'pragmatis', kamu sebenarnya sedang memilih untuk merobohkan sesuatu yang orang lain bangun dengan susah payah selama berabad abad."

    window hide
    hide wira_dewasa_terkejut
    show wira_dewasa_default at terasering_wira
    with dissolve
    pause 0.5
    window show

    wira "Gue nggak nyangka... ngatur air aja bisa serumit ini. Dan sepenting ini."

    window hide
    show garuda_berbicara at terasering_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Selamat datang pada pemahaman yang ketiga. Tapi perjalanan belum selesai."
    window hide
    window show
    narrator "GARUDA menatap cakrawala jauh dengan penuh makna."
    window hide
    window show
    garuda "Kita pergi ke tempat di mana leluhur berbicara melalui rumah dan ukiran."

    window hide
    hide wira_dewasa_default
    show wira_dewasa_bingung at terasering_wira
    with dissolve
    pause 0.3
    window show

    wira "Ke mana?"

    window hide
    show garuda_berbicara at terasering_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Toraja."

    window hide
    pause 1.0

    narrator "Cahaya emas menyilaukan. Wira dan GARUDA terangkat, melayang di atas hamparan sawah Bali yang indah."

    with fade

    jump toraja_intro

# DAERAH 4 : TORAJA
label toraja_intro:
    scene bg_toraja_lembah
    with fade
    pause 1.0

    show wira_dewasa_terkejut at lembah_wira
    with dissolve
    pause 0.8
    window show

    wira "Woah..."

    window hide
    show garuda_default at lembah_garuda
    with dissolve
    pause 0.8
    window show

    garuda "Toraja. Tanah para leluhur. Di sini, batas antara yang hidup dan yang telah tiada terasa sangat tipis."

    window hide
    hide wira_dewasa_terkejut
    show wira_dewasa_terkejut at lembah_wira
    with dissolve
    pause 0.5
    window show

    wira "Rumah rumah itu... bentuknya aneh. Kayak kapal terbalik."

    window hide
    hide garuda_default
    show garuda_berbicara at lembah_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Itu Tongkonan, rumah adat Toraja. Atapnya yang melengkung melambangkan perahu, simbol perjalanan leluhur mereka dari tanah seberang yang jauh, dan perjalanan arwah ke alam berikutnya. Setiap ukiran, setiap warna, setiap ukuran, semuanya berbicara."

    window hide
    jump toraja_scene1


label toraja_scene1:
    scene toraja_kamar1
    with fade
    pause 0.5

    show wira_dewasa_default at gerbang_wira
    with dissolve
    pause 0.5

    show garuda_default at gerbang_garuda
    with dissolve
    pause 0.8

    show toraja_aldi_heran at gerbang_aldi
    with dissolve
    pause 0.5

    show toraja_paman_darius_uji at gerbang_paman_darius
    with dissolve
    pause 0.5

    show toraja_nenek_rante at gerbang_nenek_rante
    with dissolve
    pause 0.5

    window show

    aldi "Siapa kamu? Bukan dari desa ini kayaknya."

    window hide
    window show

    wira "Saya Wira. Saya... lagi mencoba memahami Tongkonan ini."

    window hide
    window show

    paman_darius "Kalau kamu mau masuk, kamu harus bisa menjawab dulu. Ukiran di pintu ini, Pa'tedong, apa artinya menurutmu?"

    window hide
    hide toraja_aldi_heran
    show toraja_aldi_mencibir at gerbang_aldi
    with dissolve
    pause 0.3
    window show

    aldi "Ah, itu cuma hiasan kerbau. Fungsional dulu jaman dulu, tapi sekarang sudah tidak relevan. Turis lebih suka melihat sesuatu yang lebih estetik dan modern."

    window hide
    show toraja_paman_darius_uji at gerbang_paman_darius
    with dissolve
    pause 0.3
    window show

    paman_darius "Kamu setuju dengan Aldi? Atau ada pendapat lain?"

    window hide
    pause 0.5

    # PILIHAN 1   SCENE 1
    menu:
        "Pa'tedong adalah simbol kesejahteraan dan leluhur":
            jump toraja_scene1_choice_a
        "Kerbau itu penting, mungkin simbol kekuatan":
            jump toraja_scene1_choice_b
        "Ya, ukiran ini memang tidak relevan":
            jump toraja_scene1_choice_c


label toraja_scene1_choice_a:
    $ toraja_points += 25
    window show

    wira "Pa'tedong bukan sekadar gambar kerbau. Kerbau di Toraja punya tiga fungsi: pengolah sawah, alat transaksi, dan hewan persembahan untuk leluhur. Ukiran ini adalah simbol kesejahteraan, kemakmuran, dan harapan agar keturunan bisa berkembang."

    window hide
    pause 0.5
    window show

    wira "Bahkan bentuknya yang menyatukan kerbau, babi, dan kambing melambangkan kendaraan arwah, penghubung antara yang hidup dan yang telah tiada."

    window hide
    pause 0.5
    window show

    wira "Ini bukan sekadar hiasan, ini identitas dan kepercayaan keluarga."

    window hide
    pause 1.0

    # Reaksi positif
    hide toraja_paman_darius_uji
    show toraja_paman_darius_hormat at gerbang_paman_darius
    with dissolve
    pause 0.3
    window show

    paman_darius "Kamu memahami lebih dari yang kusangka. Masuk."

    window hide
    with dissolve
    pause 0.3
    window show

    aldi "Aku... tidak pernah berpikir sejauh itu tentang ukiran ini."

    window hide
    hide garuda_default
    show garuda_berbicara at gerbang_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Bagus. Tapi perjalanan belum selesai. Masih ada dua kamar lagi."

    window hide
    pause 1.0
    jump toraja_scene2


label toraja_scene1_choice_b:
    $ toraja_points += 0
    window show

    wira "Mungkin... kerbau itu penting buat orang Toraja? Lambang kekuatan mungkin?"

    window hide
    pause 0.8
    window show

    paman_darius "Jawabanmu tidak salah. Tapi juga belum sampai. Masuk dulu."

    window hide
    hide garuda_default
    show garuda_berbicara at gerbang_garuda
    with dissolve
    pause 0.5
    window show

    garuda "Kamu melihat kulitnya, tapi belum ke dalamnya. Kerbau bukan sekadar simbol kekuatan, ia adalah penghubung antara dua dunia. Simpan pemahaman itu untuk kamar kamar berikutnya."

    window hide
    pause 1.0
    jump toraja_scene2


label toraja_scene1_choice_c:
    $ toraja_points -= 25
    window show

    wira "Iya sih, kalau buat wisatawan modern, mungkin perlu desain yang lebih fresh."

    window hide
    pause 1.0

    # Reaksi negatif
    hide toraja_paman_darius_uji
    show toraja_paman_darius_tegas at gerbang_paman_darius
    with dissolve
    pause 0.5
    window show

    paman_darius "Pintu ini tidak bisa dibuka dengan pikiran seperti itu."

    window hide
    window show

    aldi "Lihat? Bahkan orang luar pun setuju denganku."

    window hide
    hide garuda_default
    show garuda_berbicara at gerbang_garuda
    with dissolve
    pause 0.5
    window show

    garuda "Wira... kamu baru saja membenarkan penghapusan sebuah identitas. Yang kamu anggap 'tidak relevan' adalah catatan ratusan tahun kehidupan keluarga ini. Relevansi bukan ditentukan oleh selera pasar."

    window hide
    pause 1.5

    jump toraja_end


label toraja_scene2:
    # SCENE 2   KAMAR LELUHUR (hanya jika pilihan A atau B di scene 1)
    scene bg_toraja_kamar2
    with fade
    pause 1.0

    show toraja_tautau at kamar_leluhur_tautau
    with dissolve
    pause 0.5

    show wira_dewasa_default at kamar_leluhur_wira
    with dissolve
    pause 0.5

    show toraja_paman_darius_tegas at kamar_leluhur_paman_darius
    with dissolve
    pause 0.5

    show garuda_default at kamar_leluhur_garuda
    with dissolve
    pause 0.3

    window show

    paman_darius "Kamar ini adalah kamar leluhur. Di sinilah foto dan benda benda milik mereka yang telah pergi disimpan. Bukan untuk ditakuti, tapi untuk diingat."

    window hide
    hide wira_dewasa_default
    show wira_dewasa_terkejut at kamar_leluhur_wira
    with dissolve
    pause 0.3
    window show

    wira "Itu... patung orang mati?"

    window hide
    pause 0.3
    window show

    paman_darius "Tau Tau adalah representasi leluhur yang telah tiada."
    window hide
    window show
    paman_darius "Di Toraja, kematian bukan akhir, melainkan bagian dari perjalanan panjang. Upacara Rambu Solo, upacara pemakaman, bisa berlangsung berhari hari, bahkan berminggu minggu, dengan menyembelih puluhan kerbau."

    window hide
    pause 0.5
    window show

    paman_darius "Bukan karena pemborosan, tapi karena kerbau adalah kendaraan arwah menuju negeri Puya, alam leluhur."

    window hide
    pause 0.8
    window show

    paman_darius "Kini pertanyaan untuk membuka kamar ini: Mengapa masyarakat Toraja justru merayakan kematian dengan pesta besar, bukan berduka dalam keheningan?"

    window hide
    pause 1.0

    # PILIHAN 2   SCENE 2
    menu:
        "Karena kematian adalah perpindahan, bukan perpisahan":
            jump toraja_scene2_choice_a
        "Mungkin karena adat mereka memang seperti itu":
            jump toraja_scene2_choice_b
        "Itu berlebihan, terlalu banyak kerbau":
            jump toraja_scene2_choice_c


label toraja_scene2_choice_a:
    $ toraja_points += 25
    window show

    wira "Karena bagi masyarakat Toraja, kematian bukan perpisahan, tapi perpindahan."
    window hide
    window show
    wira "Dengan pesta besar, mereka tidak sekadar berduka, tapi merayakan kepergian leluhur dengan bermartabat, memastikan arwah mereka dibekali dengan baik untuk perjalanan ke Puya."

    window hide
    pause 0.5
    window show

    wira "Ini juga mempererat ikatan keluarga yang mungkin tercerai berai, karena semua berkumpul. Kematian bukan akhir, tapi reuni."

    window hide
    pause 1.0

    hide toraja_paman_darius_tegas
    show toraja_paman_darius_hormat at kamar_leluhur_paman_darius
    with dissolve
    pause 0.3
    window show

    paman_darius "..."

    narrator "Paman Darius menutup mata sejenak, seperti menahan haru."

    window hide
    hide wira_dewasa_terkejut
    show wira_dewasa_default at kamar_leluhur_wira
    with dissolve
    pause 0.5
    window show

    wira "...Saya hanya mencoba mengerti."

    window hide
    hide garuda_default
    show garuda_berbicara at kamar_leluhur_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Kadang, memahami orang lain adalah cara kita memahami diri sendiri."

    window hide
    pause 1.0
    jump toraja_scene3


label toraja_scene2_choice_b:
    $ toraja_points += 0
    window show

    wira "Mungkin karena adat mereka memang seperti itu, sudah turun temurun."

    window hide
    pause 1.0
    window show

    paman_darius "Adat memang turun temurun. Tapi ada alasan mengapa ia diwariskan, bukan sekadar diulang. Masuk dulu."

    window hide
    hide garuda_default
    show garuda_berbicara at kamar_leluhur_garuda
    with dissolve
    pause 0.5
    window show

    garuda "Pikirkan dengan hati, Wira. Ini bukan tentang 'benar' atau 'salah' secara akademis. Ini tentang pemahaman yang tulus."

    window hide
    pause 1.0
    jump toraja_scene3


label toraja_scene2_choice_c:
    $ toraja_points -= 20
    window show

    wira "Jujur agak berlebihan sih. Ngapain harus sampai sembelih banyak kerbau?"

    window hide
    pause 1.0

    narrator "Keheningan panjang yang canggung. Paman Darius menutup mata sejenak."

    window hide
    window show

    paman_darius "Yang kamu sebut 'berlebihan'... adalah cara kami memastikan tidak ada yang pergi sendirian. Bahkan dalam kematian."

    window hide
    pause 1.0

    hide garuda_default
    show garuda_berbicara at kamar_leluhur_garuda
    with dissolve
    pause 0.3
    window show

    garuda "Wira. Bukan soal jumlah kerbaunya. Tapi soal apa yang rela diberikan seseorang untuk memastikan orang yang dicintainya dihormati sampai akhir. Kamu menghakimi sebelum memahami."

    window hide
    pause 1.5
    jump toraja_end


label toraja_scene3:
    # SCENE 3   RUANG MUSYAWARAH (hanya jika pilihan A atau B di scene 2)
    scene bg_toraja_kamar3
    with fade
    pause 1.0

    show wira_dewasa_default at musyawarah_wira
    with dissolve
    pause 0.3

    show garuda_default at musyawarah_garuda
    with dissolve
    pause 0.3

    show toraja_paman_darius at musyawarah_paman_darius
    with dissolve
    pause 0.3

    show toraja_aldi_normal at musyawarah_aldi
    with dissolve
    pause 0.3

    show toraja_nenek_rante at musyawarah_nenek_rante
    with dissolve
    pause 0.3

    show toraja_rena at musyawarah_rena
    with dissolve
    pause 0.4
    window show

    nenek_rante "Ini dokumen yang sudah kita tunda tiga bulan. Perusahaan itu menawarkan banyak uang, tapi syaratnya, pengelolaan Tongkonan sepenuhnya diserahkan kepada mereka."
    window hide
    window show
    nenek_rante"Kita tidak lagi bisa menentukan upacara apa yang boleh dilakukan di sini, ukiran apa yang boleh ada, siapa yang boleh masuk."

    window hide
    hide toraja_aldi_normal
    show toraja_aldi_mencibir at musyawarah_aldi
    with dissolve
    pause 0.3
    window show

    aldi "Tapi Nenek, uangnya bisa untuk renovasi, untuk biaya hidup keluarga, untuk pendidikan anak anak kita"

    window hide
    hide toraja_paman_darius
    show toraja_paman_darius_tegas at musyawarah_paman_darius
    with dissolve
    pause 0.3
    window show

    paman_darius "Kalau kita menyerahkan pengelolaan, Tongkonan ini bukan lagi rumah kita. Ia menjadi properti bisnis. Leluhur kita akan menjadi komoditas."

    window hide
    hide toraja_rena
    show toraja_rena_bingung at musyawarah_rena
    with dissolve
    pause 0.3
    window show

    rena "Kamu yang sudah melihat semua kamar ini, Wira... menurut kamu, apa yang seharusnya dilakukan keluarga kami?"

    window hide
    pause 1.0

    # PILIHAN 3   SCENE 3 (KEPUTUSAN AKHIR)
    menu:
        "Kelola sendiri dengan koperasi budaya, jual wisata lokal":
            jump toraja_scene3_choice_a
        "Coba negosiasi kontrak, minta beberapa syarat diubah":
            jump toraja_scene3_choice_b
        "Serahkan ke perusahaan demi uang yang besar":
            jump toraja_scene3_choice_c


label toraja_scene3_choice_a:
    $ toraja_points += 30
    window show

    wira "Jangan tanda tangani kontrak itu. Bukan karena takut maju, tapi karena ada cara yang lebih baik. Tongkonan bisa menjadi destinasi budaya yang dikelola sendiri oleh keluarga dan komunitas."

    window hide
    pause 0.5
    window show

    wira "Buat koperasi budaya, jual tiket wisata, sewa guide lokal, jual produk tenun dan ukiran buatan warga."
    window hide
    window show
    wira "Hasilnya untuk keluarga dan perawatan Tongkonan. Wisatawan yang datang bukan cuma melihat 'pertunjukan', tapi benar benar belajar. Itu justru lebih bernilai dan berkelanjutan."

    window hide
    pause 1.5

    narrator "Keheningan panjang. Lalu Nenek Rante tersenyum, senyuman paling tulus sepanjang game."

    window hide
    window show

    nenek_rante "Anak ini... berbicara dengan suara yang pernah aku dengar dulu. Suara seseorang yang pernah kehilangan sesuatu, dan akhirnya mengerti harganya."

    window hide
    hide toraja_paman_darius_tegas
    show toraja_paman_darius_hormat at musyawarah_paman_darius
    with dissolve
    pause 0.3
    window show

    paman_darius "Kamu tidak hanya membuka tiga kamar Tongkonan ini. Kamu membuka sesuatu di dalam dirimu sendiri."

    window hide
    with dissolve
    pause 0.3
    window show

    aldi "Aku... selama ini pikir mempertahankan tradisi berarti tertinggal. Tapi ternyata mempertahankan tradisi bisa jadi cara paling cerdas untuk maju."

    window hide
    hide toraja_rena_heran
    show toraja_rena_terharu at musyawarah_rena
    with dissolve
    pause 0.5
    window show

    rena "Terima kasih, Wira."
    window hide
    window show

    wira "Saya hanya... mencoba jujur."

    window hide
    hide garuda_default
    show garuda_berbicara at musyawarah_garuda
    with dissolve
    pause 0.5
    window show

    garuda "Kejujuran adalah awal dari segalanya, Wira."

    window hide
    pause 1.5
    jump toraja_end


label toraja_scene3_choice_b:
    $ toraja_points += 5
    window show

    wira "Mungkin bisa nego kontraknya dulu, minta beberapa syarat diubah?"

    window hide
    pause 1.0
    window show

    nenek_rante "Bernegosiasi bisa dilakukan. Tapi syarat mana yang kamu pikir bisa diubah, nak? Jika kontrol atas upacara dan ukiran tidak bisa diganggu gugat, apakah perusahaan itu masih mau?"

    window hide
    window show

    paman_darius "Kontrak seperti ini seperti tali. Kamu pikir kamu yang memegang ujungnya, tapi lama lama kamu sadar ujung yang lain sudah diikat lebih kencang."

    window hide
    hide wira_dewasa_default
    show wira_dewasa_bingung at musyawarah_wira
    with dissolve
    pause 0.5
    window show

    wira "Saya hanya... mencoba jujur."

    window hide
    hide garuda_default
    show garuda_berbicara at musyawarah_garuda
    with dissolve
    pause 0.5
    window show

    garuda "Kejujuran adalah awal dari segalanya, Wira. Tapi tanpa posisi tawar yang jelas, keluarga ini bisa berakhir di titik yang sama, atau lebih buruk. Ada jawaban yang lebih utuh dari ini, Wira."

    window hide
    pause 1.5
    jump toraja_end


label toraja_scene3_choice_c:
    $ toraja_points -= 30
    window show

    wira "Kalau uangnya memang besar dan bisa membantu keluarga, mungkin tidak ada salahnya dicoba."

    window hide
    pause 1.5

    narrator "Keheningan panjang yang berbeda dari biasanya. Nenek Rante menutup mata. Paman Darius berdiri dan berjalan ke sudut ruangan tanpa berkata apa apa."

    window hide
    hide toraja_rena_heran
    show toraja_rena_bingung at musyawarah_rena
    with dissolve
    pause 0.3
    window show

    narrator "Rena menunduk. Aldi mengambil pulpen, hampir menandatangani, tapi tangannya berhenti sendiri."

    window hide
    pause 1.0
    window show

    nenek_rante "Kalau begitu... tidak ada lagi yang perlu dibicarakan hari ini."

    window hide
    hide garuda_default
    show garuda_berbicara at musyawarah_garuda
    with dissolve
    pause 0.5
    window show

    garuda "Ayo, Wira."

    narrator "Garuda membawa Wira keluar ruangan. Di luar, Garuda berhenti dan menatap Wira."

    window hide
    pause 1.0
    window show

    garuda "Wira. Kamu baru saja menyarankan sebuah keluarga untuk menyerahkan rumah leluhur mereka kepada korporasi demi uang."
    window hide
    window show
    garuda "Dan kamu melakukannya setelah melihat sendiri betapa dalamnya makna setiap sudut rumah itu. Bukan soal menentang modernisasi. Tapi soal siapa yang berhak memutuskan nasib sebuah warisan."

    window hide
    pause 1.5
    jump toraja_end


label toraja_end:
    scene bg_toraja_lembah_tongkonan_sore
    with fade
    pause 1.5

    show wira_dewasa_default at lembah_wira
    with dissolve
    pause 0.5

    show garuda_default at lembah_garuda
    with dissolve
    pause 0.8
    window show

    narrator "Matahari terbenam di balik bukit Toraja, langit merah, jingga, ungu. Deretan Tongkonan berdiri megah dalam cahaya senja. Suara Pa'pompang mengalun syahdu dari kejauhan."

    window hide
    pause 1.5
    hide garuda_default
    show garuda_berbicara at lembah_garuda
    with dissolve
    pause 0.3
    window show

    if toraja_points >= 0:
        window show
        garuda "Checkpoint Toraja selesai. Total poinmu di Toraja: [toraja_points]"
    else:
        garuda "Checkpoint Toraja selesai. Total poinmu di Toraja: Minus [toraja_points]"

    window hide
    pause 1.0
    window show

    if toraja_points >= 80:
        garuda "Wira... kamu tidak hanya memahami Toraja. Kamu mulai memahami sesuatu yang jauh lebih dalam. Bahwa kehilangan, berapapun sakitnya, bisa menjadi pintu menuju pengertian."
        window hide
        window show
        garuda "Seperti Pa'tedong yang mengandung perjalanan arwah... kehilangan pun adalah bagian dari perjalanan."
    elif toraja_points >= 20:
        garuda "Kamu melihat sebagian dari apa yang seharusnya terlihat. Ada momen di mana kamu hampir sampai, lalu memilih berhenti di tepi. Toraja tidak menghukummu atas itu. Tapi ia mengundangmu untuk suatu hari kembali dengan mata yang lebih terbuka."
    else:
        garuda "Kamu mengunci kamar kamar itu, Wira. Bukan karena kamu tidak cerdas, tapi karena kamu masih memilih untuk tidak melihat. Masih ada waktu untuk berubah. Masih ada checkpoint yang tersisa."

    window hide
    pause 1.5
    window show

    wira "GARUDA... gue mulai ngerti kenapa lo bawa gue ke tempat tempat ini."

    window hide
    window show

    garuda "Belum sepenuhnya. Tapi kamu sudah di jalan yang benar."

    window hide
    pause 2.0

    narrator "Cahaya senja Toraja memudar. Tongkonan siluet di balik langit merah. Wira dan Garuda berdiri berdampingan, kecil di bawah langit yang luas."

    with fade

    # This ends the game for now.
