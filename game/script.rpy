# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define narrator =  Character("???", who_color = "#000000")
define wira = Character("Wira", who_color = "#ffffff")
define ibu = Character("Ibu", who_color = "#ffacc2")
define ayah = Character("Ayah", who_color = "#b5e5ff")
define garuda = Character("Garuda", who_color = "#ffd978")
define narasi = Character(None, what_italic = True)

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

    # TODO NEXT: Lanjutkan ke label checkpoint Minangkabau jika sudah dibuat.
    # jump checkpoint_minangkabau


    # This ends the game.

    return
