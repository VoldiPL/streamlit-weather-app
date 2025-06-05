import os
import pandas as pd


def save_to_excel(record):
    df_new = pd.DataFrame([record])

    # dodawanie nowego rekordu do istniejącego pliku
    # jeśli stary plik istnieje (os.path.exists)
    # odczytaj go (pd.read)
    # a następnie dodaj nowe dane (pd.concat)
    # a jeśli plik nie istnieje, zamień df_new na df i zapisz plik (df.to_excel)

    if os.path.exists("weather.xlsx"):
        df = pd.read_excel("weather.xlsx")
        df = pd.concat(
        [df, df_new],
            ignore_index=False
        )
    else:
        df = df_new

    df.to_excel("weather.xlsx", index=False)