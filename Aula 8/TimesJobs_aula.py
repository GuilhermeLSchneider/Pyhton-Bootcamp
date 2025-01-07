import time
from bs4 import BeautifulSoup
import requests

# Utilização de uma input para filtrar as vagas de acordo com a inserida
print('Insira habilidades que você não é familiarizado: ')
unfamiliar_skills = input('>')
print(f'Filtrando vagas que não contém: {unfamiliar_skills}')

def find_jobs():
    # Utilização do requests para pegar o conteúdo HTML da página
    html_text = requests.get('https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=&searchTextText=&txtKeywords=python&txtLocation=').text
    # Utilização do BeautifulSoup para fazer o parsing do conteúdo HTML
    soup = BeautifulSoup(html_text, 'lxml')
    # Utilização do find_all para pegar as seções que possuem todas as vagas
    jobs = soup.find_all('li', class_='clearfix job-bx wht-shd-bx')

    # Iteração para pegar as informações de cada vaga, e salvar em um arquivo .txt com o index da vaga
    for index, job in enumerate(jobs):
        published_date = job.find('span', class_='sim-posted').span.text
        # Verificação se a vaga foi publicada recentemente
        if 'few' in published_date:
            company_name = job.find('h3', class_='joblist-comp-name').text.replace(' ', '')
            skills = job.find('div', class_='more-skills-sections').text.replace(' ', '')
            # Pega o link da vaga a partir da href 
            more_info = job.header.h2.a['href']
            # Verificação se a vaga não contém as habilidades inseridas, caso não contenha, salva o arquivo
            if unfamiliar_skills not in skills:
                # Faz a escrita do arquivo .txt com as informações da vaga
                with open(f'posts/{index}.txt', 'w') as f:
                    f.write(f'Company Name: {company_name.strip()} \n')
                    f.write(f'Required Skills: {skills.strip()} \n')
                    f.write(f'More Info: {more_info}')
                print(f'File saved: {index}')

# Loop para filtrar as vagas a cada 15 minutos
if __name__ == '__main__': # utilização do __main__ para garantir que o código só será executado se for o arquivo principal
    while True:
        find_jobs()
        print('Filtrando vagas a cada 15 minutos...')
        time.sleep(900)