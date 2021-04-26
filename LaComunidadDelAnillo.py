from amazonComprehend import get_weights_sentiment_analysis
from colectorTuits import generate_file_content_tuits


name_file_es = "la_comunidad_del_anillo"


generate_file_content_tuits(name_file_es, query = "el%20señor%20de%20los%20anillos", mode = 'w+')
generate_file_content_tuits(name_file_es, query = "la%20comunidad%20del%20anillo", mode = 'a+')

print(get_weights_sentiment_analysis("generated_files/" + name_file_es, "es"))

name_file_en = "la_comunidad_del_anillo_en"
generate_file_content_tuits(name_file_en, query = "The%20Fellowship%20of%20the%20Ring", mode = 'w+')
generate_file_content_tuits(name_file_en, query = "The%20Lord%20of%20the%20Rings", mode = 'a+')

print(get_weights_sentiment_analysis("generated_files/" + name_file_en, "en"))

