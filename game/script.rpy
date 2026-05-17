# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define wira = Character("Wira", who_color = "#ffffff")
define narrator =  Character("???", who_color = "#000000")
define garuda = Character("Garuda",who_color ="#C92E08" )
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

# PROLOG / TERAS PAGI
image wira_ceria = "wira_ceria.png"
image bg_prolog_teras_pagi = "prolog_teras_pagi.png"
image pipit standing = "pipit_standing.png"
image pipit terbang = "pipit_terbang.png"
image wiranpipit = "wira_dan_pipit.png"
image wiranpipit serius = "wira_dan_pipit_serius.png"
image wiranpipit nunduk = "wira_dan_pipit_nunduk.png"
image wiranpipit terharu = "wira_dan_pipit_terharu.png"

# MINANGKABAU
image rumah_gadang = im.Scale("rumah_gadang.png",1920,1080)
image wira_bingung = "wira_dewasa_bingung.png"
image garuda_berdiri = "garuda_default.png"
image garuda_berbicara = "garuda_bicara.png"
image wira_tunjuk = "wira_tunjuk2.png"
image garuda_ceria = "garuda_ceria.png"


transform pipit_initial:
    xalign 0.4
    yalign 0.495
    zoom 0.13

transform wleft_small:
    xalign 0.23
    yalign 0.65
    zoom 0.6

transform wright_small:
    xalign 0.77
    yalign 0.65
    zoom 0.6

transform wcenter_small:
    xalign 0.5
    yalign 0.5
    zoom 0.6

transform teras:
    xalign 0.5
    yalign 0.72
    zoom 0.6


transform terasnew:
    xalign 0.5
    yalign 0.72
    zoom 0.65

transform ukuransetengah :
    zoom 0.5

transform ukuranseperempat :
    zoom 0.25
