# Tugas Praktikum Pemrograman Python

Repositori ini dibuat untuk memenuhi tugas praktikum mata kuliah Pemrograman Python, yang mencakup implementasi fungsi, helper statistik, utilitas akademik, validator, serta struktur package bersarang (*nested package*) untuk sistem informasi.

## Struktur Direktori Proyek
```text
Tugas_Praktikum_Python/
│
├── main.py
├── statistik_helper.py
├── utilitas_akademik.py
├── validator.py
├── jalankan_app.py
│
└── sistem_informasi/
    ├── __init__.py
    ├── model/
    │   ├── __init__.py
    │   └── mahasiswa.py
    ├── service/
    │   ├── __init__.py
    │   └── crud_service.py
    └── utils/
        ├── __init__.py
        └── validator.py
Deskripsi Singkat
Soal 1 - 3: Berisi modul helper statistik, utilitas akademik, dan fungsi validator dasar.

Soal 4 (Package): Berisi struktur nested package sistem_informasi yang terdiri dari modul model, service (CRUD data mahasiswa), dan utils (validasi NIM).

jalankan_app.py: Skrip utama untuk menguji fungsionalitas package sistem informasi.

Identitas Mahasiswa
Nama: Tazkia Rizqiani
Npm : 20241320010
Program Studi: Sistem Informasi
