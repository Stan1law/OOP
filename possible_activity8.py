class Movie:
    def __init__(self, title, rating, duration):
        self.__title = title
        self.__duration = duration
        self.set_rating(rating)

    def get_title(self):
        return self.__title

    def get_rating(self):
        return self.__rating

    def get_duration(self):
        return self.__duration

    def set_rating(self, rating):
        valid_ratings = ['G', 'PG', 'PG-13', 'R']
        if rating.upper() in valid_ratings:
            self.__rating = rating.upper()
        else:
            print("Invalid rating! Defaulting to 'G'.")
            self.__rating = 'G'

    def display_movie_info(self):
        print("\n🎥 Movie Information:")
        print(f"Title: {self.__title}")
        print(f"Rating: {self.__rating}")
        print(f"Duration: {self.__duration} minutes")

    def can_watch(self, age):
        if self.__rating == 'G':
            return True
        elif self.__rating == 'PG':
            return age >= 10
        elif self.__rating == 'PG-13':
            return age >= 13
        elif self.__rating == 'R':
            return age >= 18
        else:
            return False


def main():
    title = input("Enter movie title: ")
    rating = input("Enter movie rating (G, PG, PG-13, R): ")
    duration = int(input("Enter movie duration (minutes): "))

    movie = Movie(title, rating, duration)
    movie.display_movie_info()

    age = int(input("\nEnter viewer's age: "))
    if movie.can_watch(age):
        print("✅ Viewer is allowed to watch the movie.")
    else:
        print("❌ Viewer is NOT allowed to watch the movie due to age restrictions.")


if __name__ == "__main__":
    main()



# Movie Rating System
# Problem: Movie class with fields: title, rating (G, PG, PG-13, R), duration.
# Validate rating via setter.
# displayMovieInfo() shows all data.

# Twist: Based on rating, display if a user (based on age input) is allowed to watch.