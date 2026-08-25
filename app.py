import streamlit as st

# ============================================================
# MISS MARIE CAFE
# Clean Streamlit Website
# ============================================================

st.set_page_config(
    page_title="Miss Marie Café | Rosanna",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Playfair+Display:wght@500;600;700&display=swap');

    * {
        box-sizing: border-box;
    }

    html {
        scroll-behavior: smooth;
    }

    .stApp {
        background: #faf7f2;
        color: #29241f;
        font-family: 'DM Sans', sans-serif;
    }

    [data-testid="stHeader"] {
        background: transparent;
    }

    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    .block-container {
        max-width: 1350px;
        padding-top: 0 !important;
        padding-bottom: 0 !important;
    }

    /* -----------------------------------------
       NAVBAR
    ----------------------------------------- */

    .navbar {
        width: 100%;
        padding: 22px 5%;
        display: flex;
        align-items: center;
        justify-content: space-between;
        border-bottom: 1px solid #e7ded3;
        background: #faf7f2;
    }

    .brand {
        font-family: 'Playfair Display', serif;
        font-size: 30px;
        font-weight: 700;
        color: #28231e;
    }

    .brand span {
        color: #a26f4d;
    }

    .nav-links {
        display: flex;
        gap: 28px;
    }

    .nav-links a {
        text-decoration: none;
        color: #514a43;
        font-size: 14px;
        font-weight: 600;
    }

    .nav-links a:hover {
        color: #a26f4d;
    }

    /* -----------------------------------------
       HERO
    ----------------------------------------- */

    .hero {
        min-height: 680px;
        margin-bottom: 90px;
        border-radius: 0 0 30px 30px;

        background:
            linear-gradient(
                90deg,
                rgba(30,24,20,0.78) 0%,
                rgba(30,24,20,0.55) 45%,
                rgba(30,24,20,0.10) 100%
            ),
            url("https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=2200&q=90");

        background-size: cover;
        background-position: center;

        display: flex;
        align-items: center;
        padding: 70px 8%;
    }

    .hero-content {
        max-width: 650px;
    }

    .eyebrow {
        color: #e6c5a9;
        font-size: 13px;
        font-weight: 700;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 20px;
    }

    .hero-title {
        font-family: 'Playfair Display', serif;
        font-size: clamp(55px, 8vw, 100px);
        line-height: 0.94;
        color: white;
        margin: 0 0 25px 0;
        font-weight: 600;
    }

    .hero-description {
        color: rgba(255,255,255,0.93);
        font-size: 18px;
        line-height: 1.7;
        max-width: 570px;
        margin-bottom: 32px;
    }

    .hero-buttons {
        display: flex;
        flex-wrap: wrap;
        gap: 12px;
    }

    .hero-button {
        display: inline-block;
        padding: 15px 25px;
        border-radius: 100px;
        text-decoration: none;
        font-size: 14px;
        font-weight: 700;
    }

    .hero-button-primary {
        background: white;
        color: #29241f;
    }

    .hero-button-secondary {
        color: white;
        border: 1px solid rgba(255,255,255,0.65);
        background: rgba(255,255,255,0.10);
    }

    /* -----------------------------------------
       SECTIONS
    ----------------------------------------- */

    .section {
        padding: 0 5% 90px 5%;
    }

    .section-eyebrow {
        color: #a26f4d;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-size: 13px;
        font-weight: 700;
        margin-bottom: 12px;
    }

    .section-title {
        font-family: 'Playfair Display', serif;
        font-size: clamp(40px, 5vw, 64px);
        line-height: 1.05;
        color: #29241f;
        margin: 0 0 22px 0;
    }

    .section-text {
        max-width: 700px;
        color: #6c625a;
        font-size: 17px;
        line-height: 1.8;
    }

    /* -----------------------------------------
       FEATURE CARDS
    ----------------------------------------- */

    .card {
        background: white;
        border: 1px solid #e9e0d6;
        border-radius: 22px;
        overflow: hidden;
        height: 100%;
        box-shadow: 0 12px 35px rgba(60,45,30,0.06);
    }

    .card-image {
        width: 100%;
        height: 270px;
        object-fit: cover;
        display: block;
    }

    .card-content {
        padding: 25px;
    }

    .card-title {
        font-family: 'Playfair Display', serif;
        font-size: 29px;
        color: #29241f;
        margin-bottom: 10px;
    }

    .card-text {
        color: #70665d;
        font-size: 15px;
        line-height: 1.7;
    }

    /* -----------------------------------------
       MENU
    ----------------------------------------- */

    .menu-box {
        background: #eee4d8;
        border-radius: 28px;
        padding: 45px;
        margin: 0 5% 90px 5%;
    }

    .menu-heading {
        font-family: 'Playfair Display', serif;
        font-size: 34px;
        color: #29241f;
        margin: 35px 0 10px 0;
    }

    .menu-heading:first-child {
        margin-top: 0;
    }

    .menu-item {
        padding: 17px 0;
        border-bottom: 1px solid #d8cabc;
        display: flex;
        justify-content: space-between;
        gap: 25px;
    }

    .menu-item:last-child {
        border-bottom: none;
    }

    .menu-name {
        font-weight: 700;
        font-size: 16px;
        color: #302a25;
    }

    .menu-description {
        margin-top: 5px;
        color: #746a61;
        font-size: 14px;
        line-height: 1.5;
        max-width: 700px;
    }

    .menu-price {
        white-space: nowrap;
        font-weight: 700;
        color: #302a25;
    }

    /* -----------------------------------------
       DARK ABOUT
    ----------------------------------------- */

    .dark-section {
        background: #2d2824;
        border-radius: 30px;
        padding: 65px;
        margin: 0 5% 90px 5%;
    }

    .dark-eyebrow {
        color: #d8a982;
        text-transform: uppercase;
        letter-spacing: 3px;
        font-size: 13px;
        font-weight: 700;
    }

    .dark-title {
        font-family: 'Playfair Display', serif;
        color: white;
        font-size: clamp(42px, 5vw, 68px);
        line-height: 1;
        margin: 15px 0 25px 0;
    }

    .dark-text {
        color: #ded5ce;
        max-width: 700px;
        font-size: 17px;
        line-height: 1.8;
    }

    /* -----------------------------------------
       INFO CARDS
    ----------------------------------------- */

    .info-card {
        background: white;
        border: 1px solid #e9e0d6;
        border-radius: 22px;
        padding: 30px;
        min-height: 240px;
    }

    .info-icon {
        font-size: 28px;
        margin-bottom: 15px;
    }

    .info-title {
        font-family: 'Playfair Display', serif;
        font-size: 27px;
        color: #29241f;
        margin-bottom: 12px;
    }

    .info-text {
        color: #70665d;
        line-height: 1.7;
        font-size: 15px;
    }

    .info-link {
        color: #9b6a48;
        font-weight: 700;
        text-decoration: none;
    }

    /* -----------------------------------------
       CONTACT
    ----------------------------------------- */

    .contact-section {
        background: #e4d3c1;
        border-radius: 30px;
        padding: 55px;
        margin: 0 5% 90px 5%;
    }

    .contact-title {
        font-family: 'Playfair Display', serif;
        font-size: clamp(42px, 5vw, 65px);
        line-height: 1;
        color: #29241f;
        margin-bottom: 18px;
    }

    .contact-text {
        color: #655b52;
        font-size: 17px;
        line-height: 1.7;
        max-width: 650px;
    }

    /* -----------------------------------------
       FOOTER
    ----------------------------------------- */

    .footer {
        background: #29241f;
        margin-top: 30px;
        padding: 60px 7%;
        color: white;
    }

    .footer-brand {
        font-family: 'Playfair Display', serif;
        font-size: 34px;
        margin-bottom: 12px;
    }

    .footer-text {
        color: #cfc5bd;
        line-height: 1.7;
    }

    /* -----------------------------------------
       STREAMLIT BUTTONS
    ----------------------------------------- */

    div.stButton > button {
        border-radius: 100px !important;
        background: #302a25 !important;
        color: white !important;
        border: none !important;
        padding: 12px 25px !important;
        font-weight: 700 !important;
    }

    div.stButton > button:hover {
        background: #9b6a48 !important;
        color: white !important;
    }

    /* -----------------------------------------
       MOBILE
    ----------------------------------------- */

    @media (max-width: 800px) {

        .nav-links {
            display: none;
        }

        .navbar {
            padding: 18px 6%;
        }

        .hero {
            min-height: 650px;
            padding: 60px 7%;
            margin-bottom: 60px;
        }

        .hero-title {
            font-size: 58px;
        }

        .hero-description {
            font-size: 16px;
        }

        .section {
            padding-left: 6%;
            padding-right: 6%;
            padding-bottom: 65px;
        }

        .menu-box {
            margin-left: 4%;
            margin-right: 4%;
            padding: 27px;
            margin-bottom: 65px;
        }

        .dark-section {
            margin-left: 4%;
            margin-right: 4%;
            padding: 35px;
            margin-bottom: 65px;
        }

        .contact-section {
            margin-left: 4%;
            margin-right: 4%;
            padding: 35px;
            margin-bottom: 65px;
        }

        .menu-item {
            gap: 10px;
        }

        .menu-name {
            font-size: 15px;
        }

        .menu-description {
            font-size: 13px;
        }

        .menu-price {
            font-size: 14px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# NAVIGATION
# ============================================================

st.markdown(
    """
    <div class="navbar">
        <div class="brand">
            Miss <span>Marie</span> Café
        </div>

        <div class="nav-links">
            <a href="#about">About</a>
            <a href="#menu">Menu</a>
            <a href="#gallery">Gallery</a>
            <a href="#visit">Visit</a>
            <a href="#contact">Contact</a>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# HERO
# ============================================================

st.markdown(
    """
    <div class="hero">

        <div class="hero-content">

            <div class="eyebrow">
                Rosanna Village · Melbourne
            </div>

            <div class="hero-title">
                Creative food.<br>
                Good coffee.<br>
                Miss Marie.
            </div>

            <div class="hero-description">
                Creative breakfast and lunch dishes, housemade
                cakes and great coffee, served in the heart of
                Rosanna Village.
            </div>

            <div class="hero-buttons">

                <a class="hero-button hero-button-primary"
                   href="#menu">
                    Explore the menu
                </a>

                <a class="hero-button hero-button-secondary"
                   href="tel:0394572365">
                    Call the café
                </a>

            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# ABOUT
# ============================================================

st.markdown('<div id="about"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="section">

        <div class="section-eyebrow">
            Welcome to Miss Marie
        </div>

        <div class="section-title">
            Your neighbourhood<br>
            café in Rosanna.
        </div>

        <div class="section-text">
            Creative breakfast and lunch dishes, plus housemade
            cakes, served in trendy, compact surroundings.
            Whether you're grabbing a quick coffee, meeting
            friends for brunch or settling in for lunch,
            Miss Marie is a place to relax, eat well and enjoy
            the neighbourhood.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# FEATURE CARDS
# ============================================================

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.markdown(
        """
        <div class="card">

            <img
                class="card-image"
                src="https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=1200&q=85"
            >

            <div class="card-content">

                <div class="card-title">
                    Breakfast
                </div>

                <div class="card-text">
                    Creative breakfast favourites,
                    fresh ingredients and dishes
                    made for slow mornings.
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

with col2:
    st.markdown(
        """
        <div class="card">

            <img
                class="card-image"
                src="https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=1200&q=85"
            >

            <div class="card-content">

                <div class="card-title">
                    Lunch
                </div>

                <div class="card-text">
                    Generous lunch dishes with
                    plenty of fresh flavours and
                    options for different tastes.
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

with col3:
    st.markdown(
        """
        <div class="card">

            <img
                class="card-image"
                src="https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=1200&q=85"
            >

            <div class="card-content">

                <div class="card-title">
                    Housemade cakes
                </div>

                <div class="card-text">
                    Finish your visit with something
                    sweet from the cake cabinet.
                    Selection changes regularly.
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# SPACING
# ============================================================

st.markdown("<br><br>", unsafe_allow_html=True)

# ============================================================
# MENU
# ============================================================

st.markdown('<div id="menu"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="section">

        <div class="section-eyebrow">
            The menu
        </div>

        <div class="section-title">
            Something for<br>
            every appetite.
        </div>

        <div class="section-text">
            A selection inspired by the café's published menu.
            Menu items and prices can change, so please check
            with Miss Marie for the latest availability.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)

menu = [
    (
        "Breakfast",
        [
            (
                "Just 2 Free Range Eggs",
                "Poached, scrambled or fried on sourdough or multigrain.",
                "$11.90",
            ),
            (
                "Sweetcorn Fritters",
                "Smoked salmon, dill-caper sour cream, beetroot relish and poached egg.",
                "$24.90",
            ),
            (
                "Big Brekkie",
                "Two eggs, bacon, tomato, spinach, mushrooms, chorizo, relish and sourdough toast.",
                "$24.90",
            ),
            (
                "Veg Brekkie",
                "Summer greens, seasoned ricotta, poached egg, seeds, charred quinoa loaf and avocado.",
                "$22.90",
            ),
            (
                "Tofu Scramble",
                "Vegan tofu scramble with greens, chilli and sourdough.",
                "$22.90",
            ),
            (
                "Strawberries & Cream Pancakes",
                "A sweet breakfast favourite.",
                "$22.90",
            ),
        ],
    ),
    (
        "Lunch",
        [
            (
                "Super Salad",
                "Black quinoa, kale, charred corn, carrot, beetroot hummus, broccoli, nuts, poached egg, lime and chilli.",
                "$17.90",
            ),
            (
                "Super Salad + Chicken",
                "Add poached chicken to the super salad.",
                "+$5.00",
            ),
            (
                "Weekly Special",
                "Ask the team about the current special of the week.",
                "Ask us",
            ),
        ],
    ),
    (
        "Coffee & Drinks",
        [
            (
                "Coffee",
                "Freshly made coffee.",
                "Ask us",
            ),
            (
                "Fresh Juice",
                "Ask the team about today's selection.",
                "Ask us",
            ),
            (
                "Tea",
                "A selection of teas.",
                "Ask us",
            ),
            (
                "Cold Drinks",
                "Ask the team about today's selection.",
                "Ask us",
            ),
        ],
    ),
    (
        "Sweet Things",
        [
            (
                "Housemade Cakes",
                "Daily selection from the cake cabinet.",
                "Ask us",
            ),
            (
                "Sweet Treats",
                "Selection changes regularly.",
                "Ask us",
            ),
        ],
    ),
]

st.markdown('<div class="menu-box">', unsafe_allow_html=True)

for category, items in menu:

    st.markdown(
        f'<div class="menu-heading">{category}</div>',
        unsafe_allow_html=True,
    )

    for name, description, price in items:

        st.markdown(
            f"""
            <div class="menu-item">

                <div>
                    <div class="menu-name">
                        {name}
                    </div>

                    <div class="menu-description">
                        {description}
                    </div>
                </div>

                <div class="menu-price">
                    {price}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# ABOUT / STORY
# ============================================================

st.markdown(
    """
    <div class="dark-section">

        <div class="dark-eyebrow">
            The Miss Marie feeling
        </div>

        <div class="dark-title">
            Come hungry.<br>
            Leave happy.
        </div>

        <div class="dark-text">
            Miss Marie is a neighbourhood café in Rosanna Village
            focused on creative food, quality coffee and a relaxed
            atmosphere.

            <br><br>

            From breakfast classics to weekly specials and
            housemade cakes, there is always a reason to stop in.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# GALLERY
# ============================================================

st.markdown('<div id="gallery"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="section">

        <div class="section-eyebrow">
            The café
        </div>

        <div class="section-title">
            A little look<br>
            inside Miss Marie.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)

g1, g2 = st.columns(2, gap="large")

with g1:
    st.image(
        "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=1600&q=90",
        use_container_width=True,
    )

with g2:
    st.image(
        "https://images.unsplash.com/photo-1498804103079-a6351b050096?auto=format&fit=crop&w=1600&q=90",
        use_container_width=True,
    )

# ============================================================
# VISIT
# ============================================================

st.markdown("<br><br>", unsafe_allow_html=True)

st.markdown('<div id="visit"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="section">

        <div class="section-eyebrow">
            Find us
        </div>

        <div class="section-title">
            Come by for breakfast,<br>
            lunch or coffee.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)

info1, info2, info3 = st.columns(3, gap="large")

with info1:
    st.markdown(
        """
        <div class="info-card">

            <div class="info-icon">📍</div>

            <div class="info-title">
                Visit us
            </div>

            <div class="info-text">
                45 Beetham Parade<br>
                Rosanna VIC 3084
                <br><br>

                <a
                    class="info-link"
                    href="https://www.google.com/maps/search/?api=1&query=45+Beetham+Parade+Rosanna+VIC+3084"
                    target="_blank"
                >
                    Get directions →
                </a>
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

with info2:
    st.markdown(
        """
        <div class="info-card">

            <div class="info-icon">🕐</div>

            <div class="info-title">
                Opening hours
            </div>

            <div class="info-text">
                Monday – Friday<br>
                7:00am – 2:30pm
                <br><br>

                Saturday – Sunday<br>
                8:00am – 2:30pm
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

with info3:
    st.markdown(
        """
        <div class="info-card">

            <div class="info-icon">☎️</div>

            <div class="info-title">
                Call us
            </div>

            <div class="info-text">
                Have a question about the menu,
                bookings or today's specials?
                <br><br>

                <a
                    class="info-link"
                    href="tel:0394572365"
                >
                    (03) 9457 2365 →
                </a>
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# CONTACT
# ============================================================

st.markdown("<br>", unsafe_allow_html=True)

st.markdown('<div id="contact"></div>', unsafe_allow_html=True)

st.markdown(
    """
    <div class="contact-section">

        <div class="section-eyebrow">
            Get in touch
        </div>

        <div class="contact-title">
            Planning a visit?
        </div>

        <div class="contact-text">
            Have a question about the café, menu or a group visit?
            Send us an enquiry below.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)

with st.form("miss_marie_contact"):

    left, right = st.columns(2)

    with left:
        name = st.text_input(
            "Name",
            placeholder="Your name",
        )

    with right:
        phone = st.text_input(
            "Phone",
            placeholder="04xx xxx xxx",
        )

    email = st.text_input(
        "Email",
        placeholder="you@example.com",
    )

    enquiry = st.selectbox(
        "Enquiry type",
        [
            "General enquiry",
            "Table enquiry",
            "Group booking",
            "Catering",
            "Cake enquiry",
        ],
    )

    message = st.text_area(
        "Message",
        placeholder="How can we help?",
    )

    submitted = st.form_submit_button(
        "Send enquiry"
    )

    if submitted:

        if not name or not email or not message:

            st.error(
                "Please fill in your name, email and message."
            )

        else:

            st.success(
                "Thanks for getting in touch with Miss Marie Café!"
            )

# ============================================================
# FINAL CTA
# ============================================================

st.markdown(
    """
    <div class="section">

        <div style="
            text-align:center;
            padding:70px 20px;
        ">

            <div class="section-eyebrow">
                Rosanna Village
            </div>

            <div class="section-title">
                See you at<br>
                Miss Marie.
            </div>

            <div class="section-text"
                 style="margin:0 auto;">
                45 Beetham Parade, Rosanna VIC 3084
            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="footer">

        <div class="footer-brand">
            Miss Marie Café
        </div>

        <div class="footer-text">
            Creative breakfast & lunch dishes,
            housemade cakes and good coffee.
            <br><br>
            45 Beetham Parade, Rosanna VIC 3084
            <br>
            (03) 9457 2365
            <br><br>
            © 2026 Miss Marie Café
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)
