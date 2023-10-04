# Qonita Adestyanti
# 2106750925

- Tautan menuju aplikasi Adaptable yang sudah kamu deploy
https://qoqoncollections.adaptable.app

# TUGAS 2

- ## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, buat dulu direktori serta environtment-nya dan dependecies-nya. Setelah itu kerjakan aplikasinya seperti yang tertera pada tutorial. Kemudian implementasi MTV, Models, Templates dan Viewsnya. Digabungin semua. Tak lupa routing dan testing. Terakhir di-deploy ke Adaptable

- ## Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
     Request dari Client
              |
              v 
  urls.py   ---->  views.py   ---->  models.py   ---->  HTML
              |                |                   |
              v                v                   v
             URLs            Views              Models
              |                |                   |
              v                v                   v  
           Response         Response           Database

Penjelasan: Request (permintaan) datang dari Client (browser/aplikasi). urls.py berisi pengaturan URL yang menghubungkan permintaan dari client. views.py berisi logika dari program yang menerima permintaan dari urls.py, memprosesnya, dan kemudian merespons dengan data yang akan ditampilkan di dalam HTML serta dapat berinteraksi dengan models.py. models.py berisi defini model aplikasi yang mendefinisikan bagaimana data akan disimpan dan diatur dalam database. html berisi struktur dan tampilan halaman web yang akan diberikan kepada client. Views akan mengisi data yang sesuai ke dalam HTML untuk kemudian dikirimkan sebagai respons ke client

- ## Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Mengisolasi environtment dari aplikasi tersebut. Misal nanti ada dua aplikasi yang satunya menggunakan python versi 2.x dan yang satunya lagi menggunakan python versi 3.x, nanti mereka gabakal kecampur sehingga tidak ada fungsi yang error saat ada update dari dependencies. Kurang lebih, sebagai management dependencies. 


- ## Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

MVC (Model-View-Controller) yang sering digunakan,
Model menyimpan dan mengelola data serta logika bisnis aplikasi. View bertanggung jawab untuk menampilkan data kepada pengguna. Controller menerima input dari pengguna, memprosesnya, dan menghubungkannya dengan Model atau View yang sesuai.

MVT (Model-View-Template) menggunakan Template untuk memisahkan tampilan dari logika,
Model dan View memiliki fungsi yang sama, namun Template adalah bagian yang memisahkan tampilan HTML dari logika aplikasi yang digunakan untuk menggabungkan data dari Model ke dalam tampilan yang diberikan kepada pengguna.

MVVM (Model-View-ViewModel) memperkenalkan ViewModel, yang bertindak sebagai perantara antara Model dan View, memisahkan tampilan dari logika interaksi pengguna
Model dan View memiliki fungsi yang sama, namun ada ViewModel yang merupakan lapisan yang berfungsi sebagai perantara antara Model dan View. ViewModel mengambil data dari Model dan memformatnya agar sesuai dengan tampilan yang akan ditampilkan di View serta mengelola interaksi pengguna dengan data, sehingga View tidak perlu memiliki logika interaksi yang kompleks.

# TUGAS 3

- ## Apa perbedaan antara form POST dan form GET dalam Django?
Request sensitif yang menimbulkan perubahan pada database system sebaiknya menggunakan POST sedangkan apabila request-nya tidak menimbulkan perubahan pada server system, maka lebih baik menggunakan GET saja. Menggunakan method POST pun lebih aman karena tidak terlihat di URL daripada GET. 

- ## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
- XML (Extensible Markup Language)
Digunakan untuk pertukaran data terstruktur.
Memiliki sintaksis berbasis tag yang dapat disesuaikan.
Ekstensibel dan cocok untuk validasi data.

- JSON (JavaScript Object Notation):
Digunakan untuk pertukaran data sederhana dalam format key-value.
Sintaksis mirip dengan objek JavaScript.
Lebih ringkas dan mudah dibaca oleh manusia.

- HTML (Hypertext Markup Language):
Digunakan untuk membuat tampilan dan antarmuka pengguna web.
Digunakan untuk merender halaman web.
Bukan format data struktural yang umum digunakan untuk pertukaran data.

- ## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
karena format pertukaran data yang sangat ringan serta lebih mudah dibaca dan ditulis oleh manusia, sehingga mudah untuk diterjemahkan dan dibuat (generate) oleh komputer

- ## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Mengerjalan pada direktori tugas_pbp yang telah dikerjakan. Membuat form dengan membuat html untuk halaman utama formnya sebagai templatenya kemudian dikaitkan dengan views serta fungsi-fungsi def pada models. Kemudian menambahkan 5 fungsi views yang dapat berinteraksi (request dan respond). Setelahnya di routing dengan memsukkan url pada urls.py. 
- ## Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
<img width="854" alt="Screenshot 2023-09-15 at 20 16 06" src="https://github.com/adestyantiqonita/tugas-pbp/assets/94448470/6a93c2a1-01eb-4f50-aabc-18f347e57f7a">
<img width="856" alt="Screenshot 2023-09-15 at 20 03 58" src="https://github.com/adestyantiqonita/tugas-pbp/assets/94448470/365d5f7b-3307-4281-9056-bea942390a34">
<img width="859" alt="Screenshot 2023-09-15 at 20 04 16" src="https://github.com/adestyantiqonita/tugas-pbp/assets/94448470/137e077e-625e-4abb-850a-8122fb88acf5">
<img width="854" alt="Screenshot 2023-09-15 at 20 04 37" src="https://github.com/adestyantiqonita/tugas-pbp/assets/94448470/1bd1a007-a9c7-4092-a2bb-a8a50697d97c">
<img width="857" alt="Screenshot 2023-09-15 at 20 04 52" src="https://github.com/adestyantiqonita/tugas-pbp/assets/94448470/392d063f-1ef1-48e0-988f-9fe0d668390f">

