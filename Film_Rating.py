number_of_films = int(input())

top_rating = -float('inf')
bottom_rating = float('inf')

top_rating_name = ''
bottom_rating_name = ''
total_rating = 0

for i in range(number_of_films):
    film_name = input()
    rating = float(input())

    total_rating += rating

    if rating > top_rating:
        top_rating = rating
        top_rating_name = film_name

    if rating < bottom_rating:
        bottom_rating = rating
        bottom_rating_name = film_name

average_rating = total_rating / number_of_films

print(f"{top_rating_name} is with highest rating: {top_rating}")
print(f"{bottom_rating_name} is with highest rating: {bottom_rating}")
print(f"Average rating: {average_rating:.1f}")