import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from matplotlib.font_manager import FontProperties
import os

# 한글 폰트 설정
font_path = os.path.join(os.path.dirname(__file__), 'fonts/NanumGothic-Bold.ttf')
font_prop = FontProperties(fname=font_path)
plt.rcParams['axes.unicode_minus'] = False

sns.set_style("whitegrid")

# 페이지 기본 설정
st.set_page_config(page_title="자기소개", layout="centered")

# 시각화 섹션
st.subheader("📊 데이터 시각화")

# 1. Matplotlib 예제 - 학습 진도
st.write("**1️⃣ 기술 숙련도 (Matplotlib)**")
fig, ax = plt.subplots(figsize=(10, 5))

skills = ['Python', 'JavaScript', 'Streamlit', 'React', 'SQL']
proficiency = [85, 75, 90, 70, 80]

ax.barh(skills, proficiency, color=['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'])
ax.set_xlabel('숙련도 (%)', fontsize=12, fontproperties=font_prop)
ax.set_title('기술 스택별 숙련도', fontsize=14, fontweight='bold', fontproperties=font_prop)
ax.set_xlim(0, 100)

for i, v in enumerate(proficiency):
    ax.text(v + 2, i, str(v) + '%', va='center', fontproperties=font_prop)

st.pyplot(fig)

# 2. Seaborn 예제 - 상관관계
st.write("**2️⃣ 월별 학습 시간 (Seaborn)**")

# 샘플 데이터
np.random.seed(42)
months = ['1월', '2월', '3월', '4월', '5월', '6월']
study_hours = np.array([20, 25, 30, 28, 35, 32])
project_hours = np.array([10, 15, 20, 22, 25, 28])

fig, ax = plt.subplots(figsize=(10, 5))

x = np.arange(len(months))
width = 0.35

sns.barplot(x=x - width/2, y=study_hours, label='학습 시간', color='#45B7D1', ax=ax)
sns.barplot(x=x + width/2, y=project_hours, label='프로젝트 시간', color='#FF6B6B', ax=ax)

ax.set_xlabel('월', fontsize=12, fontproperties=font_prop)
ax.set_ylabel('시간', fontsize=12, fontproperties=font_prop)
ax.set_title('월별 학습 및 프로젝트 시간', fontsize=14, fontweight='bold', fontproperties=font_prop)
ax.set_xticks(x)
ax.set_xticklabels(months, fontproperties=font_prop)

# 범례 텍스트 한글 처리
legend = ax.legend()
for text in legend.get_texts():
    text.set_fontproperties(font_prop)

st.pyplot(fig)

# 3. Plotly 예제 - 인터랙티브 차트
st.write("**3️⃣ 프로젝트별 기여도 (Plotly)**")

projects = ['데이터 분석', 'AI 모델링', 'Web 개발', '모바일 앱', 'DevOps']
contribution = [25, 20, 30, 15, 10]
colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8']

fig = go.Figure(data=[go.Pie(
    labels=projects,
    values=contribution,
    marker=dict(colors=colors),
    hovertemplate='<b>%{label}</b><br>기여도: %{value}%<extra></extra>'
)])

fig.update_layout(
    title='프로젝트별 기여도 분포',
    font=dict(size=12),
    height=500
)

st.plotly_chart(fig, use_container_width=True)

# 4. Plotly 예제 - 라인 차트
st.write("**4️⃣ 실력 성장 추이 (Plotly)**")

weeks = list(range(1, 13))
python_level = [50, 55, 60, 62, 65, 68, 70, 72, 75, 77, 80, 85]
web_level = [40, 42, 45, 50, 52, 55, 58, 60, 62, 65, 68, 70]
ai_level = [30, 32, 35, 38, 40, 42, 45, 48, 50, 52, 55, 58]

fig = go.Figure()

fig.add_trace(go.Scatter(x=weeks, y=python_level, name='Python', mode='lines+markers', line=dict(color='#FF6B6B', width=3)))
fig.add_trace(go.Scatter(x=weeks, y=web_level, name='Web 개발', mode='lines+markers', line=dict(color='#45B7D1', width=3)))
fig.add_trace(go.Scatter(x=weeks, y=ai_level, name='AI/ML', mode='lines+markers', line=dict(color='#4ECDC4', width=3)))

fig.update_layout(
    title='12주간 실력 성장 추이',
    xaxis_title='주차',
    yaxis_title='숙련도 레벨',
    hovermode='x unified',
    height=500,
    font=dict(size=12)
)

st.plotly_chart(fig, use_container_width=True)


