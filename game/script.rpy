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
define nenek = Character("Nenek", who_color = "#ffffff")
define rena = Character("Rena", who_color = "#ffffff")
define Datuak = Character("Datuak",who_color ="#9E7B54" )
define Buya_Hamid = Character("Buya Hamid",who_color ="#224989" )
define Dr_Sari = Character("Dr Sari",who_color ="#961A2E" )
define Rosma = Character("Ibu Rosma",who_color ="#23781E" )
define Amelia = Character("Amelia",who_color ="#FF69B4" )
define Rizky = Character("Rizky",who_color ="#881e1e" )

# CHAPTER JAWA BETAWI
define Bang_Rojak = Character("Bang Rojak",who_color ="#D4A574" )
define Sari = Character("Sari",who_color ="#6B4E9D" )
define Engkong_Ali = Character("Engkong Ali",who_color ="#8B7355" )
define Pak_Sugeng = Character("Pak Sugeng",who_color ="#A0522D" )
define Kanjeng_Raden = Character("Kanjeng Raden",who_color ="#D4AF37" )
define Raden_Mas_Bagas = Character("Raden Mas Bagas",who_color ="#8B4513" )
define Dimas = Character("Dimas",who_color ="#4A4A4A" )
define Teman_Dimas = Character("Teman Dimas",who_color ="#b00404" )

# ================= SISTEM POIN =================
default player_points = 0

image black = "black-bg.jpg"

init python:
    def glow_hover(img):
        return im.MatrixColor(img, im.matrix.brightness(0.3) * im.matrix.saturation(1.1))

    renpy.music.register_channel("ambient", "sfx", loop=True)
    renpy.music.register_channel("clock", "sfx", loop=True)
    renpy.music.register_channel("bird", "sfx", loop=True)
    renpy.music.register_channel("sfx1", "sfx", loop=True)
    renpy.music.register_channel("sfx2", "sfx", loop=False)
    renpy.music.register_channel("sfx3", "sfx", loop=True)

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
image wira sedih = "wira_sedih.png"


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


# DAERAH 1 : MINANGKABAU
label minangkabau_intro:
    #minangkabau

    play music "sound/talempongminang1.MP3" fadein 1.0 loop
    play ambient "sound/aliran air.mp3" fadein 1.0 loop

    scene black
    scene rumah_gadang
    with dissolve

    show wira_bingung at wleft_small
    with dissolve

    wira " Itu..rumahnya kok atapnya kayak tanduk kerbau gitu? "
    wira "Bangunannya gede banget! Tapi kelihatannya udah lama nggak dirawat."

    window hide
    play sound "sound/Flapping Wing SFX.mp3"
    show garuda_berdiri at wright_small
    with dissolve
    pause 0.5
    window show
    hide wira_bingung

    garuda "Selamat datang di Nagari Minangkabau, Wira!"
    hide garuda_berdiri

    show wira_bingung at wleft_small
    with dissolve
    wira "Nagari? Ini semacam desa ya?"
    hide wira_bingung

    show garuda_berbicara_minang at wright_small

    garuda "Lebih dari itu. Nagari adalah unit kehidupan masyarakat Minangkabau. "
    garuda "Tempat adat dijalankan, keputusan diambil bersama, dan identitas dijaga turun temurun "
    garuda "Rumah Gadang yang kamu lihat itu ... adalah jantungnya."
    hide garuda_berbicara_minang
    show wira_tunjuk at wleft_small
    with dissolve

    wira "Jantungnya? Kelihatan sudah mau roboh di sudut sana."
    hide wira_tunjuk

    show garuda_ceria at wcenter_small

    garuda "Tepat sekali! Itulah kenapa kamu ada di sini."

    #Penjelasan MISI oleh Garuda
    image bg_misi = im.Scale("dalam_gadang.png", 1920, 1080)
    image peta_penuh = "peta_penuh.png"
    image misi_balaiadat = "balai_adat_only.png"
    image misi_rumahgadang = "rumah_gadang_only.png"
    image misi_pasar = "pasar_only.png"

    window hide

    scene black
    scene bg_misi
    with dissolve
    window show
    show garuda_berbicara_minang at wright_small

    garuda "Inilah misimu di Minangkaubau, Wira. Nagari ini sedang di persimpangan. Terdapat tiga krisis yang harus kamu hadapi."
    hide garuda_berbicara_minang
    show wira_bingung at wleft_small
    with dissolve
    wira "Tiga?"
    window hide
    hide wira_bingung

    show misi_balaiadat at wcenter_small
    with dissolve
    pause 0.5
    window show
    garuda "Pertama"
    garuda "forum musyawarah adat hampir lumpuh karena para tokoh tidak bisa mencapai kata sepakat."

    hide misi_balaiadat
    show misi_rumahgadang at wcenter_small
    with dissolve
    pause 0.5
    garuda "Kedua"
    garuda "Rumah Gadang warisan leluhur terancam diubah tampilannya tanpa pertimbangan adat."

    hide misi_rumahgadang
    show misi_pasar at wcenter_small
    with dissolve
    pause 0.5
    garuda "Ketiga"
    garuda "ada tawaran bisnis menggiurkan yang berbenturan keras dengan nilai adat dan agama."

    hide misi_pasar
    show garuda_berbicara_minang at wcenter_small
    with dissolve
    pause 0.5
    garuda " Ingat "
    garuda "Setiap pilihanmu akan mencerminkan siapa dirimu sebenarnya."
    window hide

    image forum = im.Scale("forum.png", 1920, 1080)
    image forum2 = im.Scale("forum_2.png", 1920, 1080)
    image forum3 = im.Scale("forum_3.png", 1920, 1080)
    image forum4 = im.Scale("forum_4.png", 1920, 1080)
    image forum5 = im.Scale("forum_5.png", 1920, 1080)
    image bingungsemua = im.Scale("forum_bingung.png", 1920, 1080)
    image bg_balai = im.Scale("bg_balai.png",1920,1080)
    image pilihan_a = im.Scale("pilihan_a.png",1920,1080)
    image pilihan_b = im.Scale("pilihan_b.png",1920,1080)
    image pilihan_c = im.Scale("pilihan_c.png",1920,1080)
    image saling_kecewa = im.Scale("saling_kecewa.png",1920,1080)

    # ASET RUMAH GADANG - OPENING DAN PILIHAN
    image openingscene_rumahgadang = im.Scale("openingscene_rumahgadang.png",1920,1080)
    image aset_pilihana_rumahgadang = im.Scale("aset_pilihana_rumahgadang.png",1920,1080)
    image aset_pilihanb_rumahgadang = im.Scale("aset_pilihanb_rumahgadang.png",1920,1080)
    image aset_pilihanc_rumahgadang = im.Scale("aset_pilihanc_rumahgadang.png",1920,1080)

    # ASET PASAR - OPENING DAN PILIHAN
    image visual_awal_scenepasar = im.Scale("visual_awal_scenepasar.png",1920,1080)
    image percakapan_awal_scenepasar = im.Scale("percakapan_awal_scenepasar.png",1920,1080)
    image perdebatanpanas_pasar = im.Scale("perdebatanpanas_pasar.png",1920,1080)
    image visual_semuatertujukewira = im.Scale("visual_semuatertujukewira.png",1920,1080)
    image pasar_only = im.Scale("pasar_only.png",1920,1080)
    image pasar_a_solved = im.Scale("pasar_a_solved.png",1920,1080)
    image pasar_c_solved = im.Scale("pasar_c_solved.png",1920,1080)
    image rosma_khawatir = im.Scale("rosma_khawatir.png",1920,1080)
    image percakapan_awal_rumahgadang = im.Scale("percakapan_awal_rumahgadang.png",1920,1080)
    image rumahgadang_c_solved = im.Scale("rumahgadang_c_solved.png",1920,1080)
    image poin_rendah = im.Scale("poin_rendah.png",1920,1080)
    image poin_sedang = im.Scale("poin_sedang.png",1920,1080)
    image poin_tinggi = im.Scale("poin_tinggi.png",1920,1080)
    stop ambient fadeout 1.0
    play sound "sound/langkahkayu.mp3"
    play ambient "sound/berdebat.MP3" fadein 0.8 loop
    scene forum
    with dissolve
    window show
    garuda "Perkenalkan empat pilar nagari."
    garuda "Datuak Rajo Nan Sati, Niniak Mamak, penjaga garis keturunan dan hukum adat."
    garuda "Buya Hamid, Alim Ulama, penjaga syariat Islam dalam kehidupan masyarakat."
    garuda "Dr. Sari Rahmawati, Cadiak Pandai, kaum intelektual yang membawa pengetahuan dunia luar."
    garuda "Ibu Rosma, Bundo Kanduang, simbol kebijaksanaan perempuan dalam nagari."

    wira "Kok mereka kelihatan kayak mau berantem?"

    garuda " Karena mereka sedang berselisih soal satu keputusan besar dan suara mereka tidak bulat."


    scene forum2
    with dissolve
    Datuak "Adat basandi syarak, syarak basandi Kitabullah! Segala keputusan harus lewat tangan kami, Niniak Mamak."
    Datuak "Kami yang menjaga pusaka, kami yang menentukan arah nagari!"

    scene forum3
    with dissolve
    Buya_Hamid "Benar bahwa adat bersumber pada agama. Tapi keputusan yang menyimpang dari nilai Islam tidak bisa dibenarkan hanya karena itu keputusan Niniak Mamak. Agama adalah fondasi, bukan pelengkap."

    scene forum4
    with dissolve
    Dr_Sari "Saya setuju bahwa kita harus menjaga nilai. Tapi data menunjukkan bahwa nagari yang tidak bisa beradaptasi dengan perubahan ekonomi akan ditinggal generasi mudanya. Kita tidak bisa menutup mata terhadap realita."

    scene forum5
    with dissolve
    Rosma "Anak anak kita yang pergi merantau, mereka akan pulang jika nagari ini punya jiwa. Tanpa keselarasan antara adat, agama, dan ilmu, nagari ini hanya kulit tanpa isi."
    window hide
    stop ambient fadeout 1.0
    scene bingungsemua
    with dissolve
    window show
    Datuak " Siapa anak muda ini? "

    garuda "Ia adalah tamu nagari yang sedang dalam perjalanan belajar. Izinkan ia mendengarkan forum ini."

    #pilihan
    screen pilihan_sirih():

        modal True

        default hovered = None

        hbox:
            spacing 80
            xalign 0.5
            yalign 0.75

            # ================= A =================
            vbox:
                xalign 0.5
                spacing 10
                imagebutton:
                    idle "sirih1_idle.png"
                    hover "sirih1_hover.png"
                    action Jump("pilihan_a")
                    hovered SetScreenVariable("hovered", "A")
                    unhovered SetScreenVariable("hovered", None)
                text "PILIHAN A\nMENDENGARKAN\nSEMUA UNSUR":
                    xalign 0.5
                    size 22
                    text_align 0.5

            # ================= B =================
            vbox:
                xalign 0.5
                spacing 10
                imagebutton:
                    idle "sirih2_idle.png"
                    hover "sirih2_hover.png"
                    action Jump("pilihan_b")
                    hovered SetScreenVariable("hovered", "B")
                    unhovered SetScreenVariable("hovered", None)
                text "PILIHAN B\nHANYA\nTETUA":
                    xalign 0.5
                    size 22
                    text_align 0.5

            # ================= C =================
            vbox:
                xalign 0.5
                spacing 10
                imagebutton:
                    idle "sirih3_idle.png"
                    hover "sirih3_hover.png"
                    action Jump("pilihan_c")
                    hovered SetScreenVariable("hovered", "C")
                    unhovered SetScreenVariable("hovered", None)
                text "PILIHAN C\nMENGABAIKAN\nFORUM":
                    xalign 0.5
                    size 22
                    text_align 0.5

    # ================= SCREEN POIN =================
    screen show_points():
        vbox:
            xalign 0.95
            yalign 0.05
            spacing 10

            text "POIN: [player_points]":
                size 28
                color "#FFD700"
                text_align 1.0

    # ================= SCREEN PILIHAN RUMAH GADANG =================
    screen pilihan_rumahgadang():

        modal True

        default hovered = None

        hbox:
            spacing 80
            xalign 0.5
            yalign 0.75

            # ================= A =================
            vbox:
                xalign 0.5
                spacing 10
                imagebutton:
                    idle "rumahgadang_a_idle.png"
                    hover "rumahgadang_a_hover.png"
                    action Jump("pilihan_rumahgadang_a")
                    hovered SetScreenVariable("hovered", "A")
                    unhovered SetScreenVariable("hovered", None)
                text "PILIHAN A":
                    xalign 0.5
                    size 22
                    text_align 0.5

            # ================= B =================
            vbox:
                xalign 0.5
                spacing 10
                imagebutton:
                    idle "rumahgadang_b_idle.png"
                    hover "rumahgadang_b_hover.png"
                    action Jump("pilihan_rumahgadang_b")
                    hovered SetScreenVariable("hovered", "B")
                    unhovered SetScreenVariable("hovered", None)
                text "PILIHAN B":
                    xalign 0.5
                    size 22
                    text_align 0.5

            # ================= C =================
            vbox:
                xalign 0.5
                spacing 10
                imagebutton:
                    idle "rumahgadang_c_idle.png"
                    hover "rumahgadang_c_hover.png"
                    action Jump("pilihan_rumahgadang_c")
                    hovered SetScreenVariable("hovered", "C")
                    unhovered SetScreenVariable("hovered", None)
                text "PILIHAN C":
                    xalign 0.5
                    size 22
                    text_align 0.5

    show bg_balai
    show screen show_points
    window hide
    call screen pilihan_sirih

    # PILIHAN A - MENDENGARKAN SEMUA UNSUR

