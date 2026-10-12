import streamlit as st
import datetime

# --- 페이지 설정 및 제목 ---
st.set_page_config(page_title="오늘의 띠별 운세", layout="centered")
st.title("🔮 오늘의 띠별 운세")

# 오늘 날짜 표시
today = datetime.date.today()
st.write(f"오늘 날짜: **{today.strftime('%Y년 %m월 %d일')}**")
st.divider()

# --- 띠별 운세 데이터 딕셔너리 ---
fortune_data = {
    "쥐띠": {
        "score": "⭐⭐⭐⭐☆",
        "message": "노력한 만큼 결실을 맺는 날입니다. 주변 사람과의 협력에서 좋은 기회가 생깁니다."
    },
    "소띠": {
        "score": "⭐⭐⭐☆☆",
        "message": "성급하게 결정을 내리지 말고 차분히 상황을 지켜보는 것이 이득이 됩니다."
    },
    "호랑이띠": {
        "score": "⭐⭐⭐⭐⭐",
        "message": "자신감이 넘치고 에너지가 충만한 날입니다. 새로운 도전을 시작하기에 최적입니다."
    },
    "토끼띠": {
        "score": "⭐⭐⭐☆☆",
        "message": "마음의 여유가 필요합니다. 무리한 약속보다는 휴식을 취하며 재충전하세요."
    },
    "용띠": {
        "score": "⭐⭐⭐⭐☆",
        "message": "재물운과 대인관계운이 상승세입니다. 긍정적인 마음가짐이 행운을 부릅니다."
    },
    "뱀띠": {
        "score": "⭐⭐⭐☆☆",
        "message": "사소한 오해가 생길 수 있으니 대화할 때 부드러운 태도를 유지하세요."
    },
    "말띠": {
        "score": "⭐⭐⭐⭐☆",
        "message": "바쁘게 움직일수록 얻는 것이 많습니다. 계획했던 일을 적극적으로 추진해보세요."
    },
    "양띠": {
        "score": "⭐⭐⭐⭐⭐",
        "message": "뜻밖의 행운이나 반가운 소식이 찾아옵니다. 베푼 친절이 복이 되어 돌아옵니다."
    },
    "원숭이띠": {
        "score": "⭐⭐⭐☆☆",
        "message": "집중력이 흐려질 수 있으니 중요한 문서는 두 번 이상 꼼꼼히 확인하세요."
    },
    "닭띠": {
        "score": "⭐⭐⭐⭐☆",
        "message": "직관과 판단력이 예리해지는 날입니다. 중요한 결정을 내리기에 좋습니다."
    },
    "개띠": {
        "score": "⭐⭐⭐☆☆",
        "message": "주변인의 말에 휘둘리지 말고 본인의 소신대로 일을 진행하는 것이 유리합니다."
    },
    "돼지띠": {
        "score": "⭐⭐⭐⭐⭐",
        "message": "원하던 일이 술술 풀리는 순조로운 하루입니다. 기분 좋은 만남이 기대됩니다."
    }
}

# --- 띠 선택 컴포넌트 ---
st.subheader("1. 띠를 선택하세요")
zodiac_list = list(fortune_data.keys())

# 사용자가 띠를 선택할 수 있는 selectbox 제공
selected_zodiac = st.selectbox("자신의 띠를 선택해 주세요:", options=zodiac_list)

# --- 운세 결과 출력 ---
if selected_zodiac:
    st.divider()
    st.subheader(f"✨ [{selected_zodiac}] 오늘의 운세 결과")

    # 해당 띠의 운세 내용 가져오기
    result = fortune_data[selected_zodiac]

    # 컨테이너 상자 형태로 운세 출력
    with st.container(border=True):
        st.markdown(f"**오늘의 운세 지수:** {result['score']}")
        st.info(result['message'])