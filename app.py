import streamlit as st

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

if "done_message" not in st.session_state:
    st.session_state.done_message = ""

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
        else:
            st.warning("先に目標を書いてね")