label pilihan_a:
    scene pilihan_a
    with dissolve
    window show
    
    narrator "Wira duduk tenang di sudut ruangan, mendengarkan satu per satu pendapat semua tokoh dengan seksama, tidak menyela, dan mencatat dalam ingatannya sebelum mengambil kesimpulan apa pun."
    
    pause 1.0

    scene forum2
    with dissolve
    Datuak "Anak muda ini .... Ia mendengar dengan benar."


    pause 0.5
    scene forum5
    with dissolve
    Rosma "Mendengarkan semua suara sebelum berbicara.. Itu kebijaksanaan."

    pause 0.5
    scene black
    with dissolve
    show garuda_berbicara_minang at wcenter_small
    with dissolve
    garuda "Kamu baru saja memahami inti dari musyawarah mufakat. Kebenaran tidak dimiliki satu pihak saja. Ia lahir dari pertemuan berbagai sudut pandang."

    window hide
    pause 1.0
    window show

    $ player_points += 20
    hide garuda_berbicara_minang
    narrator "Anda mendapat 20 poin! Total poin: [player_points]"

    jump scene_rumahgadang_krisis

    # PILIHAN B - HANYA MENDENGARKAN TETUA
label pilihan_b:
    scene pilihan_b
    with dissolve
    window show

    narrator "Wira fokus pada perkataan Datuak Rajo Nan Sati saja karena dianggap paling senior, mengabaikan pendapat tokoh lainnya."

    pause 1.0

    pause 1.0
    window hide
    scene bingungsemua
    with dissolve
    window show

    narrator "Buya Hamid, Dr. Sari, dan Ibu Rosma menyadari Wira hanya memperhatikan Datuak. Ketiganya saling berpandangan dengan ekspresi kecewa."

    pause 0.5
    scene saling_kecewa
    with dissolve
    Dr_Sari "Sayangnya, generasi muda masih berpikir bahwa usia yang menentukan kebenaran."

    pause 0.5
    scene black
    with dissolve
    show garuda_berbicara_minang at wcenter_small
    with dissolve
    garuda "Adat Minangkabau bukan hierarki buta, Wira. Ia adalah harmoni. Ketika kamu memilih untuk hanya mendengar satu suara, kamu merusak keseimbangan yang dibangun berabad abad."
    
    window hide
    pause 1.0
    window show

    $ player_points -= 10
    narrator "Anda kehilangan 10 poin! Total poin: [player_points]"

    jump scene_rumahgadang_krisis

    # PILIHAN C - MENGABAIKAN FORUM
label pilihan_c:
    scene pilihan_c
    with dissolve
    window show

    narrator "Wira merasa forum ini membosankan , ia berdiri di sudut sambil bermain main memperhatikan ukiran dinding."
    narrator "Suasana forum semakin tegang. Semua tokoh semakin keras mempertahankan posisinya."
    pause 1.0
    window hide
    scene bingungsemua
    with dissolve
    window show

    Datuak "Anak muda ini... tidak menghargai musyawarah adat kami!"
    Buya_Hamid "Ia bahkan tidak mencoba memahami kompleksitas masalah ini!"

    scene black
    show garuda_berbicara_minang at wcenter_small
    with dissolve
    garuda "Wira....Kehadiranmu di ruangan ini punya arti. Ketika kamu memilih untuk tidak hadir sepenuhnya, kamu membiarkan konflik tumbuh tanpa ada yang mau memahami semua sisi."
    
    window hide
    pause 1.0
    window show

    $ player_points -= 20
    narrator "Anda kehilangan 20 poin! Total poin: [player_points]"

    jump scene_rumahgadang_krisis


label scene_rumahgadang_krisis:
    scene black
    with fade

    window hide
    pause 1.0

    play sound "sound/langkahtanah.mp3"
    play ambient "sound/angin.mp3" fadein 1.0 loop
    scene openingscene_rumahgadang
    with dissolve
    window show
    
   
    play music "sound/langkahtanah.mp3" fadein 1.0 loop
    play sound "sound/angin.mp3" fadein 1.0 loop
    Amelia "Pak Rizky, saya setuju dindingnya harus diperbaiki. Tapi saya rasa kita bisa sekalian renovasi total. Tambah kaca panoramik di sisi timuR, ganti material atap dengan bahan modern yang lebih tahan lama, dan buat interior yang lebih minimalis." 
    Amelia "Lebih estetik dan fungsional!"
    stop music fadeout 1.0
    stop sound fadeout 1.0
    Rizky "Secara teknis bisa dan lebih efisien biayanya dibanding restorasi ukiran lama satu per satu."
    pause 1.0

    scene rosma_khawatir
    with dissolve

    window show

    Rosma "Amelia...yang kamu bicarakan itu bukan renovasi. Itu penggantian jiwa rumah ini."

    scene percakapan_awal_rumahgadang
    Amelia "Tapi bu, struktur bangunannya sudah tidak aman! Kalau tidak diperbaiki sekarang, bisa roboh. Lebih baik diperbarui daripada dibiarkan rusak."
    Rosma "Setiap ukiran di dinding itu punya nama. Punya cerita. Kalau diganti dengan kaca dan beton, yang tersisa hanya bentuknya saja. Bukan Rohnya."
    garuda "Rumah Gadang bukan sekadar bangunan, Wira. Ia adalah silsilah keluarga yang tertulis dalam kayu." 
    garuda "Setiap ruangan mencerminkan posisi perempuan sebagai pemegang harta pusaka."
    garuda "Setiap ukiran adalah bahasa yang berbicara tentang falsafah hidup."
    wira "Tapi kalau memang sudah mau roboh...?"
    garuda "Tepat sekali pertanyaannya. Di sinilah keputusanmu diuji"

    pause 1.0

    # ================= PILIHAN RUMAH GADANG =================
    show openingscene_rumahgadang
    show screen show_points
    window hide
    call screen pilihan_rumahgadang

    # PILIHAN RUMAH GADANG A
label pilihan_rumahgadang_a:
    scene aset_pilihana_rumahgadang
    with dissolve
    window show

    narrator "Wira memilih untuk mempertahankan struktur asli Rumah Gadang sambil melakukan restorasi yang menghormati tradisi."

    pause 1.0

    Rosma "Anak ini...mengerti bahwa warisan buka beban. Warisan adalah identitas."
    Amelia "Mungkin, saya terlalu fokus pada yang rusak, sampai lupa apa yang masih utuh dan berharga. Baiklah, kita cari ahli restorasi."
    garuda "Kamu baru saja memahami bahwa menjaga identitas budaya bukan berarti menolak perubahan. Ini berarti memastikan perubahan tidak menghapus siapa kita."
    
    window hide
    pause 1.0
    window show

    $ player_points += 25
    narrator "Anda mendapat 25 poin! Total poin: [player_points]"

    jump scene_pasar_krisis

    # PILIHAN RUMAH GADANG B
label pilihan_rumahgadang_b:
    scene aset_pilihanb_rumahgadang
    with dissolve
    window show

    wira "Mungkin bisa diambil jalan tengah? Bagian yang lapuk diganti material modern, tetapi ukirannya tetap dipertahankan. Jadi lebih aman tetapi masih ada nuansa tradisionalnya."
    garuda "Niatmu baik, Wira. Tapi jalan tengah yang tidak dipikirkan matang bisa menjadi solusi yang tidak memuaskan semua pihak. Warisan budaya butuh perlindungan penuh, bukan kompromi setengah hati"
    
    window hide
    pause 1.0
    window show

    $ player_points += 10
    narrator "Anda mendapat 10 poin! Total poin: [player_points]"

    jump scene_pasar_krisis

    # PILIHAN RUMAH GADANG C
