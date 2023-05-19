import os
import requests
from bs4 import BeautifulSoup
import smtplib


MY_EMAIL = os.environ.get('MY_EMAIL')
APP_PASSWORD = os.environ.get('APP_PASSWORD')
EMAIL_RECIPIENTS = ['email_recipient@email.com', 'second_recipient@email.com']


def recorded_future():
    rf_url = "https://therecord.media/"

    response = requests.get(rf_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    top_arts = soup.find_all('a', class_='featured-articles__article')
    arts = []
    for article in top_arts:
        text = article.text.strip()
        link = str(rf_url + article['href'])
        final_str = str(f"{text}\nURL: {link}\n\n")
        arts.append(final_str)
    return arts


def krebs_on_security():
    kos_url = "https://krebsonsecurity.com/"
    response = requests.get(kos_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    top_art = soup.find('h2', class_='entry-title')
    text = top_art.text.strip()
    link = top_art.a.get('href')
    arts = []
    final_str = str(f"{text}\nURL: {link}\n\n")
    arts.append(final_str)
    return arts


def dark_reading():
    dr_url = 'https://www.darkreading.com/'
    response = requests.get(dr_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    link = soup.find('div', class_='spotlight-left').a['href']
    title = soup.find('div', class_='spotlight-left').a.text.strip()
    title_str = str(f"{title}\nURL: {link}\n\n")
    arts = [title_str]
    top_arts = soup.find_all('a', class_='article-title')
    for article in top_arts:
        text = article.text.strip()
        link = article['href']
        final_str = str(f"{text}\nURL: {link}\n\n")
        arts.append(final_str)
    return arts


def the_hacker_news():
    thn_url = 'https://thehackernews.com/'
    response = requests.get(thn_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    top_arts = soup.find_all('div', class_='body-post clear', limit=5)
    arts = []
    for article in top_arts:
        child_title = article.find('h2', {'class': 'home-title'})
        text = child_title.text.strip()
        child_link = article.find('a', {'class': 'story-link'})
        link = child_link['href']
        final_str = str(f"{text}\nURL: {link}\n\n")
        arts.append(final_str)
    return arts


def zd_net():
    zd_url = 'https://www.zdnet.com/topic/security/'
    response = requests.get(zd_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    top_arts = soup.find('section', class_='module topic-latest')
    child_title = top_arts.find_all('li', {'class': 'item'}, limit=2)
    arts = []
    for article in child_title:
        text = article.a.get('title').strip()
        child_link = article.a.get('href')
        link = str('https://www.zdnet.com/article' + child_link)
        final_str = str(f"{text}\nURL: {link}\n\n")
        arts.append(final_str)
    return arts


def infosec_magazine():
    ism_url = 'https://www.infosecurity-magazine.com/'
    response = requests.get(ism_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    top_arts = soup.find('div', class_='whats-hot-stories')
    child_title = top_arts.find_all('a', {'class': 'wrapper-link'}, limit=4)
    arts = []
    for article in child_title:
        article_title = article.find('h3', {'class': 'content-headline'})
        text = article_title.text.strip()
        link = article.get('href')
        final_str = str(f"{text}\nURL: {link}\n\n")
        arts.append(final_str)
    return arts


def sc_magazine():
    scm_url = 'https://www.scmagazine.com/'
    response = requests.get(scm_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    top_arts = soup.find_all('a', {'class': 'font-sans fs-5'}, limit=3)
    arts = []
    for article in top_arts:
        child_text = article.find('h4', {'class': 'ContentTeaserCard_title__gIxrq'})
        child_text2 = article.find('h5', {'class': 'ContentTeaserCard_title__gIxrq'})
        if child_text is not None:
            text = child_text.text.strip()
        else:
            text = child_text2.text.strip()
        link_final = article.get('href')
        link = str('https://www.scmagazine.com' + link_final)
        final_str = str(f"{text}\nURL: {link}\n\n")
        arts.append(final_str)
    return arts


def cyberscoop():
    cs_url = 'https://cyberscoop.com/'
    response = requests.get(cs_url)
    soup = BeautifulSoup(response.content, 'html.parser')
    top_title = soup.find('div', {'class': 'featured-island'})
    top_text = top_title.find('a', {'class': 'post-item__title-link'})
    text_top = top_text.text.strip()
    top_link = top_text.get('href')
    arts = []
    title_str = str(f"{text_top}\nURL: {top_link}\n\n")
    arts.append(title_str)
    top_arts = soup.find('ol', {'class': 'featured-headlines'})
    child_text = top_arts.find_all('a', {'class': 'post-item__title-link'}, limit=3)
    for article in child_text:
        text = article.text.strip()
        link = article.get('href')
        final_str = str(f"{text}\nURL: {link}\n\n")
        arts.append(final_str)
    return arts


def print_news():
    try:
        rf = recorded_future()
    except Exception as e:
        print(f"Error fetching Recorded Future data: {e}")
        rf = []

    try:
        kos = krebs_on_security()
    except Exception as e:
        print(f"Error fetching Krebs on Security data: {e}")
        kos = []

    try:
        dr = dark_reading()
    except Exception as e:
        print(f"Error fetching Dark Reading data: {e}")
        dr = []

    try:
        thn = the_hacker_news()
    except Exception as e:
        print(f"Error fetching The Hacker News data: {e}")
        thn = []

    try:
        zd = zd_net()
    except Exception as e:
        print(f"Error fetching ZDNet data: {e}")
        zd = []

    try:
        ism = infosec_magazine()
    except Exception as e:
        print(f"Error fetching InfoSec Magazine data: {e}")
        ism = []

    try:
        sc = sc_magazine()
    except Exception as e:
        print(f"Error fetching SC Magazine data: {e}")
        sc = []

    try:
        cs = cyberscoop()
    except Exception as e:
        print(f"Error fetching CyberScoop data: {e}")
        cs = []

    arts_list = [rf, kos, dr, thn, zd, ism, sc, cs]
    print_list = []
    for li in arts_list:
        print_list.extend(li)
    return print_list


print_list = print_news()


def format_string():
    # pn = print_news()
    result_string = ''.join(print_list)
    string_ = "".join(result_string).encode('ascii', 'ignore').decode('ascii')
    return string_


string_ = format_string()


def sendmail():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=APP_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=EMAIL_RECIPIENTS,
            msg=f"subject: Cybersecurity Daily Newsletter:\n\n{string_}"
        )


sm = sendmail()

