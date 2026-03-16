import pandas as pd
import csv


# Проверка PDF
def test_pdf_file(zip_file):
    with zip_file.open("basnikr.pdf") as fl_pdf:
        pdf = fl_pdf.read().decode('cp1251')
        assert 'Однажды Лебедь, Рак, да Щука' in pdf
        assert 'Из кожи лезут вон, а возу все нет ходу!' in pdf


# Проверка XLSX
def test_xlsx_file(zip_file):
    with zip_file.open("author_basni.xlsx") as fl_xlsx:
        xlsx = pd.read_excel(fl_xlsx)
        assert len(xlsx) == 3
        assert "Крылов" in xlsx["Фамилия"].values, "Крылов известный баснописец"


# Проверка CSV
def test_csv_file(zip_file):
    with zip_file.open("author_basni.csv") as fl_csv:
        csvf = csv.reader(fl_csv.read().decode("utf-8").splitlines())
        rows = list(csvf)
        assert len(rows) == 3
        assert rows[0][0] == "Иван"
        assert rows[0] == ["Иван", "Василий", "Лев"]