label pilihan_rumahgadang_c:
    scene aset_pilihanc_rumahgadang
    with dissolve
    window show

    wira "Saya setuju dengan Amelia. Yang penting bangunannya aman dan fungsional. Bentuknya bisa disesuaikan dengan kebutuhan zaman."

    pause 1.0
    scene rumahgadang_c_solved
    garuda "Wira...kamu baru saja memilih kenyamanan sesaat. Ketika Rumah Gadang kehilangan ukirannya, generasi berikutnya tidak akan tahu dari mana mereka berasa"

    window hide
    pause 1.0
    window show

    $ player_points -= 25
    narrator "Anda kehilangan 25 poin! Total poin: [player_points]"

    jump scene_pasar_krisis

    # ================= SCREEN PILIHAN PASAR =================
    screen pilihan_pasar():

        modal True

        default hovered = None

        hbox:
            spacing 60
            xalign 0.5
            yalign 0.5

            # ================= A =================
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 15
                imagebutton:
                    idle "pasar_a_idle"
                    hover "pasar_a_hover"
                    action Jump("pilihan_pasar_a")
                    hovered SetScreenVariable("hovered", "A")
                    unhovered SetScreenVariable("hovered", None)
                text "PILIHAN A":
                    xalign 0.5
                    size 20

            # ================= B =================
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 15
                imagebutton:
                    idle "pasar_b_idle"
                    hover "pasar_b_hover"
                    action Jump("pilihan_pasar_b")
                    hovered SetScreenVariable("hovered", "B")
                    unhovered SetScreenVariable("hovered", None)
                text "PILIHAN B":
                    xalign 0.5
                    size 20

            # ================= C =================
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 15
                imagebutton:
                    idle "pasar_c_idle"
                    hover "pasar_c_hover"
                    action Jump("pilihan_pasar_c")
                    hovered SetScreenVariable("hovered", "C")
                    unhovered SetScreenVariable("hovered", None)
                text "PILIHAN C":
                    xalign 0.5
                    size 20

    # ================= SCENE PASAR - KRISIS =================
label scene_pasar_krisis:
    scene black
    with fade

    window hide
    pause 1.0

    stop ambient fadeout 1.0
    play ambient "sound/suara_pasar.MP3" fadein 1.0 loop
    play music "sound/talempongminang2.MP3" fadein 1.0 loop
    scene visual_awal_scenepasar
    with dissolve
    window show

    narrator "Setelah mengatasi situasi Rumah Gadang, Garuda membawa Wira ke pasar nagari. Suasana begitu ramai dan hidup..."

    pause 1.0

    show garuda_berbicara_minang at wcenter_small
    with dissolve

    garuda "Ini adalah tantangan terakhir, Wira. Sebuah perusahaan besar dari kota menawarkan investasi besar untuk nagari."

    pause 0.5

    garuda "Tapi ada yang janggal. Mereka ingin mengubah cara hidup masyarakat di sini. Semua orang menjadi bingung."

    hide garuda_berbicara_minang
    pause 1.0

    narrator "Wira melihat forum impromptu di pasar. Para tokoh tengah berdebat sengit tentang penawaran ini."

    narrator "Setiap keputusan akan menentukan masa depan ekonomi nagari. Wira harus memilih dengan bijak."

    pause 1.0

    # ================= PILIHAN PASAR =================
    show visual_awal_scenepasar
    show screen show_points
    call screen pilihan_pasar

    # PILIHAN PASAR A
label pilihan_pasar_a:
    scene percakapan_awal_scenepasar
    with dissolve
    window show

    wira "Pak Harlan, saya ngerti tawaran ini menarik secara ekonomi. Tapi nagari ini punya fondasi yang tidak bisa dikompromikan. Kalau investasinya memang ingin membantu nagari, bisa diajukan format yang sesuai dengan nilai Islam dan adat"
    wira "Kerja sama yang benar benar saling menguntungkan, bukan yang merusak dari dalam"

    pause 1.0

    scene pasar_a_solved
    with dissolve
    window show
    narrator "Harlan terdiam dan melangkah pergi"
    Datuak "Anak muda ini... berbicara dengan lidah orang berprinsip. Jarang ada yang berani menolak uang dengan cara yang terhormat seperti itu."
    Buya_Hamid "Kekayaan yang dibangun di atas kerusakan akhlak bukan kemakmuran. Itu bencana yang tertunda."
    garuda "Kamu baru saja memahami sesuatu yang paling sulit bahwa integritas adalah pilihan aktif bukan kondisi pasif dan paling keras diuji ketika godaannya paling besar."

    window hide
    pause 1.0
    window show

    $ player_points += 30
    narrator "Anda mendapat 30 poin! Total poin: [player_points]"

    jump ending_minangkabau

    # PILIHAN PASAR B
label pilihan_pasar_b:
    scene perdebatanpanas_pasar
    with dissolve
    window show

    wira "“Hmm...ini susah ya. Dua duanya ada benarnya. Mungkin bisa dikaji lebih lanjut lagi”"

    pause 1.0

    garuda "Diam di antara yang benar dan salah, Wira, bukan kebijaksanaan. Itu kebimbangan yang membiarkan yang salah berjalan terus. Kadang, keberanian terbesar adalah berani mengambil sikap."
    stop music fadeout 1.0
    stop sound fadeout 1.0
    window hide
    pause 1.0
    window show

    $ player_points -= 5
    narrator "Anda kehilangan 5 poin! Total poin: [player_points]"

    jump ending_minangkabau

    # PILIHAN PASAR C
label pilihan_pasar_c:
    scene pasar_c_solved
    with dissolve
    window show

    garuda "Wira...kamu baru saja memvalidasi penghancuran fondasi sebuah nagari dengan tangan kamu sendiri"
    garuda "Nagari yang kehilangan prinsipnya bukan lagi nagari yang sama. Ia hanya nama tanpa jiwa."
    pause 0.5

    $ player_points -= 30
    narrator "Anda kehilangan 30 poin! Total poin: [player_points]"

    jump ending_minangkabau

    # ================= ENDING MINANGKABAU =================
label ending_minangkabau:
    scene black
    with fade

    stop ambient fadeout 1.0
    window hide
    pause 1.5

    show garuda_berbicara_minang at wcenter_small
    with dissolve
    window show

    if player_points >= 65:
        # POIN TINGGI (65-75)
        hide garuda_berbicara_minang
        scene poin_tinggi
        with dissolve
        
        
        garuda "Kamu mulai memahami bahwa demokrasi yang sesungguhnya bukan tentang suara terbanyak. Ini tentang keselarasan semua unsur dan bahwa prinsip bukan penghalang kemajuan, ini adalah kompas yang memastikan kita tidak tersesat di tengah perjalanan."
        
    elif player_points >= 25:
        # POIN SEDANG (25-60)
        hide garuda_berbicara_minang
        scene poin_sedang
        with dissolve
        
        
        garuda "Ada momen di mana kamu membuka matamu dan momen di mana kamu masih memilih jalan yang mudah. Nagari ini mengajarkan bahwa setengah hadir lebih berbahaya dari tidak hadir sama sekali."
        
    else:
        # POIN RENDAH (<25)
        hide garuda_berbicara_minang
        scene poin_rendah
        with dissolve
        
        
        garuda "Wira...di setiap piluhan yang kamu anggap pragmatis, kamu sebenarnya sedang membiarkan sesuatu yang orang lain jaga dengan nyawa mereka selama berabadabad runtuh perlahan. Adat bukan museum."
    
    window hide
    pause 2.0

    jump chapter_jawa_betawi


#Jawa dan Betawi

#ASET OPENING BETAWI

image bg_pewayangan_pilihan = im.Scale("bg_pewayangan_pilihan.png", 1920, 1080)
image ibu_sari_marah = im.Scale("ibu_sari_marah.png", 1920, 1080)
image penjelasan_misi_betawi = im.Scale("penjelasan_misi_betawi.png", 1920, 1080)
image pilihana_festivalkampung = im.Scale("pilihana_festivalkampung.png", 1920, 1080)
image pilihana_scenetatakrama = im.Scale("pilihana_scenetatakrama.png", 1920, 1080)
image pilihana_wayang_hover = im.Scale("pilihana_wayang_hover.png", 1920, 1080)
image pilihana_wayang_idle = im.Scale("pilihana_wayang_idle.png", 1920, 1080)
image pilihanb_festivalkampung = im.Scale("pilihanb_festivalkampung.png", 1920, 1080)
image pilihanb_scenetatakrama = im.Scale("pilihanb_scenetatakrama.png", 1920, 1080)
image pilihanb_wayang_hover = im.Scale("pilihanb_wayang_hover.png", 1920, 1080)
image pilihanb_wayang_idle = im.Scale("pilihanb_wayang_idle.png", 1920, 1080)
image pilihanc_festivalkampung = im.Scale("pilihanc_festivalkampung.png", 1920, 1080)
image pilihanc_scenetatakrama = im.Scale("pilihanc_scenetatakrama.png", 1920, 1080)
image pilihanc_wayang_hover = im.Scale("pilihanc_wayang_hover.png", 1920, 1080)
image pilihanc_wayang_idle = im.Scale("pilihanc_wayang_idle.png", 1920, 1080)
image radenajak_masukkeraton = im.Scale("radenajak_masukkeraton.png", 1920, 1080)
image rapat_awal_betawi = im.Scale("rapat_awal_betawi.png", 1920, 1080)
image rapat_betawi_wira_datang = im.Scale("rapat_betawi_wira_datang.png", 1920, 1080)
image scenewayang_kekecewaanPakSugeng = im.Scale("scenewayang_kekecewaanPakSugeng.png", 1920, 1080)
image skor_rendah_daerahjawa = im.Scale("skor rendah_daerahjawa.png", 1920, 1080)
image skor_sedang_daerahjawa = im.Scale("skorsedang_daerahjawa.png", 1920, 1080)
image skor_tinggi_daerahjawa = im.Scale("skortinggi_daerahjawa.png", 1920, 1080)
image visual_hormatdenganmaubelajar = im.Scale("visual_hormatdenganmaubelajar.png", 1920, 1080)
image visual_tidakpeduli = im.Scale("visual_tidakpeduli.png", 1920, 1080)
image visualmasuk_keratonjawa = im.Scale("visualmasuk_keratonjawa.png", 1920, 1080)
image visualpilihanA_rapatbetawi = im.Scale("visualpilihanA_rapatbetawi.png", 1920, 1080)
image visualpilihanA_wayang = im.Scale("visualpilihanA_wayang.png", 1920, 1080)
image visualpilihanb_wiramemaksa = im.Scale("visualpilihanb_wiramemaksa.png", 1920, 1080)
image visualpilihanC_pakrojakmarah = im.Scale("visualpilihanC_pakrojakmarah.png", 1920, 1080)
image visualpilihanC_wiraberide = im.Scale("visualpilihanC_wiraberide.png", 1920, 1080)
image visualpilihanc_wiramembujukadaptasi = im.Scale("visualpilihanc_wiramembujukadaptasi.png", 1920, 1080)
image wira_disambutraden = im.Scale("wira_disambutraden.png", 1920, 1080)

