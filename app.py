import streamlit as st

# Sayfaya tarayıcının manifest olarak algılayacağı meta etiketi ekleyelim
st.markdown(
    """
    <head>
        <link rel="manifest" href="data:application/manifest+json;charset=utf-8,{
            'name': 'Sena\'ya Özel',
            'short_name': 'Sena',
            'start_url': './',
            'display': 'standalone',
            'background_color': '#0e1117',
            'theme_color': '#0e1117',
            'icons': []
        }">
    </head>
""",
    unsafe_allow_html=True,
)

import streamlit as st
import os
from datetime import datetime
@@ -268,4 +288,4 @@
   </div>
   """, unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
