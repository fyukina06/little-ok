import streamlit as st
import datetime
import calendar

st.set_page_config(page_title="little ok", page_icon="🌷", layout="centered")

st.markdown("""
<style>
.stApp {
    background: linear-gradient(to bottom, #87CEEB, #EAF8FF);
}

.block-container {
    padding-top: 3rem;
    max-width: 800px;
}

div[data-testid="stTextInput"] input {
    border-radius: 16px;
    border: none;
    padding: 14px 16px;
    font-size: 18px;
    background-color: white;
}

div.stButton > button {
    border-radius: 999px;
    padding: 0.7rem 1.4rem;
    border: none;
    font-weight: 600;
    font-size: 16px;
    background: white;
}

/* カレンダー用 */
.calendar-header {
    text-align: center;
    font-size: 24px;
    font-weight: bold;
    margin: 10px 0 20px 0;
}

.day-name {
    text-align: center;
    font-weight: bold;
    color: #444;
    margin-bottom: 8px;
}

.calendar-cell {
    background: rgba(255,255,255,0.45);
    border-radius: 16px;
    min-height: 70px;
    padding: 8px 4px;
    text-align: center;
    margin-bottom: 8px;
    font-size: 16px;
}

.stamp {
    font-size: 20px;
    display: block;
    margin-top: 4px;
}
</style>
""", unsafe_allow_html=True)

st.title("little ok")
st.write("今日はひとつだけでいい")

tab1, tab2, tab3, tab4 = st.tabs([
    "今日のlittle ok",
    "気分ログ",
    "できた記録",
    "ひとこと"
])

# セッション状態の初期化
if "done_message" not in st.session_state:
    st.session_state.done_message = ""

if "done_days" not in st.session_state:
    st.session_state.done_days = []

today = datetime.date.today()

if "display_year" not in st.session_state:
    st.session_state.display_year = today.year

if "display_month" not in st.session_state:
    st.session_state.display_month = today.month


# 月移動の関数
def prev_month():
    if st.session_state.display_month == 1:
        st.session_state.display_month = 12
        st.session_state.display_year -= 1
    else:
        st.session_state.display_month -= 1


def next_month():
    if st.session_state.display_month == 12:
        st.session_state.display_month = 1
        st.session_state.display_year += 1
    else:
        st.session_state.display_month += 1


with tab1:
    st.markdown("""<h3 style='text-align: center; font-size:20px;'>
        今日のリトルOKを1つ決めよう
        </h3> 
        """, unsafe_allow_html=True)

    task = st.text_input(
        "",
        placeholder="例：外の空気を吸う",
        key="task_input",
        label_visibility="collapsed"
    )

    col1, col2 = st.columns(2)

    with col1:
        decide = st.button("決めた 🌷", use_container_width=True)

    with col2:
        done = st.button("できた！✨", use_container_width=True)

    if decide:
        if task.strip():
            st.info(f"今日のlittle ok は『{task}』だね")
        else:
            st.warning("先に目標を書いてね")

    if done:
        if task.strip():
            st.balloons()
            st.success(f"おめでとう！『{task}』えらい 🎉")
            st.markdown("## 🌸 little ok 達成！ 🌸")

            # 今日の日付を記録
            if today.isoformat() not in st.session_state.done_days:
                st.session_state.done_days.append(today.isoformat())
        else:
            st.warning("先に目標を書いてね")


with tab2:
    st.write("気分ログはこれからつくる")


with tab3:
    st.markdown("<h3 style='text-align: center;'>できた記録 🌷</h3>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns([1, 3, 1])

    with col1:
        st.button("←", on_click=prev_month, use_container_width=True)

    with col2:
        st.markdown(
            f"<div class='calendar-header'>{st.session_state.display_year}年 {st.session_state.display_month}月</div>",
            unsafe_allow_html=True
        )

    with col3:
        st.button("→", on_click=next_month, use_container_width=True)

    # 曜日表示
    day_names = ["月", "火", "水", "木", "金", "土", "日"]
    cols = st.columns(7)
    for i, day_name in enumerate(day_names):
        cols[i].markdown(f"<div class='day-name'>{day_name}</div>", unsafe_allow_html=True)

    # 月カレンダー作成
    cal = calendar.monthcalendar(st.session_state.display_year, st.session_state.display_month)

    for week in cal:
        cols = st.columns(7)
        for i, day in enumerate(week):
            if day == 0:
                cols[i].markdown("<div class='calendar-cell'></div>", unsafe_allow_html=True)
            else:
                date_str = datetime.date(
                    st.session_state.display_year,
                    st.session_state.display_month,
                    day
                ).isoformat()

                if date_str in st.session_state.done_days:
                    cols[i].markdown(
                        f"<div class='calendar-cell'>{day}<span class='stamp'>🌷</span></div>",
                        unsafe_allow_html=True
                    )
                else:
                    cols[i].markdown(
                        f"<div class='calendar-cell'>{day}</div>",
                        unsafe_allow_html=True
                    )


with tab4:
    st.write("ひとことはこれからつくる")