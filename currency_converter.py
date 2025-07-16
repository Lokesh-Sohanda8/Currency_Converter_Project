import streamlit as st
import requests

# -------------------------
# 🌐 Set page config
# -------------------------
st.set_page_config(page_title="💱 Currency Converter", layout="centered")

# -------------------------
# 🎨 Custom Styles
# -------------------------
st.markdown("""
    <style>
        .main {
            background-color: #f2f2f2;
        }
        h1 {
            color: #2c3e50;
            text-align: center;
        }
        .stButton>button {
            background-color: #3498db;
            color: white;
            font-weight: bold;
            padding: 8px 20px;
            border-radius: 8px;
        }
        .stSelectbox, .stNumberInput {
            border-radius: 5px;
        }
    </style>
""", unsafe_allow_html=True)

# -------------------------
# 🧭 Title & Info
# -------------------------
st.title("💱 Currency Converter App")
st.markdown("Convert **any currency** to another in real-time using **live exchange rates** 🌍")

st.markdown("---")

# -------------------------
# 💸 Input
# -------------------------
currency_emojis = {
    "USD": "🇺🇸 USD",
    "INR": "🇮🇳 INR",
    "EUR": "🇪🇺 EUR",
    "GBP": "🇬🇧 GBP",
    "JPY": "🇯🇵 JPY",
    "AUD": "🇦🇺 AUD",
    "CAD": "🇨🇦 CAD"
}

amount = st.number_input("💰 Enter the amount", min_value=0.0, value=1.0, step=0.5)
from_curr = st.selectbox("🔻 From Currency", list(currency_emojis.keys()), format_func=lambda x: currency_emojis[x])
to_curr = st.selectbox("🔺 To Currency", list(currency_emojis.keys()), format_func=lambda x: currency_emojis[x])

st.markdown("---")

# -------------------------
# 🔄 Fetch & Convert
# -------------------------
def fetch_conversion_rate(from_curr, to_curr, amount):
    api_key = "613f7f8865772d43faecc643"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{from_curr}/{to_curr}/{amount}"

    response = requests.get(url)
    data = response.json()

    if response.status_code == 200 and data.get("conversion_result"):
        return round(data["conversion_result"], 2)
    else:
        st.error("❌ Failed to fetch conversion rate. Please check your API key or internet.")
        return None

# -------------------------
# 🎯 Conversion Button
# -------------------------
if st.button("🔁 Convert Now"):
    if from_curr == to_curr:
        st.warning("⚠️ Please select different currencies.")
    else:
        converted = fetch_conversion_rate(from_curr, to_curr, amount)
        if converted is not None:
            st.markdown(f"""
                ### ✅ Conversion Result:
                **{currency_emojis[from_curr]} {amount}** = **{currency_emojis[to_curr]} {converted}**
            """)
