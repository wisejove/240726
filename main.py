import streamlit as st
st.title('나의 첫 웹 서비스 만들기')
name = st.tect_input('이름을 번역해주세요:')
menu = st.selectbox('좋아하는 음식을 선택해주세요;', ['커피', '망고빙수', '복숭아'])
if st.button('인사말 생성')
  st.write(name+'당신이 좋아하는 음식은 '+menu+'입니다.')