# ASET PILIHAN - FESTIVAL KAMPUNG
image pilihana_festivalkampung_button = im.Scale("pilihana_festivalkampung.png", 700, 800)
image pilihanb_festivalkampung_button = im.Scale("pilihanb_festivalkampung.png", 700, 800)
image pilihanc_festivalkampung_button = im.Scale("pilihanc_festivalkampung.png", 700, 800)

# ASET PILIHAN - SCENE TATA KRAMA (KERATON JAWA)
image pilihana_scenetatakrama_button = im.Scale("pilihana_scenetatakrama.png", 700, 800)
image pilihanb_scenetatakrama_button = im.Scale("pilihanb_scenetatakrama.png", 700, 800)
image pilihanc_scenetatakrama_button = im.Scale("pilihanc_scenetatakrama.png", 700, 800)

# ===== CHAPTER JAWA DAN BETAWI =====
# Pertarungan Dalang Terakhir
# Checkpoint 2

label chapter_jawa_betawi:

    # ===== TRANSISI MEMASUKI BETAWI & KERATON JAWA =====
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    play music "sound/jalijali.MP3" fadein 1.0 loop
    play sound "sound/adzan.MP3"
    scene bg_pewayangan_pilihan
    with fade
    pause 1.0

    # Visual: Layar gelap dengan cahaya kuning menyeruak perlahan
    narrator "Cahaya kuning menyeruak perlahan dari kegelapan. Wira berdiri di sebuah Kampung Betawi di pinggiran kota. Dinding bercat putih kusam dihiasi ornamen khas Betawi - motif gigi balang, pucuk rebung, dan warna merah hijau yang mencolok."

    window hide
    pause 2.0
    window show

    garuda "Selamat datang di Kampung Betawi, Wira."
    garuda "Besok malam, kampung ini mengadakan Festival Budaya Betawi tahunan. Tapi ada masalah besar yang mengancam festival ini sebelum sempat dimulai."

    wira "Masalah apa?"

    garuda "Kamu akan segera melihatnya sendiri. Di sinilah petualanganmu dimulai. Setelah ini…kita akan melanjutkan ke jantung Keraton Jawa."

    wira "Dua tempat sekaligus?"

    garuda "Karena keduanya berbagi satu pertanyaan yang sama yaitu bagaimana seni dan budaya bisa bertahan ketika dunia terus berubah?"
    garuda "Di Betawi, kamu akan menyaksikan pergulatan itu dari luar. Di Keraton, kamu akan masuk ke dalamnya."

    # ===== PENJELASAN MISI OLEH GARUDA =====
    scene penjelasan_misi_betawi
    with dissolve

    garuda "Misimu di sini terbagi dalam tiga babak."
    garuda "Pertama, Festival Kampung yang hampir berantakan karena konflik kepanitiaan."
    garuda "Kedua, Pertunjukan Wayang yang terancam ditinggalkan generasi muda."
    garuda "Ketiga, pelajaran tata krama di dalam Keraton, di mana satu langkah bisa merusak segalanya."
    garuda "Setiap pilihanmu akan meninggalkan bekas."

    wira "Oke..."

    window hide
    pause 1.0
    window show

    # ===== SCENE FESTIVAL KAMPUNG (KEPANITIAAN YANG RETAK) =====
    play sound "sound/berdebat.MP3"
    scene penjelasan_misi_betawi
    with fade

    narrator "Sore menjelang petang. Di halaman rumah di kampung, warga berkumpul mengelilingi meja kayu penuh kertas dan jadwal."
    
    Bang_Rojak "(marah) Sudah dari dulu festivalnya pakai format yang sama! Lenong, tanjidor, ondel ondel, lalu makan bersama. Itu sudah pakem! Sari mau nubah apa lagi?"
    
    Sari "Bang, tahun lalu cuma dua puluh orang yang nonton sampai selesai! Generasi muda nggak tertarik kalau formatnya gitu gitu aja."
    Sari "Saya usul kita gabungin sama pertunjukan modern, ada sesi story telling dan dokumentasi di media sosial."

    Bang_Rojak "Itu bukan festival budaya! Itu konten TikTok! Budaya bukan tontonan, budaya adalah kehidupan!"

    Sari "Tapi kalau nggak ada yang nonton, siapa yang akan mewarisi?"

    Engkong_Ali "Kamu…anak baru di kampung ini ya?"

    wira "Saya…nggak mau ganggu, Ngkong."

    Engkong_Ali "(tersenyum) Justru kamu yang paling nggak mengganggu di sini. Dua orang itu sudah lupa caranya mendengar. Kamu, anak muda, belum lupa."

    garuda "Ini masalah yang lebih dalam dari sekadar format festival. Bang Rojak mewakili mereka yang takut kehilangan akar. Sari mewakili mereka yang takut mati karena tidak relevan."
    garuda "Kamu ada di tengah-tengah. Tentukan cara kamu merespons konflik ini."

    # ===== PILIHAN FESTIVAL KAMPUNG =====
    menu:
        "Duduk bersama dan cari format yang menjaga akar.":
            jump pilihan_festival_a
        "Pertahankan format lama tanpa perubahan.":
            jump pilihan_festival_b
        "Putuskan festival hybrid tanpa musyawarah.":
            jump pilihan_festival_c

label pilihan_festival_a:
        $ player_points += 25
        hide pilihana_festivalkampung_button
        hide pilihanb_festivalkampung_button
        hide pilihanc_festivalkampung_button

        wira "Bang Rojak, Kak Sari…dua-duanya ada benarnya."
        wira "Kalau boleh, kita duduk bareng dulu. Bang Rojak bisa ceritain bagian mana dari festival yang paling penting untuk dijaga."
        wira "Kak Sari bisa kasih tau inovasinya yang mana yang bisa jalan tanpa ngorbanin inti acara."
        wira "Engkong Ali bisa jadi penengah. Kita cari format yang jaga akar tapi nggak ngusir generasi baru."

        Engkong_Ali "(tersenyum lebar) Anak ini…tahu caranya membuat orang merasa didengar sebelum meminta mereka mendengar. Ayo, kita coba cara anak ini."

        Bang_Rojak "Baiklah…tapi lenong tetap harus ada."

        Sari "Setuju, Bang. Lenong tetap jadi bintang utama. Saya hanya ingin lebih banyak orang yang kenal bintangnya."

        garuda "Kamu baru saja mempraktikkan sesuatu yang lebih tua dari semua tradisi di kampung ini. Kamu mendengarkan sebelum memimpin. Ini dasar dari kepercayaan."

        window hide
        pause 1.0
        window show
        jump lanjut_ke_wayang

label pilihan_festival_b:
        $ player_points -= 15
        hide pilihana_festivalkampung_button
        hide pilihanb_festivalkampung_button
        hide pilihanc_festivalkampung_button

        wira "Menurut gue, Bang Rojak yang bener. Festival tradisional ya harus tradisional. Format lama dipertahanin aja, nggak perlu diubah-ubah."

        Sari "(kecewa, pergi dengan ekspresi marah)"

        garuda "Memihak memang terasa tegas. Tapi dalam komunitas yang hidupnya dari kebersamaan, memilih satu pihak tanpa mendengar yang lain bukan ketegasan."
        garuda "Ini pengkhianatan terhadap musyawarah."

        window hide
        pause 1.0
        window show
        jump lanjut_ke_wayang

label pilihan_festival_c:
        $ player_points -= 5
        hide pilihana_festivalkampung_button
        hide pilihanb_festivalkampung_button
        hide pilihanc_festivalkampung_button

        wira "Udah, gini aja. Gue punya ide. Kita bikin festival hybrid, separuh tradisional separuh modern, terus live streaming semuanya. Nggak perlu debat panjang."

        Bang_Rojak "Siapa kamu mau memutuskan urusan kampung kami?"

        garuda "Ide yang baik pun bisa ditolak kalau datang tanpa menghormati proses. Di komunitas yang menghargai adat, cara kamu mengajukan sesuatu sama pentingnya dengan isi usulanmu."

        window hide
        pause 1.0
        window show

label lanjut_ke_wayang:

    # ===== SCENE WAYANG YANG DIANGGAP KUNO =====
    scene bg_pewayangan_pilihan
    with dissolve

    narrator "Malam hari, festival sudah berdiri. Lampu kelap-kelip menghiasi panggung. Terdapat sekelompok remaja di depan panggung menonton namun tidak antusias."
    window hide
    pause 0.5
    window show

    scene scenewayang_kekecewaanPakSugeng
    play sound "sound/gamelanpelan.mp3" fadein 1.0 loop
    Dimas "Bro, ini acara apaan sih. Bayangannya doang yang keliatan, suaranya lebay, nggak ngerti ceritanya apa. Nonton anime aja lebih seru."
    Teman_Dimas "Ssst...nanti didenger Pak Sugeng."

    Pak_Sugeng "Sudah tiga generasi keluargaku menjaga wayang ini. Kakekku yang mengukir Arjuna itu. Kalau aku pergi nanti, tidak ada yang meneruskan."

    garuda "Ini lebih dari sekadar pertunjukan, Wira. Pak Sugeng adalah dalang terakhir di kampung ini. Wayang bukan hanya seni, ia adalah ensiklopedia filsafat Jawa."
    garuda "Lakon Mahabharata dan Ramayana mengandung ajaran tentang dharma, keadilan, dan kesetiaan yang bertahan ribuan tahun. Tapi kalau tidak ada yang mau belajar…"

    wira "...semuanya hilang."

    garuda "Tepat. Dimas bukan musuhnya. Ia hanya tidak tahu. Belum ada yang pernah jelaskan kepadanya."

    Pak_Sugeng "Anak muda…kamu punya pendapat tentang ini?"

    garuda "Wira, ini momen penting. Pak Sugeng butuh pembelaan, tetapi Dimas butuh jembatan, bukan tembok. Bagaimana kamu merespons?"
    stop sound fadeout 1.0
    # ===== PILIHAN WAYANG =====
    show screen show_points
    call screen pilihan_wayang
    menu:
        "Jelaskan wayang dengan bahasa anak muda.":
            jump pilihan_wayang_a
        "Paksa Dimas menghormati wayang.":
            jump pilihan_wayang_b
        "Ubah cerita wayang agar kekinian.":
            jump pilihan_wayang_c

