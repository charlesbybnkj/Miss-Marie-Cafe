import streamlit as st

# ============================================================
# MISS MARIE CAFE
# ============================================================

st.set_page_config(
    page_title="Miss Marie Café | Rosanna",
    page_icon="☕",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ============================================================
# COLORS / STYLE
# ============================================================

st.markdown("""
<style>
    .stApp {
        background-color: #faf7f2;
    }

    .block-container {
        max-width: 1200px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }

    h1, h2, h3 {
        color: #2b2520 !important;
        font-family: Georgia, serif;
    }

    p {
        color: #625a52;
    }

    .hero-text {
        font-size: 1.15rem;
        line-height: 1.7;
        color: #625a52;
    }

    .small-label {
        color: #a16f4d;
        font-weight: 700;
        letter-spacing: 3px;
        font-size: 0.8rem;
        text-transform: uppercase;
    }

    .price {
        font-weight: 700;
        color: #8d6042;
    }

    .menu-description {
        color: #716860;
        font-size: 0.9rem;
    }

    .info-box {
        background-color: white;
        padding: 1.5rem;
        border-radius: 15px;
        border: 1px solid #e6ddd3;
        min-height: 190px;
    }

    .dark-box {
        background-color: #2c2723;
        padding: 3rem;
        border-radius: 20px;
        color: white;
    }

    .dark-box h2 {
        color: white !important;
    }

    .dark-box p {
        color: #ddd4cc;
    }

    div.stButton > button {
        border-radius: 30px;
        font-weight: 600;
    }

    [data-testid="stSidebar"] {
        display: none;
    }
</style>
""", unsafe_allow_html=True)


# ============================================================
# TOP NAV
# ============================================================

top_left, top_middle, top_right = st.columns([2, 4, 2])

with top_left:
    st.markdown("## Miss Marie")

with top_middle:
    st.markdown(
        "<div style='text-align:center; padding-top:12px;'>"
        "Rosanna Village · Melbourne"
        "</div>",
        unsafe_allow_html=True
    )

with top_right:
    st.markdown(
        "<div style='text-align:right; padding-top:12px;'>"
        "☕ Breakfast · Lunch · Cakes"
        "</div>",
        unsafe_allow_html=True
    )

st.divider()


# ============================================================
# HERO
# ============================================================

hero_left, hero_right = st.columns([1.1, 1], gap="large")

with hero_left:

    st.markdown(
        '<div class="small-label">Rosanna Village</div>',
        unsafe_allow_html=True
    )

    st.title("Creative food.\nGood coffee.\nMiss Marie.")

    st.markdown(
        """
        <div class="hero-text">
        Creative breakfast and lunch dishes, plus housemade
        cakes, served in trendy, compact surroundings.
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("")

    button1, button2 = st.columns(2)

    with button1:
        st.link_button(
            "View Menu ↓",
            "#menu",
            use_container_width=True
        )

    with button2:
        st.link_button(
            "Call Café",
            "tel:0394572365",
            use_container_width=True
        )

with hero_right:

    st.image(
        "https://images.unsplash.com/photo-1495474472287-4d71bcdd2085?auto=format&fit=crop&w=1200&q=85",
        use_container_width=True
    )


st.write("")
st.write("")


# ============================================================
# INTRO
# ============================================================

st.markdown(
    '<div class="small-label">Welcome to Miss Marie</div>',
    unsafe_allow_html=True
)

st.header("Your neighbourhood café in Rosanna.")

st.write(
    """
    Miss Marie Café brings together creative breakfast and lunch,
    quality coffee and housemade cakes in the heart of Rosanna Village.

    Whether you're meeting friends, grabbing coffee or settling in
    for lunch, there's something to make your visit worth coming back for.
    """
)


# ============================================================
# FEATURED FOOD
# ============================================================

st.write("")
st.write("")

food1, food2, food3 = st.columns(3, gap="large")

with food1:
    st.image(
        "https://images.unsplash.com/photo-1533089860892-a7c6f0a88666?auto=format&fit=crop&w=900&q=85",
        use_container_width=True
    )
    st.subheader("Breakfast")
    st.write(
        "Creative breakfast favourites made for slow mornings."
    )

with food2:
    st.image(
        "https://images.unsplash.com/photo-1547592180-85f173990554?auto=format&fit=crop&w=900&q=85",
        use_container_width=True
    )
    st.subheader("Lunch")
    st.write(
        "Fresh, generous lunch dishes packed with flavour."
    )

with food3:
    st.image(
        "https://images.unsplash.com/photo-1578985545062-69928b1d9587?auto=format&fit=crop&w=900&q=85",
        use_container_width=True
    )
    st.subheader("Housemade cakes")
    st.write(
        "Something sweet waiting in the cake cabinet."
    )


# ============================================================
# MENU
# ============================================================

st.write("")
st.write("")
st.divider()
st.write("")

st.markdown(
    '<div id="menu"></div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="small-label">The Menu</div>',
    unsafe_allow_html=True
)

st.header("Something for every appetite.")

st.write(
    "A selection inspired by Miss Marie's published menu. "
    "Items and prices may change."
)

# ------------------------------------------------------------
# BREAKFAST
# ------------------------------------------------------------

st.subheader("Breakfast")

breakfast = [
    (
        "Just 2 Free Range Eggs",
        "Poached, scrambled or fried on sourdough or multigrain.",
        "$11.90"
    ),
    (
        "Sweetcorn Fritters",
        "Smoked salmon, dill-caper sour cream, beetroot relish and poached egg.",
        "$24.90"
    ),
    (
        "Big Brekkie",
        "Two eggs, bacon, tomato, spinach, mushrooms, chorizo, relish and sourdough toast.",
        "$24.90"
    ),
    (
        "Veg Brekkie",
        "Summer greens, seasoned ricotta, poached egg, seeds, charred quinoa loaf and avocado.",
        "$22.90"
    ),
    (
        "Tofu Scramble",
        "Vegan tofu scramble with greens, chilli and sourdough.",
        "$22.90"
    ),
    (
        "Strawberries & Cream Pancakes",
        "A sweet breakfast favourite.",
        "$22.90"
    )
]

for name, description, price in breakfast:

    left, right = st.columns([5, 1])

    with left:
        st.write("**" + name + "**")
        st.caption(description)

    with right:
        st.markdown(
            f"<div class='price'>{price}</div>",
            unsafe_allow_html=True
        )


# ------------------------------------------------------------
# LUNCH
# ------------------------------------------------------------

st.subheader("Lunch")

lunch = [
    (
        "Super Salad",
        "Black quinoa, kale, charred corn, carrot, beetroot hummus, broccoli, nuts, poached egg, lime and chilli.",
        "$17.90"
    ),
    (
        "Super Salad + Chicken",
        "Add poached chicken to the super salad.",
        "+$5.00"
    ),
    (
        "Weekly Special",
        "Ask the team about the current special.",
        "Ask us"
    )
]

for name, description, price in lunch:

    left, right = st.columns([5, 1])

    with left:
        st.write("**" + name + "**")
        st.caption(description)

    with right:
        st.markdown(
            f"<div class='price'>{price}</div>",
            unsafe_allow_html=True
        )


# ------------------------------------------------------------
# DRINKS
# ------------------------------------------------------------

st.subheader("Coffee & Drinks")

drinks = [
    ("Coffee", "Freshly made coffee.", "Ask us"),
    ("Fresh Juice", "Ask about today's selection.", "Ask us"),
    ("Tea", "A selection of teas.", "Ask us"),
    ("Cold Drinks", "Ask the team about today's selection.", "Ask us")
]

for name, description, price in drinks:

    left, right = st.columns([5, 1])

    with left:
        st.write("**" + name + "**")
        st.caption(description)

    with right:
        st.markdown(
            f"<div class='price'>{price}</div>",
            unsafe_allow_html=True
        )


# ------------------------------------------------------------
# SWEETS
# ------------------------------------------------------------

st.subheader("Sweet Things")

sweets = [
    ("Housemade Cakes", "Daily selection from the cake cabinet.", "Ask us"),
    ("Sweet Treats", "Selection changes regularly.", "Ask us")
]

for name, description, price in sweets:

    left, right = st.columns([5, 1])

    with left:
        st.write("**" + name + "**")
        st.caption(description)

    with right:
        st.markdown(
            f"<div class='price'>{price}</div>",
            unsafe_allow_html=True
        )


# ============================================================
# ABOUT
# ============================================================

st.write("")
st.write("")
st.divider()
st.write("")

about_left, about_right = st.columns([1, 1], gap="large")

with about_left:

    st.markdown(
        '<div class="small-label">The Miss Marie feeling</div>',
        unsafe_allow_html=True
    )

    st.header("Come hungry. Leave happy.")

    st.write(
        """
        Miss Marie is a neighbourhood café in Rosanna Village,
        bringing together good food, quality coffee and a relaxed
        atmosphere.

        From breakfast classics to weekly specials and housemade
        cakes, there's always a reason to stop in.
        """
    )

with about_right:

    st.image(
        "https://images.unsplash.com/photo-1554118811-1e0d58224f24?auto=format&fit=crop&w=1200&q=85",
        use_container_width=True
    )


# ============================================================
# GALLERY
# ============================================================

st.write("")
st.write("")
st.divider()
st.write("")

st.markdown(
    '<div class="small-label">Inside the café</div>',
    unsafe_allow_html=True
)

st.header("Come see us.")

gallery1, gallery2 = st.columns(2, gap="large")

with gallery1:
    st.image(
        "https://images.unsplash.com/photo-1517248135467-4c7edcad34c4?auto=format&fit=crop&w=1200&q=85",
        use_container_width=True
    )

with gallery2:
    st.image(
        "https://images.unsplash.com/photo-1498804103079-a6351b050096?auto=format&fit=crop&w=1200&q=85",
        use_container_width=True
    )


# ============================================================
# VISIT
# ============================================================

st.write("")
st.write("")
st.divider()
st.write("")

st.markdown(
    '<div class="small-label">Find us</div>',
    unsafe_allow_html=True
)

st.header("Come by for breakfast, lunch or coffee.")

info1, info2, info3 = st.columns(3, gap="large")

with info1:

    st.markdown(
        """
        <div class="info-box">

        ### 📍 Visit us

        **45 Beetham Parade**

        Rosanna VIC 3084

        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "Get directions",
        "https://www.google.com/maps/search/?api=1&query=45+Beetham+Parade+Rosanna+VIC+3084",
        use_container_width=True
    )

with info2:

    st.markdown(
        """
        <div class="info-box">

        ### 🕐 Opening hours

        **Monday – Friday**

        7:00am – 2:30pm

        **Saturday – Sunday**

        8:00am – 2:30pm

        </div>
        """,
        unsafe_allow_html=True
    )

with info3:

    st.markdown(
        """
        <div class="info-box">

        ### ☎️ Call us

        Questions about the menu,
        bookings or today's specials?

        **(03) 9457 2365**

        </div>
        """,
        unsafe_allow_html=True
    )

    st.link_button(
        "Call the café",
        "tel:0394572365",
        use_container_width=True
    )


# ============================================================
# CONTACT
# ============================================================

st.write("")
st.write("")
st.divider()
st.write("")

st.markdown(
    '<div class="small-label">Get in touch</div>',
    unsafe_allow_html=True
)

st.header("Planning a visit?")

st.write(
    "Have a question about the café, menu or a group visit?"
)

with st.form("contact_form"):

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Name")

    with col2:
        phone = st.text_input("Phone")

    email = st.text_input("Email")

    enquiry = st.selectbox(
        "Enquiry",
        [
            "General enquiry",
            "Table enquiry",
            "Group booking",
            "Catering",
            "Cake enquiry"
        ]
    )

    message = st.text_area("Message")

    send = st.form_submit_button(
        "Send enquiry",
        use_container_width=True
    )

    if send:

        if not name or not email or not message:

            st.warning(
                "Please complete your name, email and message."
            )

        else:

            st.success(
                "Thanks for getting in touch with Miss Marie Café!"
            )


# ============================================================
# FINAL
# ============================================================

st.write("")
st.write("")
st.divider()
st.write("")

st.markdown(
    '<div class="small-label">Rosanna Village</div>',
    unsafe_allow_html=True
)

st.header("See you at Miss Marie.")

st.write(
    "45 Beetham Parade, Rosanna VIC 3084"
)

st.link_button(
    "Call Miss Marie Café",
    "tel:0394572365"
)

st.write("")
st.write("")

st.caption(
    "Miss Marie Café · 45 Beetham Parade, Rosanna VIC 3084 · "
    "(03) 9457 2365"
)
