movie_name = input()
days = int(input())
tickets = int(input())
price_p_t = float(input())
percent = int(input())

profit_per_day = tickets * price_p_t
total_profit = profit_per_day * days
cinema_percent = total_profit * (percent/100)
total_movie_profit = total_profit - cinema_percent
print(f"The profit from the movie {movie_name} is {total_movie_profit:.2f} lv.")