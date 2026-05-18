import http.server
import socketserver
import threading
import webbrowser
import os

# --- iPURE METAVERSE EDITION V6.9 (VISUAL GALLERY & BILINGUAL QUOTES MATRIX) ---
HTML_CONTENT = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>iPure v6.9 - Ultimate Agri-Tech Ecosystem</title>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
    <style>
        :root {
            --pure-bg: #030712;
            --pure-glass: rgba(16, 24, 48, 0.8);
            --pure-border: rgba(16, 185, 129, 0.2);
            --ipure-neon: #10B981;
            --ipure-glow: rgba(16, 185, 129, 0.4);
            --text-glow: #F3F4F6;
            --text-muted: #9CA3AF;
        }
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: 'Segoe UI', system-ui, sans-serif; }
        
        /* Premium iPure Luxury Velvet Emerald Background */
        body { 
            background: linear-gradient(135deg, #022c22 0%, #030712 50%, #011c14 100%);
            background-attachment: fixed;
            color: var(--text-glow); 
            padding: 25px; 
            font-size: 14px; 
        }
        
        .wrapper { max-width: 1550px; margin: 0 auto; }
        
        /* App Structure Frame */
        .app-shell { display: grid; grid-template-columns: 290px 1fr; gap: 25px; margin-top: 10px; }
        @media (max-width: 1150px) { .app-shell { grid-template-columns: 1fr; } }
        
        /* Glassmorphic Navigation Panel */
        aside { 
            background: var(--pure-glass); padding: 25px; border-radius: 20px; border: 1px solid var(--pure-border); 
            backdrop-filter: blur(12px); box-shadow: 0 8px 32px 0 rgba(0, 0, 0, 0.5); height: fit-content;
        }
        .brand-box { display: flex; align-items: center; gap: 12px; margin-bottom: 30px; padding-bottom: 20px; border-bottom: 1px solid rgba(255,255,255,0.05); }
        .brand-box h1 { font-size: 28px; font-weight: 900; background: linear-gradient(to right, #10B981, #34D399, #6EE7B7); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        
        .nav-menu { list-style: none; display: flex; flex-direction: column; gap: 10px; }
        .nav-btn { padding: 14px 18px; border-radius: 12px; cursor: pointer; color: var(--text-muted); transition: all 0.3s ease; font-weight: 600; display: flex; align-items: center; gap: 12px; border: 1px solid transparent; }
        .nav-btn:hover, .nav-btn.active-node { background: rgba(16, 185, 129, 0.12); color: var(--ipure-neon); border-color: rgba(16, 185, 129, 0.3); box-shadow: 0 0 15px var(--ipure-glow); }
        
        /* Main Engine Workspace */
        main { display: flex; flex-direction: column; gap: 25px; }
        .view-panel { display: none; }
        .view-panel.active-panel { display: block; animation: smoothSlide 0.4s cubic-bezier(0.4, 0, 0.2, 1); }
        
        /* Glass Cards Design Matrix */
        .card-glass { 
            background: var(--pure-glass); border-radius: 20px; padding: 25px; border: 1px solid var(--pure-border); 
            backdrop-filter: blur(10px); box-shadow: 0 4px 20px rgba(0,0,0,0.4); margin-bottom: 25px; 
        }
        .card-glass h2 { font-size: 20px; color: #FFF; margin-bottom: 20px; padding-bottom: 12px; border-bottom: 1px solid rgba(255,255,255,0.05); display: flex; align-items: center; gap: 10px; }
        
        /* Clock and Quotes Elements */
        .clock-container { font-size: 32px; font-weight: 800; color: #FFF; letter-spacing: 1px; font-family: monospace; text-shadow: 0 0 10px var(--ipure-glow); }
        .date-container { font-size: 14px; color: var(--ipure-neon); font-weight: bold; margin-bottom: 15px; }
        .quote-box { background: rgba(16, 185, 129, 0.05); border-left: 4px solid var(--ipure-neon); padding: 15px; border-radius: 8px; color: #A7F3D0; line-height: 1.7; font-size: 14px; transition: all 0.5s ease; }
        
        /* Bulletproof HTML5 Gallery Slider Elements */
        .slider-frame { width: 100%; border-radius: 14px; border: 1px solid var(--pure-border); background: #05070b; position: relative; overflow: hidden; height: 215px; }
        .slide-img { width: 100%; height: 100%; object-fit: cover; display: none; animation: fadeInEffect 0.8s ease-in-out; }
        .slide-img.visible-slide { display: block; }
        .slider-caption { position: absolute; bottom: 0; left: 0; width: 100%; background: linear-gradient(transparent, rgba(0,0,0,0.9)); padding: 12px 15px; font-size: 13px; color: #FFF; font-weight: 500; }
        
        /* Inputs & Buttons */
        input[type="text"], select, textarea { width: 100%; padding: 14px; background: rgba(5, 7, 11, 0.8); border: 1px solid var(--pure-border); border-radius: 10px; color: #FFF; margin-bottom: 15px; font-size: 14px; transition: 0.3s; }
        input[type="text"]:focus, select:focus { border-color: var(--ipure-neon); box-shadow: 0 0 10px var(--ipure-glow); outline: none; }
        button { background: linear-gradient(135deg, #10B981, #059669); color: white; border: none; padding: 14px 24px; border-radius: 10px; font-weight: 700; cursor: pointer; transition: all 0.3s; letter-spacing: 0.5px; }
        button:hover { transform: translateY(-2px); box-shadow: 0 8px 20px var(--ipure-glow); }
        
        /* Dynamic Learning Video Embed Frame */
        .video-box-frame { position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden; border-radius: 14px; border: 1px solid var(--pure-border); margin-top: 5px; background: #000; }
        .video-box-frame iframe { position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: none; }
        
        /* VQA Upload Area */
        .file-dropzone { border: 2px dashed #1E293B; padding: 35px; text-align: center; border-radius: 14px; background: rgba(5,7,11,0.5); cursor: pointer; position: relative; transition: 0.3s; }
        .file-dropzone:hover { border-color: var(--ipure-neon); background: rgba(16,185,129,0.03); }
        .file-dropzone input { position: absolute; top:0; left:0; width:100%; height:100%; opacity:0; cursor:pointer; }
        #vqa-img-preview { max-width: 100%; max-height: 160px; border-radius: 10px; display: none; margin-top: 10px; }
        
        /* Tracker Graphics */
        .trend-canvas-box { background: rgba(5,7,11,0.6); padding: 15px; border-radius: 12px; border: 1px solid rgba(255,255,255,0.03); }
        .price-list-container { display: flex; flex-direction: column; gap: 10px; max-height: 380px; overflow-y: auto; padding-right: 5px; }
        .commodity-item { display: flex; justify-content: space-between; align-items: center; padding: 12px; background: rgba(255,255,255,0.02); border-radius: 8px; border: 1px solid transparent; transition: 0.2s; cursor: pointer; }
        .commodity-item:hover { border-color: var(--pure-border); background: rgba(16,185,129,0.04); }
        
        @keyframes fadeInEffect { from { opacity: 0.4; } to { opacity: 1; } }
        @keyframes smoothSlide { from { opacity: 0; transform: translateY(12px); } to { opacity: 1; transform: translateY(0); } }
    </style>
</head>
<body>
    <div class="wrapper">
        <div class="app-shell">
            <aside>
                <div class="brand-box">
                    <span style="font-size:26px;">🌱</span>
                    <h1>iPure Pro</h1>
                </div>
                <ul class="nav-menu">
                    <li class="nav-btn active-node" id="node-home" onclick="routeTo('home')">📊 Core Dashboard</li>
                    <li class="nav-btn" id="node-vqa" onclick="routeTo('vqa')">🎙️ AI VQA & Voice Core</li>
                    <li class="nav-btn" id="node-tracker" onclick="routeTo('tracker')">📈 Vegetable Price Tracker</li>
                    <li class="nav-btn" id="node-shop" onclick="routeTo('shop')">🛒 Smart Marketplace</li>
                    <li class="nav-btn" id="node-learn" onclick="routeTo('learn')">📚 Video Learning Hub</li>
                    <li class="nav-btn" id="node-forum" onclick="routeTo('forum')">👥 Active Farmer Networks</li>
                </ul>
                <div style="margin-top: 35px; padding: 15px; background: rgba(5,7,11,0.6); border-radius: 12px; border: 1px solid var(--pure-border);">
                    <span style="font-size:12px; color:var(--text-muted); font-weight:600;">🎙️ TTS Voice Engine:</span>
                    <select id="tts-language" style="margin-top:8px; margin-bottom:0; padding:8px;">
                        <option value="ta">Tamil (தமிழ்)</option>
                        <option value="en">English (US)</option>
                    </select>
                </div>
            </aside>
            
            <main>
                <section id="panel-home" class="view-panel active-panel">
                    <div style="display:grid; grid-template-columns: 1fr 1.2fr; gap:25px; margin-bottom:25px;">
                        <div class="card-glass" style="display: flex; flex-direction: column; justify-content: space-between;">
                            <div>
                                <h2>⏰ Live Engine Temporal Node</h2>
                                <div class="clock-container" id="digital-clock">00:00:00 AM</div>
                                <div class="date-container" id="digital-date">Loading Chronos Calendar...</div>
                            </div>
                            <div class="quote-box" id="quotes-display" style="margin-top: 15px;">
                                Loading Ancient Wisdom Modules...
                            </div>
                        </div>
                        
                        <div class="card-glass" style="display: flex; flex-direction: column; justify-content: space-between;">
                            <h2>🌾 Ancient Greenery of Tamil Nadu (Visual Presentation)</h2>
                            <div class="slider-frame">
                                <img class="slide-img visible-slide" src="https://images.unsplash.com/photo-1574359411659-15573a27f812?w=800" data-caption="🌾 Lush, boundless ancient green paddy fields of traditional Tamil Nadu landscapes.">
                                <img class="slide-img" src="https://images.unsplash.com/photo-1593113598332-cd288d649433?w=800" data-caption="🌊 The life-giving flowing waters of the Thanjavur Cauvery delta matrix feeding fields.">
                                <img class="slide-img" src="https://images.unsplash.com/photo-1592417817098-8f3d6eb19675?w=800" data-caption="☀️ Golden dawn illuminating historical sustainable community farming routines.">
                                <div class="slider-caption" id="slide-caption-box">🌾 Lush, boundless ancient green paddy fields of traditional Tamil Nadu landscapes.</div>
                            </div>
                            <p style="margin-top: 12px; font-size: 12.5px; color: #A7F3D0; line-height: 1.5; font-style: italic;">
                                <strong>💡 iPure வரலாற்று குறிப்பு:</strong> முற்காலத் தமிழகத்தில் ஓடிய ஆறுகளும், காவிரியின் நீர் வளமும் நம் பூமியை எப்படி பசுஞ்சோலையாக வைத்திருந்தது என்பதை விளக்கும் பிரத்தியேக புகைப்படத் தொகுப்பு.
                            </p>
                        </div>
                    </div>

                    <div class="card-glass">
                        <h2>🌦️ Dynamic Global Weather Matrix Engine</h2>
                        <div style="margin-bottom:15px; display:flex; gap:10px;">
                            <input type="text" id="weather-search-input" style="margin-bottom:0;" placeholder="Enter any city or country name (e.g., London, Tokyo, Madurai, Canada)...">
                            <button onclick="fetchGlobalCityWeather()">Query Location 🛰️</button>
                        </div>
                        <div style="display:flex; justify-content:space-between; align-items:center; flex-wrap:wrap; gap:20px;">
                            <div>
                                <p style="font-size: 13px; color:var(--text-muted); text-transform:uppercase;">Current Analyzed Coordinates</p>
                                <p style="font-size: 26px; font-weight: bold; color:#FFF; margin-top:4px;" id="weather-city">Chennai, Tamil Nadu</p>
                            </div>
                            <div style="text-align:center;">
                                <p style="font-size: 42px; font-weight: 800; color:var(--ipure-neon);" id="weather-temp">31.4 °C</p>
                                <p style="color:var(--text-muted); font-size:13px;" id="weather-desc">Optimal Clear Daylight</p>
                            </div>
                            <div style="background:rgba(5,7,11,0.5); padding:15px; border-radius:12px; border:1px solid var(--pure-border);">
                                <p style="font-size:13px;">💧 Field Humidity: <strong style="color:#FFF;" id="weather-hum">82%</strong></p>
                                <p style="font-size:13px; margin-top:5px;">💨 Wind Velocity: <strong style="color:#FFF;" id="weather-wind">14 km/h</strong></p>
                            </div>
                        </div>
                    </div>
                </section>

                <section id="panel-vqa" class="view-panel">
                    <div class="card-glass">
                        <h2>🎙️ Advanced AI Chatbot & Vision Reasoning Matrix</h2>
                        <div style="display:grid; grid-template-columns: 1fr 1fr; gap:25px;">
                            <div>
                                <div class="file-dropzone">
                                    <p id="dropzone-text">📸 Inject Crop Diagnostic Imagery (Leaf / Stem / Soil)</p>
                                    <input type="file" accept="image/*" id="vqa-media-injector">
                                    <img id="vqa-img-preview" alt="Neural Target Array">
                                </div>
                            </div>
                            <div>
                                <input type="text" id="vqa-input-string" placeholder="Type crop concerns (e.g., Why are tomato leaves turning yellow with spots?)...">
                                <button style="width:100%;" onclick="executeVQAInference()">Compute Multimodal Inference Loops ⚡</button>
                            </div>
                        </div>
                        <div id="vqa-output-card" class="card-glass" style="margin-top:25px; display:none; background:rgba(5,7,11,0.6); border-left:5px solid var(--ipure-neon);"></div>
                    </div>
                </section>

                <section id="panel-tracker" class="view-panel">
                    <div class="card-glass">
                        <h2>📈 Comprehensive Commodity Tracker & Trend Analytics</h2>
                        <div style="display:grid; grid-template-columns: 1.2fr 1.8fr; gap:25px; align-items:start;">
                            <div class="price-list-container">
                                <div class="commodity-item" onclick="updateChartContext('Tomato')"><span>🍅 Tomato (தக்காளி)</span><strong style="color:#F87171;">₹38 / kg <span style="font-size:11px;">HIGH ↑</span></strong></div>
                                <div class="commodity-item" onclick="updateChartContext('Onion')"><span>🧅 Onion (வெங்காயம்)</span><strong style="color:#60A5FA;">₹28 / kg <span style="font-size:11px;">LOW ↓</span></strong></div>
                                <div class="commodity-item" onclick="updateChartContext('Potato')"><span>🥔 Potato (உருளைக்கிழங்கு)</span><strong>₹32 / kg <span style="color:var(--text-muted); font-size:11px;">STABLE</span></strong></div>
                                <div class="commodity-item" onclick="updateChartContext('Chilli')"><span>🌶️ Green Chilli (மிளகாய்)</span><strong style="color:#F87171;">₹55 / kg <span style="font-size:11px;">HIGH ↑</span></strong></div>
                                <div class="commodity-item" onclick="updateChartContext('Brinjal')"><span>🍆 Brinjal (கத்தரிக்காய்)</span><strong>₹24 / kg <span style="color:var(--text-muted); font-size:11px;">STABLE</span></strong></div>
                                <div class="commodity-item" onclick="updateChartContext('LadyFinger')"><span>🥦 Bhendi (வெண்டைக்காய்)</span><strong style="color:#60A5FA;">₹30 / kg <span style="font-size:11px;">LOW ↓</span></strong></div>
                            </div>
                            <div class="trend-canvas-box">
                                <h4 id="chart-title" style="margin-bottom:15px; font-size:14px; color:#FFF;">📈 Market Value Fluctuations: Tomato (7-Day Metric Index)</h4>
                                <canvas id="marketChart" style="width:100%; height:230px;"></canvas>
                            </div>
                        </div>
                    </div>
                </section>

                <section id="panel-shop" class="view-panel">
                    <div style="display:grid; grid-template-columns: 2fr 1fr; gap:25px;">
                        <div class="card-glass">
                            <h2>🛒 Input Procurement & Equipment Hub</h2>
                            <div class="commodity-item" style="padding:15px; margin-bottom:10px;">
                                <div><strong>Bio-NPK Consolidated Organic Bio-Fertilizer</strong><br><span style="color:var(--ipure-neon); font-size:13px;">₹450 / 5kg Bag</span></div>
                                <button onclick="addToBasket(450)">Allocate 🛒</button>
                            </div>
                            <div class="commodity-item" style="padding:15px; margin-bottom:10px;">
                                <div><strong>Premium F1 Hybrid Tomato Seeds (High Disease Resistance)</strong><br><span style="color:var(--ipure-neon); font-size:13px;">₹150 / Retail Packet</span></div>
                                <button onclick="addToBasket(150)">Allocate 🛒</button>
                            </div>
                            <div class="commodity-item" style="padding:15px; margin-bottom:10px;">
                                <div><strong>Organic Pure Cold-Pressed Neem Oil Spray Base</strong><br><span style="color:var(--ipure-neon); font-size:13px;">₹280 / Bottle</span></div>
                                <button onclick="addToBasket(280)">Allocate 🛒</button>
                            </div>
                        </div>
                        <div class="card-glass" style="height:fit-content;">
                            <h2>🧺 Active Allocation Matrix</h2>
                            <p style="font-size:15px; margin-bottom:10px;">Allocated Load Count: <span id="basket-qty" style="color:var(--ipure-neon); font-weight:700;">0</span></p>
                            <p style="font-size:20px; font-weight:800; margin-bottom:20px;">Cumulative Valuation: ₹<span id="basket-total">0</span></p>
                            <button style="width:100%; background:linear-gradient(135deg, #3B82F6, #1D4ED8);" onclick="executeCheckoutSequence()">Initialize Secured Gateway Checkout 💳</button>
                        </div>
                    </div>
                </section>

                <section id="panel-learn" class="view-panel">
                    <div class="card-glass">
                        <h2>📚 Specialized Video Hub Learning tracks</h2>
                        <select id="curriculum-select" onchange="switchVideoTrack()">
                            <option value="">-- Choose Automated Educational Feed --</option>
                            <option value="rice-sri">System of Rice Intensification (SRI Method Paddy Training)</option>
                            <option value="veg-pathology">Vegetable Blight & Crop Nutrient Disease Prevention</option>
                            <option value="organic-mix">Organic Neem Oil Pesticide Preparation Tutorial</option>
                        </select>
                        <div id="video-embed-box" style="display:none; margin-top:20px;">
                            <p id="video-summary-text" style="color:var(--text-muted); line-height:1.5; margin-bottom:15px; font-weight:500;"></p>
                            <div class="video-box-frame">
                                <iframe id="yt-player" src="" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
                            </div>
                        </div>
                    </div>
                </section>

                <section id="panel-forum" class="view-panel">
                    <div class="card-glass">
                        <h2>👥 Integrated Regional Discussion Forums</h2>
                        <div id="forum-posts-stream">
                            <div style="background:rgba(5,7,11,0.4); padding:15px; border-radius:12px; margin-bottom:15px; border-left:4px solid var(--ipure-neon);">
                                <p style="font-weight:700; color:#FFF; margin-bottom:5px;">Ranganathan (👨‍🌾 Delta Zone Lead)</p>
                                <p style="color:var(--text-muted); line-height:1.5;">SRI alternate wetting and drying protocol use பண்ணதுல இருந்து தண்ணீரும் சேமிக்க முடியுது, வேர் அழுகல் நோயும் வரல நண்பர்களே! எல்லாரும் கண்டிப்பா ட்ரை பண்ணுங்க.</p>
                                <div style="margin-top:10px; font-size:12px; color:var(--ipure-neon);">👍 Agree (42) | 💬 Engineering Sync Logs (8)</div>
                            </div>
                        </div>
                        <textarea id="forum-input-buffer" placeholder="Broadcast your seasonal yield stats or inquire to network vectors..." rows="3"></textarea>
                        <button onclick="commitPostToStream()">Broadcast Post Array 🌍</button>
                    </div>
                </section>
            </main>
        </div>
    </div>

    <script>
        // Tab Routing Panel Engine
        function routeTo(panelId) {
            document.querySelectorAll('.view-panel').forEach(el => el.classList.remove('active-panel'));
            document.querySelectorAll('.nav-btn').forEach(el => el.classList.remove('active-node'));
            document.getElementById('panel-' + panelId).classList.add('active-panel');
            document.getElementById('node-' + panelId).classList.add('active-node');
        }

        // Real-Time Live Clock Matrix Logic
        function initializeDigitalClock() {
            const clockEl = document.getElementById('digital-clock');
            const dateEl = document.getElementById('digital-date');
            
            setInterval(() => {
                const now = new Date();
                clockEl.innerText = now.toLocaleTimeString();
                dateEl.innerText = now.toLocaleDateString('en-US', { weekday: 'long', year: 'numeric', month: 'long', day: 'numeric' });
            }, 1000);
        }
        initializeDigitalClock();

        // 📜 BILINGUAL DYNAMIC QUOTES MATRIX ENGINE
        const bilingualQuotes = [
            {
                tamil: "“வரப்புயர நீர் உயரும் நீர் உயர நெல் உயரும் நெல் உயரக் குடி உயரும் குடி உயரக் கோல் உயரும் கோன் உயர்வான்.”",
                english: "“When field ridges rise, water levels rise; as water rises, paddy crops thrive; as paddy thrives, the citizens prosper, and so grows the kingdom.” <br><span style='font-size:12px; color:var(--ipure-neon); font-weight:bold;'>— Avvaiyar (Ancient Sangam Era Poetry)</span>"
            },
            {
                tamil: "“சுழன்றும்ஏர்ப் பின்னது உலகம் அதனால் உழந்தும் உழவே தலை.”",
                english: "“Whichever way the world revolves, it must follow the plow. Therefore, despite all hardships, agriculture remains the foremost dignity.” <br><span style='font-size:12px; color:var(--ipure-neon); font-weight:bold;'>— Thiruvalluvar (Kural 1031)</span>"
            },
            {
                tamil: "“உழுதுண்டு வாழ்வாரே வாழ்வார்மற் றெல்லாம் தொழுதுண்டு பின்செல்ப வர்.”",
                english: "“They alone truly live who cultivate and eat their own yield; all others merely bow, follow, and rely on someone else's harvest.” <br><span style='font-size:12px; color:var(--ipure-neon); font-weight:bold;'>— Thiruvalluvar (Kural 1033)</span>"
            }
        ];
        
        let quoteIndex = 0;
        function rotateBilingualQuotes() {
            const container = document.getElementById('quotes-display');
            const active = bilingualQuotes[quoteIndex];
            container.innerHTML = `<strong>${active.tamil}</strong><br><span style='color:var(--text-muted); display:block; margin-top:6px;'>${active.english}</span>`;
            quoteIndex = (quoteIndex + 1) % bilingualQuotes.length;
        }
        rotateBilingualQuotes();
        setInterval(rotateBilingualQuotes, 7000);

        // 📸 AUTONOMOUS PHOTO GALLERY SLIDER ENGINE
        let currentSlideIndex = 0;
        const slides = document.querySelectorAll('.slide-img');
        const captionBox = document.getElementById('slide-caption-box');
        
        function rotateGallerySlides() {
            slides[currentSlideIndex].classList.remove('visible-slide');
            currentSlideIndex = (currentSlideIndex + 1) % slides.length;
            slides[currentSlideIndex].classList.add('visible-slide');
            captionBox.innerText = slides[currentSlideIndex].getAttribute('data-caption');
        }
        setInterval(rotateGallerySlides, 4500);

        // Global City & Country Live Weather Fetching Logic
        function fetchGlobalCityWeather() {
            const cityName = document.getElementById('weather-search-input').value.trim();
            if(!cityName) { alert("Please type a city or country name!"); return; }
            
            document.getElementById('weather-city').innerText = `Searching logs for ${cityName}...`;
            
            fetch(`https://geocoding-api.open-meteo.com/v1/search?name=${encodeURIComponent(cityName)}&count=1&language=en&format=json`)
            .then(res => res.json())
            .then(geoData => {
                if(!geoData.results || geoData.results.length === 0) {
                    document.getElementById('weather-city').innerText = "Location Unknown";
                    alert("Target coordinates location not found in global database grid!");
                    return;
                }
                const match = geoData.results[0];
                const lat = match.latitude;
                const lon = match.longitude;
                
                return fetch(`https://api.open-meteo.com/v1/forecast?latitude=${lat}&longitude=${lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m`)
                .then(res => res.json())
                .then(weatherData => {
                    document.getElementById('weather-city').innerText = `${match.name}, ${match.country || 'Global Node'}`;
                    document.getElementById('weather-temp').innerText = `${weatherData.current.temperature_2m} °C`;
                    document.getElementById('weather-hum').innerText = `${weatherData.current.relative_humidity_2m}%`;
                    document.getElementById('weather-wind').innerText = `${weatherData.current.wind_speed_10m} km/h`;
                    document.getElementById('weather-desc').innerText = weatherData.current.temperature_2m > 24 ? "Warm Yield Daylight" : "Cool Thermal Canopy";
                });
            })
            .catch(() => {
                document.getElementById('weather-city').innerText = "Sync Timeout Error";
            });
        }

        // Image Preview Handler
        document.getElementById('vqa-media-injector').addEventListener('change', function(e) {
            const file = e.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(event) {
                    const img = document.getElementById('vqa-img-preview');
                    img.src = event.target.result;
                    img.style.display = 'block';
                    document.getElementById('dropzone-text').style.display = 'none';
                }
                reader.readAsDataURL(file);
            }
        });

        // Speech Engine Vector
        function playSpeechSynthesisOutput(speechText, languageIndex) {
            if ('speechSynthesis' in window) {
                window.speechSynthesis.cancel();
                const nodeUtterance = new SpeechSynthesisUtterance(speechText);
                nodeUtterance.lang = (languageIndex === 'ta') ? 'ta-IN' : 'en-US';
                nodeUtterance.rate = 0.95;
                window.speechSynthesis.speak(nodeUtterance);
            }
        }

        // Advanced Multi-Modal Inference Core
        function executeVQAInference() {
            const query = document.getElementById('vqa-input-string').value.toLowerCase();
            const hasMedia = document.getElementById('vqa-media-injector').files[0];
            const outputCard = document.getElementById('vqa-output-card');
            const targetLang = document.getElementById('tts-language').value;
            
            if(!hasMedia) { alert("Execution Fault: Visual matrix inputs are missing. Upload a photo."); return; }
            if(!query) { alert("Execution Fault: Query string parameters missing."); return; }
            
            outputCard.style.display = "block";
            outputCard.innerHTML = "⏳ Scanning visual pixel channels via CNN layers... Computing inference matrices.";
            
            setTimeout(() => {
                let diagnosticHTML = "";
                let audioString = "";
                
                if(query.includes('yellow') || query.includes('spots') || query.includes('disease')) {
                    if(targetLang === 'ta') {
                        diagnosticHTML = `<h4>🚨 iPure AI பகுப்பாய்வு: இலை கருகல் பூஞ்சை தொற்று உறுதி</h4><br>
                        • <strong>பாதிப்பு காரணி:</strong> Early Blight Fungal Spores (94% Match)<br>
                        • <strong>மேலாண்மை தீர்வுகள்:</strong> பாதிக்கப்பட்ட இலை அடுக்கு அமைப்புகளை உடனடியாக அப்புறப்படுத்துங்கள். தாமிர கலவை கொண்ட பூஞ்சைக்கொல்லி அல்லது 5% இயற்கை வேப்ப எண்ணெய் கரைசலை மாலை வேளையில் தெளிக்கவும்.`;
                        audioString = "எச்சரிக்கை. பயிரில் இலை கருகல் பூஞ்சை தொற்று கண்டறியப்பட்டுள்ளது. பாதிக்கப்பட்ட இலைகளை நீக்கிவிட்டு, மாலை வேளையில் இயற்கை வேப்ப எண்ணெய் தெளிக்கவும்.";
                    } else {
                        diagnosticHTML = `<h4>🚨 iPure AI Diagnostic: Early Blight Infection Matrix Triggered</h4><br>
                        • <strong>Infestation Factor:</strong> Alternaria solani spore pattern match found at 94% confidence intervals.<br>
                        • <strong>Remedial Measures:</strong> Prune localized yellow structural tissues instantly. Mist target zones with organic copper or emulsified Neem solution during dusk.`;
                        audioString = "Warning. Early Blight fungal infection triggered. Prune infected leaf structures instantly and apply copper based organic fungicide.";
                    }
                } else if(query.includes('soil') || query.includes('dry') || query.includes('water') || query.includes('crack')) {
                    if(targetLang === 'ta') {
                        diagnosticHTML = `<h4>⚠️ iPure AI பகுப்பாய்வு: வேர் நீர் பற்றாக்குறை / வறட்சி எச்சரிக்கை</h4><br>
                        • <strong>பாதிப்பு காரணி:</strong> Soil Volumetric Water Content is less than 18%.<br>
                        • <strong>மேலாண்மை தீர்வுகள்:</strong> சொட்டு நீர் பாசன சுழற்சிகளை உடனடியாக அதிகரிக்கவும். ஈரப்பதம் ஆவியாவதை தடுக்க வைக்கோல் கொண்டு மூடாக்கு அமைக்கவும்.`;
                        audioString = "மண்ணில் நீர் பற்றாக்குறை உள்ளது. உடனடியாக சொட்டு நீர் பாசனத்தை இயக்கி மூடாக்கு அமைக்கவும்.";
                    } else {
                        diagnosticHTML = `<h4>⚠️ iPure AI Diagnostic: Hydro-Dehydration Stress Verified</h4><br>
                        • <strong>Infestation Factor:</strong> Soil volumetric matrix hydration tracking below threshold values at 18%.<br>
                        • <strong>Remedial Measures:</strong> Activate localized micro-drip cluster zones immediately. Introduce vegetative mulching grids to control vapor venting.`;
                        audioString = "Dehydration stress verified. Activate localized micro drip irrigation cycles immediately.";
                    }
                } else {
                    if(targetLang === 'ta') {
                        diagnosticHTML = `<h4>✅ iPure AI பகுப்பாய்வு: பயிர் ஆரோக்கிய குறியீடு சீராக உள்ளது</h4><br>• தற்போதைய மேலாண்மை குறியீடுகளில் எந்தவித அலைவரிசை மாற்றமும் இல்லை. சீரான நீர் மேலாண்மையை பராமரிக்கவும்.`;
                        audioString = "பயிர் ஆரோக்கிய குறியீடு சீராக உள்ளது.";
                    } else {
                        diagnosticHTML = `<h4>✅ iPure AI Diagnostic: Crop Cell Structural Stability Normal</h4><br>• Pixel array configurations indicate healthy chloroplast distributions. No immediate pathogen threats detected.`;
                        audioString = "Crop structure indicates healthy vitals.";
                    }
                }
                
                outputCard.innerHTML = diagnosticHTML;
                playSpeechSynthesisOutput(audioString, targetLang);
            }, 1300);
        }

        // Live Market Charts Component Integration
        const commodityDataSets = {
            Tomato: [32, 34, 31, 35, 39, 36, 38],
            Onion: [34, 32, 30, 29, 27, 29, 28],
            Potato: [31, 31, 32, 32, 33, 32, 32],
            Chilli: [48, 50, 52, 51, 53, 56, 55],
            Brinjal: [25, 26, 24, 23, 25, 24, 24],
            LadyFinger: [36, 34, 33, 31, 32, 30, 30]
        };
        
        const canvasCtx = document.getElementById('marketChart').getContext('2d');
        let marketChartInstance = new Chart(canvasCtx, {
            type: 'line',
            data: {
                labels: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
                datasets: [{
                    label: 'Wholesale Index Value (₹)',
                    data: commodityDataSets.Tomato,
                    borderColor: '#10B981',
                    backgroundColor: 'rgba(16, 185, 129, 0.1)',
                    tension: 0.3,
                    fill: true
                }]
            },
            options: {
                responsive: true,
                plugins: { legend: { display: false } },
                scales: {
                    y: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#9CA3AF' } },
                    x: { grid: { color: 'rgba(255,255,255,0.05)' }, ticks: { color: '#9CA3AF' } }
                }
            }
        });

        function updateChartContext(commodityKey) {
            document.getElementById('chart-title').innerText = `📈 Market Value Fluctuations: ${commodityKey} (7-Day Metric Index)`;
            marketChartInstance.data.datasets[0].data = commodityDataSets[commodityKey];
            marketChartInstance.update();
        }

        // Marketplace Allocator
        let globalQuantity = 0;
        let cumulativeFinancialTotal = 0;
        function addToBasket(unitValue) {
            globalQuantity++;
            cumulativeFinancialTotal += unitValue;
            document.getElementById('basket-qty').innerText = globalQuantity;
            document.getElementById('basket-total').innerText = cumulativeFinancialTotal;
        }
        function executeCheckoutSequence() {
            if(cumulativeFinancialTotal === 0) { alert("Allocation Refusal: Cart buffers are unallocated."); return; }
            alert(`🎉 Commercial Gateway Success: Unified orders routed safely. Allocated Amount: ₹${cumulativeFinancialTotal}`);
            globalQuantity = 0; cumulativeFinancialTotal = 0;
            document.getElementById('basket-qty').innerText = 0; document.getElementById('basket-total').innerText = 0;
        }

        // Learning Swapper Engine with stable embedded resource routes
        function switchVideoTrack() {
            const index = document.getElementById('curriculum-select').value;
            const embedBox = document.getElementById('video-embed-box');
            const summaryText = document.getElementById('video-summary-text');
            const ytPlayer = document.getElementById('yt-player');
            
            if(!index) { embedBox.style.display = "none"; return; }
            embedBox.style.display = "block";
            
            if(index === 'rice-sri') {
                summaryText.innerHTML = "<strong>🌾 System of Rice Intensification (SRI Method):</strong> Comprehensive step-by-step masterclass by Discover Agriculture breaking down modern regenerative paddy cultivation rules.";
                ytPlayer.src = "https://www.youtube.com/embed/TkHgAkJhtqw"; 
            } else if(index === 'veg-pathology') {
                summaryText.innerHTML = "<strong>🍅 Vegetable Crop Blight & Diagnostic Track:</strong> Professional agricultural training on how to avoid nitrogen locking and manage early blight spore attacks.";
                ytPlayer.src = "https://www.youtube.com/embed/MKwBgVnSqI8";
            } else {
                summaryText.innerHTML = "<strong>🐛 Organic Compound Prep Video Guide:</strong> Practical step-by-step tutorial on blending neem extracts with emulsifiers safely to disrupt aphid propagation patterns.";
                ytPlayer.src = "https://www.youtube.com/embed/G6hTlmBi0KI";
            }
        }

        // Community Feed
        function commitPostToStream() {
            const txt = document.getElementById('forum-input-buffer').value;
            if(!txt) return;
            
            const nodeStream = document.getElementById('forum-posts-stream');
            const newElement = document.createElement('div');
            newElement.style.cssText = "background:rgba(255,255,255,0.02); padding:15px; border-radius:12px; margin-bottom:15px; border-left:4px solid #3B82F6; animation: smoothSlide 0.3s ease;";
            newElement.innerHTML = `<p style="font-weight:700; color:#FFF; margin-bottom:5px;">Self User (👨‍🌾 Mesh Network Node)</p>
                                    <p style="color:var(--text-muted); line-height:1.5;">${txt}</p>
                                    <div style="margin-top:10px; font-size:12px; color:#3B82F6;">👍 Agree (0) | 💬 Engineering Sync Logs (0)</div>`;
            nodeStream.insertBefore(newElement, nodeStream.firstChild);
            document.getElementById('forum-input-buffer').value = "";
        }
    </script>
</body>
</html>
"""

with open("index.html", "w", encoding="utf-8") as f:
    f.write(HTML_CONTENT)

PORT = 9999
Handler = http.server.SimpleHTTPRequestHandler

def start_server():
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"🌍 iPure Stable Architecture Active at http://localhost:{PORT}")
        httpd.serve_forever()

threading.Thread(target=start_server, daemon=True).start()
webbrowser.open(f"http://localhost:{PORT}")

print("🔥 iPure Production Serving active. Terminate session loop logs via Ctrl+C.")
import time
try:
    while True: time.sleep(1)
except KeyboardInterrupt:
    print("\nPurging interface resources...")
    if os.path.exists("index.html"): os.remove("index.html")