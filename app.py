from datetime import datetime
import os
import streamlit as st

# Sayfa yapılandırması
st.set_page_config(
    page_title="Sena'ya Özel", page_icon="❤️", layout="centered"
)

# Manifest ve PWA entegrasyonu
st.markdown(
    """
    <head>
        <link rel="manifest" href="data:application/manifest+json;charset=utf-8,{
            'name': 'Sena\\'ya Özel',
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

# Şifre koruması (Doğru şifre: 19/09/2026)
OG_SIFRE = "19/09/2026"

if "giris_yapildi" not in st.session_state:
  st.session_state.giris_yapildi = False

if not st.session_state.giris_yapildi:
  st.title("Özel Alan 🔒")
  sifre_input = st.text_input("Lütfen şifreyi girin:", type="password")
  if st.button("Giriş Yap"):
    if sifre_input == OG_SIFRE:
      st.session_state.giris_yapildi = True
      st.rerun()
    else:
      st.error("Hatalı şifre!")
  st.stop()

# --- GİRİŞ YAPILDIKTAN SONRAKİ ANA SAYFA VE İÇERİKLER ---
st.title("Sena'ya Özel ❤️")

# Sayaç hesaplaması (Bugünden hedefe veya hedeften bugüne doğru artış)
hedef_tarih = datetime(2026, 9, 19)
simdi = datetime.now()
fark = simdi - hedef_tarih
gun = fark.days

st.subheader("Birlikte Geçen Zaman")
st.metric(label="Geçen Gün Sayısı", value=f"{gun} gün")

# Orijinal tasarım bileşenlerin ve kapanış etiketleri
st.markdown(
    """
    <div style="text-align: center;">
        <p>İyi ki varsın...</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown("</div>", unsafe_allow_html=True)
st.markdown("</div>", unsafe_allow_html=True)
