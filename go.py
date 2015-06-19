import fresh_tomatoes
import media

inception = media.Movie("Inception", 
	"Visionary filmmaker Christopher Nolan (Memento, The Dark Knight) writes and directs this psychological sci-fi action film about a thief who possesses the power to enter into the dreams of others. ", 
	"http://resizing.flixster.com/THwVJ6BnMSZz1ygWPdIEok_wVhA=/180x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/16/67/11166725_ori.jpg", 
	"https://www.youtube.com/watch?v=66TuSJo4dZM")
avatar = media.Movie("Avatar",
	"\"Avatar\" is the story of an ex-Marine who finds himself thrust into hostilities on an alien planet filled with exotic life forms. As an Avatar, a human mind in an alien body, he finds himself torn between two worlds, in a desperate fight for his own survival and that of the indigenous people.",
	"http://resizing.flixster.com/OPDpDBP1P_qiiOjKOW9042R4R3g=/180x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/17/67/11176792_ori.jpg",
	"https://www.youtube.com/watch?v=5PSNL1qE6VY")
road_to_perdition = media.Movie("Road to Perdition", 
	"blah blah", 
	"https://detoditocineymusica.files.wordpress.com/2013/03/camino_a_la_perdicion_2002_9.jpg", 
	"https://youtu.be/k1iCd___dNY")
good_fellas = media.Movie("Good Fellas", 
	"Martin Scorsese explores the life of organized crime with his gritty, kinetic adaptation of Nicolas Pileggi's best-selling Wiseguy, the true-life account of mobster and FBI informant Henry Hill. Set to a true-to-period rock soundtrack, the story details the rise and fall of Hill, a half-Irish, half-Sicilian New York kid who grows up idolizing the \"wise guys\" in his impoverished Brooklyn neighborhood....", 
	"http://resizing.flixster.com/YxEaDEVBtcdFyE_4KaZrzU5voyM=/180x270/dkpu1ddg7pbsk.cloudfront.net/movie/11/16/67/11166723_ori.jpg", 
	"https://www.youtube.com/watch?v=qo5jJpHtI1Y")

movies = [inception, avatar, road_to_perdition, good_fellas]

fresh_tomatoes.open_movies_page(movies)

