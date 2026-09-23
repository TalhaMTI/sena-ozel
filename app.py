from datetime import datetime, timedelta
import os
import streamlit as st
import streamlit.components.v1 as components

# Sayfa Ayarları
st.set_page_config(
    page_title="Sadece İkimize Özel...", page_icon="❤️", layout="centered"
)

# Alanya Gün Batımı ve Gece Mavisi Temalı Ultra Şık CSS (Tüm Etiketler Belirginleştirildi)
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #090d16 0%, #161f37 40%, #2a1b3d 100%);
        color: #f8fafc;
    }
    .welcome-container {
        background: rgba(255, 255, 255, 0.04);
        padding: 45px 30px;
        border-radius: 28px;
        border: 1px solid rgba(255, 110, 64, 0.4);
        box-shadow: 0 20px 40px rgba(0, 0, 0, 0.6);
        backdrop-filter: blur(15px);
        text-align: center;
        max-width: 450px;
        margin: 40px auto;
        animation: fadeIn 0.8s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-15px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .heart-icon {
        font-size: 55px;
        color: #ff6e40;
        margin-bottom: 12px;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); text-shadow: 0 0 10px rgba(255,110,64,0.4); }
        50% { transform: scale(1.12); text-shadow: 0 0 25px rgba(255,110,64,0.8); }
        100% { transform: scale(1); text-shadow: 0 0 10px rgba(255,110,64,0.4); }
    }
    .stTextInput > div > div > input {
        background-color: rgba(15, 23, 42, 0.95) !important;
        color: #ffffff !important;
        border-radius: 14px !important;
        border: 2px solid #ff6e40 !important;
        font-size: 18px;
        padding: 12px;
    }
    /* Tüm input ve select etiketlerini çok daha belirgin yaptık */
    .stTextInput label, .stSelectbox label {
        color: #ffb74d !important;
        font-weight: 600 !important;
        font-size: 16px !important;
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff6e40, #ff9f43);
        color: white;
        border: none;
        border-radius: 14px;
        padding: 12px 24px;
        font-weight: bold;
        font-size: 16px;
        width: 100%;
        box-shadow: 0 4px 15px rgba(255, 110, 64, 0.4);
        transition: 0.3s;
        margin-top: 12px;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #ff5722, #ff8f00);
        box-shadow: 0 6px 20px rgba(255, 110, 64, 0.7);
    }
    h1, h2, h3 {
        color: #ffb74d !important;
        font-family: 'Helvetica Neue', sans-serif;
        letter-spacing: 0.5px;
    }
    .content-container {
        animation: smoothOpen 1s ease-in-out;
    }
    @keyframes smoothOpen {
        from { opacity: 0; transform: scale(0.98); }
        to { opacity: 1; transform: scale(1); }
    }
    .universe-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 25px;
        border-radius: 20px;
        border-left: 6px solid #ff6e40;
        border-right: 1px solid rgba(255, 255, 255, 0.05);
        border-top: 1px solid rgba(255, 255, 255, 0.05);
        border-bottom: 1px solid rgba(255, 255, 255, 0.05);
        margin-bottom: 25px;
        font-size: 16px;
        line-height: 1.7;
        box-shadow: 0 8px 25px rgba(0,0,0,0.2);
    }
    .counter-box {
        text-align: center;
        background: linear-gradient(135deg, rgba(255, 110, 64, 0.12), rgba(255, 75, 43, 0.05));
        border: 2px solid rgba(255, 110, 64, 0.4);
        padding: 25px;
        border-radius: 22px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(255, 110, 64, 0.15);
    }
    .birthday-box-sena {
        text-align: center;
        background: linear-gradient(135deg, rgba(233, 30, 99, 0.12), rgba(156, 39, 176, 0.05));
        border: 2px solid rgba(233, 30, 99, 0.4);
        padding: 25px;
        border-radius: 22px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(233, 30, 99, 0.15);
    }
    .birthday-box-talha {
        text-align: center;
        background: linear-gradient(135deg, rgba(33, 150, 243, 0.12), rgba(0, 188, 212, 0.05));
        border: 2px solid rgba(33, 150, 243, 0.4);
        padding: 25px;
        border-radius: 22px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(33, 150, 243, 0.15);
    }
    .welcome-banner {
        background: linear-gradient(90deg, rgba(255,110,64,0.15), rgba(255,183,77,0.15));
        padding: 15px;
        border-radius: 15px;
        border: 1px solid rgba(255,183,77,0.3);
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        color: #ffb74d;
        margin-bottom: 20px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    </style>
""",
    unsafe_allow_html=True,
)

# Şifren
DOGRU_SIFRE = "19/09/2026"

# Oturum Durumu Kontrolü
if "giris_yapildi" not in st.session_state:
    st.session_state.giris_yapildi = False

# Şarkı Listesi
if "sarki_listesi" not in st.session_state:
    st.session_state.sarki_listesi = [
        (
            "Duman - Senden Daha Güzel",
            "Senden daha güzel kim var ki... 🎸",
            "spotify:search:Duman%20Senden%20Daha%20Güzel",
        ),
        (
            "Yalın - Ki Sen",
            "Ruhumuza dokunan o narince his ✨",
            "spotify:search:Yalın%20Ki%20Sen",
        ),
        (
            "İrem Derici - Kalbimin Tek Sahibine",
            "İkimizin en tatlı anı 💞",
            "spotify:search:İrem%20Derici%20Kalbimin%20Tek%20Sahibine",
        ),
    ]

# Giriş Ekranı
if not st.session_state.giris_yapildi:
    st.markdown(
        """
        <div class="welcome-container">
            <div class="heart-icon">❤️</div>
            <h2 style="margin-bottom: 5px;">Sonsuzluğun Başlangıcı</h2>
            <p style="color: #94a3b8; font-size: 14px; margin-bottom: 20px;">Bu dijital evren sadece ikimiz için kuruldu.</p>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p style="color: #ffb74d; font-size: 13px; font-weight: 500;'
        ' margin-bottom: 5px; text-align: center;">🔒 İkimiz için de en özel'
        " gün...</p>",
        unsafe_allow_html=True,
    )

    sifre = st.text_input(
        "", type="password", placeholder="", label_visibility="collapsed"
    )

    st.markdown("</div>", unsafe_allow_html=True)

    if sifre:
        if sifre == DOGRU_SIFRE:
            st.session_state.giris_yapildi = True
            st.rerun()
        else:
            st.error("Şifre yanlış sevgilim, ikimiz için özel olan o tarihi dene :)")

