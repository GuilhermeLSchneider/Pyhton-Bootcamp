from bs4 import BeautifulSoup

# with open('Aula 8/home.html', 'r') as file:
#     content = file.read()
    
#     soup = BeautifulSoup(content, 'lxml')
#     # headers = soup.find('h5')
#     courses_html_tags = soup.find_all('h5') # retorna uma lista de tags h5 que contem os nomes dos cursos
    
#     # Melhorando a visualização dos cursos
#     for course in courses_html_tags:
#         print(course.text)
    
with open('Aula 8/home.html', 'r') as file:
    content = file.read()
    
    soup = BeautifulSoup(content, 'lxml')
    course_cards = soup.find_all('div', class_='card') 
    # A utilização do class_ é para evitar conflitos com a palavra reservada class do Python,
    # fazendo com que o BeautifulSoup entenda que estamos nos referindo a um atributo de classe do HTML
    
    for course in course_cards:
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]
        print(f'{course_name} costs {course_price}')