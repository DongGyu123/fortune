import i18n
import streamlit as st

from utils.init import init_once


if __name__ == '__main__':
    # Init
    init_once()

    # Show title
    st.title(i18n.t('오늘의 운세'))

    # Show page description
    st.write(i18n.t('이름, 성별, 생년월일, 태어난 시각을 선택하면 오늘의 운세를 알려드립니다!'))

    # Show github link
    st.write(f'* Github: {i18n.t("https://github.com/DongGyu123/20225155.git")}')
