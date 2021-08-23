import streamlit as st
import pandas as pd
import requests
import json
import time
import vk
import sys


st.title('Сервис для проверки физического лица')

st.sidebar.header('Введите данные для проверки ФССП и по списку террористов')


def user_input_features():
    firstname = st.sidebar.text_input('Введите ИМЯ')
    lastname = st.sidebar.text_input('Введите ФАМИЛИЮ')
    secondname = st.sidebar.text_input('Введите Отчество')
    region = st.sidebar.text_input('Введите РЕГИОН')
    birthdate = st.sidebar.text_input('Введите Дату Рождения дд.мм.гггг')
    data = {'ИМЯ': [firstname],
            'Фамилия': [lastname],
            'Отчество':[secondname],
            'Регион': [region],
            'Дата Рождения дд.мм.гггг': [birthdate]}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('Проверяемое физическое лицо')
st.write(df)

st.subheader('Результаты проверки ФССП')

submit = st.sidebar.button('Проверить ФССП')
submit4 = st.sidebar.button('Проверить по списку террористов')

if submit:
    token = "igaAOGpeDc5L"
    region = df['Регион'].values
    firstname = df['ИМЯ'].values
    lastname = df['Фамилия'].values
    secondname = df['Отчество'].values
    birthdate = df['Дата Рождения дд.мм.гггг'].values
    get_params = {'token': 'igaAOGpeDc5L', 'region': region, 'firstname': firstname, 'lastname': lastname, 'birthdate': birthdate}
    response = requests.get('https://api-ip.fssp.gov.ru/api/v1.0/search/physical', params=get_params)
    todos = json.loads(response.text)
    values = list(todos.values())
# print(values[3])
    val = list(values[3].values())
#print(val[0])
    v = str(val[0])
    status = requests.get('https://api-ip.fssp.gov.ru/api/v1.0/status', params={'token': 'igaAOGpeDc5L', 'task': v})
    stat = json.loads(status.text)
    star = list(stat.values())
    strr = list(star[3].values())
    s = int(strr[0])
    while s != 0:
        time.sleep(3)
        status = requests.get('https://api-ip.fssp.gov.ru/api/v1.0/status', params={'token': 'igaAOGpeDc5L', 'task': v})
        stat = json.loads(status.text)
        star = list(stat.values())
        strr = list(star[3].values())
        s = int(strr[0])
    result = requests.get('https://api-ip.fssp.gov.ru/api/v1.0/result', params={'token': 'igaAOGpeDc5L', 'task': v})
#print(result.json())

    result1 = json.loads(result.text)
    #df1 = pd.DataFrame.from_dict(result1, orient='columns')
    values1 = list(result1.values())
    values2 = list(values1[3].values())
    values3 = list(values2[3])
    pd.set_option('display.max_rows', 2)
    pd.set_option('display.max_columns', 4)
    pd.set_option('display.max_colwidth', None)
    df1 = pd.DataFrame(values3)
    df2 = df1['result'].tolist()
    st.write(df2)


st.subheader('Результаты проверки по Соц. сети ВК')
st.sidebar.header('Введите ссылку на аккаунт ВК')
ids = st.sidebar.text_input('Введите ссылку')

submit2 = st.sidebar.button('Проверить ВК')
if submit2:
#ids = 'pavlovsemen'
    token = "9fedfe869fedfe869fedfe86da9f9a681d99fed9fedfe86ff6878bde6fbf0523510ed49"  # Сервисный ключ доступа
    session = vk.Session(access_token=token)
    api = vk.API(session, v='11.9.1')
    person = api.users.get(user_ids=ids, fields='about, education, home_town, exports, interests, bdate')
    st.write(person)


st.sidebar.header('Полезные ссылки')
st.write('https://kad.arbitr.ru')










