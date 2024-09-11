LINK PwS : http://kadek-savitri-glowmoure.pbp.cs.ui.ac.id/

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