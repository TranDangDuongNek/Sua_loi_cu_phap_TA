import streamlit as st
import streamlit.components.v1 as components

# ===== CONFIG =====
st.set_page_config(page_title="Cat Grammar Checker", layout="wide")

# ===== LOAD CSS =====
def load_css():
    with open("giao_dien/app.css", encoding="utf-8") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# ===== TITLE =====
st.markdown('<div class="title">🐱 Cat Grammar Checker</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Welcome to your fun English fixing website!</div>', unsafe_allow_html=True)

# ===== HOME CARD =====
st.markdown("""
<div class="card">
    <h3>Welcome 👋</h3>
    <p>This is the homepage. Go to Input page to check grammar!</p>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div class="card">
    <h3>🔍 Features</h3>
    <p>
    - Detect grammar mistakes<br>
    - AI-based correction (Google Gemini)<br>
    - Dataset-based error detection<br>
    - Fast and accurate results
    </p>
</div>

<div class="card">
    <h3>📘 How to use</h3>
    <p>
    1. Go to <b>Input page</b><br>
    2. Enter your sentence<br>
    3. Click <b>Check</b><br>
    4. View the result
    </p>
</div>

<div class="card">
    <h3>💡 Example</h3>
    <div style="background:#f4f4f4;padding:10px;border-radius:10px;font-family:monospace;">
        He don't know the answer.
    </div>
</div>

<div class="card">
    <h3>⚙️ Technologies Used</h3>
    <p>
    - Python<br>
    - Streamlit<br>
    - Google Generative AI<br>
    - Pandas
    </p>
</div>
""", unsafe_allow_html=True)

st.markdown('<div class="card" style="text-align:center;">✅ Ready to try? Go to <b>Input page</b>!</div>', unsafe_allow_html=True)


import streamlit as st
import streamlit.components.v1 as components

st.title("Test Cat 🐱")

# ===== CAT MOVING (JS) =====
components.html("""
<html>
<body style="margin:0; overflow:hidden;">

<div id="container"></div>

<script>
const container = document.getElementById("container");

// 🐱 danh sách ảnh (có thể thêm)
const images = [
    "https://i.pinimg.com/originals/2a/97/20/2a972054847bc3f0412083ac13871873.gif",
    "https://i.pinimg.com/736x/d0/b0/ad/d0b0ad9455df702aa7dab8ab12b41a72.jpg"
];

// tạo vật rơi
function spawnItem() {
    const item = document.createElement("img");

    item.src = images[Math.floor(Math.random() * images.length)];

    item.style.position = "fixed";
    item.style.top = "-120px"; // bắt đầu ngoài màn hình
    item.style.left = Math.random() * (window.innerWidth - 100) + "px";
    item.style.width = "100px";
    item.style.zIndex = "9999";
    item.style.cursor = "pointer";

    container.appendChild(item);

    let y = -120;
    let rotation = 0;
    let speed = 1.5 + Math.random() * 2;

    function fall() {
        y += speed;
        rotation += 3;

        item.style.top = y + "px";
        item.style.transform = "rotate(" + rotation + "deg)";

        if (y < window.innerHeight) {
            requestAnimationFrame(fall);
        } else {
            item.remove();
        }
    }

    fall();

    // 💥 CLICK NỔ
    item.onclick = () => {
        item.style.transition = "0.2s";
        item.style.transform = "scale(2) rotate(360deg)";
        item.style.opacity = "0";
        setTimeout(() => item.remove(), 200);
    };
}

// ⏱️ spawn liên tục
setInterval(() => {
    const count = Math.floor(Math.random() * 3) + 1; // 1-3 con
    for (let i = 0; i < count; i++) {
        spawnItem();
    }
}, 2000);

</script>
</body>
</html>
""", height=500)