# TUGAS 4

- ## Apa itu Django UserCreationForm, dan jelaskan apa kelebihan dan kekurangannya?
UserCreationForm adalah salah satu fitur yang disediakan oleh Django untuk membuat form dengan mudah dalam pembuatan web yang terdiri dari tiga fields, yaitu username, password1, dan password 2 (untuk konfirmasi password). Fitur ini selain mudah digunakan juga sudah di integrasi dengan model "User" sehingga data yang dimasukkan akan langsung masuk ke database. Namun, karena berasal dari Django, maka fitur ini akan bergantung pada Django dan perlu dikembangkan formulir sendiri jika tidak ingin kustomisasi standar.
- ## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi adalah proses memeriksa identitas pengguna dan memastikan bahwa orang tersebut merupakan user yang sebenarnya. Memiliki fungsi untuk memverifikasi apakah User tersebut memiliki hak akses ke aplikasi dengan memvalidasi identitas dengan cara melibatkan proses  login, autentikasi berbasis token, ataupun otentikasi pihak ketiga. Sedangkan Otorisasi proses menentukan hak akses yang dimiliki oleh User setelah orang tersebut berhasil diautentikasi. Memiliki fungsi untuk memeriksa apa yang diizinkan atau tidak diizinkan oleh User  setelah diautentikasi, yakni menentukan apa yang dapat dilihat, diubah, atau diakses oleh User dalam aplikasi berdasarkan peran (roles) atau izin (permissions) yang diberikan.

Kedua hal tersebut penting karena untuk memberikan keamanan kepada User serta pengalaman yang baik. Sehingga mereka merasa aman dengan data yang mereka input. Hal ini juga merupakan bagian dari kepatuhan kepada hukum akan perlindungan keamanan. 

- ## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
Cookies merupakan semacam file yang ditempatkan pada komputer user saat berkunjung ke website tertentu. Tujuannya agar website tersebut dapat merekam kegiatan yang pengguna lakukan saat berkunjung Sehingga tidak perlu untuk loading ke fungsi yang sama dan dapat meningkatkan efisien dan efektivitas. 

- ## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Aman saja asalkan penggunaannya benar. Ada beberapa risiko potensial, beberapa diantaranya keamanan data karena cookie yang tidak dienskripsi, risiko CSRF, cookie beresiko dicuri dan masih banyak lagi. 

- ## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Membuat fungsi form, tombol login serta logout pada views.py yang menerima request. Tidak lupa meng-import library yang dibutuhkan serta menambah halaman untuk form registrasinya. Menambahkan cookie pada code last login. Yang terakhir menghubungkan model Product dengan User sehingga pengguna yang sedang terotorisasi hanya melihat produk-produk yang telah dibuat sendiri.


# TUGAS 5

- ## Jelaskan manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya.
Element Selector dapat digunakan untuk memilih elemen HTML dengan tipe tertentu berdasarkan apa yang diinginkan, nanti bakal diaplikasikan ke seluruh elemen yang sudah disetting. Sebagai contoh : 
.header h1 {
  font-size: 12px;
  color: #777;
}

maka nanti elemen < h1 > dengan class header akan memiliki gaya sesuai settingan yang telah ditulis diatas. 

- ## Jelaskan HTML5 Tag yang kamu ketahui.
Hypertext Markup Language 5 merupakan HTML versi terbaru. HTML5 Tag adalah bagian dari kode HTML yang digunakan untuk mendefinisikan elemen-elemen dalam halaman web yang diawali dengan tanda kurung sudut (<) dan diakhiri dengan tanda kurung sudut pula (>). HTML5 Tag membantu browser web untuk memahami dan merender konten halaman web dengan benar. Contohnya ada <html>, <head>, <link>, dan lainnya. 


- ## Jelaskan perbedaan antara margin dan padding.
Margin adalah sebuah ruang diluar elemen sehingga dapat mengatur jarak antara HTML dan dengan elemen disekitarnya, nilainya dapat negatif sehingga bisa bertumpang tindih dengan elemen lainnya, dan tidak mempengaruhi tampilan elemen karna tidak memiliki background atau warna. Sedangkan Padding adalah ruang didalam elemen sehingga dapat mengatur jarak antara batas elemen HTML dengan kontennya itu sendiri, nilainya tidak bisa negatif serta dapat menggunakan background dan warna sehingga dapat mempengaruhi tampilan dari elemen tersebut. 

- ## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap. Kapan sebaiknya kita menggunakan Bootstrap daripada Tailwind, dan sebaliknya?
Boostrap menerapkan component-first yang artinya komponen dan gaya telah ditentukan sebelumnya. Sedangkan Tailwind menerapkan utility-first yang artinya membangun tampilan dengan menggabungkan kelas-kelas kecil yang menggambarkan perilaku terlebih dahulu. Tailwind lebih dapat di-custom daripada Bootstap. Boootstap leb ih mudah dipelajari daripada Tailwind. Sehingga, apabila ingin membuat web yang banyak customnya dan bisa belajar lebih, maka lebih disarankan menggunakan Tailwind. Namun, apabila pemula dan cukup dengan web sederhana(tidak banyak customnya) saja, lebih disarankan menggunakan Bootstrap. 