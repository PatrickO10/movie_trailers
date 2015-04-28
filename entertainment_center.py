import fresh_tomatoes
import media
'''
Below are the instances of the movie class.
Parameters of the movie class:
  Name
  Year
  Movie title
  Poster Image
  Youtube Url
  Parental Rating
'''
hobbit_3 = media.Movie("The Hobbit: The Battle of the Five Armies",
                       "(2014)",
                       "http://upload.wikimedia.org/wikipedia/en/0/0e/The_Hobbit_-_The_Battle_of_the_Five_Armies.jpg",
                       "https://www.youtube.com/watch?v=iVAgTiBrrDA",
                       "PG-13")
amadeus = media.Movie("Amadeus",
                      "(1984)",
                      "http://upload.wikimedia.org/wikipedia/en/2/2f/Amadeusmov.jpg",
                      "https://www.youtube.com/watch?v=yIzhAKtEzY0",
                      "R")
django_unchained = media.Movie("Django Unchained",
                               "(2012)",
                               "http://upload.wikimedia.org/wikipedia/en/8/8b/Django_Unchained_Poster.jpg",
                               "https://www.youtube.com/watch?v=eUdM9vrCbow",
                               "R")
jiro_sushi = media.Movie("Jiro Dreams of Sushi",
                         "(2011)",
                         "http://upload.wikimedia.org/wikipedia/en/4/47/Jiro_sushi_poster.jpg",
                         "https://www.youtube.com/watch?v=buF540VBwAE",
                         "PG")
star_trek_into_darkness = media.Movie("Star Trek Into Darkness",
                                      "(2013)",
                                  "http://upload.wikimedia.org/wikipedia/en/5/50/StarTrekIntoDarkness_FinalUSPoster.jpg",
                                  "https://www.youtube.com/watch?v=r5gdbUC9mWU",
                                  "PG-13")
war_of_arrows = media.Movie("War of Arrows",
                            "(2011)",
                            "http://upload.wikimedia.org/wikipedia/en/4/4f/War_of_the_Arrows_film_poster.jpg",
                            "https://www.youtube.com/watch?v=XDyIjb272kU",
                            "R")
beat_that_my_heart_skipped = media.Movie("The Beat That My Heart Skipped",
                                         "(2005)",
                                         "http://upload.wikimedia.org/wikipedia/en/f/fd/The_Beat_That_My_Heart_Skipped_poster.jpg",
                                         "https://www.youtube.com/watch?v=af4SirQ6ip4",
                                         "Unrated")
american_psycho = media.Movie("American Psycho",
                              "(2000)",
                              "http://upload.wikimedia.org/wikipedia/en/6/63/Americanpsychoposter.jpg",
                              "https://www.youtube.com/watch?v=2GIsExb5jJU",
                              "R")
big_lebowski = media.Movie("The Big Lebowski",
                           "(1998)",
                           "http://upload.wikimedia.org/wikipedia/en/3/35/Biglebowskiposter.jpg",
                           "https://www.youtube.com/watch?v=cd-go0oBF4Y",
                           "R")
ferris_bueller = media.Movie("Ferris Bueller's Day Off",
                             "(1986)",
                             "http://upload.wikimedia.org/wikipedia/en/9/9b/Ferris_Bueller%27s_Day_Off.jpg",
                             "https://www.youtube.com/watch?v=R-P6p86px6U",
                             "PG-13")
good_bad_ugly = media.Movie("The Good, the Bad, and the Ugly",
                            "(1966)",
                            "http://upload.wikimedia.org/wikipedia/en/4/45/Good_the_bad_and_the_ugly_poster.jpg",
                            "https://www.youtube.com/watch?v=WCN5JJY_wiA",
                            "Unrated")
snatch = media.Movie("Snatch",
                     "(2000)",
                     "http://upload.wikimedia.org/wikipedia/en/a/a7/Snatch_ver4.jpg",
                     "https://www.youtube.com/watch?v=lUloT3Dh3-E",
                      "R")
kiss_kiss_bang_bang = media.Movie("Kiss Kiss Bang Bang",
                                  "(2005)",
                                  "http://upload.wikimedia.org/wikipedia/en/6/61/Kiss_kiss_bang_bang_poster.jpg",
                                  "https://www.youtube.com/watch?v=__PnD1HWXSo",
                                  "R")
old_boy = media.Movie("Old Boy",
                      "(2000)",
                      "http://cdn8.nflximg.net/webp/5968/2435968.webp",
                      "https://www.youtube.com/watch?v=tphnn5EPj2w",
                      "R")
perfume = media.Movie("Perfume: The Story of a Murderer",
                      "(2006)",
                      "http://upload.wikimedia.org/wikipedia/en/6/69/Perfume_poster.jpg",
                      "https://www.youtube.com/watch?v=zutiIw_2e2g",
                      "R")

# Python data structure containing the list of movies.
movies = [
          hobbit_3,
          django_unchained,
          amadeus,
          beat_that_my_heart_skipped,
          good_bad_ugly,
          big_lebowski,
          jiro_sushi,
          star_trek_into_darkness,
          war_of_arrows,
          american_psycho,
          snatch,
          kiss_kiss_bang_bang,
          ferris_bueller,
          old_boy,
          perfume
          ]

fresh_tomatoes.open_movies_page(movies)