# ASET PASAR  PILIHAN BUTTONS
image pasar_a_idle = im.Scale("pasar_a_idle.png", 700, 800)
image pasar_a_hover = im.Scale("pasar_a_hover.png", 700, 800)
image pasar_b_idle = im.Scale("pasar_b_idle.png", 700, 800)
image pasar_b_hover = im.Scale("pasar_b_hover.png", 700, 800)
image pasar_c_idle = im.Scale("pasar_c_idle.png", 700, 800)
image pasar_c_hover = im.Scale("pasar_c_hover.png", 700, 800)

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


    #minangkabau


    scene black
    scene rumah_gadang 
    with dissolve

    show wira_bingung at wleft_small
    with dissolve 
    
    wira " Itu..rumahnya kok atapnya kayak tanduk kerbau gitu? "
    wira "Bangunannya gede banget! Tapi kelihatannya udah lama nggak dirawat." 

    window hide
    show garuda_berdiri at wright_small
    with dissolve
    pause 0.5
    window show
    hide wira_bingung
    play music "sound/talempongminang1.mp3" fadein 2 
    play sound "sound/aliran air.mp3" fadein 1.0 loop
    garuda "Selamat datang di Nagari Minangkabau, Wira!"
    hide garuda_berdiri

    show wira_bingung at wleft_small
    with dissolve 
    wira "Nagari? Ini semacam desa ya?"
    hide wira_bingung

    show garuda_berbicara at wright_small
    
    garuda "Lebih dari itu. Nagari adalah unit kehidupan masyarakat Minangkabau. "
    garuda "Tempat adat dijalankan, keputusan diambil bersama, dan identitas dijaga turun temurun "
    garuda "Rumah Gadang yang kamu lihat itu ... adalah jantungnya."
    hide garuda_berbicara
    show wira_tunjuk at wleft_small
    with dissolve

    wira "Jantungnya? Kelihatan sudah mau roboh di sudut sana."
    hide wira_tunjuk

    show garuda_ceria at wcenter_small

    garuda "Tepat sekali! Itulah kenapa kamu ada di sini."
    stop music fadeout 1.0
    stop sound fadeout 1.0
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
    show garuda_berbicara at wright_small
    play music "sound/talempongminang2.mp3" fadein 2
    garuda "Inilah misimu di Minangkaubau, Wira. Nagari ini sedang di persimpangan. Terdapat tiga krisis yang harus kamu hadapi."
    hide garuda_berbicara
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
    show garuda_berbicara at wcenter_small
    with dissolve
    pause 0.5
    garuda " Ingat "
    garuda "Setiap pilihanmu akan mencerminkan siapa dirimu sebenarnya."
    window hide
    stop music fadeout 2.0
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

    # ASET RUMAH GADANG  OPENING DAN PILIHAN
    image openingscene_rumahgadang = im.Scale("openingscene_rumahgadang.png",1920,1080)
    image aset_pilihana_rumahgadang = im.Scale("aset_pilihana_rumahgadang.png",1920,1080)
    image aset_pilihanb_rumahgadang = im.Scale("aset_pilihanb_rumahgadang.png",1920,1080)
    image aset_pilihanc_rumahgadang = im.Scale("aset_pilihanc_rumahgadang.png",1920,1080)
    define audio.audioaliranair = "audio/aliran_air.mp3"
    define audio.talempongminang1 = "audio/talempong_minang1.mp3"
    define audio.talempongminang2 = "audio/talempong_minang2.mp3"

    # ASET PASAR  OPENING DAN PILIHAN
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
    scene forum
    with dissolve
    window show
    play music "sound/langkahkayu.mp3" fadein 1.0

    
    garuda "Perkenalkan empat pilar nagari."
    garuda "Datuak Rajo Nan Sati, Niniak Mamak, penjaga garis keturunan dan hukum adat."
    garuda "Buya Hamid, Alim Ulama, penjaga syariat Islam dalam kehidupan masyarakat."
    garuda "Dr. Sari Rahmawati, Cadiak Pandai, kaum intelektual yang membawa pengetahuan dunia luar."
    garuda "Ibu Rosma, Bundo Kanduang, simbol kebijaksanaan perempuan dalam nagari."
    stop music fadeout 1.0

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

    # PILIHAN A  MENDENGARKAN SEMUA UNSUR
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
    show garuda_berbicara at wcenter_small
    with dissolve
    garuda "Kamu baru saja memahami inti dari musyawarah mufakat. Kebenaran tidak dimiliki satu pihak saja. Ia lahir dari pertemuan berbagai sudut pandang."
    
    window hide
    pause 1.0
    window show
    
    $ player_points += 20
    hide garuda_berbicara
    narrator "Anda mendapat 20 poin! Total poin: [player_points]"
    
    jump scene_rumahgadang_krisis

    # PILIHAN B  HANYA MENDENGARKAN TETUA
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
    show garuda_berbicara at wcenter_small
    with dissolve
    garuda "Adat Minangkabau bukan hierarki buta, Wira. Ia adalah harmoni. Ketika kamu memilih untuk hanya mendengar satu suara, kamu merusak keseimbangan yang dibangun berabad abad."
    
    window hide
    pause 1.0
    window show
    
    $ player_points = 10
    narrator "Anda kehilangan 10 poin! Total poin: [player_points]"
    
    jump scene_rumahgadang_krisis

    # PILIHAN C  MENGABAIKAN FORUM
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
    show garuda_berbicara at wcenter_small
    with dissolve
    garuda "Wira....Kehadiranmu di ruangan ini punya arti. Ketika kamu memilih untuk tidak hadir sepenuhnya, kamu membiarkan konflik tumbuh tanpa ada yang mau memahami semua sisi."
    
    window hide
    pause 1.0
    window show
    
    $ player_points = 20
    narrator "Anda kehilangan 20 poin! Total poin: [player_points]"
    
    jump scene_rumahgadang_krisis

    