label pilihan_wayang_a:
        $ player_points += 25
        hide pilihana_wayang_idle
        hide pilihanb_wayang_idle
        hide pilihanc_wayang_idle

        wira "Lo tau nggak, Dimas, karakter Arjuna yang dipaksa milih antara keluarga dan kebenaran itu…mirip banget sama dilema di film superhero kesukaan lo."
        wira "Wayang bukan cuma bayang-bayang, bro. Itu cerita manusia yang udah dipikirin ribuan tahun lalu sebelum kita lahir."

        Pak_Sugeng "Ia menerangkan wayang dengan bahasa anak muda…Kakekku dulu bilang, dalang yang baik bisa bicara dalam bahasa siapapun yang duduk di depannya."

        Dimas "Pak…Arjuna itu ceritanya gimana sih sebenernya?"

        Pak_Sugeng "(tersenyum dan mulai mengangkat wayang Arjuna ke depan layar)"

        garuda "Kamu tidak membela wayang. Kamu membuka pintu menuju wayang. Itu jauh lebih baik."

        window hide
        pause 1.0
        window show
        jump lanjut_ke_keraton

label pilihan_wayang_b:
        $ player_points -= 10
        hide pilihana_wayang_idle
        hide pilihanb_wayang_idle
        hide pilihanc_wayang_idle

        wira "Dimas, lo nggak boleh gitu. Ini budaya nenek moyang kita. Harus dihormatin, suka atau nggak suka."

        Dimas "(mengangguk kaku dan rasa penasaran yang sempat muncul langsung padam)"

        garuda "Kewajiban tanpa pemahaman melahirkan keterpaksaan, bukan kecintaan. Tradisi yang dipaksakan akan ditinggalkan begitu tidak ada yang memaksa lagi."

        window hide
        pause 1.0
        window show
        jump lanjut_ke_keraton

label pilihan_wayang_c:
        $ player_points -= 15
        hide pilihana_wayang_idle
        hide pilihanb_wayang_idle
        hide pilihanc_wayang_idle

        wira "Pak Sugeng, mungkin wayangnya bisa di-dubbing pakai suara yang lebih kekinian? Atau ceritanya diganti yang lebih relevan gitu? Biar anak muda tertarik."

        Pak_Sugeng "(kecewa) Kalau ceritanya diganti…itu bukan wayang lagi, Nak. Itu hanya boneka kayu."

        garuda "Ada batas antara adaptasi yang menghidupkan dan perubahan yang menghilangkan jiwa. Kamu baru saja melewati batas itu."

        window hide
        pause 1.0
        window show

label lanjut_ke_keraton:

    # ===== TRANSISI MEMASUKI KERATON JAWA =====
    play sound "sound/Flapping Wing (Berat) SFX.mp3"
    play music "sound/sarwolaras.MP3" fadein 1.0 loop
    scene visualmasuk_keratonjawa
    with fade

    narrator "Cahaya festival Betawi perlahan memudar. Wira dan Garuda terangkat ke udara. Lampu-lampu kampung mengecil seperti kunang-kunang. Perlahan-lahan, kompleks bangunan besar muncul di bawah cahaya bulan."
    narrator "Atap joglo berlapis-lapis berwarna hijau tua dan emas. Alun-alun luas dengan dua pohon beringin kembar yang berdiri seperti penjaga."

    window hide
    pause 2.0
    window show

    wira "Gue ngerasain sesuatu…tempat ini beda. Kerasa lebih…berat."

    garuda "Karena di sini, setiap hal bermakna. Cara kamu berdiri, berjalan, berbicara, bahkan cara kamu diam. Tempat ini memiliki bahasa yang dibangun selama berabad-abad untuk menunjukkan rasa hormat kepada sesama dan kepada Sang Pencipta."

    wira "Berarti gue harus hati-hati banget?"

    garuda "Bukan hanya hati-hati, kamu harus hadir sepenuhnya."

    window hide
    pause 1.0
    window show

    scene visual_hormatdenganmaubelajar
    with dissolve

    Kanjeng_Raden "Poro tamu ingkang kinurmatan…sugeng rawuh ing Keraton. Mugi saged manggih karaharjan lan kawicaksanan ing mriki."

    wira "Itu artinya apa?"

    garuda "Beliau menyambut kamu dengan doa agar kamu menemukan keselamatan dan kebijaksanaan di sini. Di Keraton, bahasa bukan hanya komunikasi. Bahasa adalah penghormatan."

    # ===== SCENE TATA KRAMA (BAHASA YANG BERBICARA) =====
    play sound "sound/langkahkayu.mp3"
    play ambient "sound/gamelansebelah.MP3" fadein 1.0 loop
    scene visual_tidakpeduli
    with dissolve

    narrator "Kanjeng Raden membawa Wira dan Garuda memasuki Pendopo utama Keraton. Ruangan besar beratap tinggi dengan tiang-tiang kayu jati besar."
    narrator "Raden Mas Bagas sedang berlatih memainkan wayang sendirian. Ia penerus tradisi dalang Keraton, penerus generasi ketujuh belas."

    Raden_Mas_Bagas "Tamu dari luar. Jarang ada yang masuk sejauh ini. Saya Bagas, calon dalang Keraton generasi ketujuh belas."

    wira "Eh, sori…gue harusnya gimana ya di sini?"

    Kanjeng_Raden "Nggih, mboten menopo. Tamu ingkang sae punika ingkang purun nyuwun pirsa."

    garuda "Di Keraton, ada tata cara yang disebut unggah-ungguh. Bukan untuk mempermalukan tamu, tapi untuk menjaga keselarasan ruang dan relasi antar manusia."
    garuda "Kamu akan menghadapi beberapa situasi. Bagaimana kamu merespons akan mencerminkan siapa kamu."
    garuda "Wira, Kanjeng Raden akan melewatimu. Apa yang kamu lakukan?"

    # ===== PILIHAN TATA KRAMA =====
    menu:
        "Bertanya dan belajar tata krama.":
            jump pilihan_krama_a
        "Tetap berdiri tanpa memberi jalan.":
            jump pilihan_krama_b
        "Menyingkir dan membungkuk tanpa bertanya.":
            jump pilihan_krama_c

label pilihan_krama_a:
        $ player_points += 30
        hide pilihana_scenetatakrama_button
        hide pilihanb_scenetatakrama_button
        hide pilihanc_scenetatakrama_button

        wira "Kanjeng, maaf…tadi saya harusnya ngapaian ya yang bener? Saya mau belajar tata caranya di sini."

        wira "(segera menyingkir ke tepi, sedikit membungkuk badan sebagai tanda hormat)"

        Kanjeng_Raden "(tersenyum) Yang paling sulit bukan belajar tata krama. Yang paling sulit adalah menyadari bahwa kamu belum tahu dan tidak malu untuk bertanya."

        Raden_Mas_Bagas "Jujur, saya kuliah di luar negeri empat tahun dan baru bisa nyantai di sini setelah enam bulan balik. Kamu baru masuk tapi udah nanya yang bener."

        garuda "Tata krama bukan tentang tunduk. Akan tetapi, tentang mengakui bahwa ada sesuatu yang lebih besar dari dirimu sendiri di dalam ruangan ini dan kamu memilih untuk hadir dengan hormat bukan dengan ego."

        window hide
        pause 1.0
        window show
        jump lanjut_ke_dialog_bagas

label pilihan_krama_b:
        $ player_points -= 20
        hide pilihana_scenetatakrama_button
        hide pilihanb_scenetatakrama_button
        hide pilihanc_scenetatakrama_button

        wira "(berdiri saja di tempatnya, membiarkan Kanjeng Raden yang menyesuaikan jalan, sambil melihat ke arah lain)"

        Raden_Mas_Bagas "Di sini, cara kamu berdiri dan memberikan jalan itu bukan formalitas. Ini sebuah cara kamu bilang \"Saya tahu tempat saya dan saya menghormati orang lain\" Kalau kamu nggak melakukan itu…"

        garuda "...kamu bukan orang yang kasar. Akan tetapi, kamu tidak hadir dan ini adalah kehilangan terbesar."

        window hide
        pause 1.0
        window show
        jump lanjut_ke_dialog_bagas

label pilihan_krama_c:
        $ player_points += 10
        hide pilihana_scenetatakrama_button
        hide pilihanb_scenetatakrama_button
        hide pilihanc_scenetatakrama_button

        wira "(menyingkir dan membungkuk hormat, tapi tidak bertanya lebih lanjut dan hanya berdiam diri)"

        Raden_Mas_Bagas "Kamu tahu caranya hormat. Tapi kamu belum tahu alasannya. Itu beda tipis, tapi beda."

        garuda "Menghormati tanpa memahami adalah ritual. Menghormati dengan memahami adalah kesadaran. Keraton tidak butuh robot yang tahu gerakannya. Keraton butuh manusia yang tahu mengapa."

        window hide
        pause 1.0
        window show

label lanjut_ke_dialog_bagas:

    # ===== SCENE DIALOG RADEN MAS BAGAS =====
    stop ambient fadeout 1.0
    play music "sound/gamelanpelan.mp3" fadein 1.0 loop
    scene visual_hormatdenganmaubelajar
    with dissolve

    Raden_Mas_Bagas "Saya mau jujur denganmu, Wira. Saya sempat mau meninggalkan semua ini."
    Raden_Mas_Bagas "Waktu di luar negeri, saya belajar teknik pertunjukan modern yang lebih efektif dan lebih relevan. Saya pikir, kenapa saya harus balik ke sini dan mengikat diri dengan aturan yang rasanya kuno?"

    Raden_Mas_Bagas "Tapi saya menyadari satu hal. Di negara manapun saya pergi, nggak ada yang punya wayang. Nggak ada yang punya gamelan, dan nggak ada yang punya filosofi tentang keselarasan kayak yang ada di sini."
    Raden_Mas_Bagas "Mereka punya banyak hal yang saya kagumi, tapi nggak punya ini semua."

    wira "Terus kamu balik."

    Raden_Mas_Bagas "Saya balik dan sekarang saya lagi belajar untuk membawa dunia luar masuk ke sini. Bukan untuk mengubah Keraton tetapi untuk membuat lebih banyak orang dapat merasakan apa yang bisa saya rasakan waktu duduk di sini pertama kali."

    garuda "Dengarkan baik-baik, Wira. Ini bukan cerita tentang masa lalu melawan masa depan. Ini tentang menemukan apa yang tidak bisa digantikan lalu menjaganya dengan kedua tanganmu."

    window hide
    pause 2.0
    window show

    # ===== AKHIR CHECKPOINT =====
    # Menampilkan skor akhir
    $ skor_akhir = player_points

    if skor_akhir >= 50:
        scene skor_tinggi_daerahjawa
        with fade
        narrator "Keputusanmu selama perjalanan di Betawi dan Keraton Jawa menunjukkan pemahaman mendalam tentang keseimbangan antara tradisi dan modernitas. Kamu telah membuktikan bahwa mendengarkan dan memahami adalah kunci untuk mempertahankan warisan budaya di tengah perubahan zaman."
    elif skor_akhir >= 0:
        scene skor_sedang_daerahjawa
        with fade
        narrator "Perjalananmu menunjukkan kesadaran terhadap pentingnya budaya, meski masih ada ruang untuk berkembang. Kamu mulai memahami bahwa setiap keputusan membawa konsekuensi yang mendalam bagi komunitas dan tradisi."
    else:
        scene skor_rendah_daerahjawa
        with fade
        narrator "Perjalananmu menunjukkan bahwa masih banyak yang perlu dipelajari tentang menghargai tradisi dan mendengarkan orang lain. Warisan budaya memerlukan lebih dari sekedar niat - ia memerlukan kehadiran dan kepedulian yang sejati."

    window hide
    pause 3.0
    window show

    narrator "Checkpoint 2 Selesai: Betawi & Keraton Jawa"
    narrator "Poin yang dikumpulkan: [player_points]"

    stop music fadeout 1.0
    jump bali_intro

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
image bali_bu_nyoman_kecewa = "bali_bu_nyoman_kecewa.png"
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

