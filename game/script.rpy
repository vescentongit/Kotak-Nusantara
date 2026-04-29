# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define wira = Character("Wira", who_color = "#ffffff")
define narrator =  Character("???", who_color = "#000000")



# PROLOG / TERAS PAGI
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

# PROLOG / TAMAN KOTA SORE
image taman = im.Scale("prolog_taman_kota_sore.png", 1920, 1080)


label start:

    scene bg_prolog_teras_pagi
    show pipit standing at pipit_initial
    with fade

    narrator "Pada suatu hari..."

    show wira_ceria at wleft_small
    with dissolve 

    # These display lines of dialogue.
    wira "Wah... hari ini cerah sekali ya!"

    window hide
    show wira_ceria at teras
    with ease   
    pause 0.5
    window show

    wira "Pipit... lihat deh. Matahari pagi ini bagus banget, kan?"

    window hide

    pause 0.3
    show pipit terbang at pipit_initial with dissolve
    pause 0.5

    scene bg_prolog_teras_pagi
    show wiranpipit at teras
    with dissolve
    window show

    narrator "Wira Terkekeh geli, matanya semakin berbinar"
    wira "Ih, geli! Kamu suka ya aku elus elus?"
    narrator "Bagi WIRA, dunia luar penuh dengan suara bising dan kebingungan. Namun, di teras ini, bersama Pipit... semuanya terasa benar."

    window hide
    show wiranpipit serius at teras
    with dissolve
    pause 0.5
    window show

    wira "Pipit... kalau nanti sayapmu sudah kuat... kalau kamu sudah bisa terbang jauh sampai ke awan..."

    window hide
    show wiranpipit nunduk at terasnew
    with dissolve
    pause 1.5
    show wiranpipit terharu at teras
    with dissolve
    pause 1.5
    window show

    wira "...jangan tinggalin aku ya? Janji?"

    narrator "Di teras rumah itu, WIRA Kecil mengunci separuh hatinya pada seekor burung peliharaan, menjadikannya satu satunya dunia kecil yang dia miliki."
    
    window hide

    scene taman
    with dissolve

    narrator "prolog 2....... "

    # This ends the game.

    return
