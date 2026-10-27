# === File: statistik_helper.py ===
import math
import statistics


def hitung_statistik(data):
  if not data:
    return {}

  try:
    modus_val = statistics.mode(data)
  except statistics.StatisticsError:
    modus_val = "Tidak ada modus tunggal"

  return {
      "mean": statistics.mean(data),
      "median": statistics.median(data),
      "modus": modus_val,
      "range": max(data) - min(data),
      "standard_deviation": statistics.stdev(data) if len(data) > 1 else 0.0,
  }


if __name__ == "__main__":
  angka = [10, 20, 20, 30, 40, 50]
  print("Hasil Analisis Statistik:")
  print(hitung_statistik(angka))