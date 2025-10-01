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
    ### 🧩 STC Ecosystem
    
    1. [STC Analytics](https://stc-analytics.streamlit.app/)
    2. [STC GasVision](https://stc-gasvision.streamlit.app/)
    3. [STC Converter](https://stc-converter.streamlit.app/)
    4. [STC Bench](https://stc-bench.streamlit.app/)
    5. [STC Insight](https://stc-insight.streamlit.app/)
    6. [STC Plugin](https://smartourism.elpeef.com/)
    7. [STC GasX](https://stc-gasx.streamlit.app/)
    8. [STC CarbonPrint](https://stc-carbonprint.streamlit.app/)
    9. [STC ImpactViz](https://stc-impactviz.streamlit.app/)
    10. [STC IoT Connect](https://stc-connect.streamlit.app/)

    ---  
    ### ⛓ RANTAI Communities

    > 💡 RANTAI Communities adalah ekosistem apps eksperimental berbasis Web3 & AI untuk riset, kolaborasi, dan inovasi. Dibangun di atas 3 core: Dev → Build, Net → Connect, Lab → Grow.
    
    🔧 Dev → “Build the chain”
    1. [Numerical Methods Lab](https://metnumlab.streamlit.app/)
    2. [Computational Analytics Studio](https://komnumlab.streamlit.app/)
    3. [BlockPedia](https://blockpedia.streamlit.app/)
    4. [Learn3](https://learn3.streamlit.app/)
    5. [LearnPy](https://rantai-learnpy.streamlit.app/)
    6. [Cruise](https://rantai-cruise.streamlit.app/)
    7. [IndustriX](https://rantai-industrix.streamlit.app/)
    8. [ChainBoard](https://chainboard.streamlit.app/)

    🌐 Net → “Connect the chain”
    1. [SmartFaith](https://smartfaith.streamlit.app/)
    2. [Nexus](https://rantai-nexus.streamlit.app/)
    3. [Decentralized Supply Chain](https://rantai-trace.streamlit.app/)
    4. [ESG Compliance Manager](https://rantai-sentinel.streamlit.app/)
    5. [Decentralized Storage Optimizer](https://rantai-greenstorage.streamlit.app/)
    6. [Cloud Carbon Footprint Tracker](https://rantai-greencloud.streamlit.app/)
    7. [Cloud.Climate.Chain](https://rantai-3c.streamlit.app/)
    8. [Property Management System](https://rantai-pms.streamlit.app/)
    9. [DataHub](https://rantai-data.streamlit.app/)
    
    🌱 Lab → “Grow the chain”
    1. [BlockBook](https://blockbook.streamlit.app/)
    2. [Data Insights & Visualization Assistant](https://rantai-diva.streamlit.app/)
    3. [Exploratory Data Analysis](https://rantai-exploda.streamlit.app/)
    4. [Business Intelligence](https://rantai-busi.streamlit.app/)
    5. [Predictive Modelling](https://rantai-model-predi.streamlit.app/)
    6. [Ethic & Bias Checker](https://rantai-ethika.streamlit.app/)
    7. [Smart Atlas For Environment](https://rantai-safe.streamlit.app/)
    8. [Blockchain Healthcare Revolution](https://healthchain.streamlit.app/)
    9. [Academic Flow Diagram Generator](https://mermaind.streamlit.app/)
    10. [Decentralized Agriculture](https://agroviz.streamlit.app/)
    
    ---
    #### 🙌 Dukungan & kontributor
    
    - ⭐ **Star / Fork**: [GitHub repo](https://github.com/mrbrightsides/rantai-pms)
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
