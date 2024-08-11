import streamlit as st

# 페이지 정보 저장을 위한 딕셔너리
if 'responses' not in st.session_state:
    st.session_state.responses = {}

# 1번 페이지: 심리테스트 설명 및 시작 버튼
def page1():
    st.markdown(
        """
        <style>
        /* 페이지 전체 배경 이미지 설정 */
        [data-testid="stAppViewContainer"] > .main {
            background-image: url('https://url.kr/yrp8ow');
            background-size: 100vw 100vh;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }
        /* 중앙에 이미지 배치 */
        .centered-image {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 50%;
        }
        /* 버튼 스타일링 */
        .stButton button {
            background-image: url('https://url.kr/5ttzmc');
            background-size: cover;
            color: white;
            font-size: 20px;
            height: 50px;
            width: 200px;
            border-radius: 12px;
            border: none;
            cursor: pointer;
            transition: background-color 0.3s ease;
        }
        .stButton button:hover {
            background-color: #555555;  /* 호버 시 배경 색상 변경 */
        }
        /* 헤더와 풋터 숨기기 */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div style="text-align: center; color: white; font-size: 48px; font-weight: bold;">심리테스트</div>', unsafe_allow_html=True)

    # 중앙에 GIF 이미지 배치
    st.markdown('<img src="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" class="centered-image">', unsafe_allow_html=True)

    st.write('<p style="text-align: center; color: white;">이 심리테스트는 간단한 질문을 통해 당신의 성향을 파악합니다. 테스트를 시작하려면 아래 버튼을 눌러주세요.</p>', unsafe_allow_html=True)

    if st.button("테스트 시작하기"):
        st.session_state.page = 2
        st.experimental_rerun()

# 2번 페이지: 사탕을 좋아하나요?
def page2():
    st.markdown(
        """
        <style>
        /* 헤더와 풋터 숨기기 */
        header {visibility: hidden;}
        footer {visibility: hidden;}
        </style>
        """,
        unsafe_allow_html=True
    )
    
    st.title("사탕에 대한 질문")
    st.markdown(f'<img src="https://url.kr/yrp8ow" width="700" class="centered-image">', unsafe_allow_html=True)  # HTML로 이미지 삽입
    st.write("사탕을 좋아하십니까?")
    if st.button("좋아한다"):
        st.session_state.responses['사탕'] = "좋아한다"
        st.session_state.page = 3
        st.experimental_rerun()
    elif st.button("안 좋아한다"):
        st.session_state.responses['사탕'] = "안 좋아한다"
        st.session_state.page = 3
        st.experimental_rerun()

# 3번 페이지: 초콜릿을 좋아하나요?
def page3():
    st.title("초콜릿에 대한 질문")
    st.image('https://url.kr/yrp8ow')  # 초콜릿 질문 페이지에 이미지 추가
    st.write("초콜릿을 좋아하십니까?")
    if st.button("좋아한다"):
        st.session_state.responses['초콜릿'] = "좋아한다"
        st.session_state.page = 4
        st.experimental_rerun()
    elif st.button("안 좋아한다"):
        st.session_state.responses['초콜릿'] = "안 좋아한다"
        st.session_state.page = 4
        st.experimental_rerun()

# 4번 페이지: 결과
def page4():
    st.title("테스트 결과")
    st.image('https://url.kr/yrp8ow')  # 결과 페이지에 이미지 추가
    st.write("테스트가 종료되었습니다.")
    st.write("당신의 선택은 다음과 같습니다:")
    st.write(f"사탕: {st.session_state.responses['사탕']}")
    st.write(f"초콜릿: {st.session_state.responses['초콜릿']}")
    st.write("테스트에 참여해 주셔서 감사합니다!")

# 페이지 이동 로직
if 'page' not in st.session_state:
    st.session_state.page = 1

if st.session_state.page == 1:
    page1()
elif st.session_state.page == 2:
    page2()
elif st.session_state.page == 3:
    page3()
elif st.session_state.page == 4:
    page4()
