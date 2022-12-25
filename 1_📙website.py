import requests
import streamlit as st
from streamlit_lottie import st_lottie  
from PIL import Image
from streamlit_option_menu import option_menu


# Find more emojis here: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(page_title= "Teknik Sipil", page_icon=":construction:", layout="wide")

def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


# Use local CSS
def local_css(file_name):   
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style/style.css")

# ---- LOAD ASSETS ----
lottie_coding = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_qcrbuch7.json")
img_vid1 = Image.open("images/1.png")
img_vid2 = Image.open("images/sipil_what.jpg")
img_construction = Image.open("images/wow.jpg")


# BAGIAN NAVBAR
selected2 = option_menu(None, ["Home", "Upload", "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal")
selected2

# 3. CSS style definitions
selected3 = option_menu(None, ["Home", "Upload",  "Tasks", 'Settings'], 
    icons=['house', 'cloud-upload', "list-task", 'gear'], 
    menu_icon="cast", default_index=0, orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "25px"}, 
        "nav-link": {"font-size": "25px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "green"},
    }
)

# ---- BAGIAN HEADER ----
with st.container():
    st.title("Pengantar Teknik Sipil :construction:")
    st.image(img_construction)
    st.subheader("Rincian singkat tentang Teknik Sipil")
    st.write(
        "Teknik sipil adalah salah satu cabang ilmu teknik yang mempelajari tentang bagaimana merancang, membangun, merenovasi tidak hanyagedung dan infrastruktur, tetapi juga mencakup lingkungan untuk kemaslahatan hidup manusia."
    )
    st.write(
        "Teknik sipil mempunyai ruang lingkup yang luas, di dalamnya pengetahuan matematika, fisika, kimia, biologi, geologi, lingkunganhingga komputer mempunyai peranannya masing-masing. Teknik sipil dikembangkan sejalan dengan tingkat kebutuhan manusia dan pergerakannya, hingga bisa dikatakan ilmu ini bisa merubah sebuah hutan menjadi kota besar."
    )
    
# ---- APA YANG KITA LAKUKAN ----
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Apa yang kita lakukan ?")
        st.write("##")
        st.write(
            """
            Dalam Teknik Sipil, terdapat beberapa bidang umum, yakni:
            - Manajemen Konstruksi.
            - Geoteknik.
            - Transportasi.
            - Hidrologi/Hidrolika.
            - Stuktur Bangunan.
            """
        )
        st.write("[YouTube Channel >](https://youtube.com/c/CodingIsFun)")
    with right_column:
        st_lottie(lottie_coding, height=300, key="coding")

# ---- BACKGROUND ----
def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.pixabay.com/photo/2019/04/24/11/27/flowers-4151900_960_720.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
    )

    # ---- REFERENSI ----

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_vid1)
    with text_column:
        st.subheader("Jurusan Kuliah : Teknik Sipil oleh Edulab Indonesia")
        st.write(
            """
            Hallo Edulabers, cita-cita kamu ingin masuk Teknik Sipil? Belajar apa aja sih di Teknik Sipil? Nanti kerja bakalan jadi ahli bangunan apa ya?

Dari pada penasaran yuk nonton videonya sekarang dan share juga ke temen-temen kamu yaa.’.
            """
        )
        st.markdown("[Tonton video...](https://youtu.be/FOULV9Xij_8)")
        

with st.container():
    image_column, text_column = st.columns((1, 2))
    with image_column:
        st.image(img_vid2)
    with text_column:
        st.subheader("Pengenalan Teknik Sipil (Video Tugas PTD)")
        st.write(
            """
            Assalamu'alaikum,wr,wb. Perkenalkan Kami dari kelompok SI-7 Mata Kuliah Pengantar Transformasi Digital
            Ingin membahas tentang website kita, yaitu tentang Teknik Sipil’.
            """
        )
        st.markdown("[Tonton video...](https://youtu.be/HOz_iGercHU)")