# ===================================================================
# CHAPTER PAPUA - DANAU SENTANI
# Checkpoint 5
# ===================================================================
default player_points = 0

# ===================================================================
# KARAKTER
# ===================================================================

define Mama_Tita = Character("Mama Tita", who_color="#8B4513")
define Tetua_Asei = Character("Tetua Asei", who_color="#5C3317")
define Tetua_Asmat = Character("Tetua Asmat", who_color="#654321")
define Perempuan_Tua = Character("Perempuan Tua", who_color="#8B4513")
define Pemuda_Yoboi = Character("Pemuda Yoboi", who_color="#6B8E23")

# ===================================================================
# SPRITE KARAKTER
# ===================================================================

# WIRA
image wira_bingung = "wira dewasa bingung.png"
image wira_terharu = "wira dewasa terharu.png"
image wira_sinis = "wira dewasa sinis.png"

# GARUDA
image garuda_berdiri = "garuda_default.png"
image garuda_terbang = "garuda_terbang.png"
image garuda_berbicara = "garuda_berbicara.png"

# TETUA
image perempuan_tua = "perempuan_tua.png"
image mama_tita = "mama_tita.png"
image tetua_asei = "tetua_asei.png"
image tetua_asmat = "tetua_asmat.png"
image pemuda_yoboi = "pemuda_yoboi.png"

# ===================================================================
# BACKGROUND
# ===================================================================

image bg_danau_sentani = im.Scale("danau_sentani.png", 1920, 1080)
image bg_pulau_asei = im.Scale("pulau_asei.png", 1920, 1080)
image bg_kampung_ayapo = im.Scale("kampung_ayapo.png", 1920, 1080)
image bg_barapen = im.Scale("lapangan_barapen.png", 1920, 1080)
image bg_hutan_yoboi = im.Scale("hutan_yoboi.png", 1920, 1080)
image bg_rawa_asmat = im.Scale("sungai_rawa_asmat.png", 1920, 1080)
image bg_gua_air_suci = im.Scale("gua_air_suci.png", 1920, 1080)

# ===================================================================
# VISUAL PILIHAN
# ===================================================================

# SCENE 2
image pilihan2_a_idle = im.Scale("danau_sentani.png", 350, 220)
image pilihan2_a_hover = im.Scale("danau_sentani.png", 370, 240)

image pilihan2_b_idle = im.Scale("kampung_ayapo.png", 350, 220)
image pilihan2_b_hover = im.Scale("kampung_ayapo.png", 370, 240)

image pilihan2_c_idle = im.Scale("hutan_yoboi.png", 350, 220)
image pilihan2_c_hover = im.Scale("hutan_yoboi.png", 370, 240)

# SCENE 3
image pilihan3_a_idle = im.Scale("lapangan_barapen.png", 350, 220)
image pilihan3_a_hover = im.Scale("lapangan_barapen.png", 370, 240)

image pilihan3_b_idle = im.Scale("pulau_asei.png", 350, 220)
image pilihan3_b_hover = im.Scale("pulau_asei.png", 370, 240)

image pilihan3_c_idle = im.Scale("sungai_rawa_asmat.png", 350, 220)
image pilihan3_c_hover = im.Scale("sungai_rawa_asmat.png", 370, 240)

# SCENE 4
image pilihan4_a_idle = im.Scale("gua_air_suci.png", 350, 220)
image pilihan4_a_hover = im.Scale("gua_air_suci.png", 370, 240)

image pilihan4_b_idle = im.Scale("kampung_ayapo.png", 350, 220)
image pilihan4_b_hover = im.Scale("kampung_ayapo.png", 370, 240)

image pilihan4_c_idle = im.Scale("sungai_rawa_asmat.png", 350, 220)
image pilihan4_c_hover = im.Scale("sungai_rawa_asmat.png", 370, 240)

# ===================================================================
# ENDING
# ===================================================================

image ending_baik_papua = im.Scale("danau_sentani.png", 1920, 1080)
image ending_netral_papua = im.Scale("kampung_ayapo.png", 1920, 1080)
image ending_buruk_papua = im.Scale("sungai_rawa_asmat.png", 1920, 1080)

# ===================================================================
# SCREEN PILIHAN SCENE 2
# ===================================================================

