# ===================================================================
# CHAPTER PAPUA - DANAU SENTANI
# Checkpoint 5
# ===================================================================

default player_points = 0

# ===================================================================
# KARAKTER
# ===================================================================

define wira          = Character("Wira",           who_color="#4169E1")
define garuda        = Character("Garuda",          who_color="#FFD700")
define Mama_Tita     = Character("Mama Tita",       who_color="#8B4513")
define Tetua_Asei    = Character("Tetua Asei",      who_color="#5C3317")
define Tetua_Asmat   = Character("Tetua Asmat",     who_color="#654321")
define Perempuan_Tua = Character("Perempuan Tua",   who_color="#8B4513")
define Pemuda_Yoboi  = Character("Pemuda Yoboi",    who_color="#6B8E23")

# ===================================================================
# TRANSFORM (POSISI SPRITE)
# ===================================================================

transform wleft_small:
    xalign 0.1
    yalign 1.0
    zoom 0.65

transform wright_small:
    xalign 0.9
    yalign 1.0
    zoom 0.65

transform wcenter_small:
    xalign 0.5
    yalign 1.0
    zoom 0.65

# ===================================================================
# SPRITE KARAKTER
# ===================================================================

image wira_bingung    = "wira dewasa bingung.png"
image wira_terharu    = "wira dewasa terharu.png"
image wira_sinis      = "wira dewasa sinis.png"

image garuda_berdiri   = "garuda_default.png"
image garuda_terbang   = "garuda_terbang.png"
image garuda_berbicara = "garuda_berbicara.png"

image perempuan_tua   = "perempuan_tua.png"
image mama_tita       = "mama_tita.png"
image tetua_asei      = "tetua_asei.png"
image tetua_asmat     = "tetua_asmat.png"
image pemuda_yoboi    = "pemuda_yoboi.png"

# ===================================================================
# BACKGROUND
# ===================================================================

image bg_danau_sentani  = Transform("danau_sentani.png",         size=(1920, 1080))
image bg_pulau_asei     = Transform("pulau_asei.png",            size=(1920, 1080))
image bg_kampung_ayapo  = Transform("kampung_ayapo.png",         size=(1920, 1080))
image bg_barapen        = Transform("lapangan_barapen.png",      size=(1920, 1080))
image bg_hutan_yoboi    = Transform("hutan_yoboi.png",           size=(1920, 1080))
image bg_rawa_asmat     = Transform("sungai_rawa_asmat.png",     size=(1920, 1080))
image bg_gua_air_suci   = Transform("gua_air_suci.png",          size=(1920, 1080))

# ===================================================================
# VISUAL PILIHAN — PNG foto khusus per pilihan
# ===================================================================

# SCENE 2 — A=Bijak, B=Netral, C=Egois (urutan tetap)
image pilihan2_a_idle  = Transform("pilihana_scene2.png", size=(350, 220))
image pilihan2_a_hover = Transform("pilihana_scene2.png", size=(370, 240))
image pilihan2_b_idle  = Transform("pilihanb_scene2.png", size=(350, 220))
image pilihan2_b_hover = Transform("pilihanb_scene2.png", size=(370, 240))
image pilihan2_c_idle  = Transform("pilihanc_scene2.png", size=(350, 220))
image pilihan2_c_hover = Transform("pilihanc_scene2.png", size=(370, 240))

# SCENE 3 — A=Netral, B=Egois, C=Bijak
image pilihan3_a_idle  = Transform("pilihana_scene3.png", size=(350, 220))
image pilihan3_a_hover = Transform("pilihana_scene3.png", size=(370, 240))
image pilihan3_b_idle  = Transform("pilihanb_scene3.png", size=(350, 220))
image pilihan3_b_hover = Transform("pilihanb_scene3.png", size=(370, 240))
image pilihan3_c_idle  = Transform("pilihanc_scene3.png", size=(350, 220))
image pilihan3_c_hover = Transform("pilihanc_scene3.png", size=(370, 240))

