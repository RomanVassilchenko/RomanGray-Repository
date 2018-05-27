import vk
import json

MY_USER_ID = "269965000"
session = vk.Session()
vkapi = vk.API(session)

p = vkapi.friends.get(user_id=MY_USER_ID,fields='uid,20first_name,%20last_name,%20sex,%20bdate,%20city,%20country,%20photo_200,%20online,%20lists,%20screen_name,%20contacts,%20education,%20universities,%20schools,%20activity,%20last_seen,%20relation,%20counters,%20nickname,%20relatives,%20interests,%20movies,%20tv,%20books,%20games,%20about,%20connections',v=5.74)

user_city=''
user_university_name=''
user_faculty_name=''
user_school=''
w='''<html><head><title>Отчет о друзьях</title><meta charset="utf-8">
<style>
body {
background: gray;
}
.pic {
display: inline-block;
vertical-align: top;
width: 200px;
height: auto;
margin-bottom: 10px;
}
.text {
display: inline-block;
vertical-align: top;
width: calc(100% - 300px);
height: auto;
padding-left: 20px;
margin-bottom: 10px;
}
.all {
background: white;
padding: 30px;
margin: 30px;
border-radius: 5px;
}
.all2 {
background: silver;
}
.two {
font-weight: bold;
color: red;
}
</style>
</head><body>'''

for x in p['items']:
    print('Ищем друзей юзера '+str(x['id']))
    w=w+'<a target="_blank" href="http://vk.com/id'+str(x['id'])+'"><div class="all all2"><div class="pic">'
    if(('photo_200' in x) and (x['photo_200']!='')):
        w=w+'<img src="'+x['photo_200'].translate(non_bmp_map)+'">'
    w=w+'</div><div class="text">'
    if('first_name' in x):
        w=w+'<div class="one">'+('Имя: '+x['first_name'])+'</div>'
    if('last_name' in x):
        user_last_name=x['last_name']
        w=w+'<div class="one">Фамилия: '+user_last_name+'</div>'
    if('sex' in x):
        if(x['sex']==2):
            w=w+'<div class="one">'+('Пол: мужской')+'</div>'
        if(x['sex']==1):
            w=w+'<div class="one">'+('Пол: женский')+'</div>'
    if(('nickname' in x) and (x['nickname']!='')):
        w=w+'<div class="one">'+('Ник: '+x['nickname'])+'</div>'
    if(('screen_name' in x) and (x['screen_name']!='')):
        w=w+'<div class="one">'+('Ник2: '+x['screen_name'])+'</div>'
    if('bdate' in x):
        user_date=str(x['bdate'])
        w=w+'<div class="one">'+('День рождения: '+str(x['bdate']))+'</div>'
    if(('city' in x) and (x['city']!=0)):
        ss=requests.get('https://api.vk.com/method/database.getCitiesById?city_ids='+str(x['city'])).text
        pp = json.loads(ss)
        user_city=pp['response'][0]['name']
        w=w+'<div class="one">Город: '+user_city+'</div>'
    if('last_seen' in x):
        w=w+'<div class="one">Последний раз был(а) - '+(time.ctime(x['last_seen']['time']))+'</div>'
    if(('university_name' in x) and (x['university_name']!='')):
        user_university_name=x['university_name'].translate(non_bmp_map)
        w=w+'<div class="one">Университет: '+user_university_name+'</div>'
    if(('faculty_name' in x) and (x['faculty_name']!='')):
        user_faculty_name=x['faculty_name'].translate(non_bmp_map)
        w=w+'<div class="one">Факультет: '+user_faculty_name+'</div>'
    if(('interests' in x) and (x['interests']!='')):
        w=w+'<div class="one">'+('Интересы: '+x['interests'].translate(non_bmp_map))+'</div>'
    if(('movies' in x) and (x['movies']!='')):
        w=w+'<div class="one">'+('Фильмы: '+x['movies'].translate(non_bmp_map))+'</div>'
    if(('tv' in x) and (x['tv']!='')):
        w=w+'<div class="one">'+('Шоу: '+x['tv'].translate(non_bmp_map))+'</div>'
    if(('books' in x) and (x['books']!='')):
        w=w+'<div class="one">'+('Книги: '+x['books'].translate(non_bmp_map))+'</div>'
    if(('games' in x) and (x['games']!='')):
         w=w+'<div class="one">'+('Игры: '+x['games'].translate(non_bmp_map))+'</div>'
    if(('schools' in x) and (len(x['schools'])>0)):
        for z in x['schools']:
            y='<div class="one">'
            y=y+('Школа: ')
            user_school=z['id']
            y=y+(z['name'])
            if('year_graduated' in z):
                y=y+(' '+str(z['year_graduated']))
            y=y+'</div>'
            w=w+y
    if(('about' in x) and (x['about']!='')):
        w=w+'<div class="one">'+('О себе: '+x['about'].translate(non_bmp_map))+'</div>'
    w=w+'</div></div></a>'

p = vkapi.friends.get(user_id=MY_USER_ID,v=5.74)
friends=''
fr=[]
for x in p['items']:
    friends=friends+str(x)+','
    fr.append(str(x))
friends = friends[0:-1]

