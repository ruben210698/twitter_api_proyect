from amazonComprehend import get_weights_sentiment_analysis
from colectorTuits import generate_file_content_tuits
from colectorTuitsHttps import get_tweets_from_html

#name_file_es = "anne_with_an_e"
#print(generate_file_content_tuits(name_file_es, query = "Anne%20with%20an%20E", mode = 'w+'))
#print(generate_file_content_tuits(name_file_es, query = "Anne%20Netflix", mode = 'a'))



name_dest_file = "generated_files_from_html/parasitos"

get_tweets_from_html("https_downloaded/parasitos/Parásitos pelicula - Búsqueda de Twitter _ Twitter1.html", name_dest_file, mode="w+")
get_tweets_from_html("https_downloaded/parasitos/Parásitos pelicula - Búsqueda de Twitter _ Twitter2.html", name_dest_file, mode="a")
get_tweets_from_html("https_downloaded/parasitos/Parásitos pelicula - Búsqueda de Twitter _ Twitter3.html", name_dest_file, mode="a")
get_tweets_from_html("https_downloaded/parasitos/Parásitos pelicula - Búsqueda de Twitter _ Twitter4.html", name_dest_file, mode="a")
get_tweets_from_html("https_downloaded/parasitos/Parásitos pelicula - Búsqueda de Twitter _ Twitter5.html", name_dest_file, mode="a")
get_tweets_from_html("https_downloaded/parasitos/Parásitos pelicula - Búsqueda de Twitter _ Twitter6.html", name_dest_file, mode="a")
get_tweets_from_html("https_downloaded/parasitos/Parásitos pelicula - Búsqueda de Twitter _ Twitter7.html", name_dest_file, mode="a")
get_tweets_from_html("https_downloaded/parasitos/Parásitos pelicula - Búsqueda de Twitter _ Twitter9.html", name_dest_file, mode="a")

print()
print(get_weights_sentiment_analysis(name_dest_file, "es"))