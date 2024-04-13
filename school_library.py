list_of_books = input().split("&")
command = input().split(" | ")
while command[0] != 'Done':
    change = command[0]
    book_name = command[1]
    if change == "Add Book":
        if book_name not in list_of_books:
            list_of_books.insert(0, book_name)
    elif change == "Take Book":
        if book_name in list_of_books:
            list_of_books.remove(book_name)
    elif change == "Swap Books":
        new_book = command[2]
        if book_name in list_of_books and new_book in list_of_books:
            book_1, book_2 = list_of_books.index(book_name), list_of_books.index(new_book)
            list_of_books[book_1], list_of_books[book_2] = list_of_books[book_2], list_of_books[book_1]
    elif change == "Insert Book":
        if book_name not in list_of_books:
            list_of_books.append(book_name)
    elif change == "Check Book":
        current_index = 0
        step = int(book_name)
        current_index += step
        if 0 <= current_index <= len(list_of_books) - 1:
            print(list_of_books[current_index])
    command = input().split(" | ")
print(", ".join(list_of_books))
