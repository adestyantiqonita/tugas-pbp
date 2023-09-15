## Qonita Adestyanti
## 2106750925

- Tautan menuju aplikasi Adaptable yang sudah kamu deploy
https://qoqoncollections.adaptable.app

## Tugas 1

- # Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
Pertama, buat dulu direktori serta environtment-nya dan dependecies-nya. Setelah itu kerjakan aplikasinya seperti yang tertera pada tutorial. Kemudian implementasi MTV, Models, Templates dan Viewsnya. Digabungin semua. Tak lupa routing dan testing. Terakhir di-deploy ke Adaptable

- # Buatlah bagan yang berisi request client ke web aplikasi berbasis Django beserta responnya dan jelaskan pada bagan tersebut kaitan antara urls.py, views.py, models.py, dan berkas html.
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

- # Jelaskan mengapa kita menggunakan virtual environment? Apakah kita tetap dapat membuat aplikasi web berbasis Django tanpa menggunakan virtual environment?

Mengisolasi environtment dari aplikasi tersebut. Misal nanti ada dua aplikasi yang satunya menggunakan python versi 2.x dan yang satunya lagi menggunakan python versi 3.x, nanti mereka gabakal kecampur sehingga tidak ada fungsi yang error saat ada update dari dependencies. Kurang lebih, sebagai management dependencies. 


- # Jelaskan apakah itu MVC, MVT, MVVM dan perbedaan dari ketiganya.

MVC (Model-View-Controller) yang sering digunakan,
Model menyimpan dan mengelola data serta logika bisnis aplikasi. View bertanggung jawab untuk menampilkan data kepada pengguna. Controller menerima input dari pengguna, memprosesnya, dan menghubungkannya dengan Model atau View yang sesuai.

MVT (Model-View-Template) menggunakan Template untuk memisahkan tampilan dari logika,
Model dan View memiliki fungsi yang sama, namun Template adalah bagian yang memisahkan tampilan HTML dari logika aplikasi yang digunakan untuk menggabungkan data dari Model ke dalam tampilan yang diberikan kepada pengguna.

MVVM (Model-View-ViewModel) memperkenalkan ViewModel, yang bertindak sebagai perantara antara Model dan View, memisahkan tampilan dari logika interaksi pengguna
Model dan View memiliki fungsi yang sama, namun ada ViewModel yang merupakan lapisan yang berfungsi sebagai perantara antara Model dan View. ViewModel mengambil data dari Model dan memformatnya agar sesuai dengan tampilan yang akan ditampilkan di View serta mengelola interaksi pengguna dengan data, sehingga View tidak perlu memiliki logika interaksi yang kompleks.

- ## Apa perbedaan antara form POST dan form GET dalam Django?
 - ## Apa perbedaan utama antara XML, JSON, dan HTML dalam konteks pengiriman data?
 - ## Mengapa JSON sering digunakan dalam pertukaran data antara aplikasi web modern?
 - ## Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial).
 - ## Mengakses kelima URL di poin 2 menggunakan Postman, membuat screenshot dari hasil akses URL pada Postman, dan menambahkannya ke dalam README.md.
![Uploading Screenshot 2023-09-15 at 20.09.03.png…]()
<img width="856" alt="Screenshot 2023-09-15 at 20 03 58" src="https://github.com/adestyantiqonita/tugas-pbp/assets/94448470/365d5f7b-3307-4281-9056-bea942390a34">
<img width="859" alt="Screenshot 2023-09-15 at 20 04 16" src="https://github.com/adestyantiqonita/tugas-pbp/assets/94448470/137e077e-625e-4abb-850a-8122fb88acf5">
<img width="854" alt="Screenshot 2023-09-15 at 20 04 37" src="https://github.com/adestyantiqonita/tugas-pbp/assets/94448470/1bd1a007-a9c7-4092-a2bb-a8a50697d97c">
<img width="857" alt="Screenshot 2023-09-15 at 20 04 52" src="https://github.com/adestyantiqonita/tugas-pbp/assets/94448470/392d063f-1ef1-48e0-988f-9fe0d668390f">



