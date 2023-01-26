import streamlit as st

# 이미지를 첨부하여 업로드하려면...
from PIL import Image # 파이썬 기본라이브러리는 바로 사용 가능!
import os

# 사이드바 만드는 방법 1: st.sidebar.요소명 
# Using object notation
# 사이드바에 셀렉트박스(혹은 라디오버튼 등등 뭐라도 좋습니다)로 
# 각 드라마 혹은 애니메이션의 제목 세개를 
# 선택할 수 있도록 해주세요
drama_select = ['더 글로리', '막내집 재벌아들', '환혼']
drama_select_option = st.sidebar.selectbox('좋아하는 드라마를 선택하세요', drama_select, index=2)

manhwa_select = ['짱구는 못말려', '도라에몽', '스폰지밥']
manhwa_select_option = st.sidebar.selectbox('좋아하는 만화를 선택하세요', manhwa_select, index=1)

# # 본문
folder = './data/'

# [col1, col2] = st.columns(2)

# with col1:
#     drama_image_files = ['the-glory.jfif', 'reborn-rich.jfif', 'soul.jfif']

#     # 사이드바에 있는 드라마 리스트의 0, 1, 2 순서에 맞춰서 텍스트 데이터가 호출된다
#     html = """
#     <style>
#     h2 {
#         color : blue;
#     }
#     <style>
#     """

#     st.markdown(html, unsafe_allow_html=True)
#     st.header(drama_select_option)

#     # 서로 다른 리스트를 묶어서 호출하려면 같은 인덱스에 있음을 이용하면 됩니다
#     drama_select_index = drama_select.index(drama_select_option)

#     st.write(drama_select_index)
#     st.image(folder + drama_image_files[drama_select_index])

# with col2:
#     # 사이드바에 아까 선택하지 않은 것(애니메이션, 영화, 책 등등) 이미지파일3개 가져오셔서
#     manhwa_image_files = ['jjanggu.png',  'mong.jfif', 'bob.png']

#     # 사이드바에 있는 드라마 리스트의 0, 1, 2 순서에 맞춰서 텍스트 데이터가 호출된다
#     st.header(manhwa_select_option)

#     # 서로 다른 리스트를 묶어서 호출하려면 같은 인덱스에 있음을 이용하면 됩니다
#     manhwa_select_index = manhwa_select.index(manhwa_select_option)

#     st.write(manhwa_select_index)
#     st.image(folder + manhwa_image_files[manhwa_select_index])


import streamlit as st
import cv2
import numpy as np

# img_file_buffer = st.camera_input("Take a picture")

# if img_file_buffer is not None:
#     # To read image file buffer with OpenCV:
#     bytes_data = img_file_buffer.getvalue()
#     cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

#     # Check the type of cv2_img:
#     # Should output: <class 'numpy.ndarray'>
#     st.write(type(cv2_img))

#     # Check the shape of cv2_img:
#     # Should output shape: (height, width, channels)
#     st.write(cv2_img.shape)


    # 보통 사이드바 / 메뉴는 주제별로 서비스를 분류할 때 쓰입니다
    # 1) 드라마 좋아하는 목록
    # 2) 만화 좋아하는 목록
    # 3) 사진찍기




# 리팩토링(refactoring)

# 1. 하나의 파일에 3개를 다 때려박아놓고 클릭할 때마다 해당 div만 보이게 만들기
# 2. 각 기능별로 별도 파일 혹은 폴더로 만들어 놓고 클릭할 때마다 해당 파일에 들어가도록 만들기 
# 보통은 2번의 구조를 많이 사용합니다 
# -> 1_drama_app.py, 2_manhwa_app.py, 3_picture_app.py 3개로 파일을 분리해주세요 
# streamlit run 1_drama_app.py 
# streamlit run 2_manhwa_app.py
# streamlit run 3_picture_app.py

tab1, tab2, tab3 = st.tabs(["드라마", "만화", "사진"])

with tab1:
    drama_image_files = ['the-glory.jfif', 'reborn-rich.jfif', 'soul.jfif']

    # 사이드바에 있는 드라마 리스트의 0, 1, 2 순서에 맞춰서 텍스트 데이터가 호출된다
    html = """
    <style>
    h2 {
        color : blue;
    }
    <style>
    """

    st.markdown(html, unsafe_allow_html=True)
    st.header(drama_select_option)

    # 서로 다른 리스트를 묶어서 호출하려면 같은 인덱스에 있음을 이용하면 됩니다
    drama_select_index = drama_select.index(drama_select_option)

    st.write(drama_select_index)
    st.image(folder + drama_image_files[drama_select_index])

with tab2:
    # 사이드바에 아까 선택하지 않은 것(애니메이션, 영화, 책 등등) 이미지파일3개 가져오셔서
    manhwa_image_files = ['jjanggu.png',  'mong.jfif', 'bob.png']

    # 사이드바에 있는 드라마 리스트의 0, 1, 2 순서에 맞춰서 텍스트 데이터가 호출된다
    st.header(manhwa_select_option)

    # 서로 다른 리스트를 묶어서 호출하려면 같은 인덱스에 있음을 이용하면 됩니다
    manhwa_select_index = manhwa_select.index(manhwa_select_option)

    st.write(manhwa_select_index)
    st.image(folder + manhwa_image_files[manhwa_select_index])


with tab3:
    st.header("사진")
    img_file_buffer = st.camera_input("Take a picture")

    if img_file_buffer is not None:
        # To read image file buffer with OpenCV:
        bytes_data = img_file_buffer.getvalue()
        cv2_img = cv2.imdecode(np.frombuffer(bytes_data, np.uint8), cv2.IMREAD_COLOR)

        # Check the type of cv2_img:
        # Should output: <class 'numpy.ndarray'>
        st.write(type(cv2_img))

        # Check the shape of cv2_img:
        # Should output shape: (height, width, channels)
        st.write(cv2_img.shape)