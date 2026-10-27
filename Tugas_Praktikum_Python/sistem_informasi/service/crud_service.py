_db_mahasiswa = {}


def create(nim, nama, jurusan):
  if nim in _db_mahasiswa:
    return False, "NIM sudah terdaftar."
  _db_mahasiswa[nim] = {"nama": nama, "jurusan": jurusan}
  return True, "Data berhasil disimpan."


def read(nim=None):
  if nim:
    return _db_mahasiswa.get(nim, "Data tidak ditemukan.")
  return _db_mahasiswa


def delete(nim):
  if nim in _db_mahasiswa:
    del _db_mahasiswa[nim]
    return True, "Data berhasil dihapus."
  return False, "NIM tidak ditemukan."