# BALI PILIHAN IMAGES
image bali_scene1_pilihan_A_img = "bali_scene1_pilihan_A.png"
image bali_scene1_pilihan_B_img = "bali_scene1_pilihan_B.png"
image bali_scene1_pilihan_C_img = "bali_scene1_piliihan_C.png"
image bali_scene2_pilihan_A_img = "bali_scene2_pilihan_A.png"
image bali_scene2_pilihan_B_img = "bali_scene2_pilihan_B.png"
image bali_scene2_pilihan_C_img = "bali_scene2_pilihan_C.png"
image bali_scene3_pilihan_A_img = "bali_scene3_pilihan_A.png"
image bali_scene3_pilihan_B_img = "bali_scene3_pilihan_B.png"
image bali_scene3_pilihan_C_img = "bali_scene3_pilihan_C.png"

# TORAJA PILIHAN IMAGES
image toraja_scene1_pilihan_A_img = "toraja_scene1_pilihan_A.png"
image toraja_scene1_pilihan_B_img = "toraja_scene1_pilihan_B.png"
image toraja_scene1_pilihan_C_img = "toraja_scene1_pilihan_C.png"
image toraja_scene2_pilihan_A_img = "toraja_scene2_pilihan_A.png"
image toraja_scene2_pilihan_B_img = "toraja_scene2_pilihan_B.png"
image toraja_scene2_pilihan_C_img = "toraja_scene2_pilihan_C.png"
image toraja_scene3_pilihan_A_img = "toraja_scene3_pilihan_A.png"
image toraja_scene3_pilihan_B_img = "toraja_scene3_pilihan_B.png"
image toraja_scene3_pilihan_C_img = "toraja_scene3_pilihan_C.png"

# Transform for glow effect on hover
transform pilihan_glow(idle_img):
    contains:
        idle_img
        zoom 1.05
    contains:
        idle_img
        zoom 1.0
        matrixcolor BrightnessMatrix(0.3)
    time 0.15
    contains:
        idle_img
        zoom 1.08
        matrixcolor BrightnessMatrix(0.5)
    time 0.15



# BALI PILIHAN SCREENS - Horizontal layout, scaled down
screen bali_scene1_pilih:
    imagebutton:
        idle im.Scale("bali_scene1_pilihan_A.png", 450, 700)
        hover glow_hover(im.Scale("bali_scene1_pilihan_A.png", 450, 700))
        xpos 0.25 ypos 0.5 anchor (0.5, 0.5)
        action [SetVariable("bali_points", bali_points + 20), SetVariable("scene1_choice", "A"), Jump("scene1_ending_a")]

    imagebutton:
        idle im.Scale("bali_scene1_pilihan_B.png", 450, 700)
        hover glow_hover(im.Scale("bali_scene1_pilihan_B.png", 450, 700))
        xpos 0.5 ypos 0.5 anchor (0.5, 0.5)
        action [SetVariable("bali_points", bali_points - 5), SetVariable("scene1_choice", "B"), Jump("scene1_ending_b")]

    imagebutton:
        idle im.Scale("bali_scene1_piliihan_C.png", 450, 700)
        hover glow_hover(im.Scale("bali_scene1_piliihan_C.png", 450, 700))
        xpos 0.75 ypos 0.5 anchor (0.5, 0.5)
        action [SetVariable("bali_points", bali_points - 20), SetVariable("scene1_choice", "C"), Jump("scene1_ending_c")]

screen bali_scene2_pilih:
    imagebutton:
        idle im.Scale("bali_scene2_pilihan_A.png", 450, 700)
        hover glow_hover(im.Scale("bali_scene2_pilihan_A.png", 450, 700))
        xpos 0.25 ypos 0.5 anchor (0.5, 0.5)
        action [SetVariable("bali_points", bali_points + 20), SetVariable("scene2_choice", "A"), Jump("scene2_ending_a")]

    imagebutton:
        idle im.Scale("bali_scene2_pilihan_B.png", 450, 700)
        hover glow_hover(im.Scale("bali_scene2_pilihan_B.png", 450, 700))
        xpos 0.5 ypos 0.5 anchor (0.5, 0.5)
        action [SetVariable("bali_points", bali_points + 0), SetVariable("scene2_choice", "B"), Jump("scene2_ending_b")]

    imagebutton:
        idle im.Scale("bali_scene2_pilihan_C.png", 450, 700)
        hover glow_hover(im.Scale("bali_scene2_pilihan_C.png", 450, 700))
        xpos 0.75 ypos 0.5 anchor (0.5, 0.5)
        action [SetVariable("bali_points", bali_points - 20), SetVariable("scene2_choice", "C"), Jump("scene2_ending_c")]

screen bali_scene3_pilih:
    imagebutton:
        idle im.Scale("bali_scene3_pilihan_A.png", 450, 700)
        hover glow_hover(im.Scale("bali_scene3_pilihan_A.png", 450, 700))
        xpos 0.25 ypos 0.5 anchor (0.5, 0.5)
        action [SetVariable("bali_points", bali_points + 30), SetVariable("scene3_choice", "A"), Jump("scene3_ending_a")]

    imagebutton:
        idle im.Scale("bali_scene3_pilihan_B.png", 450, 700)
        hover glow_hover(im.Scale("bali_scene3_pilihan_B.png", 450, 700))
        xpos 0.5 ypos 0.5 anchor (0.5, 0.5)
        action [SetVariable("bali_points", bali_points - 5), SetVariable("scene3_choice", "B"), Jump("scene3_ending_b")]

    imagebutton:
        idle im.Scale("bali_scene3_pilihan_C.png", 450, 700)
        hover glow_hover(im.Scale("bali_scene3_pilihan_C.png", 450, 700))
        xpos 0.75 ypos 0.5 anchor (0.5, 0.5)
        action [SetVariable("bali_points", bali_points - 15), SetVariable("scene3_choice", "C"), Jump("scene3_ending_c")]

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

# MINANGKABAU
image rumah_gadang = im.Scale("rumah_gadang.png",1920,1080)
image wira_bingung = "wira_dewasa_bingung.png"
image garuda_berdiri = "garuda_default.png"
image garuda_berbicara_minang = "garuda_bicara.png"
image wira_tunjuk = "wira_tunjuk2.png"
image garuda_ceria = "garuda_ceria.png"



transform wright_small:
    xalign 0.77
    yalign 0.65
    zoom 0.6

transform wcenter_small:
    xalign 0.5
    yalign 0.5
    zoom 0.6

transform wleft_lower:                                                                         
    xalign 0.36                                                                             
    yalign 0.8                                                                              
    zoom 0.6                                                                                   
                                                                                         
transform wright_lower:                                                                        
    xalign 0.77                                                                                
    yalign 0.8                                                                             
    zoom 0.6                                                                                   
                        


# ASET PASAR - PILIHAN BUTTONS
image pasar_a_idle = im.Scale("pasar_a_idle.png", 700, 800)
image pasar_a_hover = im.Scale("pasar_a_hover.png", 700, 800)
image pasar_b_idle = im.Scale("pasar_b_idle.png", 700, 800)
image pasar_b_hover = im.Scale("pasar_b_hover.png", 700, 800)
image pasar_c_idle = im.Scale("pasar_c_idle.png", 700, 800)
image pasar_c_hover = im.Scale("pasar_c_hover.png", 700, 800)

# TORAJA PILIHAN SCREENS - Horizontal layout, scaled down
screen toraja_scene1_pilih:
    imagebutton:
        idle im.Scale("toraja_scene1_pilihan_A.png", 500, 720)
        hover glow_hover(im.Scale("toraja_scene1_pilihan_A.png", 500, 720))
        xpos 0.25 ypos 0.5 anchor (0.5, 0.5)
        action Jump("toraja_scene1_choice_a")

    imagebutton:
        idle im.Scale("toraja_scene1_pilihan_B.png", 500, 720)
        hover glow_hover(im.Scale("toraja_scene1_pilihan_B.png", 500, 720))
        xpos 0.5 ypos 0.5 anchor (0.5, 0.5)
        action Jump("toraja_scene1_choice_b")

    imagebutton:
        idle im.Scale("toraja_scene1_pilihan_C.png", 500, 720)
        hover glow_hover(im.Scale("toraja_scene1_pilihan_C.png", 500, 720))
        xpos 0.75 ypos 0.5 anchor (0.5, 0.5)
        action Jump("toraja_scene1_choice_c")

screen toraja_scene2_pilih:
    imagebutton:
        idle im.Scale("toraja_scene2_pilihan_A.png", 500, 720)
        hover glow_hover(im.Scale("toraja_scene2_pilihan_A.png", 500, 720))
        xpos 0.25 ypos 0.5 anchor (0.5, 0.5)
        action Jump("toraja_scene2_choice_a")

    imagebutton:
        idle im.Scale("toraja_scene2_pilihan_B.png", 500, 720)
        hover glow_hover(im.Scale("toraja_scene2_pilihan_B.png", 500, 720))
        xpos 0.5 ypos 0.5 anchor (0.5, 0.5)
        action Jump("toraja_scene2_choice_b")

    imagebutton:
        idle im.Scale("toraja_scene2_pilihan_C.png", 500, 720)
        hover glow_hover(im.Scale("toraja_scene2_pilihan_C.png", 500, 720))
        xpos 0.75 ypos 0.5 anchor (0.5, 0.5)
        action Jump("toraja_scene2_choice_c")

screen toraja_scene3_pilih:
    imagebutton:
        idle im.Scale("toraja_scene3_pilihan_A.png", 500, 720)
        hover glow_hover(im.Scale("toraja_scene3_pilihan_A.png", 500, 720))
        xpos 0.25 ypos 0.5 anchor (0.5, 0.5)
        action Jump("toraja_scene3_choice_a")

    imagebutton:
        idle im.Scale("toraja_scene3_pilihan_B.png", 500, 720)
        hover glow_hover(im.Scale("toraja_scene3_pilihan_B.png", 500, 720))
        xpos 0.5 ypos 0.5 anchor (0.5, 0.5)
        action Jump("toraja_scene3_choice_b")

    imagebutton:
        idle im.Scale("toraja_scene3_pilihan_C.png", 500, 720)
        hover glow_hover(im.Scale("toraja_scene3_pilihan_C.png", 500, 720))
        xpos 0.75 ypos 0.5 anchor (0.5, 0.5)
        action Jump("toraja_scene3_choice_c")

