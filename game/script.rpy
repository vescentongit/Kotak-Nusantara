# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator =  Character("???", who_color = "#000000")
define wira = Character("Wira", who_color = "#ffffff")
define ibu = Character("Ibu", who_color = "#ffacc2")
define ayah = Character("Ayah", who_color = "#b5e5ff")

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

    scene kamarwira
    with dissolve

    show wira sinis at chara_wira_sinis
    narrator "(Telepon berdering)"
    show wira bingung at chara_wira_sinis
    with dissolve
    wira "Halo?"
    ibu "Wira, besok kamu ke desa Nenek ya. Sudah Ibu siapkan semuanya."
    # wira "(Mendengus)"
    show wira sinis at chara_wira_sinis
    with dissolve
    wira "Ma, aku bukan anak kecil lagi yang bisa disuruh suruh ke desa nggak jelas gitu. Males."
    
    ayah "Wira! Turuti kata Ibu! Kamu terlalu banyak membuang waktu dengan hal hal nggak berguna di sana."
    ayah "Kalau besok kamu tidak berangkat, Papa potong uang jajan dan sita semua peralatan game mu!"
    show wira bingung at chara_wira_sinis
    # wira "(Mengepalkan tangan, ekspresi kesal)"
    wira "Apa-apaan sih? Kok jadi ngancem gitu?!"
    ibu "Ini untuk kebaikanmu, Sayang. Besok berangkat ya. Dadah!"
    # wira "(Membanting HP ke kasur)"
    wira "Males deh, selalu aja kayak gini."


    # This ends the game.

    return