# SCENE 4 — A=Egois, B=Bijak, C=Netral
image pilihan4_a_idle  = Transform("pilihana_scene4.png", size=(350, 220))
image pilihan4_a_hover = Transform("pilihana_scene4.png", size=(370, 240))
image pilihan4_b_idle  = Transform("pilihanb_scene4.png", size=(350, 220))
image pilihan4_b_hover = Transform("pilihanb_scene4.png", size=(370, 240))
image pilihan4_c_idle  = Transform("pilihanc_scene4.png", size=(350, 220))
image pilihan4_c_hover = Transform("pilihanc_scene4.png", size=(370, 240))

# ===================================================================
# ENDING
# ===================================================================

image ending_baik_papua   = Transform("danau_sentani.png",     size=(1920, 1080))
image ending_netral_papua = Transform("kampung_ayapo.png",     size=(1920, 1080))
image ending_buruk_papua  = Transform("sungai_rawa_asmat.png", size=(1920, 1080))

# ===================================================================
# SCREEN PILIHAN SCENE 2
# A = Bijak [+25], B = Netral [0], C = Egois [-25]
# ===================================================================

screen pilihan_pendekatan_suku():

    modal True

    hbox:
        spacing 60
        xalign 0.5
        yalign 0.72

        vbox:
            spacing 10
            imagebutton:
                idle  "pilihan2_a_idle"
                hover "pilihan2_a_hover"
                action Jump("pilihan_pendekatan_a")
            text "PILIHAN A\nDATANGI\nSATU PER SATU":
                xalign 0.5
                text_align 0.5
                size 24

        vbox:
            spacing 10
            imagebutton:
                idle  "pilihan2_b_idle"
                hover "pilihan2_b_hover"
                action Jump("pilihan_pendekatan_b")
            text "PILIHAN B\nSAMPAIKAN\nPESAN":
                xalign 0.5
                text_align 0.5
                size 24

        vbox:
            spacing 10
            imagebutton:
                idle  "pilihan2_c_idle"
                hover "pilihan2_c_hover"
                action Jump("pilihan_pendekatan_c")
            text "PILIHAN C\nPAKSA\nBERHENTI":
                xalign 0.5
                text_align 0.5
                size 24

# ===================================================================
# SCREEN PILIHAN SCENE 3
# A = Netral [0], B = Egois [-25], C = Bijak [+25]
# ===================================================================

screen pilihan_barapen():

    modal True

    hbox:
        spacing 60
        xalign 0.5
        yalign 0.72

        vbox:
            spacing 10
            imagebutton:
                idle  "pilihan3_a_idle"
                hover "pilihan3_a_hover"
                action Jump("pilihan_barapen_a")
            text "PILIHAN A\nTUMPUK\nSEMUA":
                xalign 0.5
                text_align 0.5
                size 24

        vbox:
            spacing 10
            imagebutton:
                idle  "pilihan3_b_idle"
                hover "pilihan3_b_hover"
                action Jump("pilihan_barapen_b")
            text "PILIHAN B\nTIGA BATU\nSAJA":
                xalign 0.5
                text_align 0.5
                size 24

        vbox:
            spacing 10
            imagebutton:
                idle  "pilihan3_c_idle"
                hover "pilihan3_c_hover"
                action Jump("pilihan_barapen_c")
            text "PILIHAN C\nIKUTI\nADAT":
                xalign 0.5
                text_align 0.5
                size 24

# ===================================================================
# SCREEN PILIHAN SCENE 4
# A = Egois [-25], B = Bijak [+25], C = Netral [0]
# ===================================================================

screen pilihan_ukiran_asmat():

    modal True

    hbox:
        spacing 60
        xalign 0.5
        yalign 0.72

        vbox:
            spacing 10
            imagebutton:
                idle  "pilihan4_a_idle"
                hover "pilihan4_a_hover"
                action Jump("pilihan_ukiran_a")
            text "PILIHAN A\nPAKSA\nTETUA":
                xalign 0.5
                text_align 0.5
                size 24

        vbox:
            spacing 10
            imagebutton:
                idle  "pilihan4_b_idle"
                hover "pilihan4_b_hover"
                action Jump("pilihan_ukiran_b")
            text "PILIHAN B\nRENUNGI\nUKIRAN":
                xalign 0.5
                text_align 0.5
                size 24

        vbox:
            spacing 10
            imagebutton:
                idle  "pilihan4_c_idle"
                hover "pilihan4_c_hover"
                action Jump("pilihan_ukiran_c")
            text "PILIHAN C\nTANYA\nWARGA":
                xalign 0.5
                text_align 0.5
                size 24

