import os
import pandas as pd
import csv
from zipfile import ZipFile


# PDF — басня
with open('files/basnikr.pdf','w') as pdf:
    pdf.write("Однажды Лебедь, Рак, да Щука\n"
              "Везти с поклажей воз взялись,\n"
              "И вместе трое все в него впряглись;\n"
              "Из кожи лезут вон, а возу все нет ходу!\n")


# XSLX - авторы басен
df = pd.DataFrame({
        "Имя": ["Иван", "Василий", "Лев"],
        "Фамилия": ["Крылов", "Жуковский", "Толстой"],
        "Отчество": ["Андреевич", "Андреевич", "Николаевич"],
        "Город": ["Москва", "Мишенское", "Ясная Поляна"],
        "Басня": ["Лебедь, Щука и Рак", "Орёл и Голубка", "Белка и волк"]
    })
df.to_excel('files/basni_author.xlsx', index=False)


# CSV - авторы
with open('files/author_basni.csv', 'w', newline='',encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Иван", "Василий", "Лев"])
    writer.writerow(["Крылов", "Жуковский", "Толстой"])
    writer.writerow(["Лебедь, Щука и Рак", "Орёл и Голубка", "Белка и волк"])



# Запись в архив
with ZipFile("files/basni.zip", 'w') as zip:   #архив
    zip.write('files/basnikr.pdf', arcname='basnikr.pdf')           # добавляем файлы в архив
    zip.write('files/basni_author.xlsx', arcname='author_basni.xlsx')
    zip.write('files/author_basni.csv', arcname='author_basni.csv')


#  Чтение и проверка содержимое каждого файла из архива — НЕ РАСПАКОВЫВАЯ архив!
with ZipFile("files/basni.zip", 'r') as zip:
    # Проверка PDF
    with zip.open("basnikr.pdf") as fl_pdf:
        pdf = fl_pdf.read().decode('cp1251')
        assert 'Однажды Лебедь, Рак, да Щука' in pdf
        assert 'Из кожи лезут вон, а возу все нет ходу!' in pdf


    # Проверка XLSX
    with zip.open("author_basni.xlsx") as fl_xlsx:
        xlsx = pd.read_excel(fl_xlsx)
        assert len(xlsx) == 3
        assert "Крылов" in xlsx["Фамилия"].values, "Крылов известный баснописец"
        #print(xlsx.head(2))
        #print(df.tail(1))

    # Проверка CSV
    with zip.open("author_basni.csv") as fl_csv:
        csv = csv.reader(fl_csv.read().decode("utf-8").splitlines())
        rows = list(csv)
        assert len(rows) == 3
        assert rows[0][0] == "Иван"
        assert rows[0] == ["Иван", "Василий", "Лев"]