label start:
    # ==========================================================================================================================
    # PROLOG / TERAS PAGI
    # ==========================================================================================================================
    stop music fadeout 1.0
    stop ambient fadeout 1.0
    stop clock fadeout 1.0
    stop bird fadeout 1.0
    play music "sound/MUSIC BOX BGM.mp3" fadein 1.5 volume 0.55
    play ambient "sound/Angin SFX.mp3" fadein 1.0 volume 0.35
    play clock "sound/Clock SFX.mp3" fadein 1.0 volume 0.22
    play bird "sound/Suara pipit SFX.mp3" fadein 1.0 volume 0.28

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
    play sound "sound/Suara pipit SFX.mp3" volume 0.65
    play sfx2 "sound/Flapping Wing SFX.mp3" volume 0.45
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

    # ==========================================================================================================================
    # PROLOG / TAMAN KOTA SORE
    # ==========================================================================================================================

    stop music fadeout 1.0
    stop clock fadeout 1.0
    stop bird fadeout 1.0
    play music "sound/MUSIC BOX BGM.mp3" fadein 1.5 volume 0.42
    play ambient "sound/Angin SFX.mp3" fadein 1.0 volume 0.45

    scene taman
    with dissolve

    show wira megang sangkar at wira_megang_sangkar
    with dissolve
    pause 1.0

    window show
    wira "Kita sudah sampai, Pipit! Lihat, di sini jauh lebih luas daripada kamar aku."
    window hide
    pause 0.5

    show wira duduk sangkar at wira_duduk_sangkar
    with dissolve

    pause 1.0
    window show
    wira "Aku buka ya pintunya? Tapi kamu jangan terbang tinggi tinggi... aku takut nggak bisa liat kamu lagi."
    play sound "sound/PINTU ISEKAI SFX.mp3" volume 0.35
    wira "Ayo... keluar sebentar..."

    window hide
    pause 0.5

    show wira ketiup angin at wira_ketiup_angin
    show pipit hinggap di sangkar at pipit_sangkar
    with dissolve
    play sound "sound/AnginKuat SFX.mp3" volume 0.65


    pause 1.0

    window show

    wira "Pipit?! Tunggu!"

    window hide
    pause 0.5
    show sangkar at sangkar_kosong
    show wira ngejar at wira_ketiup_angin
    show pipit terbang at atas_sangkar
    with dissolve
    play sound "sound/Flapping Wing SFX.mp3" volume 0.7
    play sfx2 "sound/Suara pipit SFX.mp3" volume 0.8
    pause 0.5

    show pipit terbang at pipit_leaving
    with ease

    hide pipit terbang

    pause 0.5
    window show
    wira "JANGAN TINGGALIN AKU! PIPIT!!!"
    pause 1.0
    window hide
    scene taman
    show wira sedih at wira_ketiup_angin
    with dissolve

    pause 2.0

    stop ambient fadeout 1.0
    stop music fadeout 2.0
    stop clock fadeout 1.0
    stop bird fadeout 1.0
    scene black
    with dissolve
    narrator "...."
    narrator "Pipit terbang.... entah kemana..."

    # =============================================================
    # PROLOG : KAMAR WIRA
    # =============================================================

    play ambient "sound/Clock SFX.mp3" fadein 1.0 volume 0.35
    scene kamarwira
    with dissolve

    show wira sinis at chara_wira_sinis
    play sound "sound/Phone Ringing SFX.mp3" volume 0.8
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
    play sound "sound/TUT TUT SFX.mp3" volume 0.7
    # wira "(Membanting HP ke kasur)"
    wira "Males deh, selalu aja kayak gini."

    # =============================================================
    # SCENE 5: GUDANG NENEK - KOTAK "PETUALANGAN NUSANTARA"
    # =============================================================

    stop ambient fadeout 1.0
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
    play sound "sound/PINTU ISEKAI SFX.mp3" volume 0.85
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
    play ambient "sound/AnginKuat SFX.mp3" fadein 0.5 volume 0.75
    play sound "sound/Flapping Wing (Berat) SFX.mp3" volume 0.8

    # TODO SFX: Angin menderu, gesekan logam ajaib, sayap mengepak sangat keras.
    wira "H-hei! Apa-apaan ini?! Lantainya... lantainya ilang?!"

    # TODO VFX: Tubuh Wira transparan lalu berubah menjadi butiran data/cahaya.
    hide wira panik
    show vfx_wira_data at center_placeholder
    with dissolve

    pause 1.0

    scene black
    with fade
    stop ambient fadeout 1.0

    narasi "Beberapa pintu dibuka untuk melarikan diri... tapi kotak ini dibuka untuk membuatmu kembali."

    # =============================================================
    # SCENE 7: DUNIA GAME - PERTEMUAN GARUDA
    # =============================================================

    scene bg_pulau_terapung
    show wira bingung at left_placeholder
    with fade
    play music "sound/MUSIC BOX BGM.mp3" fadein 1.5 volume 0.45
    play ambient "sound/Angin SFX.mp3" fadein 1.0 volume 0.4

    wira "Gue... gue di mana? Barusan tadi... gue di gudang..."
    wira "Gue masuk ke dalem game?! Gak mungkin, ini pasti gara-gara gue kurang tidur..."

    # TODO SFX: Kepakan sayap besar mendarat tepat di belakang Wira.
    play sound "sound/Flapping Wing (Berat) SFX.mp3" volume 0.85
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
    play sound "sound/Flapping Wing (Berat) SFX.mp3" volume 0.75
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
    play sound "sound/Flapping Wing (Berat) SFX.mp3" volume 0.9
    play sfx2 "sound/AnginKuat SFX.mp3" volume 0.75
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
    stop ambient fadeout 1.0
    stop clock fadeout 1.0
    stop bird fadeout 1.0
    stop music fadeout 1.5
    jump minangkabau_intro

# DAERAH 3 : BALI
label bali_intro:
    # BALI INTRODUCTION   JATILUWIH & SUBAK
    play music "sound/Gambuh Gamelan BGM.mp3"
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
    play sfx1 "sound/Cangkul SFX.mp3"
    play sfx2 "sound/Suara Burung SFX.mp3"
    play sfx3 "sound/Suara air (bisa diganti ke yg di Minangkabau) SFX.MP3"
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
    call screen bali_scene1_pilih

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
    stop sfx1
    stop sfx2
    stop sfx3
    play sfx1 "sound/Drone SFX.MP3" volume 0.8
    play sfx2 "sound/AnginKuat SFX.mp3"
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
    hide bali_bima_normal
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
    window show

    narrator "Bima menunggu jawaban. Nyoman menatap Wira dengan harapan."

    bima "Kamu seperti teman Nyoman. Apa pendapatmu tentang ini?"

    window hide
    pause 1.0

    # PILIHAN 2   SCENE 2
    call screen bali_scene2_pilih

label scene2_ending_a:
    window show
    window hide
    hide bali_bu_nyoman_tegas
    show bali_bu_nyoman_lega at hilir_nyoman
    with dissolve
    pause 0.5
    window show

    nyoman "Terima kasih, anak. Tidak banyak anak muda yang masih peduli soal ini."

    window hide
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

    narrator "Bima tersenyum kecil, mencium peluang dari kebimbangan Wira."
    window hide
    window show
    bima "Nah, berarti kamu juga setuju kalau ini bisa didiskusikan lagi, kan? Bu Nyoman, kita bisa duduk lagi"

    window hide
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
    window show

    narrator "Bima langsung tersenyum lebar dan menepuk bahu Wira."
    window hide
    window show
    bima "Nah, ini baru anak muda yang realistis! Bu Nyoman, dengarkan teman kamu ini"

    window hide
    hide bali_bu_nyoman_tegas
    show bali_bu_nyoman_kecewa at hilir_nyoman
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
    stop sfx1
    stop sfx2
    stop music fadeout 1.0
    play music "sound/Gambuh Gamelan (Khidmat) BGM.MP3" fadein 1.0
    play sfx1 "sound/AnginKuat SFX.mp3"
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
    call screen bali_scene3_pilih

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
    stop sfx1
    stop music fadeout 1.0
    play music "sound/Gambuh Gamelan (Semangat) BGM.MP3" fadein 1.0
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
    stop music fadeout 1.0
    play music "sound/Pa_Pompang BGM.MP3" fadein 1.0
    window hide
    pause 1.0
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
    call screen toraja_scene1_pilih

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
    call screen toraja_scene2_pilih

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
    call screen toraja_scene3_pilih

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
        garuda "Checkpoint Toraja selesai. Total poinmu di Toraja: Minus [-1 * toraja_points]"

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

    jump ending_final



# ==============================================================
# SECTION 12: ENDING FINAL
# ==============================================================
# --- CLOSING: GOOD ENDING ---
image closing_good_teras        = im.Scale("closing_good_teras.png", 1920, 1080)
image closing_good_minum_teh    = im.Scale("closing_good_minum_teh.png", 1920, 1080)
image closing_good_taman        = im.Scale("closing_good_taman.png", 1920, 1080)
image closing_good_pipit_bahu   = im.Scale("closing_good_pipit_bahu.png", 1920, 1080)
image closing_flashback_taman   = im.Scale("prolog_taman_kota_sore.png", 1920, 1080)
image closing_good_zoomout      = im.Scale("closing_good_zoomout.png", 1920, 1080)

# --- CLOSING: BAD ENDING ---
image closing_bad_kamar         = im.Scale("closing_bad_kamar.png", 1920, 1080)
image closing_bad_jendela       = im.Scale("closing_bad_jendela.png", 1920, 1080)
image closing_bad_jalan_sepi    = im.Scale("closing_bad_jalan_sepi.png", 1920, 1080)
image closing_bad_nenek_jatuh        = im.Scale("closing_bad_nenek_jatuh.png", 1920, 1080)
image closing_bad_nenek_jatuh_Wira  = im.Scale("closing_bad_nenek_jatuh_Wira.png", 1920, 1080)
image closing_bad_cermin        = im.Scale("closing_bad_cermin.png", 1920, 1080)
image closing_bad_sudut_kamar   = im.Scale("closing_bad_sudut_kamar.png", 1920, 1080)

