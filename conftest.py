import pytest
import os
import pandas as pd
import csv
from zipfile import ZipFile


@pytest.fixture(scope='session', autouse=True)
def test_files():
    os.mkdir('files')
    # PDF — басня
    with open('files/basnikr.pdf', 'w') as pdf:
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
    with open('files/author_basni.csv', 'w', newline='', encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Иван", "Василий", "Лев"])
        writer.writerow(["Крылов", "Жуковский", "Толстой"])
        writer.writerow(["Лебедь, Щука и Рак", "Орёл и Голубка", "Белка и волк"])

    # Запись в архив
    with ZipFile("files/basni.zip", 'w') as zip:  # архив
        zip.write('files/basnikr.pdf', arcname='basnikr.pdf')  # добавляем файлы в архив
        zip.write('files/basni_author.xlsx', arcname='author_basni.xlsx')
        zip.write('files/author_basni.csv', arcname='author_basni.csv')


@pytest.fixture(scope='function')
def zip_file():
    with ZipFile("files/basni.zip", 'r') as zip:
        yield zip