screen pilihan_pendekatan_suku():

    modal True
    default hovered = None

    hbox:
        spacing 60
        xalign 0.5
        yalign 0.72

        # A
        vbox:
            spacing 10

            imagebutton:
                idle "pilihan2_a_idle"
                hover "pilihan2_a_hover"
                action Jump("pilihan_pendekatan_a")

            text "PILIHAN A\nDATANGI\nSATU PER SATU":
                xalign 0.5
                text_align 0.5
                size 24

        # B
        vbox:
            spacing 10

            imagebutton:
                idle "pilihan2_b_idle"
                hover "pilihan2_b_hover"
                action Jump("pilihan_pendekatan_b")

            text "PILIHAN B\nSAMPAIKAN\nPESAN":
                xalign 0.5
                text_align 0.5
                size 24

        # C
        vbox:
            spacing 10

            imagebutton:
                idle "pilihan2_c_idle"
                hover "pilihan2_c_hover"
                action Jump("pilihan_pendekatan_c")

            text "PILIHAN C\nPAKSA\nBERHENTI":
                xalign 0.5
                text_align 0.5
                size 24

# ===================================================================
# SCREEN PILIHAN SCENE 3
# ===================================================================

screen pilihan_barapen():

    modal True

    hbox:
        spacing 60
        xalign 0.5
        yalign 0.72

        # A
        vbox:
            spacing 10

            imagebutton:
                idle "pilihan3_a_idle"
                hover "pilihan3_a_hover"
                action Jump("pilihan_barapen_a")

            text "PILIHAN A\nIKUTI\nADAT":
                xalign 0.5
                text_align 0.5
                size 24

        # B
        vbox:
            spacing 10

            imagebutton:
                idle "pilihan3_b_idle"
                hover "pilihan3_b_hover"
                action Jump("pilihan_barapen_b")

            text "PILIHAN B\nTUMPUK\nSEMUA":
                xalign 0.5
                text_align 0.5
                size 24

        # C
        vbox:
            spacing 10

            imagebutton:
                idle "pilihan3_c_idle"
                hover "pilihan3_c_hover"
                action Jump("pilihan_barapen_c")

            text "PILIHAN C\nTIGA BATU\nSAJA":
                xalign 0.5
                text_align 0.5
                size 24

# ===================================================================
# SCREEN PILIHAN SCENE 4
# ===================================================================

screen pilihan_ukiran_asmat():

    modal True

    hbox:
        spacing 60
        xalign 0.5
        yalign 0.72

        # A
        vbox:
            spacing 10

            imagebutton:
                idle "pilihan4_a_idle"
                hover "pilihan4_a_hover"
                action Jump("pilihan_ukiran_a")

            text "PILIHAN A\nRENUNGI\nUKIRAN":
                xalign 0.5
                text_align 0.5
                size 24

        # B
        vbox:
            spacing 10

            imagebutton:
                idle "pilihan4_b_idle"
                hover "pilihan4_b_hover"
                action Jump("pilihan_ukiran_b")

            text "PILIHAN B\nTANYA\nWARGA":
                xalign 0.5
                text_align 0.5
                size 24

        # C
        vbox:
            spacing 10

            imagebutton:
                idle "pilihan4_c_idle"
                hover "pilihan4_c_hover"
                action Jump("pilihan_ukiran_c")

            text "PILIHAN C\nPAKSA\nTETUA":
                xalign 0.5
                text_align 0.5
                size 24

# ===================================================================
# LABEL UTAMA
# ===================================================================

label chapter_papua:

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

    call screen pilihan_pendekatan_suku

# ===================================================================
# PILIHAN SCENE 2
# ===================================================================

label pilihan_pendekatan_a:

    scene bg_kampung_ayapo
    with dissolve

    show wira_terharu at wleft_small
    show garuda_berbicara at wright_small

    wira "Aku akan mendatangi mereka satu per satu, Nek."

    garuda "Langkah yang lambat, tapi seringkali paling pasti, Wira."

    narrator "Wira duduk bersama tiap suku dan mendengarkan semua keluhan mereka."

    narrator "Semua suku akhirnya merasa dihargai."

    $ player_points += 25

    jump scene_barapen

label pilihan_pendekatan_b:

    scene bg_kampung_ayapo
    with dissolve

    show wira_bingung at wleft_small
    show garuda_berbicara at wright_small

    wira "Aku akan sampaikan pesan saja ke ketua tiap suku."

    garuda "Efisien. Tapi manusia bukan sekadar angka di atas peta."

    narrator "Pertemuan berlangsung dingin dan tanpa kehangatan."

    jump scene_barapen

label pilihan_pendekatan_c:

    scene bg_kampung_ayapo
    with dissolve

    show wira_sinis at wleft_small
    show garuda_berbicara at wright_small

    garuda "Wira! Kesombongan hanya akan membakar jembatan!"

    wira "Kalian ini bodoh sekali!"

    with hpunch

    narrator "Wira diusir dari kampung setelah memaksa para suku."

    $ player_points -= 25

    jump ending_checkpoint_papua

# ===================================================================
# SCENE 3 BARAPEN
# ===================================================================