# ===================================================================
# LABEL START
# ===================================================================

label start:
    jump chapter_papua

# ===================================================================
# LABEL UTAMA
# ===================================================================

label chapter_papua:

    $ player_points = 0

    scene bg_danau_sentani
    with fade

    narrator "Dari POV Wira, danau luas membentang. Gunung ada di kejauhan dan kabut tipis melayang di atas permukaan air."

    show wira_bingung at wleft_small
    with dissolve

    narrator "Terdengar suara percikan air. Tiba-tiba suara teriakan dan perkelahian memecah suasana."

    wira "Loh, itu ada apa? Aku harus sembunyi sekarang."

    pause 1.0

    narrator "Setelah beberapa lama bersembunyi, keadaan sedikit mereda tetapi Garuda belum muncul."

    wira "Mana sih Garuda, kok nggak muncul-muncul. Masa aku harus ngelewatin misi ini sendirian?"

    hide wira_bingung

    show garuda_terbang at wright_small
    with dissolve

    show wira_bingung at wleft_small
    with dissolve

    garuda "Halo Wira, selamat datang di misi terakhirmu."

    garuda "Seperti yang kamu lihat, ada pertikaian antara 5 suku yang tinggal di sekitar Danau Sentani karena permasalahan wilayah tangkap ikan."

    garuda "Kamu adalah satu-satunya kunci agar konflik ini dapat selesai dan kehidupan mereka kembali normal."

    wira "Jadi aku harus apa, Gar? Nemuin mereka satu per satu? Aku orang luar, apa mereka mau dengerin pendapatku?"

    garuda "Pilihan ada di tanganmu seorang. Ingat, caramu mendekati mereka akan menentukan nasib danau ini."

# ===================================================================
# SCENE 2
# ===================================================================

    scene bg_pulau_asei
    with dissolve

    narrator "Wira menaiki perahu kecil menuju Pulau Suku Asei."

    show perempuan_tua at wright_small
    show wira_terharu at wleft_small
    with dissolve

    wira "Selamat siang, Nenek. Maaf mengganggu."

    Perempuan_Tua "Kamu orang baru. Perahumu tidak seperti perahu kami."

    wira "Aku dari jauh, Nenek. Aku datang dengan hati yang ingin belajar."

    Perempuan_Tua "Belajar? Belajar apa? Tidak ada yang menarik di sini."

    wira "Aku ingin belajar tentang danau ini. Tentang suku-suku di sini. Aku dengar... ada konflik? Mungkin aku bisa membantu."

    Perempuan_Tua "Membantu? Banyak orang datang mau membantu. Semua pergi setelah dapat apa yang mereka mau."

    wira "Tidak, Nek. Aku akan menunjukkan bahwa aku benar-benar berbeda dari mereka."

    narrator "Wira membantu memindahkan daun sagu hingga pekerjaannya selesai."

    Perempuan_Tua "Kamu orang asing. Mau bantu kami berdamai?"

    Perempuan_Tua "Kamu mau pakai cara apa?"

    hide perempuan_tua
    hide wira_terharu

    call screen pilihan_pendekatan_suku

# ===================================================================
# PILIHAN SCENE 2
# ===================================================================

# --- A: BIJAK [+25] ---
label pilihan_pendekatan_a:

    scene bg_kampung_ayapo
    with dissolve

    show wira_terharu at wleft_small
    show garuda_berbicara at wright_small
    with dissolve

    wira "Aku akan mendatangi mereka satu per satu, Nek. Aku akan duduk, minum bersama mereka, dan mendengarkan apa yang sebenarnya membuat hati mereka sakit."

    garuda "Langkah yang lambat, tapi seringkali paling pasti, Wira."

    narrator "Wira duduk di berbagai rumah adat, minum kopi, mengangguk mendengarkan keluhan warga."

    wira "Saya mengerti, Bapak. Batas jaring itu memang penting untuk keluarga Bapak."

    narrator "Semua suku akhirnya merasa dihargai. Mereka setuju dengan ajakan Wira untuk berdamai. Perwakilan kelima suku berkumpul di tengah Danau Sentani dengan wajah penuh harapan."

    $ player_points += 25

    jump scene_barapen

