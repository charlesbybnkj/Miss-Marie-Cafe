import streamlit as st
import base64

# ============================================================
# MISS MARIE CAFE
# Streamlit Website
# ============================================================

st.set_page_config(
    page_title="Miss Marie Café | Rosanna",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# IMAGE HELPERS
# ============================================================

def image_url(url):
    return url


HERO_IMAGE = (
    "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085"
    "?auto=format&fit=crop&w=2200&q=90"
)

BREAKFAST_IMAGE = (
    "https://images.unsplash.com/photo-1533089860892-a7c6f0a88666"
    "?auto=format&fit=crop&w=1200&q=85"
)

COFFEE_IMAGE = (
    "https://images.unsplash.com/photo-1498804103079-a6351b050096"
    "?auto=format&fit=crop&w=1200&q=85"
)

CAKE_IMAGE = (
    "https://images.unsplash.com/photo-1578985545062-69928b1d9587"
    "?auto=format&fit=crop&w=1200&q=85"
)

LUNCH_IMAGE = (
    "https://images.unsplash.com/photo-1547592180-85f173990554"
    "?auto=format&fit=crop&w=1200&q=85"
)

INTERIOR_IMAGE = (
    "https://images.unsplash.com/photo-1554118811-1e0d58224f24"
    "?auto=format&fit=crop&w=1600&q=85"
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

html {
    scroll-behavior: smooth;
}

.stApp {
    background: #fbf8f2;
    color: #28231f;
    font-family: 'DM Sans', sans-serif;
}

#MainMenu {
    visibility: hidden;
}

footer {
    visibility: hidden;
}

header {
    background: transparent !important;
}

/* Remove Streamlit padding */
.block-container {
    padding-top: 0 !important;
    padding-bottom: 0 !important;
    max-width: 1400px;
}

/* Main typography */

h1, h2, h3 {
    font-family: 'Playfair Display', serif !important;
    color: #28231f !important;
}

p {
    color: #625a53;
}

/* Navigation */

.navbar {
    width: 100%;
    padding: 22px 4%;
    display: flex;
    justify-content: space-between;
    align-items: center;
    background: rgba(251,248,242,0.96);
    border-bottom: 1px solid #e9e1d7;
    position: relative;
    z-index: 10;
}

.logo {
    font-family: 'Playfair Display', serif;
    font-size: 30px;
    font-weight: 700;
    color: #28231f;
    letter-spacing: -1px;
}

.logo span {
    color: #9b6d4b;
}

.nav-right {
    display: flex;
    gap: 28px;
    align-items: center;
}

.nav-link {
    color: #504941;
    text-decoration: none;
    font-size: 14px;
    font-weight: 600;
}

.nav-link:hover {
    color: #9b6d4b;
}

/* Hero */

.hero {
    min-height: 680px;
    border-radius: 0 0 28px 28px;
    background-image:
        linear-gradient(
            90deg,
            rgba(20,16,13,0.72) 0%,
            rgba(20,16,13,0.45) 45%,
            rgba(20,16,13,0.10) 100%
        ),
        url("HERO_PLACEHOLDER");
    background-size: cover;
    background-position: center;
    display: flex;
    align-items: center;
    padding: 80px 8%;
    margin-bottom: 80px;
}

.hero-content {
    max-width: 650px;
}

.hero-kicker {
    color: #e9cdb4;
    font-size: 14px;
    text-transform: uppercase;
    letter-spacing: 3px;
    font-weight: 700;
    margin-bottom: 18px;
}

.hero h1 {
    color: white !important;
    font-size: clamp(54px, 7vw, 96px);
    line-height: 0.95;
    margin: 0 0 25px 0;
}

.hero-text {
    color: rgba(255,255,255,0.92);
    font-size: 19px;
    line-height: 1.7;
    max-width: 570px;
}

.hero-buttons {
    display: flex;
    gap: 14px;
    margin-top: 32px;
    flex-wrap: wrap;
}

.hero-button {
    display: inline-block;
    padding: 15px 25px;
    border-radius: 999px;
    text-decoration: none;
    font-weight: 700;
    font-size: 14px;
}

.hero-primary {
    background: #ffffff;
    color: #28231f;
}

.hero-secondary {
    border: 1px solid rgba(255,255,255,0.6);
    color: white;
    background: rgba(255,255,255,0.10);
}

/* Sections */

.section {
    padding: 30px 5% 90px 5%;
}

.section-kicker {
    color: #a16e4b;
    font-size: 13px;
    font-weight: 700;
    letter-spacing: 3px;
    text-transform: uppercase;
    margin-bottom: 10px;
}

.section-title {
    font-size: clamp(38px, 5vw, 60px);
    line-height: 1.05;
    margin-top: 0;
}

.section-description {
    max-width: 650px;
    font-size: 17px;
    line-height: 1.8;
}

/* Cards */

.feature-card {
    background: white;
    border-radius: 22px;
    overflow: hidden;
    border: 1px solid #ece4da;
    height: 100%;
    box-shadow: 0 10px 35px rgba(60,45,30,0.06);
}

.feature-image {
    width: 100%;
    height: 280px;
    object-fit: cover;
}

.feature-content {
    padding: 25px;
}

.feature-content h3 {
    font-size: 28px;
    margin-top: 0;
}

/* Menu */

.menu-wrapper {
    background: #f1e9df;
    border-radius: 28px;
    padding: 45px;
    margin: 20px 5% 90px 5%;
}

.menu-category {
    font-family: 'Playfair Display', serif;
    font-size: 32px;
    margin-top: 15px;
    margin-bottom: 20px;
}

.menu-item {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    padding: 18px 0;
    border-bottom: 1px solid #d9cbbd;
}

.menu-item:last-child {
    border-bottom: none;
}

.menu-name {
    font-weight: 700;
    font-size: 16px;
}

.menu-description {
    color: #776c63;
    font-size: 14px;
    margin-top: 5px;
    line-height: 1.5;
}

.menu-price {
    font-weight: 700;
    white-space: nowrap;
}

/* About */

.about-box {
    background: #2e2925;
    border-radius: 28px;
    padding: 70px;
    color: white;
}

.about-box h2 {
    color: white !important;
    font-size: clamp(40px, 5vw, 65px);
}

.about-box p {
    color: #e2d8cf;
    line-height: 1.8;
    font-size: 17px;
}

/* Info */

.info-card {
    background: white;
    border: 1px solid #e8dfd5;
    border-radius: 22px;
    padding: 30px;
    height: 100%;
}

.info-icon {
    font-size: 28px;
    margin-bottom: 15px;
}

.info-card h3 {
    font-size: 25px;
    margin-bottom: 10px;
}

.info-card a {
    color: #986b4d;
    text-decoration: none;
    font-weight: 700;
}

/* Gallery */

.gallery-image {
    width: 100%;
    height: 300px;
    object-fit: cover;
    border-radius: 20px;
}

/* Contact */

.contact-box {
    background: #e7d8c9;
    border-radius: 28px;
    padding: 60px;
}

.contact-box h2 {
    font-size: 50px;
}

/* Buttons */

div.stButton > button {
    border-radius: 999px !important;
    border: none !important;
    background: #302a26 !important;
    color: white !important;
    padding: 12px 28px !important;
    font-weight: 700 !important;
}

div.stButton > button:hover {
    background: #9b6d4b !important;
}

/* Inputs */

.stTextInput input,
.stTextArea textarea,
.stSelectbox div[data-baseweb="select"] > div {
    border-radius: 12px !important;
    border: 1px solid #d9cec2 !important;
    background: white !important;
}

/* Footer */

.footer {
    background: #29231f;
    color: white;
    padding: 60px 7%;
    margin-top: 30px;
}

.footer-logo {
    font-family: 'Playfair Display', serif;
    font-size: 34px;
}

.footer p {
    color: #cfc4bb;
}

.footer a {
    color: #e9cdb4;
    text-decoration: none;
}

/* Mobile */

@media (max-width: 800px) {

    .navbar {
        padding: 18px 5%;
    }

    .nav-right {
        display: none;
    }

    .logo {
        font-size: 25px;
    }

    .hero {
        min-height: 650px;
        padding: 60px 7%;
        border-radius: 0 0 20px 20px;
    }

    .hero h1 {
        font-size: 58px;
    }

    .hero-text {
        font-size: 16px;
    }

    .section {
        padding-left: 6%;
        padding-right: 6%;
    }

    .menu-wrapper {
        margin-left: 4%;
        margin-right: 4%;
        padding: 25px;
    }

    .about-box {
        padding: 35px;
    }

    .contact-box {
        padding: 35px;
    }

    .contact-box h2 {
        font-size: 40px;
    }
}

</style>
""".replace("HERO_PLACEHOLDER", HERO_IMAGE), unsafe_allow_html=True)


# ============================================================
# NAVIGATION
# ============================================================

st.markdown("""
<div class="navbar">
    <div class="logo">Miss <span>Marie</span> Café</div>

    <div class="nav-right">
        <a class="nav-link" href="#about">About</a>
        <a class="nav-link" href="#menu">Menu</a>
        <a class="nav-link" href="#gallery">Gallery</a>
        <a class="nav-link" href="#visit">Visit</a>
        <a class="nav-link" href="#contact">Contact</a>
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# HERO
# ============================================================

st.markdown("""
<div class="hero">
    <div class="hero-content">

        <div class="hero-kicker">
            Rosanna Village · Melbourne
        </div>

        <h1>
            Creative food.<br>
            Good coffee.<br>
            Miss Marie.
        </h1>

        <div class="hero-text">
            Breakfast and lunch favourites, housemade cakes,
            great coffee and a welcoming neighbourhood atmosphere.
        </div>

        <div class="hero-buttons">
            <a class="hero-button hero-primary" href="#menu">
                Explore the menu
            </a>

            <a class="hero-button hero-secondary"
               href="tel:0394572365">
                Call 03 9457 2365
            </a>
        </div>

    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================
# INTRO
# ============================================================

st.markdown("""
<div class="section" id="about">

    <div class="section-kicker">Welcome to Miss Marie</div>

    <h2 class="section-title">
        Your neighbourhood<br>
        café in Rosanna.
    </h2>

    <p class="section-description">
        Creative breakfast & lunch dishes, plus housemade cakes,
        served in trendy, compact surroundings. Whether you're
        grabbing coffee on the way to the station, meeting friends
        for brunch or settling in for lunch, Miss Marie is made
        for easy mornings and relaxed afternoons.
    </p>

</div>
""", unsafe_allow_html=True)


# ============================================================
# FEATURE CARDS
# ============================================================

c1, c2, c3 = st.columns(3, gap="large")

with c1:
    st.markdown(f"""
    <div class="feature-card">
        <img class="feature-image" src="{BREAKFAST_IMAGE}">
        <div class="feature-content">
            <h3>Breakfast</h3>
            <p>
                Creative breakfast dishes made for slow mornings,
                big appetites and everything in between.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown(f"""
    <div class="feature-card">
        <img class="feature-image" src="{LUNCH_IMAGE}">
        <div class="feature-content">
            <h3>Lunch</h3>
            <p>
                Fresh, generous lunch dishes with vegetarian,
                vegan and gluten-free options available.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown(f"""
    <div class="feature-card">
        <img class="feature-image" src="{CAKE_IMAGE}">
        <div class="feature-content">
            <h3>Housemade cakes</h3>
            <p>
                Finish your coffee with something sweet from
                the cake cabinet.
            </p>
        </div>
    </div>
    """, unsafe_allow_html=True)


# ============================================================
# MENU
# ============================================================

st.markdown("""
<div id="menu"></div>

<div class="section" style="padding-bottom:20px;">

    <div class="section-kicker">What's cooking</div>

    <h2 class="section-title">
        A menu worth<br>
        coming back for.
    </h2>

    <p class="section-description">
        A selection inspired by the café's published menu.
        Dishes and prices can change, so please check with
        the café for the latest availability.
    </p>

</div>
""", unsafe_allow_html=True)


menu_items = {
    "Breakfast": [
        ("Just 2 Free Range Eggs", "Poached, scrambled or fried on sourdough / multigrain", "$11.90"),
        ("Sweetcorn Fritters", "Smoked salmon, dill-caper sour cream, beetroot relish and poached egg", "$24.90"),
        ("Big Brekkie", "2 eggs, bacon, tomato, spinach, mushrooms, chorizo, relish and sourdough toast", "$24.90"),
        ("Veg Brekkie", "Summer greens, chilli, seasoned ricotta, poached egg, seeds, charred quinoa loaf and avocado", "$22.90"),
        ("Tofu Scramble", "Vegan — bok choy, asparagus, green beans, Brussels sprouts, chilli and sourdough", "$22.90"),
        ("Strawberries & Cream Pancakes", "A sweet breakfast favourite", "$22.90"),
    ],

    "Lunch": [
        ("Super Salad", "Black quinoa, kale, charred corn, carrot, beetroot hummus, broccoli, nuts, poached egg, lime and chilli", "$17.90"),
        ("Super Salad + Chicken", "Add poached chicken to the super salad", "+$5.00"),
        ("Lunch Specials", "Ask the team about the current special of the week", "Ask us"),
    ],

    "Coffee & Drinks": [
        ("Coffee", "Espresso coffee made to order", "Ask us"),
        ("Fresh Juice", "Selection varies", "Ask us"),
        ("Tea", "A selection of teas", "Ask us"),
        ("Cold Drinks", "Ask the team about today's selection", "Ask us"),
    ],

    "Sweet Things": [
        ("Housemade Cakes", "Daily selection from the cake cabinet", "Ask us"),
        ("Sweet Treats", "Selection changes regularly", "Ask us"),
    ]
}


st.markdown('<div class="menu-wrapper">', unsafe_allow_html=True)

for category, items in menu_items.items():

    st.markdown(
        f'<div class="menu-category">{category}</div>',
        unsafe_allow_html=True
    )

    for name, description, price in items:
        st.markdown(f"""
        <div class="menu-item">
            <div>
                <div class="menu-name">{name}</div>
                <div class="menu-description">{description}</div>
            </div>
            <div class="menu-price">{price}</div>
        </div>
        """, unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# ABOUT SECTION
# ============================================================

st.markdown('<div class="section">', unsafe_allow_html=True)

st.markdown("""
<div class="about-box">

    <div class="section-kicker" style="color:#d6a982;">
        The Miss Marie feeling
    </div>

    <h2>
        Come hungry.<br>
        Leave happy.
    </h2>

    <p>
        Miss Marie is a neighbourhood café in the heart of
        Rosanna Village. The focus is simple — good food,
        quality coffee, housemade treats and a relaxed place
        to catch up with friends and family.
    </p>

    <p>
        With breakfast and lunch available, there is always
        something worth stopping in for.
    </p>

</div>
""", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# GALLERY
# ============================================================

st.markdown("""
<div class="section" id="gallery">

    <div class="section-kicker">Inside Miss Marie</div>

    <h2 class="section-title">
        Come see us.
    </h2>

</div>
""", unsafe_allow_html=True)

g1, g2 = st.columns(2, gap="large")

with g1:
    st.markdown(
        f'<img class="gallery-image" src="{INTERIOR_IMAGE}">',
        unsafe_allow_html=True
    )

with g2:
    st.markdown(
        f'<img class="gallery-image" src="{COFFEE_IMAGE}">',
        unsafe_allow_html=True
    )


# ============================================================
# VISIT INFORMATION
# ============================================================

st.markdown("""
<div class="section" id="visit">

    <div class="section-kicker">Find us</div>

    <h2 class="section-title">
        Come by for breakfast,<br>
        lunch or coffee.
    </h2>

</div>
""", unsafe_allow_html=True)


i1, i2, i3 = st.columns(3, gap="large")

with i1:
    st.markdown("""
    <div class="info-card">

        <div class="info-icon">📍</div>

        <h3>Visit</h3>

        <p>
            45 Beetham Parade<br>
            Rosanna VIC 3084
        </p>

        <a href="https://www.google.com/maps/search/?api=1&query=45+Beetham+Parade+Rosanna+VIC+3084"
           target="_blank">
            Get directions →
        </a>

    </div>
    """, unsafe_allow_html=True)

with i2:
    st.markdown("""
    <div class="info-card">

        <div class="info-icon">☕</div>

        <h3>Opening hours</h3>

        <p>
            Monday – Friday<br>
            7:00am – 2:30pm
        </p>

        <p>
            Saturday – Sunday<br>
            8:00am – 2:30pm
        </p>

    </div>
    """, unsafe_allow_html=True)

with i3:
    st.markdown("""
    <div class="info-card">

        <div class="info-icon">☎️</div>

        <h3>Call us</h3>

        <p>
            Questions about the menu,
            bookings or today's specials?
        </p>

        <a href="tel:0394572365">
            (03) 9457 2365 →
        </a>

    </div>
    """, unsafe_allow_html=True)


# ============================================================
# CONTACT / RESERVATION FORM
# ============================================================

st.markdown("""
<div class="section" id="contact">

    <div class="contact-box">

        <div class="section-kicker">
            Get in touch
        </div>

        <h2>
            Planning a visit?
        </h2>

        <p>
            Send us an enquiry and we'll get back to you.
            For immediate questions, give us a call.
        </p>

    </div>

</div>
""", unsafe_allow_html=True)


with st.form("contact_form"):

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input(
            "Your name",
            placeholder="Jane Smith"
        )

    with col2:
        phone = st.text_input(
            "Phone number",
            placeholder="04xx xxx xxx"
        )

    email = st.text_input(
        "Email address",
        placeholder="you@example.com"
    )

    enquiry_type = st.selectbox(
        "What can we help with?",
        [
            "General enquiry",
            "Table enquiry",
            "Group booking",
            "Catering",
            "Cake enquiry"
        ]
    )

    message = st.text_area(
        "Message",
        placeholder="Tell us what you need..."
    )

    submitted = st.form_submit_button(
        "Send enquiry"
    )

    if submitted:

        if not name or not email or not message:

            st.error(
                "Please enter your name, email and message."
            )

        else:

            st.success(
                "Thanks! Your enquiry has been received. "
                "For urgent enquiries, please call "
                "(03) 9457 2365."
            )


# ============================================================
# CALL TO ACTION
# ============================================================

st.markdown("""
<div class="section">

    <div style="
        text-align:center;
        padding:60px 20px;
    ">

        <div class="section-kicker">
            Rosanna Village
        </div>

        <h2 class="section-title">
            See you at Miss Marie.
        </h2>

        <p class="section-description"
           style="margin-left:auto;margin-right:auto;">
            45 Beetham Parade, Rosanna VIC 3084
        </p>

        <br>

        <a href="tel:0394572365"
           style="
             display:inline-block;
             background:#302a26;
             color:white;
             padding:15px 30px;
             border-radius:999px;
             text-decoration:none;
             font-weight:700;
           ">
            Call the café
        </a>

    </div>

</div>
""", unsafe_allow_html=True)


# ============================================================
# FOOTER
# ============================================================

st.markdown("""
<div class="footer">

    <div class="footer-logo">
        Miss Marie Café
    </div>

    <p>
        Creative breakfast & lunch dishes,
        housemade cakes and good coffee.
    </p>

    <p>
        45 Beetham Parade, Rosanna VIC 3084<br>
        (03) 9457 2365
    </p>

    <p>
        © 2026 Miss Marie Café
    </p>

</div>
""", unsafe_allow_html=True)