label scene_rumahgadang_krisis:
    scene black
    with fade
    
    window hide
    pause 1.0
    
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
    garuda "Rumah Gadang bukan sekadar bangunan, Wira. Ia adalah silsilah keluarga yang tertulis dalam kayu. Setiap ruangan mencerminkan posisi perempuan sebagai pemegang harta pusaka. Setiap ukiran adalah bahasa yang berbicara tentang falsafah hidup."
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
    
    $ player_points = 25
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

    # ================= SCREEN PILIHAN FESTIVAL KAMPUNG =================
    screen pilihan_festival_kampung():
        
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
                    idle "pilihana_festivalkampung" 
                    hover "pilihana_festivalkampung" 
                    at ukuransetengah
                    action Jump("pilihan_festival_a")
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
                    idle "pilihanb_festivalkampung" 
                    hover "pilihanb_festivalkampung"
                    at ukuransetengah
                    action Jump("pilihan_festival_b")
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
                    idle "pilihanc_festivalkampung" 
                    hover "pilihanc_festivalkampung" 
                    at ukuransetengah
                    action Jump("pilihan_festival_c")
                    hovered SetScreenVariable("hovered", "C")
                    unhovered SetScreenVariable("hovered", None)
                text "PILIHAN C":
                    xalign 0.5
                    size 20

    # ================= SCREEN PILIHAN WAYANG =================
    screen pilihan_wayang():
        
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
                spacing 10
                imagebutton:
                    idle "pilihana_wayang_idle" 
                    hover "pilihana_wayang_hover"
                    at ukuranseperempat
                    action Jump("pilihan_wayang_a")
                    hovered SetScreenVariable("hovered", "A")
                    unhovered SetScreenVariable("hovered", None)
                text "PILIHAN A":
                    xalign 0.5
                    size 20

            # ================= B =================
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 10
                imagebutton:
                    idle "pilihanb_wayang_idle"
                    hover "pilihanb_wayang_hover"
                    at ukuranseperempat
                    action Jump("pilihan_wayang_b")
                    hovered SetScreenVariable("hovered", "B")
                    unhovered SetScreenVariable("hovered", None)
                text "PILIHAN B":
                    xalign 0.5
                    size 20

            # ================= C =================
            vbox:
                xalign 0.5
                yalign 0.5
                spacing 10
                imagebutton:
                    idle "pilihanc_wayang_idle"
                    hover "pilihanc_wayang_hover"
                    at ukuranseperempat
                    action Jump("pilihan_wayang_c")
                    hovered SetScreenVariable("hovered", "C")
                    unhovered SetScreenVariable("hovered", None)
                text "PILIHAN C":
                    xalign 0.5
                    size 20

    # ================= SCREEN PILIHAN TATA KRAMA =================
    screen pilihan_tata_krama():
        
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
                    idle "pilihana_scenetatakrama" 
                    hover "pilihana_scenetatakrama"
                    at ukuransetengah 
                    action Jump("pilihan_krama_a")
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
                    idle "pilihanb_scenetatakrama" 
                    hover "pilihanb_scenetatakrama"
                    at ukuransetengah
                    action Jump("pilihan_krama_b")
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
                    idle "pilihanc_scenetatakrama"
                    hover "pilihanc_scenetatakrama"
                    at ukuransetengah
                    action Jump("pilihan_krama_c")
                    hovered SetScreenVariable("hovered", "C")
                    unhovered SetScreenVariable("hovered", None)
                text "PILIHAN C":
                    xalign 0.5
                    size 20

    # ================= SCENE PASAR  KRISIS =================
label scene_pasar_krisis:
    scene black
    with fade
    
    window hide
    pause 1.0
    
    scene visual_awal_scenepasar
    with dissolve
    window show
    
    narrator "Setelah mengatasi situasi Rumah Gadang, Garuda membawa Wira ke pasar nagari. Suasana begitu ramai dan hidup..."
    
    pause 1.0
    play music "sound/suara_pasar.mp3" fadein 1.0 loop
    play sound "sound/talempongminang1.mp3" fadein 1.0 loop
    show garuda_berbicara at wcenter_small
    with dissolve
    
    garuda "Ini adalah tantangan terakhir, Wira. Sebuah perusahaan besar dari kota menawarkan investasi besar untuk nagari."
    
    pause 1.0
    
    garuda "Tapi ada yang janggal. Mereka ingin mengubah cara hidup masyarakat di sini. Semua orang menjadi bingung."
    
    hide garuda_berbicara
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
    stop music fadeout 1.0
    stop sound fadeout 1.0
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
    
    $ player_points = 5
    narrator "Anda kehilangan 5 poin! Total poin: [player_points]"
    
    jump ending_minangkabau

    # PILIHAN PASAR C
label pilihan_pasar_c:
    scene pasar_c_solved
    with dissolve
    window show

    garuda "Wira...kamu baru saja memvalidasi penghancuran fondasi sebuah nagari dengan tangan kamu sendiri"
    
    garuda "Nagari yang kehilangan prinsipnya bukan lagi nagari yang sama. Ia hanya nama tanpa jiwa."
    stop music fadeout 1.0
    stop sound fadeout 1.0
    pause 0.5
    
    $ player_points = 30
    narrator "Anda kehilangan 30 poin! Total poin: [player_points]"
    
    jump ending_minangkabau

    # ================= ENDING MINANGKABAU =================
