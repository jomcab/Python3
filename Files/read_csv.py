import csv

# Reading CSV File (basic)
with open("logger.csv") as log_csv_file:
  print(log_csv_file.read())

# Directory Reader
with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row['Cool Fact'])

# Directory Reader with Delimiter
with open("books.csv") as books_csv:
  books_reader = csv.DictReader(books_csv, delimiter="@")
  isbn_list = []
  for book in books_reader:
    isbn_list.append(book['ISBN'])