# --- B: NETRAL [0] ---
label pilihan_pendekatan_b:

    scene bg_kampung_ayapo
    with dissolve

    show wira_bingung at wleft_small
    show garuda_berbicara at wright_small
    with dissolve

    wira "Aku akan sampaikan pesan saja ke ketua tiap suku. Sampaikan batas wilayah yang logis, beres. Tidak perlu repot mengurus drama mereka."

    garuda "Efisien. Tapi ingat, Wira, manusia bukan sekadar angka di atas peta."

    narrator "Wira membagikan pembagian wilayah secara cepat tanpa banyak bicara."

    wira "Ini batasnya. Jangan dilewati. Besok kumpul di tengah danau untuk tanda tangan kesepakatan adat."

    narrator "Semua suku setuju untuk berkumpul karena alasan praktis. Tapi pertemuan itu kaku, dingin, dan tidak menyambut perdamaian ini dengan hati."

    jump scene_barapen

# --- C: EGOIS [-25] ---
label pilihan_pendekatan_c:

    scene bg_kampung_ayapo
    with dissolve

    show wira_sinis at wleft_small
    show garuda_berbicara at wright_small
    with dissolve

    garuda "Wira! Kesombongan hanya akan membakar jembatan yang belum sempat kau bangun!"

    wira "Kalian ini bodoh sekali! Tinggal bagi saja daerah-daerah perairan di sini, apa susahnya?! Kumpul sekarang atau kalian semua rugi!"

    with hpunch

    narrator "Semua suku marah besar. Mereka merasa dilecehkan dan mengusir Wira secara bersama-sama."

    $ player_points -= 25

    jump ending_checkpoint_papua

# ===================================================================
# SCENE 3 BARAPEN
# ===================================================================

label scene_barapen:

    hide wira_terharu
    hide wira_bingung
    hide garuda_berbicara

    scene bg_barapen
    with fade

    narrator "Batu-batu panas membara. Asap mengepul. Kelima suku sudah duduk melingkar."

    show tetua_asei at wright_small
    show wira_bingung at wleft_small
    with dissolve

    garuda "Sekarang sudah saatnya mereka melakukan ritual perdamaian Barapen — bakar batu. Kamu di sini diminta untuk menjadi pemimpin upacaranya. Ini simbol penyatuan."

    wira "Tapi aku tidak tau caranya, Gar! Aku hanya diberi tahu sedikit tentang upacara ini!"

    garuda "Tenang saja, ikuti intuisimu — mereka akan mengarahkanmu lewat isyarat."

    Tetua_Asei "Nak Wira. Kamu yang menyatukan mereka. Sekarang kamu yang memimpin Barapen. Batu dari utara, selatan, timur, barat, tengah sudah siap. Doa sudah siap. Makanan sudah siap. Sekarang... bagaimana cara kamu memimpin?"

    hide tetua_asei
    hide wira_bingung

    call screen pilihan_barapen

# ===================================================================
# PILIHAN SCENE 3
# ===================================================================

# --- A: NETRAL [0] ---
label pilihan_barapen_a:

    scene bg_barapen
    with dissolve

    show wira_bingung at wleft_small
    with dissolve

    wira "Baiklah, tumpuk semua batunya di tengah sekalian, taruh daun dan dagingnya. Mari kita masak."

    narrator "Ritual berjalan biasa saja. Tidak ada yang salah, tapi tidak ada maknanya."

    narrator "Orang-orang makan dalam diam. Perdamaian secara tertulis tercapai, namun tidak ada suasana kekeluargaan. Dingin."

    jump scene_ukiran_asmat

