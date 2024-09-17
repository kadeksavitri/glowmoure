LINK PwS : http://kadek-savitri-glowmoure.pbp.cs.ui.ac.id/

Tugas Individu 1
Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)

1. Mengaktifkan Virtual Environment dan Menyiapkan Dependencies
Pertama, saya membuat direktori proyek dan mengaktifkan virtual environment menggunakan perintah python -m venv venv. Setelah itu, saya menginstal dependencies yang diperlukan dan membuat berkas requirements.txt untuk mendokumentasikan paket yang akan diinstal nanti saat deployment.

2. Inisialisasi Git dan Unggah ke GitHub
Setelah menyiapkan proyek, saya menginisialisasi repository Git untuk melacak perubahan kode. Saya juga menambahkan berkas .gitignore agar file yang tidak diperlukan, seperti file virtual environment, tidak diunggah. Setelah itu, proyek diunggah ke GitHub dengan perintah git add, git commit, dan git push.

3. Pembuatan Proyek Django
Saya membuat proyek Django baru dengan nama glowmoure menggunakan perintah django-admin startproject toko. Ini menciptakan struktur proyek Django dasar.

4. Membangun Aplikasi 'Main' dalam Proyek
Di dalam proyek toko, saya membuat aplikasi baru bernama main menggunakan perintah python manage.py startapp main. Aplikasi ini akan menangani fitur utama dari proyek.

5. Menghubungkan Aplikasi dengan Proyek Melalui Settings
Saya menghubungkan aplikasi main dengan proyek toko melalui berkas settings.py dengan menambahkan aplikasi tersebut ke dalam daftar INSTALLED_APPS agar dapat diakses oleh proyek Django.

6. Pembuatan Model 'ProductDetail' untuk Penyimpanan Data
Di dalam models.py aplikasi main, saya membuat model Product dengan atribut name, price, description, dan quantity untuk menyimpan informasi produk yang akan ditampilkan di aplikasi.

7. Melakukan Migrasi untuk Membuat Database
Setelah model selesai, saya menjalankan perintah python manage.py makemigrations dan python manage.py migrate untuk membuat dan memperbarui tabel Product di database sesuai dengan model yang telah didefinisikan.

8. Membuat View untuk Menampilkan Informasi pada Template HTML
Di dalam views.py, saya membuat fungsi home yang akan menampilkan halaman HTML yang berisi informasi aplikasi serta nama dan kelas pengguna. Fungsi ini akan digunakan sebagai halaman utama.

9. Membuat Template HTML untuk Menampilkan Data
Saya membuat berkas main.html di dalam direktori templates, yang akan menerima data dari views.py dan menampilkannya sebagai halaman web yang dapat diakses oleh pengguna.

10. Mengatur Routing URL pada urls.py
Saya mengatur routing di urls.py untuk memetakan URL ke fungsi home di views.py. Ini memastikan bahwa ketika pengguna mengakses URL utama aplikasi, mereka diarahkan ke halaman yang sesuai.

11. Melakukan Commit dan Push ke Repository GitHub
Setelah semua perubahan selesai, saya melakukan commit dengan perintah git commit dan mengunggah seluruh kode terbaru ke GitHub menggunakan git push.

12. Deployment Aplikasi ke PWS
Terakhir, saya melakukan deployment aplikasi ke platform hosting seperti Heroku atau Railway dengan menyiapkan file konfigurasi seperti Procfile, lalu melakukan deployment melalui Git.

Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.


Client (Browser) -----> urls.py (main APP)  ---->  views.py  ---->  models.py   ---->  Template (HTML)  ---->   Response Client
        |                        |                        |                    |                   
        |                        |                        |                    |                                 
    HTTP Request              URL Routing             View Logic         Database       

Penjelasan Alur:
Client (Browser): Pengguna mengirimkan permintaan HTTP (seperti GET atau POST) melalui URL yang dimasukkan di browser untuk mengakses halaman atau sumber daya tertentu pada aplikasi.

urls.py: Django akan memeriksa URL yang diminta dan mencocokkannya dengan pola yang didefinisikan di urls.py. URL ini kemudian akan diarahkan ke fungsi yang sesuai di views.py.

views.py: Setelah URL berhasil dipetakan, Django menjalankan fungsi di views.py. Di sini, logika aplikasi dijalankan untuk memproses data atau permintaan dari pengguna. Jika diperlukan, fungsi ini dapat berinteraksi dengan database melalui model di models.py.

models.py: Jika aplikasi perlu mengakses atau memodifikasi data, fungsi di views.py akan menggunakan model yang didefinisikan di models.py. Django ORM bertugas untuk menghubungkan model Python dengan tabel-tabel yang ada di database.

Template (HTML): Setelah semua data diproses oleh views.py, data tersebut dikirimkan ke template HTML. Template ini bertugas merender data menjadi tampilan web yang sesuai, yang kemudian dikirim kembali ke pengguna sebagai respons dalam bentuk halaman web.