label scene_barapen:

    scene bg_barapen
    with fade

    narrator "Batu-batu panas membara. Kelima suku duduk melingkar."

    show tetua_asei at wright_small
    show wira_bingung at wleft_small

    garuda "Sekarang sudah saatnya ritual Barapen."

    wira "Tapi aku tidak tau caranya, Gar!"

    Tetua_Asei "Sekarang kamu yang memimpin."

    call screen pilihan_barapen

# ===================================================================
# PILIHAN BARAPEN
# ===================================================================

label pilihan_barapen_a:

    scene bg_barapen
    with dissolve

    show wira_terharu at wleft_small

    wira "Mari kita mulai dari batu Timur."

    narrator "Ritual berjalan penuh penghormatan."

    show tetua_asei at wright_small

    Tetua_Asei "Leluhur kita tersenyum hari ini."

    $ player_points += 25

    jump scene_ukiran_asmat

label pilihan_barapen_b:

    scene bg_barapen
    with dissolve

    show wira_bingung at wleft_small

    wira "Tumpuk semua batunya di tengah."

    narrator "Ritual berjalan biasa saja tanpa makna mendalam."

    jump scene_ukiran_asmat

label pilihan_barapen_c:

    scene bg_barapen
    with dissolve

    show wira_sinis at wleft_small

    wira "Ambil tiga batu saja!"

    with hpunch

    show tetua_asei at wright_small

    Tetua_Asei "Ini penghinaan!"

    narrator "Perdamaian gagal total."

    $ player_points -= 25

    jump ending_checkpoint_papua

# ===================================================================
# SCENE 4
# ===================================================================

label scene_ukiran_asmat:

    scene bg_hutan_yoboi
    with fade

    show mama_tita at wright_small
    show wira_bingung at wleft_small

    Mama_Tita "Kamu. Orang asing. Dari mana?"

    wira "Dari Danau Sentani, Mama."

    Mama_Tita "Kalau kamu mau cari Air Suci, pecahkan teka-teki ukiran ini."

    call screen pilihan_ukiran_asmat

# ===================================================================
# PILIHAN UKIRAN
# ===================================================================

label pilihan_ukiran_a:

    scene bg_hutan_yoboi
    with dissolve

    show wira_terharu at wleft_small

    narrator "Wira merenungkan makna ukiran itu selama berjam-jam."

    scene bg_rawa_asmat
    with dissolve

    narrator "Dia menemukan rawa tanpa nama."

    scene bg_gua_air_suci
    with dissolve

    show garuda_berbicara at wright_small

    garuda "Auranya sangat murni!"

    narrator "Wira mendapatkan air suci bercahaya."

    $ player_points += 25

    jump ending_checkpoint_papua

label pilihan_ukiran_b:

    scene bg_hutan_yoboi
    with dissolve

    show wira_bingung at wleft_small

    narrator "Wira mencari jawaban dengan bertanya pada warga."

    scene bg_gua_air_suci
    with dissolve

    show garuda_berbicara at wright_small

    garuda "Mengapa air ini terasa hampa?"

    narrator "Air yang ditemukan keruh dan tidak suci."

    jump ending_checkpoint_papua

label pilihan_ukiran_c:

    scene bg_hutan_yoboi
    with dissolve

    show wira_sinis at wleft_small
    show mama_tita at wright_small

    wira "Katakan padaku di mana air sucinya!"

    Mama_Tita "Orang sombong selalu menuju kehancuran."

    scene bg_rawa_asmat
    with dissolve

    narrator "Mama Tita membawa Wira ke rawa gelap."

    scene bg_gua_air_suci
    with dissolve

    show garuda_berbicara at wright_small

    garuda "Itu kutukan rawa mati!"

    narrator "Air yang ditemukan hitam dan berbau busuk."

    $ player_points -= 25

    jump ending_checkpoint_papua

# ===================================================================
# ENDING
# ===================================================================

label ending_checkpoint_papua:

    scene black
    with fade

    pause 1.0

    if player_points >= 65:

        scene ending_baik_papua
        with dissolve

        show garuda_berbicara at wcenter_small

        garuda "Perdamaian lahir ketika seseorang mau mendengar dan menghormati tradisi."

    elif player_points >= 15:

        scene ending_netral_papua
        with dissolve

        show garuda_berbicara at wcenter_small

        garuda "Perdamaian tercapai, tetapi belum sepenuhnya menyatu."

    else:

        scene ending_buruk_papua
        with dissolve

        show garuda_berbicara at wcenter_small

        garuda "Kamu menghancurkan kepercayaan yang membutuhkan generasi untuk dibangun."

    narrator "Checkpoint 5 Selesai: Papua — Danau Sentani"
    narrator "Total poin akhir: [player_points]"

    return