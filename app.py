import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="STC IoT CONNECT",
    page_icon="🌀",
    layout="wide"
)

with st.sidebar:
    st.sidebar.image(
        "https://i.imgur.com/7j5aq4l.png",
        use_container_width=True
    )
    st.sidebar.markdown("📘 **About**")
    st.sidebar.markdown("""
    **STC Connect** adalah middleware API yang menjadi jembatan antara aplikasi, perangkat IoT, dan blockchain dalam ekosistem **SmartTourismChain (STC)**.  
    Didesain agar developer dan researcher dapat dengan mudah mengintegrasikan fitur **on-chain** maupun **off-chain** ke dalam sistem mereka tanpa harus menulis kode blockchain yang kompleks.  
    
    ### 🎯 Tujuan Utama
    - Memudahkan akses ke fungsi blockchain melalui REST API.
    - Menyediakan antarmuka standar untuk aplikasi, device, dan analitik.
    - Membantu proses adopsi SmartTourismChain di berbagai use case (pariwisata, edukasi, IoT, smart city, dll).
    
    ### ⚡ Teknologi
    - **Backend**: Node.js / Python FastAPI (pluggable)  
    - **Database**: PlaytimeDB (mockup & integration ready)  
    - **Blockchain**: Ethereum Sepolia Testnet (default)  
    - **Analytics**: Streamlit + Realtime Dashboard  
    
    ### 🌐 Integrasi
    - **IoT**: Kirim event sensor/log ke blockchain via STC Connect.  
    - **Booking System**: Catat transaksi booking langsung ke chain.  
    - **Analytics**: Dapatkan insight real-time untuk monitoring & dashboard.
    
    ---
    #### 🔮 Vision Statement
    
    **STC Connect** hadir sebagai pintu gerbang untuk mempertemukan **dunia nyata** (aplikasi, device, user) dengan **dunia blockchain**.  
    Visi kami adalah menjadikan STC Connect sebagai **API Hub** yang sederhana namun powerful, yang bisa dipakai siapa saja: akademisi, developer, bahkan industri.  
    
    1. **Simplifikasi** → Membuat blockchain integration semudah memanggil REST API.  
    2. **Kolaborasi** → Menjadi platform terbuka untuk komunitas STC dan RANTAI dalam mengembangkan use case.  
    3. **Skalabilitas** → Mendukung pertumbuhan ekosistem SmartTourismChain dari skala kecil (mockup) hingga implementasi nyata.  
    4. **Transparansi** → Menyediakan akses real-time terhadap data transaksi, log IoT, dan analytics untuk memastikan akuntabilitas.  
    
    ### 🚀 Roadmap
    - **Phase 1** → Core API (Auth, Booking, Transaction, Analytics).  
    - **Phase 2** → IoT Integration (event logger + device gateway).  
    - **Phase 3** → Smart Contract Functions (deploy & call).  
    - **Phase 4** → Open API Hub (developer & partner contributions).  
    
    > *Connecting people, devices, and blockchain — seamlessly.*
   
    ---
    ### 🧩 Apps Showcase
    Lihat disini untuk semua tools yang kami kembangkan:
    [ELPEEF](https://showcase.elpeef.com/)
    
    ---
    #### 🙌 Dukungan & kontributor
    
    - ⭐ **Star / Fork**: [GitHub repo](https://github.com/mrbrightsides/stc-iot-connect)
    - Built with 💙 by [Khudri](https://s.id/khudri)
    - Dukung pengembangan proyek ini melalui: 
      [💖 GitHub Sponsors](https://github.com/sponsors/mrbrightsides) • 
      [☕ Ko-fi](https://ko-fi.com/khudri) • 
      [💵 PayPal](https://www.paypal.com/paypalme/akhmadkhudri) • 
      [🍵 Trakteer](https://trakteer.id/akhmad_khudri)

    Versi UI: v1.0 • Streamlit • Theme Dark
    """)

import streamlit.components.v1 as components

def embed_iframe(src, hide_top_px=100, hide_bottom_px=0, height=800):
    components.html(f"""
    <style>
        @media (max-width: 768px) {{
            .hide-on-mobile {{
                display: none !important;
            }}
            .show-on-mobile {{
                display: block !important;
                padding: 24px 12px;
                background: #ffecec;
                color: #d10000;
                font-weight: bold;
                text-align: center;
                border-radius: 12px;
                font-size: 1.2em;
                margin-top: 24px;
                animation: fadeIn 0.6s ease-in-out;
                box-shadow: 0 4px 12px rgba(0,0,0,0.2);
            }}
        }}
        @media (min-width: 769px) {{
            .show-on-mobile {{
                display: none !important;
            }}
        }}
        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(12px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}
    </style>

    <!-- Desktop view -->
    <div class="hide-on-mobile" style="height:{height}px; overflow:hidden; position:relative;">
        <iframe src="{src}" 
                style="width:100%; height:calc(100% + {hide_top_px + hide_bottom_px}px); 
                       border:none; position:relative; top:-{hide_top_px}px;">
        </iframe>
    </div>

    <!-- Mobile fallback -->
    <div class="show-on-mobile">
        📱 Tampilan ini tidak tersedia di perangkat seluler.<br>
        Silakan buka lewat laptop atau desktop untuk pengalaman penuh 💻
    </div>
    """, height=height + hide_top_px + hide_bottom_px)

iframe_url = "https://stc-connect.elpeef.com/"

embed_iframe(iframe_url, hide_top_px=40, hide_bottom_px = -145, height=800)