label ending_minangkabau:
    scene black
    with fade
    play music "sound/talempongminang2.mp3" fadein 1.0 loop
    window hide
    pause 1.5
    
    show garuda_berbicara at wcenter_small
    with dissolve
    window show
    
    if player_points >= 65:
        # POIN TINGGI (6575)
        hide garuda_berbicara
        scene poin_tinggi
        with dissolve
        
        
        garuda "Kamu mulai memahami bahwa demokrasi yang sesungguhnya bukan tentang suara terbanyak. Ini tentang keselarasan semua unsur dan bahwa prinsip bukan penghalang kemajuan, ini adalah kompas yang memastikan kita tidak tersesat di tengah perjalanan."
        
    elif player_points >= 25:
        # POIN SEDANG (2560)
        hide garuda_berbicara
        scene poin_sedang
        with dissolve
        
        
        garuda "Ada momen di mana kamu membuka matamu dan momen di mana kamu masih memilih jalan yang mudah. Nagari ini mengajarkan bahwa setengah hadir lebih berbahaya dari tidak hadir sama sekali."
        
    else:
        # POIN RENDAH (<25)
        hide garuda_berbicara
        scene poin_rendah
        with dissolve
        
        
        garuda "Wira...di setiap piluhan yang kamu anggap pragmatis, kamu sebenarnya sedang membiarkan sesuatu yang orang lain jaga dengan nyawa mereka selama berabadabad runtuh perlahan. Adat bukan museum."
    
    window hide
    pause 2.0
    stop music fadeout 1.0
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
image visual_awal_betawi = im.Scale("visual_awal_betawi.png", 1920, 1080)
# ASET PILIHAN  FESTIVAL KAMPUNG
image pilihana_festivalkampung = "pilihana_festivalkampung.png"
image pilihanb_festivalkampung = "pilihanb_festivalkampung.png"
image pilihanc_festivalkampung = "pilihanc_festivalkampung.png"

# ASET PILIHAN  SCENE TATA KRAMA (KERATON JAWA)
image pilihana_scenetatakrama  = "pilihana_scenetatakrama.png"
image pilihanb_scenetatakrama = "pilihanb_scenetatakrama.png"
image pilihanc_scenetatakrama = "pilihanc_scenetatakrama.png"
image ending_jawabetawi = im.Scale("ending_jawabetawi.png", 1920, 1080)

call chapter_jawa_betawi

# ===== CHAPTER JAWA DAN BETAWI =====
# Pertarungan Dalang Terakhir
# Checkpoint 2

