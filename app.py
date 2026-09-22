from datetime import datetime
import streamlit as st

# Sayfa yapılandırması
st.set_page_config(page_title="Sena'ya Özel", page_icon="❤️", layout="centered")

# Manifest ve PWA entegrasyonu için HTML head meta etiketi
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

# --- GİRİŞ YAPILDIKTAN SONRAKİ ANA SAYFA ---
st.title("Sena'ya Özel ❤️")

# Hedef tarih ve bugünün tarihi (Bugün: 22 Eylül 2026)
hedef_tarih = datetime(2026, 9, 19)
simdi = datetime.now()

# Sayaç düzeltmesi: Geçen süreyi doğru hesaplamak için (Şimdiki zaman - Hedef tarih)
fark = simdi - hedef_tarih
gun = fark.days

st.subheader("Birlikte Geçecek / Geçen Zaman")
st.metric(label="Geçen Gün Sayısı", value=f"{gun} gün")

st.write(
    "İyi ki varsın, bu özel alan tamamen senin için tasarlandı ve hazırlandı."
)