# --- B: EGOIS [-25] ---
label pilihan_barapen_b:

    scene bg_barapen
    with dissolve

    show wira_sinis at wleft_small
    show tetua_asei at wright_small
    with dissolve

    wira "Ambil tiga batu saja, itu sudah cukup panas! Tidak usah repot-repot berdoa panjang lebar, kita semua lapar. Masukkan umbinya sekarang!"

    with hpunch

    Tetua_Asei "Ini penghinaan! Batu dari selatan kau buang, doa kau lupakan! Kau tidak menghargai roh nenek moyang kami!"

    narrator "Suku-suku kecewa berat. Beberapa ketua marah dan meninggalkan lapangan. Barapen dianggap tidak sah. Perdamaian hancur berantakan."

    $ player_points -= 25

    jump ending_checkpoint_papua

# --- C: BIJAK [+25] ---
label pilihan_barapen_c:

    scene bg_barapen
    with dissolve

    show wira_terharu at wleft_small
    show tetua_asei at wright_small
    with dissolve

    wira "Mari kita mulai dari batu Timur tempat matahari terbit, lalu memutar... dan terakhir batu Tengah, yang menyatukan kita semua di danau ini."

    narrator "Wira menyusunnya dengan penuh penghormatan."

    narrator "Asap membubung tinggi. Wajah para ketua suku berbinar."

    Tetua_Asei "Leluhur kita tersenyum hari ini. Kau menghormati arah, kau menghormati kehidupan."

    narrator "Para suku terharu. Mereka makan bersama sambil berbincang tentang masa lalu yang indah sebelum konflik. Suasana berubah menjadi tentram, hangat, dan bahagia."

    $ player_points += 25

    jump scene_ukiran_asmat

# ===================================================================
# SCENE 4
# ===================================================================

label scene_ukiran_asmat:

    hide wira_terharu
    hide wira_bingung
    hide wira_sinis
    hide tetua_asei

    scene bg_hutan_yoboi
    with fade

    show mama_tita at wright_small
    show wira_bingung at wleft_small
    with dissolve

    Mama_Tita "Kamu. Orang asing. Dari mana?"

    wira "Dari Danau Sentani, Mama. Aku Wira."

    Mama_Tita "Sentani? Jauh. Apa yang kamu cari di sini?"

    wira "Air Suci, Mama. Kami butuh air suci untuk menyempurnakan perdamaian di Sentani."

    Mama_Tita "Air Suci. Banyak yang cari. Tiga orang sebelum kamu. Dua gila. Satu mati. Kamu yakin mau coba?"

    wira "Aku yakin, Mama."

    Mama_Tita "Kalau kamu mau cari Air Suci... kamu harus pecahkan teka-teki ukiran ini dulu."

    narrator "Mama Tita mengulurkan sebatang kayu ukiran sepanjang lengan. Motifnya berlapis-lapis: binatang, manusia, lalu lingkaran kosong di ujungnya."

    Mama_Tita "Ukiran ini bicara. Tapi dia hanya bicara pada yang mau mendengar. Bukan dengan telinga... tapi dengan hati dan ingatan. Bawa ini. Pecahkan maknanya."

    hide mama_tita
    hide wira_bingung

    call screen pilihan_ukiran_asmat

# ===================================================================
# PILIHAN SCENE 4
# ===================================================================

# --- A: EGOIS [-25] ---
label pilihan_ukiran_a:

    scene bg_hutan_yoboi
    with dissolve

    show wira_sinis at wleft_small
    show mama_tita at wright_small
    with dissolve

    wira "Ini tidak masuk akal! Ukiran kayu kok disuruh bicara?! Katakan padaku di mana air sucinya, Mama! Jangan buang waktuku, atau aku akan menghancurkan ukiran kesayanganmu ini!"

    Mama_Tita "Orang sombong selalu menemukan jalannya sendiri menuju kehancuran."

    narrator "Mama Tita membawa Wira ke sebuah gua kecil yang gelap di kaki bukit, lalu meninggalkannya sendirian."

    scene bg_rawa_asmat
    with dissolve

    narrator "Mama Tita membawa Wira ke rawa gelap."

    scene bg_gua_air_suci
    with dissolve

    show garuda_berbicara at wright_small
    with dissolve

    narrator "Tangan Wira gemetar saat menciduk air. Air itu hitam pekat, kental, dan mengeluarkan asap berbau busuk."

    wira "Uhuk! Bau sekali, seperti darah dan bangkai ikan!"

    garuda "Wira, buang itu! Itu kutukan rawa mati! Jika dibawa kembali, ini akan membawa wabah penyakit bagi 5 suku di Danau Sentani!"

    $ player_points -= 25

    jump ending_checkpoint_papua

