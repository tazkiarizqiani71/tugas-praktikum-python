# === File: validator.py ===


def validasi_data(data, schema, *required_fields, **options):
  errors = []

  # Cek field wajib dari *args
  for field in required_fields:
    if field not in data:
      errors.append(f"Field '{field}' wajib disertakan.")

  # Cek aturan tipe & rentang dari schema
  for field, rules in schema.items():
    if field not in data:
      continue

    val = data[field]
    if "type" in rules and not isinstance(val, rules["type"]):
      errors.append(
          f"Field '{field}' harus bertipe {rules['type'].__name__}, bukan"
          f" {type(val).__name__}."
      )
      continue

    if "min" in rules and val < rules["min"]:
      errors.append(
          f"Field '{field}' bernilai {val}, di bawah batas minimum"
          f" ({rules['min']})."
      )
    if "max" in rules and val > rules["max"]:
      errors.append(
          f"Field '{field}' bernilai {val}, melebihi batas maksimum"
          f" ({rules['max']})."
      )

  return len(errors) == 0, errors


if __name__ == "__main__":
  aturan = {"usia": {"type": int, "min": 17, "max": 60}}
  input_data = {"usia": 15}

  is_valid, pesan_error = validasi_data(input_data, aturan, "nama")
  print(f"Apakah data valid? {is_valid}")
  print(f"Daftar Error: {pesan_error}")