from config import TEAM_MEMBERS, EMOJI
import streamlit as st

def team_members():
    st.markdown(f"<h1 style='text-align:center;'>Meet our dedicated team members</h1>", unsafe_allow_html=True)
    st.markdown("<br><br>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(
            f"""
            <a href={TEAM_MEMBERS[0]['links'][0]} target="_blank">
                <div class='team-member'>
                    <h3>{TEAM_MEMBERS[0]['name']}</h3>
                    <p>{TEAM_MEMBERS[0]['role']}</p>
                </div>
            </a>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown(
            f"""
            <a href={TEAM_MEMBERS[1]['links'][0]} target="_blank">
                <div class='team-member'>
                    <h3>{TEAM_MEMBERS[1]['name']}</h3>
                    <p>{TEAM_MEMBERS[1]['role']}</p>
                </div>
            </a>
            """,
            unsafe_allow_html=True
        )

    with col3:
        st.markdown(
            f"""
            <a href={TEAM_MEMBERS[2]['links'][0]} target="_blank">
                <div class='team-member'>
                    <h3>{TEAM_MEMBERS[2]['name']}</h3>
                    <p>{TEAM_MEMBERS[2]['role']}</p>
                </div>
            </a>
            """,
            unsafe_allow_html=True
        )

    st.markdown("<br><div style='text-align:center;'>", unsafe_allow_html=True)
    
    # st.markdown("</div>", unsafe_allow_html=True)
