# === File: utilitas_akademik.py ===


def konversi_nilai_huruf(angka):
  if angka >= 85:
    return "A"
  elif angka >= 70:
    return "B"
  elif angka >= 55:
    return "C"
  elif angka >= 40:
    return "D"
  return "E"


def hitung_ipk(daftar_mk):
  bobot = {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "E": 0.0}
  total_poin = 0
  total_sks = 0

  for mk in daftar_mk:
    huruf = konversi_nilai_huruf(mk["nilai"])
    total_poin += bobot[huruf] * mk["sks"]
    total_sks += mk["sks"]

  return round(total_poin / total_sks, 2) if total_sks > 0 else 0.0


def generate_transkrip(nama, daftar_mk):
  teks = [f"=== Transkrip Nilai: {nama} ==="]
  for mk in daftar_mk:
    huruf = konversi_nilai_huruf(mk["nilai"])
    teks.append(f"- {mk['nama_mk']} ({mk['sks']} SKS): {mk['nilai']} ({huruf})")
  teks.append(f"IPK Total: {hitung_ipk(daftar_mk)}")
  return "\n".join(teks)


if __name__ == "__main__":
  print("Modul utilitas_akademik aktif.")