# --- CLOSING: SPRITE BARU ---
image wira_dewasa_senyum        = "wira_dewasa_senyum.png"
image wira_dewasa_marah         = "wira_dewasa_marah.png"
image wira_dewasa_pusing        = "wira_dewasa_pusing.png"
image wira_sedih                = "wira_sedih.png"
image nenek_senyum              = "nenek_senyum.png"
image nenek_melambai            = "nenek_melambai.png"
image nenek_nunjuk              = "nenek_nunjuk.png"

label ending_final:

    scene black
    with fade
    window hide
    pause 1.5

    if player_points >= 120:
        jump closing_good_ending
    else:
        jump closing_bad_ending

# ==============================================================
# GOOD ENDING
# ==============================================================
transform pipit_kursi:
    xalign 0.9
    yalign 0.8
    zoom 0.3

transform pipit_bahu:
    xalign 0.5
    yalign 0.4
    zoom 0.15

transform wira_taman:
    xalign 0.35
    yalign 0.5
    zoom 0.6

label closing_good_ending:

    # --- Scene 1: Teras Rumah Nenek ---
    scene black
    with dissolve
    pause 0.5

    scene closing_good_teras
    with dissolve

    window show
    narrator "Wira membuka mata."
    narrator "Pemandangan pertama yang ia tangkap adalah teras rumah nenek, tapi kali ini berbeda dari yang ia ingat."
    narrator "Pagar kayu yang dulu keropos sudah diganti. Bunga bunga tumbuh di pot tanah liat. Anak anak berlarian di jalan."
    window hide

    pause 1.0

    play sound "sound/Kota BGM.mp3"    # suara percakapan warga + tawa anak-anak

    window show
    narrator "Suara tawa anak anak mengalir dari ujung gang. Seseorang menyapa tetangganya. Ada yang berbagi makanan di teras sebelah."
    window hide

    pause 1.0

    # Nenek masuk
    show nenek_senyum at wright_small
    with dissolve
    window show

    nenek "Nak Wira... sudah bangun? Nenek buatkan teh manis pakai jahe. Dingin dingin begini enak."

    show wira_dewasa_terharu at wleft_small
    with dissolve

    wira "Iya, Nek. Makasih."

    # --- Scene 2: Minum Teh Bersama ---
    scene closing_good_minum_teh
    with dissolve
    window show

    wira "Nek... kampung kita... kok sekarang jadi lebih... hidup?"

    nenek "Hidup? Memang pernah mati?"

    wira "Bukan gitu, Nek. Maksud aku... dulu kayaknya sepi. Sekarang jadi lebih rame. Orang orang kayak... lebih peduli sama satu sama lain."

    nenek "Mungkin... karena ada yang belajar sesuatu dari perjalanannya. Dan bawa pulang pelajaran itu."

    window hide

    show wira_dewasa_terharu at wleft_small
    with dissolve
    pause 1.0

    window show
    narrator "Wira terdiam. Dia merasa neneknya tahu lebih dari yang dia kira."
    window hide

    # --- Scene 3: Taman Belakang, Pipit Datang ---
    scene closing_good_taman
    with dissolve
    pause 1.0

    stop sound fadeout 1.0
    play sound "sound/Suara pipit SFX.mp3"    # suara kicauan + angin

    # 1. Munculkan Wira dan Pipit terlebih dahulu di sini
    show wira_dewasa_terharu as wira at wira_taman
    show pipit_standing as pipit at pipit_kursi
    with dissolve # Berikan efek transisi saat mereka berdua muncul

    # 2. Baru setelah itu teks narasi dimulai
    window show
    narrator "Wira pergi menghampiri pohon besar di taman belakang rumah nenek."
    narrator "Seekor burung pipit kecil hinggap di dekatnya"
    window hide

    pause 1.0

    window show
    narrator "Suara kicauannya... familier. Persis seperti suara Garuda setiap kali memberi saran di game."
    window hide

    pause 0.5

    # 1. Munculkan sprite terharu dan burung pipit
    show wira_dewasa_terharu as wira at wira_taman
    show pipit_standing as pipit at pipit_kursi
    with dissolve
    
    window show

    # 2. Dialog ini akan menahan gambar di atas agar tetap terlihat oleh pemain
    wira "Pipit...?"
  
    # 3. Ganti gambar wira dengan ekspresi baru (menggunakan alias 'as wira' agar otomatis menggantikan yang lama)
    show wira_dewasa_pipit as wira at wira_taman
    hide pipit 
    with dissolve
    window hide

    pause 1.5

    # --- Kilas Balik ---
    scene black
    with dissolve
    pause 0.5

    scene closing_flashback_taman
    with dissolve

    show wira duduk sangkar at wira_duduk_sangkar
    with dissolve
    pause 1.0

    window show
    wira "Ayo... keluar sebentar..."
    window hide
    pause 0.5

    show wira ketiup angin at wira_ketiup_angin
    show pipit hinggap di sangkar at pipit_sangkar
    with dissolve
    pause 1.0

    window show
    wira "Pipit?! Tunggu!"
    window hide
    pause 0.5

    show sangkar at sangkar_kosong
    show wira ngejar at wira_ketiup_angin
    show pipit terbang at atas_sangkar
    with dissolve
    pause 0.5

    show pipit terbang at pipit_leaving
    with ease
    hide pipit terbang
    pause 0.5

    window show
    wira "JANGAN TINGGALIN AKU! PIPIT!!!"
    pause 1.0
    window hide

    scene closing_flashback_taman
    show wira sedih at wira_ketiup_angin
    with dissolve
    pause 2.0

    scene black
    with dissolve
    pause 0.5

    # Kembali ke taman
    scene closing_good_taman
    with dissolve
    pause 1.0

    show wira_dewasa_pipit as wira at wira_taman
    with dissolve

    window show
    wira "Kamu... tidak pernah benar benar pergi, ya? Kamu bahkan sampai menemani aku di dalam game itu"
    window hide

    pause 0.5

    play sound "sound/Suara pipit SFX.mp3"
    pause 1.0

    window show
    narrator "Burung pipit itu berkicau riang."
    window hide

    pause 1.5

    # --- Zoom Out + Quote Penutup ---
    scene closing_good_zoomout
    with dissolve
    pause 2.0

    stop sound fadeout 2.0

    window show
    narrator "\"Kearifan sejati tidak hanya mendamaikan dunia luar...\""
    pause 1.0
    narrator "\"...tetapi juga mempertemukan kita kembali dengan bagian diri kita yang paling murni.\""
    window hide

    pause 2.0

    scene black
    with dissolve
    pause 1.5

    return


# ==============================================================
# BAD ENDING
# ==============================================================

label closing_bad_ending:

    # --- Scene 1: Kamar Wira, Bangun Kaget ---
    scene closing_bad_kamar
    with dissolve
    pause 0.5

    show wira_dewasa_pusing at wleft_lower
    with dissolve

    play sound "sound/AnginKuat SFX.mp3"    # suara napas tidak teratur
    pause 1.5
    stop sound fadeout 1.0

    window show
    wira "Aku... gagal. Aku gagal total."
    window hide

    pause 1.0

    # --- Scene 2: Melihat dari Jendela ---
    scene closing_bad_jendela
    with dissolve
    pause 0.5

    play sound "sound/Angin SFX.mp3"    # keheningan hampa, minim interaksi

    scene closing_bad_jalan_sepi
    with dissolve

    window show
    narrator "Di luar, kampung itu terasa asing."
    narrator "Semua orang yang berlalu lalang memegang handphone masing masing. Headphone di telinga. Mata tertuju ke layar. Tidak ada yang saling menyapa."
    window hide

    pause 1.5

    # Nenek jatuh, orang-orang merekam
    scene closing_bad_nenek_jatuh
    with dissolve
    pause 0.5

    window show
    narrator "Seorang nenek jatuh di halaman depan."
    narrator "Orang orang di sekitarnya mengeluarkan HP. Merekam. Tidak ada yang bergerak untuk membantu."
    window hide

    pause 1.0

    scene closing_bad_nenek_jatuh_Wira
    with dissolve
    window show

    wira "Bantu dia, dong... kenapa kalian cuma lihat?"

    window hide
    pause 1.0

    window show
    narrator "Tapi Wira sendiri tidak bergerak."
    narrator "Dia baru menyadari bahwa dia melakukan hal yang sama. Hanya melihat. Diam."
    window hide

    pause 1.5

    # --- Scene 3: Nenek Memanggil ---
    stop sound fadeout 1.0
    
    scene closing_bad_kamar
    with dissolve
    pause 0.5

    show wira_dewasa_marah at wleft_lower
    show nenek_senyum as nenek at wright_lower
    with dissolve
    

    window show
    nenek "Wira... kamu sudah bangun? Nenek buatkan teh. Turun, ya."

    wira "Gak usah! Aku gak mau teh! Aku mau sendirian!"

    hide nenek
    show nenek_melambai at wright_lower
    with dissolve

    window hide
    pause 0.5

    window show
    nenek "Baiklah... nanti kalau kamu mau, ambil saja di meja. Nenek taruh tehnya di meja."
    window hide

    hide nenek_melambai
    with dissolve
    pause 0.5

    play sound "sound/langkahkayu.mp3"    # langkah kaki perlahan menjauh
    pause 1.5
    stop sound fadeout 1.0

    window show
    narrator "Keheningan."
    narrator "Wira terdiam. Tangannya gemetar."
    narrator "Dia tahu dia bersikap buruk. Tapi dia tidak bisa berbuat lain. Marah adalah satu satunya cara yang dia ketahui untuk bertahan."
    window hide

    pause 1.5

    # --- Scene 4: Di Depan Cermin ---
    scene closing_bad_kamar 
    with dissolve
    pause 0.5

    scene closing_bad_cermin
    with dissolve
    window show
    narrator "Wira berdiri di depan cermin. Wajahnya lelah, Matanya merah, dan merasa Wira ada kehilangan sesuatu."
    window hide

    pause 1.0

    window show
    wira "Kamu... kamu egois!"
    pause 0.3
    wira "Kamu kasar! Kamu seenaknya sendiri!"
    pause 0.3
    wira "Ga heran semua orang di game benci kamu!"
    pause 0.3
    wira "Ga heran... ga heran sekarang semua orang di sini juga jadi egois."
    pause 0.3
    wira "Karena siapa? Karena kamu!"
    window hide
    with dissolve

    pause 1.0

    # --- Scene 5: Sudut Kamar, Quote Penutup ---
    scene closing_bad_sudut_kamar
    with dissolve

    play sound "sound/Clock SFX.mp3"    # suara AC yang monoton
    pause 2.0

    window show
    narrator "\"Ketika kita memaksa dunia untuk tunduk pada keegoisan kita...\""
    pause 1.0
    narrator "\"...kita hanya akan mewariskan kehancuran baik di tanah orang lain, maupun di rumah kita sendiri.\""
    window hide

    pause 2.0

    stop sound fadeout 2.0

    scene black
    with dissolve
    pause 1.5

    return

    # This ends the game for now.
