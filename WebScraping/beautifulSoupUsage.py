from bs4 import BeautifulSoup

SIMPLE_HTML = '''<html>
<head></head>
<body>
<h1>This is a title</h1>
<p class="subtitle">Lorem ipsum dolor sit amet. Consectetur adipiscim elit.</p>
<p>Here's another p without a class</p>
<ul>
    <li>Rolf</li>
    <li>Charlie</li>
    <li>Jen</li>
    <li>Jose</li>
</ul>
</body>
</html>'''

simple_soup = BeautifulSoup(SIMPLE_HTML,'html.parser')

print(simple_soup.find('h1').string)

def find_list():
    li=simple_soup.find_all('li')
    ls= [i.string for i in li]
    print(ls)

def find_subtitle():
    sub=simple_soup.find('p',{'class':'subtitle'})
    print(sub)

def find_p():
    sub=simple_soup.find_all('p')
    ls=[l for l in sub if 'subtitle' not in l.attrs.get('class',[]) ]
    print(ls)

find_p()