# İçerik Ekranı
if st.session_state.giris_yapildi:
    st.markdown('<div class="content-container">', unsafe_allow_html=True)

    # Karşılama bandı
    st.markdown(
        """
        <div class="welcome-banner">
            ✨ Sonsuzluk kapısı aralandı... Hoş geldin sevgilim! 💞
        </div>
    """,
        unsafe_allow_html=True,
    )
    st.balloons()

    # Türkiye Saati Baz Alınarak Ortak Zaman
    simdi = datetime.utcnow() + timedelta(hours=3)

    # --- 1. BÖLÜM: BİRLİKTE GEÇEN ZAMAN SAYAÇI ---
    st.markdown("---")
    st.header("⏳ 💞 Sonsuzluğa Adım Atalı 💞")

    baslangic_tarihi = datetime(2026, 9, 19, 15, 11, 0)
    fark = simdi - baslangic_tarihi

    toplam_saniye = int(fark.total_seconds())
    if toplam_saniye < 0:
        toplam_saniye = 0

    gun = toplam_saniye // 86400
    saat = (toplam_saniye % 86400) // 3600
    dakika = (toplam_saniye % 3600) // 60

    st.markdown(
        f"""
    <div class="counter-box">
        <h3 style="color: #ffb74d; margin: 0; font-size: 20px;">Birlikte Geçen Her Anımız</h3>
        <p style="font-size: 32px; font-weight: bold; color: #ffffff; margin: 12px 0; text-shadow: 0 0 10px rgba(255,110,64,0.5);">{gun} Gün, {saat} Saat, {dakika} Dakika</p>
        <p style="color: #ffd54f; font-size: 14px; margin: 0; font-weight: 500;">19 Eylül 2026 Cuma, 15:11'den sonsuza...</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # --- DOĞUM GÜNÜ SAYAÇLARI ---
    st.markdown("---")
    st.header("🎂 Heyecanla Beklenen Günler")

    # Sena'nın Doğum Günü (19 Mayıs 2027)
    sena_dg = datetime(2027, 5, 19, 0, 0, 0)
    fark_sena = sena_dg - simdi
    sena_saniye = int(fark_sena.total_seconds())
    if sena_saniye < 0:
        sena_saniye = 0
    sena_gun = sena_saniye // 86400
    sena_saat = (sena_saniye % 86400) // 3600
    sena_dakika = (sena_saniye % 3600) // 60

    st.markdown(
        f"""
    <div class="birthday-box-sena">
        <h3 style="color: #ff80ab; margin: 0; font-size: 20px;">🌸 Sena'nın Doğum Gününe Kalan</h3>
        <p style="font-size: 28px; font-weight: bold; color: #ffffff; margin: 12px 0; text-shadow: 0 0 10px rgba(233,30,99,0.5);">{sena_gun} Gün, {sena_saat} Saat, {sena_dakika} Dakika</p>
        <p style="color: #ff80ab; font-size: 14px; margin: 0; font-weight: 500;">19 Mayıs 2027 ✨</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # Talha'nın Doğum Günü (20 Şubat 2027)
    talha_dg = datetime(2027, 2, 20, 0, 0, 0)
    fark_talha = talha_dg - simdi
    talha_saniye = int(fark_talha.total_seconds())
    if talha_saniye < 0:
        talha_saniye = 0
    talha_gun = talha_saniye // 86400
    talha_saat = (talha_saniye % 86400) // 3600
    talha_dakika = (talha_saniye % 3600) // 60

    st.markdown(
        f"""
    <div class="birthday-box-talha">
        <h3 style="color: #4fc3f7; margin: 0; font-size: 20px;">🎉 Talha'nın Doğum Gününe Kalan</h3>
        <p style="font-size: 28px; font-weight: bold; color: #ffffff; margin: 12px 0; text-shadow: 0 0 10px rgba(33,150,243,0.5);">{talha_gun} Gün, {talha_saat} Saat, {talha_dakika} Dakika</p>
        <p style="color: #4fc3f7; font-size: 14px; margin: 0; font-weight: 500;">20 Şubat 2027 🚀</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # --- 2. BÖLÜM: MÜZİK ÇALAR ---
    st.markdown("---")
    st.header("🎶 Kıraç - Endamın Yeter")
    st.write("Kulaklığını tak ve müziğin akışına bırak kendini...")

    audio_path = "endaminyeter.mp3"
    if os.path.exists(audio_path):
        st.audio(audio_path, format="audio/mp3", autoplay=True)
    else:
        st.info(
            "🎵 Şarkı çaları aktif etmek için 'endaminyeter.mp3' dosyasını proje"
            " klasörüne ekleyebilirsin."
        )

    # --- 3. BÖLÜM: SONSUZLUK VE ANA GÖRSEL ---
    st.markdown("---")
    st.header("🌌 Sonsuzluğun Ufku")

    img_path = "alanya.jpg"
    if os.path.exists(img_path):
        st.image(
            img_path,
            caption="Yıldızların altında, el ele...",
            use_container_width=True,
        )
    else:
        st.warning(
            "⚠️ Lütfen fotoğrafı proje klasörüne 'alanya.jpg' adıyla kaydet."
        )

    st.markdown(
        """
    <div class="universe-card">
    Zamanın akıp gittiği bu evrende, yıldızların altında düşündüm de; bu evren ne kadar büyük ve uçsuz bucaksız olursa olsun, benim gözümde senin bakışının derinliğinin yanında sadece sığ bir detay kalır.<br>
    Bütün ışıklar sönse, gökyüzündeki bütün takımyıldızları kaybolsa bile, senin o gülüşün ömrümün her köşesini aydınlatmaya yeter.<br>
    Bu site; dünyanın gürültüsünden uzakta, kalplerimizin atışına sakladığımız, sadece ruhunun huzur bulacağı bizim sonsuzluk limanımız...
    </div>
    """,
        unsafe_allow_html=True,
    )

    # --- 4. BÖLÜM: FOTOĞRAF GALERİSİ ---
    st.markdown("---")
    st.header("📸 Anı Albümümüz")
    st.write("Yanyana durduğumuz, güldüğümüz o özel kareler...")

    col1, col2 = st.columns(2)
    with col1:
        if os.path.exists("fotograf1.jpg"):
            st.image("fotograf1.jpg", use_container_width=True)
        else:
            st.info("📷 Klasöre 'fotograf1.jpg' ekle")
    with col2:
        if os.path.exists("fotograf2.jpg"):
            st.image("fotograf2.jpg", use_container_width=True)
        else:
            st.info("📷 Klasöre 'fotograf2.jpg' ekle")

    # --- 5. BÖLÜM: ORTAK YAPILACAKLAR LİSTESİ ---
    st.markdown("---")
    st.header("🎯 Birlikte Yapacaklarımız")
    st.write(
        "Gelecekte hayalini kurduğumuz ve birlikte gerçekleştireceğimiz"
        " anlar..."
    )

    bucket_list = [
        (
            "Karatay Şehir Parkı'nda gölet kenarındaki kamelyalarda oturup baş"
            " başa çay içmek 🌳"
        ),
        (
            "Mevlana Meydanı çevresindeki tarihi sokaklarda ve çarşılarda el ele"
            " yürümek ✨"
        ),
        (
            "Karatay'da yöresel lezzetlerin yapıldığı nezih bir esnaf"
            " lokantasında veya restoranda baş başa yemek yemek 🍽️"
        ),
        (
            "Yüksek bir tepede gün batımına karşı kahve içip manzarayı"
            " izlemek 🏰"
        ),
        ("Sahilde dalga sesleri eşliğinde akşam yürüyüşü yapmak 🌊"),
        ("Doğanın kalbinde baş başa huzurlu vakit geçirmek 🌿"),
    ]

    for item in bucket_list:
        st.checkbox(item, value=False)

    # --- 6. BÖLÜM: GELECEĞİN ORTAK ŞARKI LİSTESİ VE SPOTIFY ENTEGRASYONU ---
    st.markdown("---")
    st.header("🎵 Geleceğin Şarkı Listesi & Ortak Nota")
    st.markdown(
        """
    <div class="universe-card">
    Burası ikimizin müzik arşivimiz. Şarkılara tıklayarak doğrudan Spotify uygulamasını açabilirsin 💖
    </div>
    """,
        unsafe_allow_html=True,
    )

    for sarki, aciklama, spotify_link in st.session_state.sarki_listesi:
        st.markdown(
            f"🎧 <a href='{spotify_link}'"
            " style='color: #ffb74d; text-decoration: none; font-weight: bold;'>"
            f"{sarki}</a> — <em>{aciklama}</em>",
            unsafe_allow_html=True,
        )

    st.markdown("---")
    st.subheader("✨ Listeye Yeni Bir Şarkı Ekle")

    yeni_sarki = st.text_input("Şarkı Adı ve Sanatçı", placeholder="")
    yeni_not = st.text_input("Şarkıyla İlgili Küçük Bir Not", placeholder="")

    if st.button("Şarkıyı Listeye Ekle ve Spotify'da Aç 🎶"):
        if yeni_sarki:
            s_url = f"spotify:search:{yeni_sarki.replace(' ', '%20')}"
            st.session_state.sarki_listesi.append(
                (
                    yeni_sarki,
                    yeni_not if yeni_not else "Bizim Şarkımız",
                    s_url,
                )
            )
            st.success(
                f"Harika! '{yeni_sarki}' başarıyla listemize eklendi ve"
                " Spotify uygulamasında açılıyor! 🎉"
            )

            components.html(
                f"""
                <script>
                    window.location.href = "{s_url}";
                </script>
            """,
                height=0,
            )

            st.rerun()
        else:
            st.warning("Lütfen eklemek istediğin şarkı adını boş bırakma sevgilim.")

    # --- 7. BÖLÜM: ÖZEL NOT ---
    st.markdown("---")
    st.header("✨ Kalbimden Dökülenler")
    st.markdown(
        """
    <div class="universe-card">
    Hayatta her şeyin bir sıradanlığı varken, seninle her an bambaşka bir hikayeye dönüşüyor. İlk gördüğüm andan beri bende bıraktığın o özel his, zaman geçtikçe çok daha derin ve anlamlı bir yere ulaştı.<br><br>
    Bazen sokaklarda yürüyken, bazen yan yana oturup sessizce yolu izlerken, bazen de sadece gözlerinin içine bakarken fark ediyorum ki; hayatın koşturmacası içinde en huzur bulduğum yer senin yanın. Dışarıdan bakıldığında belki kendi halinde, sert görünen biriyim ama konu sen olunca içimdeki o yumuşak ve korumacı tarafı sadece sen biliyorsun.<br><br>
    İyi ki yollarımız kesişti, iyi ki hayatımdasın. Seni çok seviyorum.
    </div>
    """,
        unsafe_allow_html=True,
    )

    # --- 8. BÖLÜM: ORTAK ROTALARIMIZ ---
    st.markdown("---")
    st.header("🗺️ Bizim Rotalarımız")

    rota = st.selectbox(
        "Birlikte kaybolmak istediğimiz noktayı seç",
        [
            "Seçiniz...",
            "Tarihi Surlar ve Gün Batımı",
            "Sonsuzluk Sahil Yürüyüşü",
            "Tarihi Sokaklar ve Liman Gezisi",
            "Doğanın Kalbinde Huzur",
        ],
    )

    if rota == "Tarihi Surlar ve Gün Batımı":
        st.write(
            "Uçsuz bucaksız manzara karşı saatlerce konuşacağımız o huzur..."
        )
    elif rota == "Sonsuzluk Sahil Yürüyüşü":
        st.write(
            "Yürürken dalgaların sesine karışan gülüşmelerimiz..."
        )
    elif rota == "Tarihi Sokaklar ve Liman Gezisi":
        st.write(
            "Işıklar yanarken el ele yapacağımız o nostaljik yürüyüş..."
        )
    elif rota == "Doğanın Kalbinde Huzur":
        st.write(
            "Suyun sesi ve doğanın kalbinde baş başa geçireceğimiz sakin"
            " saatler..."
        )

    # --- 9. SON BÖLÜM ---
    st.markdown("---")
    st.markdown(
        """
    <div style="text-align: center; color: #ffb74d; font-size: 18px; margin-top: 30px; padding: 25px; background: rgba(255,255,255,0.03); border-radius: 16px; border: 1px solid rgba(255,110,64,0.2);">
    <b>İyi ki varsın sevgilim. Seni çok seviyorum.</b><br>
    <i>- Sonsuzluğun Başlangıcından...</i>
    </div>
    """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)
