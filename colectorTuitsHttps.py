"""
El inicio del texto del tweet es:
class="css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"><span class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0">

El final del texto del tweet es:
<span class="css-901oao css-16my406 r-4qtqp9 r-ip8ujx r-sjv1od r-zw8f10 r-bnwqim r-h9hxbl">

Espacios:
</span><span class="css-901oao css-16my406 r-poiln3 r-b88u0q r-bcqeeo r-qvutc0">
"""



import re


inicio_texto = 'class="css-901oao r-18jsvk2 r-1qd0xha r-a023e6 r-16dba41 r-rjixqe r-bcqeeo r-bnwqim r-qvutc0"><span class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0">'
fin_texto = '<span class="css-901oao css-16my406 r-4qtqp9 r-ip8ujx r-sjv1od r-zw8f10 r-bnwqim r-h9hxbl">'
caracter_espacio = '</span><span class="css-901oao css-16my406 r-poiln3 r-b88u0q r-bcqeeo r-qvutc0">'
caracter_espacio2 = '</span><span class="css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0">'


def remove_paterns(line):
    line = re.sub('src="([./\- A-z, áéíóú0-9])*"', " ", line)
    #line = re.sub('<(["./\- A-z, áéíóú0-9])*>', " ", line)
    line = re.sub('<div class="[./\- A-z, áéíóú0-9]*">', " ", line)
    line = re.sub('<div lang="[./\- A-z, áéíóú0-9]*" dir="[./\- A-z, áéíóú0-9]*" ', " ", line)
    line = re.sub('<[./\- A-z, áéíóú0-9]*="[./\- A-z, áéíóú0-9]*" ', " ", line)
    line = re.sub('[./\- A-z, áéíóú0-9]*="[./\- A-z, áéíóú0-9]*" ', " ", line)
    line = re.sub('</[./\- A-z, áéíóú0-9]*>', " ", line)
    line = re.sub('class ="[./\- A-z, áéíóú0-9]*" >', " ", line)
    line = re.sub('[A-záéíóú0-9]*="[./\- A-z, áéíóú0-9]*"', " ", line)

    return line


def get_tweets_from_html(name_html_file, name_dest_file, mode="w+"):
    fd = open(name_html_file)
    fd_salida = open(name_dest_file, mode)

    is_in_text = False
    text_tweet = []
    for line in fd.readlines():
        line_origin = line
        if is_in_text or line.__contains__(inicio_texto):
            index_init = 0
            if line.__contains__(inicio_texto):
                index_init = line.index(inicio_texto)
                line = line[index_init+inicio_texto.__len__():]
            if line.__contains__(fin_texto):
                index_end = line.index(fin_texto)
                line = line[:index_end-fin_texto.__len__()]

            is_in_text = True
            line = line.replace(inicio_texto, "").replace(caracter_espacio, " ").replace(caracter_espacio2, " ")\
                .replace("class="," ").replace("<", " <")
            line = remove_paterns(line)
            if line.__contains__("<"):
                end_line=line.index("<")
                line = line[:end_line-1]
            text_tweet.append(line.replace("\n", ""))
        if is_in_text and line_origin.__contains__(fin_texto):
            is_in_text = False
            print(text_tweet)
            fd_salida.write(" ".join(text_tweet) + "\n")
            text_tweet = []


