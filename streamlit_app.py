import streamlit as st

# 페이지 기본 설정
st.set_page_config(page_title="자기소개", layout="centered")

# 헤더 섹션
st.title("👋 자기소개")
st.divider()

# 프로필 섹션
col1, col2 = st.columns([1, 2])
with col1:
    st.image("https://via.placeholder.com/200", width=200)

with col2:
    st.subheader("왕효원")
    st.write("학생")
    st.write("**소속:** 숙명여자대학교")

st.divider()

# 자기소개 섹션
st.subheader("📝 자기소개")
st.write("""
당신의 자기소개를 여기에 작성하세요.
- 경력사항
- 관심분야
- 목표
""")

st.divider()

# 기술 스택 섹션
st.subheader("🛠️ 기술 스택")
col1, col2, col3 = st.columns(3)
with col1:
    st.write("**언어**")
    st.write("- Python\n- JavaScript")

with col2:
    st.write("**프레임워크**")
    st.write("- Streamlit\n- React")

with col3:
    st.write("**기타**")
    st.write("- Git\n- SQL")

st.divider()

# 경력 섹션
st.subheader("💼 경력/프로젝트")
st.write("""
**프로젝트 1**
- 설명: 프로젝트 설명

**프로젝트 2**
- 설명: 프로젝트 설명
""")