# --- B: BIJAK [+25] ---
label pilihan_ukiran_b:

    scene bg_hutan_yoboi
    with dissolve

    show wira_terharu at wleft_small
    with dissolve

    wira "Aku butuh waktu untuk memahami ini."

    narrator "Wira duduk bersila berjam-jam di bawah pohon besar. Dia menutup mata, mengusap permukaan ukiran kayu itu perlahan."

    wira "Binatang... manusia... bersatu. Tapi kenapa di ujungnya kosong? Kosong... tempat yang tidak ada di peta para suku Sentani."

    narrator "Wira mengingat semua pelajaran dari suku-suku di Sentani. Lalu dia sadar: lingkaran kosong itu mewakili Rawa Tanpa Nama di belakang desa lama — wilayah netral yang tak bertuan."

    narrator "Dia berlari ke sana, menyelam ke dasar rawa yang dingin, dan menemukan sebuah gua kristal tersembunyi."

    scene bg_rawa_asmat
    with dissolve

    narrator "Wira menemukan rawa tanpa nama."

    scene bg_gua_air_suci
    with dissolve

    show garuda_berbicara at wright_small
    with dissolve

    narrator "Wira keluar dari gua membawa botol bambu. Air di dalamnya memancarkan cahaya biru yang lembut dan jernih."

    garuda "Luar biasa, Wira! Auranya sangat murni!"

    narrator "Dengan air ini, perdamaian di Sentani akan abadi dan mengikat jiwa semua suku dalam harmoni."

    $ player_points += 25

    jump ending_checkpoint_papua

# --- C: NETRAL [0] ---
label pilihan_ukiran_c:

    scene bg_hutan_yoboi
    with dissolve

    show wira_bingung at wleft_small
    with dissolve

    wira "Aduh, aku paling tidak bisa teka-teki sastra begini."

    narrator "Wira keliling desa menanyai orang-orang yang lewat sambil membawa ukiran itu."

    wira "Permisi, Bapak tahu air suci? Ibu, pernah lihat simbol ini?"

    narrator "Wira tidak sabar duduk lama. Dia terus mencari jalan pintas. Akhirnya, saat dia lelah dan bersandar, dia terpeleset dan menemukan gua di balik air terjun kecil di pinggir desa."

    scene bg_gua_air_suci
    with dissolve

    show garuda_berbicara at wright_small
    with dissolve

    narrator "Wira keluar membawa air yang warnanya abu-abu keruh. Tidak ada cahaya."

    garuda "Wira... air apa ini? Mengapa rasanya hampa?"

    narrator "Air ini tidak suci. Jika digunakan, perdamaian di Sentani hanya akan bertahan seumur jagung sebelum perang pecah kembali."

    jump ending_checkpoint_papua

# ===================================================================
# ENDING
# ===================================================================

label ending_checkpoint_papua:

    hide wira_terharu
    hide wira_bingung
    hide wira_sinis
    hide garuda_berbicara
    hide mama_tita

    scene black
    with fade

    pause 1.0

    if player_points >= 65:

        scene ending_baik_papua
        with dissolve

        show garuda_berbicara at wcenter_small
        with dissolve

        garuda "Perdamaian lahir ketika seseorang mau mendengar dan menghormati tradisi."

    elif player_points >= 15:

        scene ending_netral_papua
        with dissolve

        show garuda_berbicara at wcenter_small
        with dissolve

        garuda "Perdamaian tercapai, tetapi belum sepenuhnya menyatu."

    else:

        scene ending_buruk_papua
        with dissolve

        show garuda_berbicara at wcenter_small
        with dissolve

        garuda "Kamu menghancurkan kepercayaan yang membutuhkan generasi untuk dibangun."

    narrator "Checkpoint 5 Selesai: Papua — Danau Sentani"
    narrator "Total poin akhir: [player_points]"

    return