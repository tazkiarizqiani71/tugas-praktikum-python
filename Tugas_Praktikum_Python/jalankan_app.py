from sistem_informasi.service import crud_service as crud
from sistem_informasi.utils.validator import cek_format_nim

if __name__ == "__main__":
  nomor_induk = "2024010"

  if cek_format_nim(nomor_induk):
    status, pesan = crud.create(
        nomor_induk, "Tazkia Rizqiani", "Sistem Informasi"
    )
    print(pesan)
    print("Isi Database:", crud.read())