Jelaskan fungsi git dalam pengembangan perangkat lunak!
Git berfungsi sebagai sistem kontrol versi yang sangat penting dalam pengembangan perangkat lunak. Fungsinya adalah untuk membantu pengembang melacak setiap perubahan yang terjadi pada file proyek, sehingga memudahkan mereka dalam mengelola dan mengembalikan versi file sebelumnya jika terjadi kesalahan. Git juga memungkinkan kolaborasi yang lebih efektif antar tim developer dengan fitur branching dan merging, di mana setiap pengembang dapat bekerja pada fitur atau perbaikan bug secara terpisah tanpa mengganggu pekerjaan rekan tim lainnya.

Git menyimpan berbagai versi proyek, mencatat siapa yang melakukan perubahan, kapan perubahan tersebut dilakukan, dan apa yang diubah, sehingga riwayat proyek selalu jelas dan dapat diaudit. Selain itu, repositori dapat disimpan secara remote di server (misalnya, GitHub atau GitLab) yang berfungsi sebagai backup sekaligus tempat kolaborasi. Fitur branching memungkinkan pengembangan fitur atau eksperimen dilakukan di cabang terpisah dari kode utama (main branch), dan setelah selesai, dapat digabungkan kembali (merge) ke kode utama tanpa konflik.


Menurut Anda, dari semua framework yang ada, mengapa framework Django dijadikan permulaan pembelajaran pengembangan perangkat lunak?
Django sering dipilih sebagai framework awal dalam pembelajaran pengembangan perangkat lunak karena menyediakan banyak fitur siap pakai, seperti autentikasi, manajemen sesi, ORM, dan routing URL, yang membuatnya lebih mudah diakses oleh pemula. Sebagai framework full-stack, Django membantu pengembang mempelajari aspek front-end dan back-end secara bersamaan, memberikan pengalaman pengembangan yang menyeluruh. Django juga memiliki aturan dan konvensi yang jelas, yang memungkinkan pemula untuk fokus pada logika bisnis tanpa perlu menghabiskan waktu pada pengaturan yang rumit. Ditambah lagi, dengan komunitas yang besar dan dokumentasi yang lengkap, Django memudahkan para pemula untuk menemukan tutorial atau solusi ketika menghadapi kendala. Fitur keamanan bawaan dan penerapan praktik terbaik sejak awal membuat Django ideal sebagai sarana belajar, memastikan pengembang memahami dasar pengembangan perangkat lunak yang profesional.

Mengapa model pada Django disebut sebagai ORM?
Model dalam Django dikenal sebagai ORM (Object-Relational Mapping) karena berperan sebagai penghubung antara objek Python dengan tabel database relasional. Dengan menggunakan ORM, pengembang bisa berinteraksi dengan database hanya melalui kode Python tanpa perlu menulis query SQL secara langsung. Django secara otomatis menerjemahkan operasi yang dilakukan pada objek Python menjadi query SQL dan mengonversi hasilnya kembali ke dalam bentuk objek Python. Salah satu kelebihan utama ORM adalah memudahkan pengembang yang mungkin tidak menguasai SQL untuk tetap bisa bekerja dengan berbagai jenis database dengan lebih mudah. Selain itu, ORM juga membantu meningkatkan keamanan dengan melindungi aplikasi dari serangan seperti SQL Injection.

========================================================================================================
Tugas Individu 2

Jelaskan mengapa kita memerlukan data delivery dalam pengimplementasian sebuah platform?
Jawab: 
data delivery sangat diperlukan pengimplementasian sebuah platform karena data delivery memungkinkan mentransfer data pada berbagai komponen dalam platform, baik itu antar frontend dan backend atau antar server. Hal ini dilakukan untuk mengirim data dari database ke user interface atau sebaliknya sehingga ata delivery memungkinkan pertukaran ata ini terjadi secara efisien an terorganisir. Metode data delivery yang digunakan seperti XML dan JSON membantu menyederhanakan proses dengan menyediakan format yang mudah dibaca dan diproses oleh mesin. 

Menurutmu, mana yang lebih baik antara XML dan JSON? Mengapa JSON lebih populer dibandingkan XML?
Jawab: 
Tergantung pada spesifik aplikasi yang dibuat. Jika ingin menyimpan data berbagai data yang berbeda dengan banyak penggunaan variable maka gunakanlah XML karena XML dapat memeriksa kesalahan pada struktur data yang kompleks dan memiliki berbagai tipe data bawaan yang berbeda serta mendukung proses skema XSD dan proses validasi data yang lebih baik dari pada JSON, namun kompleksitas XML memiliki sintaks dan struktur yang lebih rumit serta XML lebih verbose yang mengakibatkan ukuran dile yang lebih besar dan Waktu penguraian yang lebih lama. 

