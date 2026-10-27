# === File: main.py ===
from utilitas_akademik import generate_transkrip


def main():
  krs_mhs = [
      {"nama_mk": "Pemrograman Web", "sks": 3, "nilai": 82},
      {"nama_mk": "Sistem Basis Data", "sks": 3, "nilai": 90},
      {"nama_mk": "Jaringan Komputer", "sks": 3, "nilai": 65},
  ]

  print(generate_transkrip("Tazkia Rizqiani", krs_mhs))


if __name__ == "__main__":
  main()