label chapter_jawa_betawi:
    
    # ===== TRANSISI MEMASUKI BETAWI & KERATON JAWA =====
    scene visual_awal_betawi
    with fade
    pause 1.0
    play sound "sound/adzan.mp3" fadein 1.0 
    # Visual: Layar gelap dengan cahaya kuning menyeruak perlahan
    narrator "Cahaya kuning menyeruak perlahan dari kegelapan. Wira berdiri di sebuah Kampung Betawi di pinggiran kota. Dinding bercat putih kusam dihiasi ornamen khas Betawi (motif gigi balang, pucuk rebung, dan warna merah hijau yang mencolok.)"
    stop sound fadeout 1.0
    play music "sound/jalijali.mp3" fadein 1.0 loop
    window hide
    pause 2.0
    window show
    
    garuda "Selamat datang di Kampung Betawi, Wira."
    garuda "Besok malam, kampung ini mengadakan Festival Budaya Betawi tahunan. Tapi ada masalah besar yang mengancam festival ini sebelum sempat dimulai."
    
    wira "Masalah apa?"
    
    garuda "Kamu akan segera melihatnya sendiri. Di sinilah petualanganmu dimulai. Setelah ini kita akan melanjutkan ke jantung Keraton Jawa."
    
    wira "Dua tempat sekaligus?"
    
    garuda "Karena keduanya berbagi satu pertanyaan yang sama yaitu bagaimana seni dan budaya bisa bertahan ketika dunia terus berubah?"
    garuda "Di Betawi, kamu akan menyaksikan pergulatan itu dari luar. Di Keraton, kamu akan masuk ke dalamnya."
    stop music fadeout 1.0
    # ===== PENJELASAN MISI OLEH GARUDA =====
    scene penjelasan_misi_betawi
    with dissolve
    
    garuda "Misimu di sini terbagi dalam tiga babak."
    garuda "Pertama, Festival Kampung yang hampir berantakan karena konflik kepanitiaan."
    garuda "Kedua, Pertunjukan Wayang yang terancam ditinggalkan generasi muda."
    garuda "Ketiga, pelajaran tata krama di dalam Keraton, di mana satu langkah bisa merusak segalanya."
    garuda "Setiap pilihanmu akan meninggalkan bekas."
    
    wira "Oke..."
    stop music fadeout 1.0
    window hide
    pause 1.0
    window show
    
    # ===== SCENE FESTIVAL KAMPUNG (KEPANITIAAN YANG RETAK) =====
    scene rapat_awal_betawi
    with fade
    play music "sound/berdebat.mp3" fadein 1.0 loop
    narrator "Sore menjelang petang. Di halaman rumah di kampung, warga berkumpul mengelilingi meja kayu penuh kertas dan jadwal."
    
    Bang_Rojak "(marah) Sudah dari dulu festivalnya pakai format yang sama! Lenong, tanjidor, ondel ondel, lalu makan bersama. Itu sudah pakem! Sari mau nubah apa lagi?"
    
    Sari "Bang, tahun lalu cuma dua puluh orang yang nonton sampai selesai! Generasi muda nggak tertarik kalau formatnya gitu gitu aja."
    Sari "Saya usul kita gabungin sama pertunjukan modern, ada sesi story telling dan dokumentasi di media sosial."
    
    Bang_Rojak "Itu bukan festival budaya! Itu konten TikTok! Budaya bukan tontonan, budaya adalah kehidupan!"
    
    Sari "Tapi kalau nggak ada yang nonton, siapa yang akan mewarisi?"
    scene rapat_betawi_wira_datang
    Engkong_Ali "Kamu...anak baru di kampung ini ya?"
    
    wira "Saya...nggak mau ganggu, Ngkong."
    
    Engkong_Ali "(tersenyum) Justru kamu yang paling nggak mengganggu di sini. Dua orang itu sudah lupa caranya mendengar. Kamu, anak muda, belum lupa."
    
    garuda "Ini masalah yang lebih dalam dari sekadar format festival. Bang Rojak mewakili mereka yang takut kehilangan akar. Sari mewakili mereka yang takut mati karena tidak relevan."
    garuda "Kamu ada di tengahtengah. Tentukan cara kamu merespons konflik ini."
    stop music fadeout 1.0
    # ===== PILIHAN FESTIVAL KAMPUNG =====
    show screen show_points
    call screen pilihan_festival_kampung
    
    label pilihan_festival_a:
        $ player_points += 25
        
        wira "Bang Rojak, Kak Sari...dua duanya ada benarnya."
        wira "Kalau boleh, kita duduk bareng dulu. Bang Rojak bisa ceritain bagian mana dari festival yang paling penting untuk dijaga."
        wira "Kak Sari bisa kasih tau inovasinya yang mana yang bisa jalan tanpa ngorbanin inti acara."
        wira "Engkong Ali bisa jadi penengah. Kita cari format yang jaga akar tapi nggak ngusir generasi baru."
        
        Engkong_Ali "(tersenyum lebar) Anak ini...tahu caranya membuat orang merasa didengar sebelum meminta mereka mendengar. Ayo, kita coba cara anak ini."
        
        Bang_Rojak "Baiklah...tapi lenong tetap harus ada."
        
        Sari "Setuju, Bang. Lenong tetap jadi bintang utama. Saya hanya ingin lebih banyak orang yang kenal bintangnya."
        
        garuda "Kamu baru saja mempraktikkan sesuatu yang lebih tua dari semua tradisi di kampung ini. Kamu mendengarkan sebelum memimpin. Ini dasar dari kepercayaan."
        
        window hide
        pause 1.0
        window show
        jump lanjut_ke_wayang
    
    label pilihan_festival_b:
        $ player_points = 15
        
        wira "Menurut gue, Bang Rojak yang bener. Festival tradisional ya harus tradisional. Format lama dipertahanin aja, nggak perlu diubah ubah."
        scene ibu_sari_marah
        Sari "(kecewa, pergi dengan ekspresi marah)"
        
        garuda "Memihak memang terasa tegas. Tapi dalam komunitas yang hidupnya dari kebersamaan, memilih satu pihak tanpa mendengar yang lain bukan ketegasan."
        garuda "Ini pengkhianatan terhadap musyawarah."
        
        window hide
        pause 1.0
        window show
        jump lanjut_ke_wayang
    
    label pilihan_festival_c:
        $ player_points = 5
        scene visualpilihanC_wiraberide
        wira "Udah, gini aja. Gue punya ide. Kita bikin festival hybrid, separuh tradisional separuh modern, terus live streaming semuanya. Nggak perlu debat panjang."
        scene visualpilihanC_pakrojakmarah
        Bang_Rojak "Siapa kamu mau memutuskan urusan kampung kami?"
        
        garuda "Ide yang baik pun bisa ditolak kalau datang tanpa menghormati proses. Di komunitas yang menghargai adat, cara kamu mengajukan sesuatu sama pentingnya dengan isi usulanmu."
        
        window hide
        pause 1.0
        window show
    
    label lanjut_ke_wayang:
    
    # ===== SCENE WAYANG YANG DIANGGAP KUNO =====
    scene bg_pewayangan_pilihan
    with dissolve
    
    narrator "Malam hari, festival sudah berdiri. Lampu kelap kelip menghiasi panggung. Terdapat sekelompok remaja di depan panggung menonton namun tidak antusias."
    window hide
    pause 0.5
    window show

    scene scenewayang_kekecewaanPakSugeng
    play sound "sound/gamelanpelan.mp3" fadein 1.0 loop
    Dimas "Bro, ini acara apaan sih. Bayangannya doang yang keliatan, suaranya lebay, nggak ngerti ceritanya apa. Nonton anime aja lebih seru."
    Teman_Dimas "Ssst...nanti didenger Pak Sugeng."
    
    Pak_Sugeng "Sudah tiga generasi keluargaku menjaga wayang ini. Kakekku yang mengukir Arjuna itu. Kalau aku pergi nanti, tidak ada yang meneruskan."
    
    garuda "Ini lebih dari sekadar pertunjukan, Wira. Pak Sugeng adalah dalang terakhir di kampung ini. Wayang bukan hanya seni, ia adalah ensiklopedia filsafat Jawa."
    garuda "Lakon Mahabharata dan Ramayana mengandung ajaran tentang dharma, keadilan, dan kesetiaan yang bertahan ribuan tahun. Tapi kalau tidak ada yang mau belajar..."
    
    wira "...semuanya hilang."
    
    garuda "Tepat. Dimas bukan musuhnya. Ia hanya tidak tahu. Belum ada yang pernah jelaskan kepadanya."
    
    Pak_Sugeng "Anak muda...kamu punya pendapat tentang ini?"
    
    garuda "Wira, ini momen penting. Pak Sugeng butuh pembelaan, tetapi Dimas butuh jembatan, bukan tembok. Bagaimana kamu merespons?"
    stop sound fadeout 1.0
    # ===== PILIHAN WAYANG =====
    show screen show_points
    call screen pilihan_wayang
    
    label pilihan_wayang_a:
        $ player_points += 25
        scene visualpilihanA_wayang
        with dissolve
        wira "Lo tau nggak, Dimas, karakter Arjuna yang dipaksa milih antara keluarga dan kebenaran itu…mirip banget sama dilema di film superhero kesukaan lo."
        wira "Wayang bukan cuma bayangbayang, bro. Itu cerita manusia yang udah dipikirin ribuan tahun lalu sebelum kita lahir."
        
        Pak_Sugeng "Ia menerangkan wayang dengan bahasa anak muda...Kakekku dulu bilang, dalang yang baik bisa bicara dalam bahasa siapapun yang duduk di depannya."
        
        Dimas "Pak...Arjuna itu ceritanya gimana sih sebenernya?"
        
        Pak_Sugeng "(tersenyum dan mulai mengangkat wayang Arjuna ke depan layar)"
        
        garuda "Kamu tidak membela wayang. Kamu membuka pintu menuju wayang. Itu jauh lebih baik."
        
        window hide
        pause 1.0
        window show
        jump lanjut_ke_keraton
    
    label pilihan_wayang_b:
        $ player_points = 10
        scene visualpilihanb_wiramemaksa
        with dissolve
        
        wira "Dimas, lo nggak boleh gitu. Ini budaya nenek moyang kita. Harus dihormatin, suka atau nggak suka."
        
        Dimas "(mengangguk kaku dan rasa penasaran yang sempat muncul langsung padam)"
        
        garuda "Kewajiban tanpa pemahaman melahirkan keterpaksaan, bukan kecintaan. Tradisi yang dipaksakan akan ditinggalkan begitu tidak ada yang memaksa lagi."
        
        window hide
        pause 1.0
        window show
        jump lanjut_ke_keraton
    
    label pilihan_wayang_c:
        $ player_points = 15
        scene visualpilihanc_wiramembujukadaptasi
        with dissolve
        
        wira "Pak Sugeng, mungkin wayangnya bisa didubbing pakai suara yang lebih kekinian? Atau ceritanya diganti yang lebih relevan gitu? Biar anak muda tertarik."
        
        Pak_Sugeng "(kecewa) Kalau ceritanya diganti, itu bukan wayang lagi, Nak. Itu hanya boneka kayu."
        
        garuda "Ada batas antara adaptasi yang menghidupkan dan perubahan yang menghilangkan jiwa. Kamu baru saja melewati batas itu."
        
        window hide
        pause 1.0
        window show
    
    label lanjut_ke_keraton:
    
    # ===== TRANSISI MEMASUKI KERATON JAWA =====
    scene visualmasuk_keratonjawa
    with fade
    play music "sound/sarwolaras.mp3" fadein 1.0 loop
    narrator "Cahaya festival Betawi perlahan memudar. Wira dan Garuda terangkat ke udara."
    narrator " Lampu lampu kampung mengecil seperti kunang kunang. Perlahan lahan, kompleks bangunan besar muncul di bawah cahaya bulan."
    narrator "Atap joglo berlapis lapis berwarna hijau tua dan emas. Alunalun luas dengan dua pohon beringin kembar yang berdiri seperti penjaga."
    
    window hide
    pause 2.0
    window show
    
    wira "Gue ngerasain sesuatu...tempat ini beda. Kerasa lebih...berat."
    
    garuda "Karena di sini, setiap hal bermakna. Cara kamu berdiri, berjalan, berbicara, bahkan cara kamu diam."
    garuda "Tempat ini memiliki bahasa yang dibangun selama berabadabad untuk menunjukkan rasa hormat kepada sesama dan kepada Sang Pencipta."
    
    wira "Berarti gue harus hatihati banget?"
    
    garuda "Bukan hanya hatihati, kamu harus hadir sepenuhnya."
    
    window hide
    pause 1.0
    window show
    
    scene wira_disambutraden
    with dissolve
    
    Kanjeng_Raden "Poro tamu ingkang kinurmatan sugeng rawuh ing Keraton." 
    Kanjeng_Raden "Mugi saged manggih karaharjan lan kawicaksanan ing mriki."
    
    wira "Itu artinya apa?"
    
    garuda "Beliau menyambut kamu dengan doa agar kamu menemukan keselamatan dan kebijaksanaan di sini. Di Keraton, bahasa bukan hanya komunikasi. Bahasa adalah penghormatan."
    stop music fadeout 1.0
    # ===== SCENE TATA KRAMA (BAHASA YANG BERBICARA) =====
    scene radenajak_masukkeraton
    with dissolve
    play sound "sound/gamelansebelah.mp3" fadein 1.0 loop
    narrator "Kanjeng Raden membawa Wira dan Garuda memasuki Pendopo utama Keraton. Ruangan besar beratap tinggi dengan tiangtiang kayu jati besar."
    narrator "Raden Mas Bagas sedang berlatih memainkan wayang sendirian. Ia penerus tradisi dalang Keraton, penerus generasi ketujuh belas."
    
    Raden_Mas_Bagas "Tamu dari luar. Jarang ada yang masuk sejauh ini. Saya Bagas, calon dalang Keraton generasi ketujuh belas."
    
    wira "Eh, sori…gue harusnya gimana ya di sini?"
    
    Kanjeng_Raden "Nggih, mboten menopo. Tamu ingkang sae punika ingkang purun nyuwun pirsa."
    
    garuda "Di Keraton, ada tata cara yang disebut unggahungguh." 
    garuda "Bukan untuk mempermalukan tamu, tapi untuk menjaga keselarasan ruang dan relasi antar manusia."
    garuda "Kamu akan menghadapi beberapa situasi. Bagaimana kamu merespons akan mencerminkan siapa kamu."
    garuda "Wira, Kanjeng Raden akan melewatimu. Apa yang kamu lakukan?"
    
    # ===== PILIHAN TATA KRAMA =====
    show screen show_points
    call screen pilihan_tata_krama
    
    label pilihan_krama_a:
        $ player_points += 30
        scene visual_hormatdenganmaubelajar
        with dissolve
        wira "Kanjeng, maaf…tadi saya harusnya ngapain ya yang bener? Saya mau belajar tata caranya di sini."
        
        wira "(segera menyingkir ke tepi, sedikit membungkuk badan sebagai tanda hormat)"
        
        Kanjeng_Raden "(tersenyum) Yang paling sulit bukan belajar tata krama. Yang paling sulit adalah menyadari bahwa kamu belum tahu dan tidak malu untuk bertanya."
        
        Raden_Mas_Bagas "Jujur, saya kuliah di luar negeri empat tahun dan baru bisa nyantai di sini setelah enam bulan balik. Kamu baru masuk tapi udah nanya yang bener."
        
        garuda "Tata krama bukan tentang tunduk. Akan tetapi, tentang mengakui bahwa ada sesuatu yang lebih besar dari dirimu sendiri di dalam ruangan ini"
        garuda " dan kamu memilih untuk hadir dengan hormat bukan dengan ego."
        
        window hide
        pause 1.0
        window show
        jump lanjut_ke_dialog_bagas
    
    label pilihan_krama_b:
        $ player_points -= 20
        scene visual_tidakpeduli
        with dissolve
        wira "(berdiri saja di tempatnya, membiarkan Kanjeng Raden yang menyesuaikan jalan, sambil melihat ke arah lain)"
        
        Raden_Mas_Bagas "Di sini, cara kamu berdiri dan memberikan jalan itu bukan formalitas. Ini sebuah cara kamu bilang \"Saya tahu tempat saya dan saya menghormati orang lain\" Kalau kamu nggak melakukan itu…"
        
        garuda "...kamu bukan orang yang kasar. Akan tetapi, kamu tidak hadir dan ini adalah kehilangan terbesar."
        
        window hide
        pause 1.0
        window show
        jump lanjut_ke_dialog_bagas
    
    label pilihan_krama_c:
        $ player_points += 10
        
        wira "(menyingkir dan membungkuk hormat, tapi tidak bertanya lebih lanjut dan hanya berdiam diri)"
        
        Raden_Mas_Bagas "Kamu tahu caranya hormat. Tapi kamu belum tahu alasannya. Itu beda tipis, tapi beda."
        
        garuda "Menghormati tanpa memahami adalah ritual. Menghormati dengan memahami adalah kesadaran."
        garuda "Keraton tidak butuh robot yang tahu gerakannya. Keraton butuh manusia yang tahu mengapa."
        
        window hide
        pause 1.0
        window show
    
    label lanjut_ke_dialog_bagas:
    
    # ===== SCENE DIALOG RADEN MAS BAGAS =====
    stop sound fadeout 1.0
    scene visual_hormatdenganmaubelajar
    with dissolve
    
    Raden_Mas_Bagas "Saya mau jujur denganmu, Wira. Saya sempat mau meninggalkan semua ini."
    Raden_Mas_Bagas "Waktu di luar negeri, saya belajar teknik pertunjukan modern yang lebih efektif dan lebih relevan."
    Raden_Mas_Bagas "Saya pikir, kenapa saya harus balik ke sini dan mengikat diri dengan aturan yang rasanya kuno?"
    
    Raden_Mas_Bagas "Tapi saya menyadari satu hal. Di negara manapun saya pergi, nggak ada yang punya wayang."
    Raden_Mas_Bagas "Nggak ada yang punya gamelan, dan nggak ada yang punya filosofi tentang keselarasan kayak yang ada di sini."
    Raden_Mas_Bagas "Mereka punya banyak hal yang saya kagumi, tapi nggak punya ini semua."
    
    wira "Terus kamu balik."
    
    Raden_Mas_Bagas "Saya balik dan sekarang saya lagi belajar untuk membawa dunia luar masuk ke sini. Bukan untuk mengubah Keraton tetapi untuk membuat lebih banyak orang dapat merasakan apa yang bisa saya rasakan waktu duduk di sini pertama kali."
    
    garuda "Dengarkan baik baik, Wira. Ini bukan cerita tentang masa lalu melawan masa depan. Ini tentang menemukan apa yang tidak bisa digantikan lalu menjaganya dengan kedua tanganmu."
    
    window hide
    pause 2.0
    window show
    
    # ===== AKHIR CHECKPOINT =====
    # Menampilkan skor akhir
    $ skor_akhir = player_points
    play sound "sound/gamelankeras.mp3" fadein 1.0 loop
    Raden_Mas_Bagas "Checkpoint Betawi dan Keraton Jawa selesai, Wira. Mari kita lihat hasil perjalananmu."
    if skor_akhir >= 50:
        scene skor_tinggi_daerahjawa
        with fade
        garuda "Keputusanmu selama perjalanan di Betawi dan Keraton Jawa menunjukkan pemahaman mendalam tentang keseimbangan antara tradisi dan modernitas."
        garuda "Kamu telah membuktikan bahwa mendengarkan dan memahami adalah kunci untuk mempertahankan warisan budaya di tengah perubahan zaman."
        
    elif skor_akhir >= 0:
        scene skor_sedang_daerahjawa
        with fade
        garuda "Perjalananmu menunjukkan kesadaran terhadap pentingnya budaya, meski masih ada ruang untuk berkembang."
        garuda "Kamu mulai memahami bahwa setiap keputusan membawa konsekuensi yang mendalam bagi komunitas dan tradisi."
    else:
        scene skor_rendah_daerahjawa
        with fade
        garuda "Perjalananmu menunjukkan bahwa masih banyak yang perlu dipelajari tentang menghargai tradisi dan mendengarkan orang lain."
        garuda "Warisan budaya memerlukan lebih dari sekedar niat  ia memerlukan kehadiran dan kepedulian yang sejati."
    
    window hide
    pause 3.0
    window show
    
    garuda "Poin yang dikumpulkan: [player_points]"
    scene ending_jawabetawi
    garuda "Masih ada tiga gerbang lagi. Yang berikutnya akan membawamu ke pulau terindah di Indonesia, Bali."
    stop sound fadeout 2.0
    return
