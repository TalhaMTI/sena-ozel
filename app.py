from datetime import datetime, timedelta
import os
import streamlit as st
import streamlit.components.v1 as components

# Sayfa Ayarları
st.set_page_config(
    page_title="Sadece İkimize Özel...", page_icon="❤️", layout="centered"
)

# Tasarım ve Kalp Geçiş Animasyonu İçin CSS/JS
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(135deg, #0f172a 0%, #1e1b4b 50%, #31103f 100%);
        color: #e2e8f0;
    }
    .welcome-container {
        background: rgba(255, 255, 255, 0.05);
        padding: 40px;
        border-radius: 25px;
        border: 1px solid rgba(255, 110, 64, 0.4);
        box-shadow: 0 15px 35px rgba(0,0,0,0.5);
        backdrop-filter: blur(10px);
        text-align: center;
        max-width: 400px;
        margin: 50px auto;
    }
    .heart-icon {
        font-size: 50px;
        color: #ff6e40;
        margin-bottom: 10px;
        animation: pulse 2s infinite;
    }
    @keyframes pulse {
        0% { transform: scale(1); }
        50% { transform: scale(1.1); }
        100% { transform: scale(1); }
    }
    .stTextInput > label {
        color: #ffb74d !important;
        font-weight: 600 !important;
        font-size: 15px !important;
    }
    .stTextInput > div > div > input {
        background-color: rgba(15, 23, 42, 0.9) !important;
        color: #ffffff !important;
        border-radius: 12px !important;
        border: 1.5px solid #ff6e40 !important;
        font-size: 15px !important;
    }
    .stButton>button {
        background: linear-gradient(45deg, #ff6e40, #ff8f00);
        color: white;
        border: none;
        border-radius: 12px;
        padding: 10px 20px;
        font-weight: bold;
        width: 100%;
        box-shadow: 0 4px 12px rgba(255, 110, 64, 0.3);
        transition: 0.3s;
    }
    .stButton>button:hover {
        background: linear-gradient(45deg, #f4511e, #ff6f00);
        box-shadow: 0 6px 16px rgba(255, 110, 64, 0.5);
    }
    h1, h2, h3 {
        color: #ffb74d !important;
        font-family: 'Helvetica Neue', sans-serif;
    }
    .alanya-card {
        background: rgba(255, 255, 255, 0.04);
        padding: 25px;
        border-radius: 20px;
        border-left: 5px solid #ff6e40;
        border-right: 1px solid rgba(255, 255, 255, 0.08);
        border-top: 1px solid rgba(255, 255, 255, 0.08);
        border-bottom: 1px solid rgba(255, 255, 255, 0.08);
        margin-bottom: 20px;
        font-size: 16px;
        line-height: 1.6;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }
    .counter-box {
        text-align: center;
        background: linear-gradient(135deg, rgba(255, 110, 64, 0.1), rgba(255, 75, 43, 0.05));
        border: 1px solid rgba(255, 110, 64, 0.3);
        padding: 20px;
        border-radius: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 25px rgba(255, 110, 64, 0.1);
    }
    .birthday-box-sena {
        text-align: center;
        background: linear-gradient(135deg, rgba(233, 30, 99, 0.1), rgba(156, 39, 176, 0.05));
        border: 1px solid rgba(233, 30, 99, 0.3);
        padding: 20px;
        border-radius: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 25px rgba(233, 30, 99, 0.1);
    }
    .birthday-box-talha {
        text-align: center;
        background: linear-gradient(135deg, rgba(33, 150, 243, 0.1), rgba(0, 188, 212, 0.05));
        border: 1px solid rgba(33, 150, 243, 0.3);
        padding: 20px;
        border-radius: 20px;
        margin-bottom: 20px;
        box-shadow: 0 8px 25px rgba(33, 150, 243, 0.1);
    }
    .welcome-banner {
        background: linear-gradient(90deg, rgba(255,110,64,0.15), rgba(255,183,77,0.15));
        padding: 12px;
        border-radius: 12px;
        border: 1px solid rgba(255,183,77,0.3);
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        color: #ffb74d !important;
        margin-bottom: 20px;
    }
    .spotify-link {
        color: #1ed760 !important;
        text-decoration: none;
        font-weight: bold;
        transition: 0.2s;
    }
    .spotify-link:hover {
        color: #1fdf64 !important;
        text-decoration: underline;
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

# Şarkı Listesi Hafızası
if "sarki_listesi" not in st.session_state:
    st.session_state.sarki_listesi = [
        ("İrem Derici - Aşkımız Olay Olacak", "Tam hayallerimiz gibisin, aşkımız olay olacak! ✨"),
        ("Duman - Senden Daha Güzel", "Senden Daha Güzeli mi Var? 🎸🔥"),
        ("Yalın - Melekler Seni Bana Yazmış", "Kalbimin En Güzel Köşesi 🤍"),
        ("Yalın - Ki Sen", "En Özel Hissiyatlar 🌙"),
    ]

# Giriş Ekranı
if not st.session_state.giris_yapildi:
    st.markdown(
        """
        <div class="welcome-container">
            <div class="heart-icon">❤️</div>
            <h2 style="margin-bottom: 5px;">Sonsuzluğun Başlangıcı ✨</h2>
            <p style="color: #94a3b8; font-size: 14px; margin-bottom: 20px;">Bu dijital dünya sadece ikimiz için kuruldu.</p>
    """,
        unsafe_allow_html=True,
    )

    st.markdown(
        '<p style="color: #ffb74d; font-size: 13px; font-weight: 600;'
        ' margin-bottom: 5px; text-align: center;">🔒 İkimiz için de en özel'
        " gün...</p>",
        unsafe_allow_html=True,
    )

    sifre = st.text_input(
        "", type="password", placeholder="", label_visibility="collapsed"
    )

    st.markdown("</div>", unsafe_allow_html=True,)

    if sifre:
        if sifre == DOGRU_SIFRE:
            st.session_state.giris_yapildi = True
            st.rerun()
        else:
            st.error("Şifre yanlış, ikimiz için özel olan o tarihi dene :)")

# İçerik Ekranı
if st.session_state.giris_yapildi:
    # Karşılama bandı
    st.markdown(
        """
        <div class="welcome-banner">
            ✨ Kapı aralandı... Hoş geldin! 💞
        </div>
    """,
        unsafe_allow_html=True,
    )
    
    # Şifre girildikten sonra tetiklenen TAM KALP ŞEKLİNDE romantik geçiş efekti (Canvas Confetti SVG Kalp Entegrasyonu)
    components.html("""
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
        <script>
            // SVG Kalp Şekli Tanımı
            const scalar = 2;
            const heartShape = confetti.shapeFromPath({
                path: 'M167 72c19,-36 71,-41 97,0c23,37 0,91 -97,143c-97,-52 -120,-106 -97,-143c26,-41 78,-36 97,0z'
            });

            function fireRomanticHearts() {
                let duration = 3.5 * 1000;
                let animationEnd = Date.now() + duration;
                let defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 99999 };

                function randomInRange(min, max) {
                    return Math.random() * (max - min) + min;
                }

                let interval = setInterval(function() {
                    let timeLeft = animationEnd - Date.now();

                    if (timeLeft <= 0) {
                        return clearInterval(interval);
                    }

                    let particleCount = 50 * (timeLeft / duration);
                    
                    // Kalp yağmuru patlamaları
                    confetti(Object.assign({}, defaults, {
                        particleCount,
                        origin: { x: randomInRange(0.1, 0.3), y: Math.random() - 0.2 },
                        shapes: [heartShape],
                        scalar: scalar,
                        colors: ['#ff0000', '#ff69b4', '#ff1493', '#ff4081', '#ff80ab']
                    }));
                    confetti(Object.assign({}, defaults, {
                        particleCount,
                        origin: { x: randomInRange(0.7, 0.9), y: Math.random() - 0.2 },
                        shapes: [heartShape],
                        scalar: scalar,
                        colors: ['#ff0000', '#ff69b4', '#ff1493', '#ff4081', '#ff80ab']
                    }));
                }, 250);
            }

            // Sayfa açıldığı an çalıştır
            fireRomanticHearts();
        </script>
    """, height=0)

    # Türkiye Saati Baz Alınarak Ortak Zaman
    simdi = datetime.utcnow() + timedelta(hours=3)

    # --- 1. BÖLÜM: BİRLİKTE GEÇEN ZAMAN SAYAÇI ---
    st.markdown("---")
    st.header("⏳ 💞 Bizim Zamanımız 💞")

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
        <h3 style="color: #ffb74d; margin: 0; font-size: 18px;">Birlikte Geçen Her Anımız</h3>
        <p style="font-size: 30px; font-weight: bold; color: #ffffff; margin: 10px 0; text-shadow: 0 0 10px rgba(255,110,64,0.4);">{gun} Gün, {saat} Saat, {dakika} Dakika</p>
        <p style="color: #cbd5e1; font-size: 13px; margin: 0;">19 Eylül 2026 Cuma, 15:11'den sonsuza...</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

    # --- DOĞUM GÜNÜ SAYAÇLARI ---
    st.markdown("---")
    st.header("🎂 Heyecanla Beklenen Günler")

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
        <h3 style="color: #ff80ab; margin: 0; font-size: 18px;">🌸 Sena'nın Doğum Gününe Kalan</h3>
        <p style="font-size: 26px; font-weight: bold; color: #ffffff; margin: 10px 0; text-shadow: 0 0 10px rgba(233,30,99,0.4);">{sena_gun} Gün, {sena_saat} Saat, {sena_dakika} Dakika</p>
        <p style="color: #cbd5e1; font-size: 13px; margin: 0;">19 Mayıs 2027 ✨</p>
    </div>
    """,
        unsafe_allow_html=True,
    )

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
        <h3 style="color: #4fc3f7; margin: 0; font-size: 18px;">🎉 Talha'nın Doğum Gününe Kalan</h3>
        <p style="font-size: 26px; font-weight: bold; color: #ffffff; margin: 10px 0; text-shadow: 0 0 10px rgba(33,150,243,0.4);">{talha_gun} Gün, {talha_saat} Saat, {talha_dakika} Dakika</p>
        <p style="color: #cbd5e1; font-size: 13px; margin: 0;">20 Şubat 2027 🚀</p>
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

    # --- 3. BÖLÜM: ALANYA KALESİ VE ANA GÖRSEL ---
    st.markdown("---")
    st.header("🏰 Alanya Kalesi'nden Akdeniz'e Bakış")

    img_path = "alanya.jpg"
    if os.path.exists(img_path):
        st.image(
            img_path,
            caption="Kızılkule'nin gölgesinde Akdeniz mavisi...",
            use_container_width=True,
        )
    else:
        st.warning(
            "⚠️ Lütfen Alanya fotoğrafını proje klasörüne 'alanya.jpg' adıyla"
            " kaydet."
        )

    st.markdown(
        """
    <div class="alanya-card">
    Alanya Kalesi'nin surlarından denize bakarken düşündüm de; bu Akdeniz ne kadar derin ve uçsuz bucaksız olursa olsun, senin gözümde senin bakışının derinliğinin yanında sadece sığ bir su damlası kalır. 
    Şehrin bütün ışıkları sönse, Kızılkule'nin feneri bile sönük kalsa, senin o gülüşün ömrümün her köşesini aydınlatmaya yeter. 
    Bu site; dünyanın gürültüsünden uzakta, dalga seslerinin arasına sakladığımız, sadece ruhunun huzur bulacağı bizim dijital limanımız...
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
            "Alanya Kalesi surlarında gün batımına karşı kahve içip manzarayı"
            " izlemek 🏰"
        ),
        (
            "Kleopatra Plajı'nda dalga sesleri eşliğinde akşam yürüyüşü"
            " yapmak 🌊"
        ),
        ("Dim Çayı'nın serin sularında baş başa huzurlu vakit geçirmek 🌿"),
    ]

    for item in bucket_list:
        st.checkbox(item, value=False)

    # --- 6. BÖLÜM: GELECEĞİN ORTAK ŞARKI LİSTESİ VE EKLEME KUTUSU ---
    st.markdown("---")
    st.header("🎵 Geleceğin Şarkı Listesi & Ortak Nota")
    st.markdown(
        """
    <div class="alanya-card">
    Burası ikimizin müzik arşivimiz. Dilediğiniz zaman buraya yeni bir şarkı ekleyebilir, listemizi birlikte büyütebiliriz! 💖 <br>
    <i>(Şarkıların üstüne tıklayarak doğrudan Spotify uygulamasında açabilirsin!)</i>
    </div>
    """,
        unsafe_allow_html=True,
    )

    for sarki, aciklama in st.session_state.sarki_listesi:
        spotify_app_url = f"spotify:search:{sarki.replace(' ', '%20')}"
        st.markdown(f"🎧 <a href='{spotify_app_url}' class='spotify-link'>{sarki}</a> — *{aciklama}*", unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("✨ Listeye Yeni Bir Şarkı Ekle")
    yeni_sarki = st.text_input("Şarkı Adı ve Sanatçı:", placeholder="", key="yeni_sarki_input")
    yeni_not = st.text_input("Şarkıyla İlgili Küçük Bir Not:", placeholder="", key="yeni_not_input")

    if st.button("Şarkıyı Listeye Ekle 🎶"):
        if yeni_sarki:
            st.session_state.sarki_listesi.append((yeni_sarki, yeni_not if yeni_not else "Bizim Şarkımız"))
            st.success(f"Harika! '{yeni_sarki}' başarıyla listemize eklendi! 🎉")
            
            spotify_app_url = f"spotify:search:{yeni_sarki.replace(' ', '%20')}"
            components.html(f"""
                <script>
                    window.location.href = "{spotify_app_url}";
                </script>
            """, height=0)
            
            st.rerun()
        else:
            st.warning("Lütfen eklemek istediğin şarkı adını boş bırakma.")

    # --- 7. BÖLÜM: ÖZEL NOT ---
    st.markdown("---")
    st.header("✨ Kalbimden Dökülenler")
    st.markdown(
        """
    <div class="alanya-card">
    Hayatta her şeyin bir sıradanlığı varken, seninle her an bambaşka bir hikayeye dönüşüyor. İlk gördüğüm andan beri bende bıraktığın o özel his, zaman geçtikçe çok daha derin ve anlamlı bir yere ulaştı.<br><br>
    Bazen sokaklarda yürüyken, bazen arabada yan yana oturup sessizce yolu izlerken, bazen de sadece gözlerinin içine bakarken fark ediyorum ki; hayatın koşturmacası içinde en huzur bulduğum yer senin yanın. Dışarıdan bakıldığında belki kendi halinde, sert görünen biriyim ama konu sen olunca içimdeki o yumuşak ve korumacı tarafı sadece sen biliyorsun.<br><br>
    İyi ki yollarımız kesişti, iyi ki hayatımdasın.
    </div>
    """,
        unsafe_allow_html=True,
    )

    # --- 8. BÖLÜM: ALANYA ROTALARIMIZ ---
    st.markdown("---")
    st.header("🗺️ Alanya'da Bizim Rotalarımız")

    rota = st.selectbox(
        "Birlikte kaybolmak istediğimiz Alanya noktasını seç:",
        [
            "Seçiniz...",
            "Alanya Kalesi Surları (Gün Batımı)",
            "Kleopatra Plajı Sahil Yürüyüşü",
            "Kızılkule ve Liman Gezisi",
            "Dim Çayı Serinliği",
        ],
    )

    if rota == "Alanya Kalesi Surları (Gün Batımı)":
        st.write(
            "Tarihi surların tepesinde, uçsuz bucaksız Akdeniz manzarasına karşı"
            " saatlerce konuşacağımız o huzur..."
        )
    elif rota == "Kleopatra Plajı Sahil Yürüyüşü":
        st.write(
            "Kumların üstünde ayak izlerimiz kalırken, dalgaların sesine karışan"
            " gülüşmelerimiz..."
        )
    elif rota == "Kızılkule ve Liman Gezisi":
        st.write(
            "Akşam liman ışıkları yanarken el ele yapacağımız o nostaljik yürüyüş..."
        )
    elif rota == "Dim Çayı Serinliği":
        st.write(
            "Yaz sıcağında suyun sesi ve doğanın kalbinde baş başa geçireceğimiz sakin"
            " saatler..."
        )

    # --- 9. SON BÖLÜM ---
    st.markdown("---")
    st.markdown(
        """
    <div style="text-align: center; color: #ffb74d; font-size: 16px; margin-top: 30px; padding: 20px; background: rgba(255,255,255,0.03); border-radius: 15px; border: 1px solid rgba(255,110,64,0.2);">
    <b>İyi ki varsın.</b><br>
    <i>- Senin Tarzınla, Benim Elimden...</i>
    </div>
    """,
        unsafe_allow_html=True,
    )
