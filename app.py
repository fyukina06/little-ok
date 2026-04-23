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

/* カレンダー */
.calendar-table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 6px;
    table-layout: fixed;
    margin-top: 10px;
}

.calendar-table th {
    text-align: center;
    font-size: 14px;
    color: #333;
    padding: 6px 0;
}

.calendar-table td {
    background: rgba(255,255,255,0.45);
    border-radius: 14px;
    height: 64px;
    text-align: center;
    vertical-align: top;
    font-size: 15px;
    padding-top: 8px;
    word-break: keep-all;
}

.calendar-day {
    display: block;
    font-weight: 600;
}

.calendar-stamp {
    display: block;
    margin-top: 4px;
    font-size: 18px;
}

@media (max-width: 640px) {
    .calendar-table {
        border-spacing: 4px;
    }

    .calendar-table th {
        font-size: 12px;
    }

    .calendar-table td {
        height: 52px;
        font-size: 13px;
        padding-top: 6px;
        border-radius: 10px;
    }

    .calendar-stamp {
        font-size: 15px;
        margin-top: 2px;
    }
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

    col1, col2, col3 = st.columns([1, 2, 1])

    with col1:
        st.button("←", key="prev_month_btn", on_click=prev_month, use_container_width=True)

    with col2:
        st.markdown(
            f"<div class='calendar-header'>{st.session_state.display_year}年 {st.session_state.display_month}月</div>",
            unsafe_allow_html=True
        )

    with col3:
        st.button("→", key="next_month_btn", on_click=next_month, use_container_width=True)

    cal = calendar.monthcalendar(
        st.session_state.display_year,
        st.session_state.display_month
    )
    day_names = ["月", "火", "水", "木", "金", "土", "日"]

    table_html = "<table class='calendar-table'>"
    table_html += "<thead><tr>"

    for day_name in day_names:
        table_html += f"<th>{day_name}</th>"

    table_html += "</tr></thead><tbody>"

    for week in cal:
        table_html += "<tr>"
        for day in week:
            if day == 0:
                table_html += "<td></td>"
            else:
                date_str = datetime.date(
                    st.session_state.display_year,
                    st.session_state.display_month,
                    day
                ).isoformat()

                stamp_html = ""
                if date_str in st.session_state.done_days:
                    stamp_html = "<span class='calendar-stamp'>🌷</span>"

                table_html += f"""
                <td>
                    <span class='calendar-day'>{day}</span>
                    {stamp_html}
                </td>
                """
        table_html += "</tr>"

    table_html += "</tbody></table>"

    st.markdown(table_html, unsafe_allow_html=True)


with tab4:
    st.write("ひとことはこれからつくる")