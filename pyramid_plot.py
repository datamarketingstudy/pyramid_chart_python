#pip install plotly

# import library
import pandas as pd
import plotly.graph_objs as go

# import data (Korea Population in 2021)
data = pd.read_excel('/Users/geonseunglee/Desktop/Python/population_data.xlsx')
data.head()

# Data Preprocessing
age_sgmt = data['연령대']
male_data = data['남자']*-1
female_data = data['여자']

# Pyramid Plot
# Created figure
fig = go.Figure()

# Adding Male Data
fig.add_trace(go.Bar(x = male_data,
                    y = age_sgmt,
                    name = '남성',
                    orientation = 'h',
                    text = round(-1*male_data/10000,1)))
# Adding Female Data
fig.add_trace(go.Bar(x = female_data,
                    y = age_sgmt,
                    name = '여성',
                    orientation = 'h',
                    text = round(female_data/10000, 1)))

# Updating the layout for our graph
fig.update_layout(title = '2020년 대한민국 인구 피라미드',
                 title_font_size = 22,
                 barmode = 'overlay',
                 bargap = 0.0,
                 bargroupgap = 0,
                 xaxis = dict(tickvals = [-3000000, -2000000, -1000000, 0, 1000000, 2000000, 3000000],
                             ticktext = ['3백만', '2백만', '1백만', '0', '1백만', '2백만', '3백만'],
                             title = '인구 수(백만명)',
                             title_font_size = 14))

fig.show()

## Population & User

# Import Data (User Data)
user_data = pd.read_excel('/Users/geonseunglee/Desktop/Python/user_cnt_data.xlsx')
user_data.head()

# Data Preprocessing
user_age_sgmt = user_data['연령대']
user_male_data = user_data['남자(자사 서비스)']*-1
user_female_data = user_data['여자(자사 서비스)']

# Pyramid Plot with User
# Created figure
fig = go.Figure()

# Adding Male Data
fig.add_trace(go.Bar(x = male_data,
                    y = age_sgmt,
                    name = '남성',
                    orientation = 'h',
                    marker=dict(color='powderblue'),
                    text = round(-1*male_data/10000,1)))

# Adding Female Data
fig.add_trace(go.Bar(x = female_data,
                    y = age_sgmt,
                    name = '여성',
                    orientation = 'h',
                    marker=dict(color='seagreen'),
                    text = round(female_data/10000, 1)))

# Adding Male User Data
fig.add_trace(go.Bar(x = user_male_data,
                    y = user_age_sgmt,
                    name = '남성 유저',
                    orientation='h',
                    hoverinfo='x',
                    showlegend=False,
                    opacity=0.5,
                    marker=dict(color='teal'),
                    text = round(-1*user_male_data/10000,1)))

# Adding Female User Data
fig.add_trace(go.Bar(x = user_female_data,
                    y = user_age_sgmt,
                    name = '남성 유저',
                    orientation='h',
                    hoverinfo='x',
                    showlegend=False,
                    opacity=0.5,
                    marker=dict(color='darkgreen'),
                    text = round(user_female_data/10000, 1)))


# Updating the layout for our graph
fig.update_layout(title = '2020년 대한민국 인구 피라미드&자사 서비스 유저 수',
                 title_font_size = 22,
                 barmode = 'overlay',
                 bargap = 0.0,
                 bargroupgap = 0,
                 xaxis = dict(tickvals = [-3000000, -2000000, -1000000, 0, 1000000, 2000000, 3000000],
                             ticktext = ['3백만', '2백만', '1백만', '0', '1백만', '2백만', '3백만'],
                             title = '인구 수(백만명)',
                             title_font_size = 14))

fig.show()