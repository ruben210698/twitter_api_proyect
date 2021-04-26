from amazonComprehend import get_weights_sentiment_analysis
from colectorTuits import generate_file_content_tuits
from colectorTuitsHttps import get_tweets_from_html

#name_file_es = "anne_with_an_e"
#print(generate_file_content_tuits(name_file_es, query = "Anne%20with%20an%20E", mode = 'w+'))
#print(generate_file_content_tuits(name_file_es, query = "Anne%20Netflix", mode = 'a'))



name_html_file5 = "https_downloaded/anne_with_e/anne with an e - Búsqueda de Twitter _ Twitter5.html"
name_html_file4 = "https_downloaded/anne_with_e/anne with an e - Búsqueda de Twitter _ Twitter4.html"
name_html_file3 = "https_downloaded/anne_with_e/anne with an e - Búsqueda de Twitter _ Twitter3.html"
name_html_file2 = "https_downloaded/anne_with_e/anne with an e - Búsqueda de Twitter _ Twitter2.html"
name_html_file1 = "https_downloaded/anne_with_e/anne with an e - Búsqueda de Twitter _ Twitter.html"

name_dest_file = "generated_files_from_html/anne_with_e_tweets"

get_tweets_from_html(name_html_file1, name_dest_file, mode="w+")
get_tweets_from_html(name_html_file2, name_dest_file, mode="a")
get_tweets_from_html(name_html_file3, name_dest_file, mode="a")
get_tweets_from_html(name_html_file4, name_dest_file, mode="a")
get_tweets_from_html(name_html_file5, name_dest_file, mode="a")

print()
print(get_weights_sentiment_analysis(name_dest_file, "es"))