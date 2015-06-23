import fresh_tomatoes
# Provided module for displaying movie information in clear and concise manner.
import media
# Contains Movie class definition.

# Create an object for every one of my favorite movie.
inception = media.Movie("Inception",
                        "2010",
                        "Visionary filmmaker Christopher Nolan (Memento, The Dark Knight) \
                        writes and directs this psychological sci-fi action \
                        film about a thief who possesses the power to enter \
                        into the dreams of others.",
                        "http://resizing.flixster.com/THwVJ6BnMSZz1ygWPdIEok_wVhA=/180x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/16/67/11166725_ori.jpg",
                        "https://www.youtube.com/watch?v=66TuSJo4dZM")

avatar = media.Movie("Avatar",
                     "2009",
                     "\"Avatar\" is the story of an ex-Marine who finds himself \
                     thrust into hostilities on an alien planet filled with \
                     exotic life forms. As an Avatar, a human mind in an \
                     alien body, he finds himself torn between two worlds, \
                     in a desperate fight for his own survival and that of \
                     the indigenous people.",
                     "http://resizing.flixster.com/OPDpDBP1P_qiiOjKOW9042R4R3g=/180x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/17/67/11176792_ori.jpg",
                     "https://www.youtube.com/watch?v=5PSNL1qE6VY")

road_to_perdition = media.Movie("Road to Perdition",
                                "2002",
                                "Bonds of loyalty are put to the test when a \
                                hitman's son witnesses what his father does \
                                for a living.",
                                "https://detoditocineymusica.files.wordpress.com/2013/03/camino_a_la_perdicion_2002_9.jpg",
                                "https://youtu.be/k1iCd___dNY")

gangs_of_ny = media.Movie("Gangs of New York",
                          "2002",
                          "In 1863, Amsterdam Vallon returns to the Five \
                          Points area of New York City seeking \
                          revenge against Bill the Butcher, \
                          his father's killer.",
                          "http://vignette4.wikia.nocookie.net/moviepedia/images/c/c6/Gangsofny.jpg/revision/latest?cb=20140212195522&path-prefix=de",
                          "https://www.youtube.com/watch?v=UYsS_3zdwmA")

good_fellas = media.Movie("Good Fellas",
                          "1990",
                          "Martin Scorsese explores the life of organized crime \
                          with his gritty, kinetic adaptation of Nicolas \
                          Pileggi's best-selling Wiseguy, the true-life \
                          account of mobster and FBI informant Henry Hill. \
                          Set to a true-to-period rock soundtrack, \
                          the story details the rise and fall of Hill, \
                          a half-Irish, half-Sicilian New York kid who \
                          grows up idolizing the \"wise guys\" in his \
                          impoverished Brooklyn neighborhood....",
                          "http://resizing.flixster.com/YxEaDEVBtcdFyE_4KaZrzU5voyM=/180x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/16/67/11166723_ori.jpg",
                          "https://www.youtube.com/watch?v=qo5jJpHtI1Y")


the_departed = media.Movie("The Departed",
                           "2006",
                           "An undercover cop and a mole in the police attempt \
                           to identify each other while infiltrating an Irish \
                           gang in South Boston...",
                           "http://www.impawards.com/2006/posters/departed_xlg.jpg",
                           "https://www.youtube.com/watch?v=auYbpnEwBBg")


# sign the desired movie Title et.c to movies.
movies = [inception, avatar, road_to_perdition, good_fellas,
          gangs_of_ny, the_departed]

# display movie.
fresh_tomatoes.open_movies_page(movies)
