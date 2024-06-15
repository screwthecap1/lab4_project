import csv
from datetime import datetime
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')


class Visit:
    def __init__(self, number, name, date_time, visit_type):
        self.number = number
        self.name = name
        self.date_time = date_time
        self.visit_type = visit_type

    def __repr__(self):
        return f"Visit({self.number}, {self.name}, {self.date_time.strftime('%d.%m.%Y %H:%M')}, {self.visit_type})"

    def __setattr__(self, name, value):
        object.__setattr__(self, name, value)


class VisitCollection:
    def __init__(self):
        self.visits = []

    def add_visit(self, visit):
        if isinstance(visit, Visit):
            self.visits.append(visit)

    def __getitem__(self, index):
        return self.visits[index]

    def __setitem__(self, index, value):
        if isinstance(value, Visit):
            self.visits[index] = value

    def __iter__(self):
        return iter(self.visits)

    def __repr__(self):
        return '\n'.join(repr(visit) for visit in self.visits)

    @staticmethod
    def read_csv_file(file_path):
        collection = VisitCollection()
        with open(file_path, mode='r', newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                number = int(row['№'])
                name = row['ФИО']
                date_time = datetime.strptime(
                    row['Дата и время'], '%d.%m.%Y %H:%M')
                visit_type = row['Тип обращения']
                collection.add_visit(
                    Visit(number, name, date_time, visit_type))
        return collection

    def sort_by_number(self):
        self.visits.sort(key=lambda x: x.number)

    def save_to_csv(self, file_path):
        with open(file_path, mode='w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['№', 'ФИО', 'Дата и время', 'Тип обращения'])
            for visit in self.visits:
                writer.writerow([visit.number, visit.name, visit.date_time.strftime(
                    '%d.%m.%Y %H:%M'), visit.visit_type])


# Использование классов
collection = VisitCollection.read_csv_file('data.csv')
print(collection)  # Печать всех визитов
collection.sort_by_number()  # Сортировка по номеру
collection.save_to_csv('sorted_data.csv')  # Сохранение отсортированных данных
'# Feature branch change' 
