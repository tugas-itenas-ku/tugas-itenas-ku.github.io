import requests
import streamlit as st
from streamlit_lottie import st_lottie  
from PIL import Image

# ---LOAD ASSETS---
gam_1 = Image.open("images/sejarah1.jpg")
gam_2 = Image.open("images/sejarah2.jpg")
gam_3 = Image.open("images/sejarah3.jpeg")
gam_4 = Image.open("images/sejarah4.jpg")

#---PENGHILANG HEADER, FOOTER, DAN BRANDING---
def local_css(file_name):   
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# ---- BAGIAN HEADER ----
with st.container():
    st.title("Sejarah singkat Teknik Sipil :scroll:")
    st.subheader("Sejarah Peradaban")
    st.image(gam_1)
    
    st.write(
        "Teknik Sipil telah menjadi aspek kehidupan sejak awal keberadaan manusia. Praktik paling awal dari Teknik Sipil mungkin telah dimulai antara 4000 dan 2000 SM di Mesir Kuno dan Mesopotamia (Irak Kuno) ketika manusia mulai meninggalkan keberadaan nomaden, sehingga menyebabkan kebutuhan untuk pembangunan tempat berlindung. Selama waktu ini, transportasi menjadi semakin penting yang mengarah pada pengembangan roda dan pelayaran."
    )
    st.write(
        "Sampai zaman modern tidak ada perbedaan yang jelas antara Teknik sipil dan arsitektur, dan istilah insinyur dan arsitek terutama variasi geografis yang mengacu pada orang yang sama, sering digunakan secara bergantian. Pembangunan Piramida di Mesir (sekitar 2700-2500 SM) dapat dianggap sebagai contoh pertama dari konstruksi struktur besar."
    )
    st.write("---")
    st.subheader("Sejarah Pendidikan")
    st.image(gam_2)
    st.write("Di Inggris pada awal abad ke-19, terdapat pembagian pendidikan teknik, yaitu teknik sipil dan teknik militer (dilayani oleh Akademi Militer Kerajaan, Woolwich), ditambah dengan tuntutan Revolusi Industri, melahirkan prakarsa pendidikan teknik baru, yaitu Kelas Teknik Sipil dan Pertambangan. Didirikan di King's College London pada tahun 1838. Pendidikan teknik baru ini dibuat terutama sebagai tanggapan terhadap pertumbuhan sistem perkeretaapian dan kebutuhan akan insinyur yang lebih berkualitas.")
    st.write("##")
    st.image(gam_3)
    st.write(
        " Dilansir dari [wikipedia.com](https://en.wikipedia.org/wiki/Civil_engineering#:~:text=The%20earliest%20practice%20of%20civil,for%20the%20construction%20of%20shelter.), Perguruan tinggi swasta pertama yang mengajar teknik sipil di Amerika Serikat adalah Universitas Norwich, didirikan pada tahun 1819 oleh Kapten Alden Partridge. Perguruan Tinggi swasta untuk Insinyur Sipil di Putney didirikan pada tahun 1839, dan Gelar Teknik Inggris yang pertama didirikan di Universitas Glasgow pada tahun 1840. Gelar pertama bidang teknik sipil di Amerika Serikat ini diberikan oleh Institut Politeknik Rensselaer pada tahun 1835. Lalu gelar pertama yang diberikan kepada seorang wanita diberikan oleh Universitas Cornell kepada Nora Stanton Blatch pada tahun 1905."
    )
    st.write("##")
    st.subheader("Awal Mula Pendidikan di Indonesia")
    st.image(gam_4)
    st.write(
        " Di Indonesia sendiri, pendidikan tinggi teknik sipil pertama kali diajarkan di Technische Hogeschool te Bandoeng atau yang kita kenal sekarang adalah ITB (Institut Teknologi Bandung) sejak 3 Juli 1920, dengan satu fakultas yakni Fakultas Ilmu Pengetahuan Teknik yang hanya mempunyai satu jurusan yaitu Departemen Jalan dan Struktur Air."
    )