p = vkapi.users.get(user_ids=friends, fields='uid,%20first_name,%20last_name,%20sex,%20bdate,%20city,%20country,%20photo_200,%20online,%20lists,%20screen_name,%20contacts,%20education,%20universities,%20schools,%20activity,%20last_seen,%20relation,%20counters,%20nickname,%20relatives,%20interests,%20movies,%20tv,%20books,%20games,%20about,%20connections',v=5.74)

w=w+'<div class="friends">'

for x in p:
    print(x)
    w=w+'<div class="all" id="id'+str(x['id'])+'"><div class="pic">'
    if(('photo_200' in x) and (x['photo_200']!='')):
        w=w+'<img src="'+x['photo_200'].translate(non_bmp_map)+'">'
    w=w+'</div><div class="text"><div class="one"><a target="_blank" href="http://vk.com/id'+str(x['id'])+'">http://vk.com/id'+str(x['id'])+'</a></div>'
    if('first_name' in x):
        w=w+'<div class="one">'+('Имя: '+x['first_name'])+'</div>'
    if('last_name' in x):
        w=w+'<div class="one">'+('Фамилия: '+x['last_name'])+'</div>'
    if('sex' in x):
        if(x['sex']==2):
            w=w+'<div class="one">'+('Пол: мужской')+'</div>'
        if(x['sex']==1):
            w=w+'<div class="one">'+('Пол: женский')+'</div>'
    if(('nickname' in x) and (x['nickname']!='')):
        w=w+'<div class="one">'+('Ник: '+x['nickname'])+'</div>'
    if(('screen_name' in x) and (x['screen_name']!='')):
        w=w+'<div class="one">'+('Ник2: '+x['screen_name'])+'</div>'
    if(('bdate' in x) and (str(x['bdate'])!='')):
        w=w+'<div class="one">'+('День рождения: '+str(x['bdate']))+'</div>'
    if(('city' in x) and (x['city']!=0)):
        ss=requests.get('https://api.vk.com/method/database.getCitiesById?city_ids='+str(x['city'])).text
        pp = json.loads(ss)
        w=w+'<div class="one">Город: '+pp['response'][0]['name']+'</div>'
        if((user_city!='') and (user_city==pp['response'][0]['name'])):
            w=w+'<div class="one two">'+('Живет в одном городе с данной личностью')+'</div>'
    if('last_seen' in x):
        w=w+'<div class="one">Последний раз был(а) - '+(time.ctime(x['last_seen']['time']))+'</div>'
    if(('university_name' in x) and (x['university_name']!='')):
        w=w+'<div class="one">Университет: '+x['university_name'].translate(non_bmp_map)+'</div>'
        if(user_university_name==x['university_name'].translate(non_bmp_map)):
            w=w+'<div class="one two">'+('Учились в одном университете')+'</div>'
    if(('faculty_name' in x) and (x['faculty_name']!='')):
        w=w+'<div class="one">Факультет: '+x['faculty_name'].translate(non_bmp_map)+'</div>'
        if(user_faculty_name==x['faculty_name'].translate(non_bmp_map)):
            w=w+'<div class="one two">Факультет: '+('Учились на одном факультете')+'</div>'
    if(('interests' in x) and (x['interests']!='')):
        w=w+'<div class="one">'+('Интересы: '+x['interests'].translate(non_bmp_map))+'</div>'
    if(('movies' in x) and (x['movies']!='')):
        w=w+'<div class="one">'+('Фильмы: '+x['movies'].translate(non_bmp_map))+'</div>'
    if(('tv' in x) and (x['tv']!='')):
        w=w+'<div class="one">'+('Шоу: '+x['tv'].translate(non_bmp_map))+'</div>'
    if(('books' in x) and (x['books']!='')):
        w=w+'<div class="one">'+('Книги: '+x['books'].translate(non_bmp_map))+'</div>'
    if(('games' in x) and (x['games']!='')):
        w=w+'<div class="one">'+('Игры: '+x['games'].translate(non_bmp_map))+'</div>'
    if(('schools' in x) and (len(x['schools'])>0)):
        for z in x['schools']:
            if(z['id']==user_school):
                w=w+'<div class="one two">'+('Учились в одной школе')+'</div>'
            y='<div class="one">'
            y=y+('Школа: ')
            user_school=z['id']
            y=y+(z['name'])
            if('year_graduated' in z):
                y=y+(' '+str(z['year_graduated']))
            y=y+'</div>'
            w=w+y
    if(('about' in x) and (x['about']!='')):
        w=w+'<div class="one">'+('О себе: '+x['about'].translate(non_bmp_map))+'</div>'
    try:    
        ppp = vkapi.friends.get(user_id=str(x['id']),v=5.74)
    except:
        print('user deactivated!')
    r=''
    try:
        for xxx in ppp['items']:
            if(str(xxx) in fr):
                pppp=p = vkapi.users.get(user_ids=str(xxx), fields='first_name,%20last_name',v=5.74)
                mn=''
                for xxxx in pppp:
                    if('first_name' in xxxx):
                        mn=mn+xxxx['first_name']+' '
                    if('last_name' in xxxx):
                        mn=mn+xxxx['last_name']
                r=r+'<a href="#id'+str(xxx)+'">'+mn+' (id'+str(xxx)+')</a>, '
    except: pass
    if(r!=''):
        w=w+'<div class="one">Общие друзья: '+r+'</div>'
    

    w=w+'</div></div>'
    
w=w+'</div>'
print("Process complete")
with open("out.html","w",encoding='utf-8') as out:
    print(w, file=out)
out.close()