Namun, jika ingin mendapatkan kecepatan dan efisiensi dalam pemrosesan data, maka gunakanlah JSON. Dengan ukuran data yang lebih kecil, JSON mempercepat waktu penguraian dan transmisi, ideal untuk aplikasi yang membutuhkan performa tinggi. Formatnya yang sederhana memudahkan pembacaan dan penulisan, mendukung pengembangan yang lebih cepat dan lebih intuitif.

JSON lebih popular dibandingkan XML karena:
- Keefisienan: JSON menggunakan lebih sedikit data dan mengurangi overhead bandwidth sehingga meningkatkan kecepatan.
- Kemudahan penggunaan: sintak JSON lebih sederhana dan mudah dipahami dibandingkan dengan XML. dan Struktur JSON yang felksibel memudahkan manipulasi dan penggunaan dalam aplikasi dinamis
- JSON luas didukung dalam banyak Bahasa pemrograman dan framework sehingga lebih fleksibel untuk pengembangan modern aplikasi web dan mobile. 

Jelaskan fungsi dari method is_valid() pada form Django dan mengapa kita membutuhkan method tersebut?
Jawab: 
Method is_valid() digunakan utuk memvalidasi data yang dikirim melalui form sesuai dengan aturan yang ditetapkan alam model Django. Method ini memeriksa kevalidan data, seperti memastikan format, tipe data, dan nilainya sheingga perlu untuk dipastikan lagi integritas data sebelum disimpan ke database untuk menghidari kesalahan dan menjaga keamanan aplikasi.

Mengapa kita membutuhkan csrf_token saat membuat form di Django? Apa yang dapat terjadi jika kita tidak menambahkan csrf_token pada form Django? Bagaimana hal tersebut dapat dimanfaatkan oleh penyerang?
Jawab: 
csrf_token atau Cross-Site Request Forgery token diperlukan untuk melindungi aplikasi web dari serangan CSRF. Penyerang bisa memanipulasi pengguna untuk melakukan aksi tidak diinginkan ada aplikasi web yang sudah mereka autentikasikan.Jikas suatu form tidak memiliki csrf_token, aplikasi menjadi rentan terhadap serangan cyber, dimana penyerang apat mengirimkan request berbahaya melalui Tindakan pengguna yang tidak menyadarinya, seprti mengubah kata sandi atau email mereka tanpa persetujan lalu mengambil alih aplikasi web tersebut. 

Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Jawab: 
1. Membuat Input Form: 
- Sebelum membuat form input, saya akan memastikan model data seperti ProductDetail yang digunakan untuk menyimpan data product yang akan ditambahkan oleh pengunna sudah ada pada file models.py. 
- Kemudian saya membuat form.py dengan ModelForm untuk mempermudah pengambilan dan validasi data dari pengguna. 
- Selanjutnya saya menambahkan views.py untuk menampilkan form kepada pengguna dan mneyimpan data saat form disubmit. 
- Terakhir, saya membuat template HTML untuk menampilkan form dengan menggunakan token CSRF untuk keamanan seprti mencegah serangan berbahaya yang emmeanfaatkan celah di formular web. 

2. Menambahkan Fungsi Views untuk XML dan JSON
Langkah kedua adalah menambahkan fungsi untuk mengembalikan data dalam format XML dan JSON. Tujuannya adalah menyediakan metode untuk mengirimkan data kepada aplikasi atau layanan lain yang membutuhkan format standar ini. XML dan JSON banyak digunakan dalam integrasi antar-aplikasi karena kedua format tersebut mudah dibaca oleh mesin. Dengan menggunakan serializers di Django, kita dapat mengonversi objek Product Detail menjadi format XML atau JSON, memungkinkan data mood diakses dalam format yang lebih fleksibel dan umum digunakan. Selain itu, dibuat juga fungsi untuk mengembalikan data berdasarkan ID tertentu agar data dapat difilter sesuai kebutuhan pengguna atau aplikasi.

3. Routing URL untuk views
Setelah views selesai, kita harus menambahkan routing pada urls.py untuk setiap fungsi yang telah dibuat. Ini bertujuan agar setiap endpoint dapat diakses oleh pengguna dan aplikasi eksternal. Misalnya, kita menambahkan path untuk form input, serta path untuk mendapatkan data dalam format XML dan JSON, baik untuk seluruh data maupun untuk data spesifik berdasarkan ID. Routing ini memungkinkan aplikasi untuk menangani berbagai permintaan dari pengguna, seperti menambahkan data baru atau mengambil data yang ada dalam format tertentu.

Referensi : 
Django Software Foundation. (n.d.). Cross Site Request Forgery protection. Django documentation. Diakses dari https://docs.djangoproject.com/en/stable/ref/csrf/ 
Kurniawan, A. (2020). Pengenalan Format Data: XML vs JSON. Diakses dari w3schools.com
Ultahost. (n.d.). Perbandingan antara XML dan JSON: Mana yang lebih baik? Diakses dari https://ultahost.com/blog/id/perbandingan-antara-xml-dan-json-mana-yang-lebih-baik/ 