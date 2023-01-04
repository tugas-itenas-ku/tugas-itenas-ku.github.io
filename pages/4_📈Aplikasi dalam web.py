import plotly_express as px
import streamlit as st
import pandas as pd


#---PENGHILANG HEADER, FOOTER, DAN BRANDING---
def local_css(file_name):   
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")

# Judul dan Sub-judul

st.title("Aplikasi dalam web")
ket1 = "Aplikasi Visualisasi Diagram batang\n(Total Dosen Hadir)"
st.header("Aplikasi Visualisasi Diagram batang")
st.subheader("Total Dosen Hadir")
jurusan, kelas, semester = st.columns(3)
jurusan.metric("Jurusan", "Teknik sipil")
kelas.metric("Kelas", "DD")
semester.metric("Semester", "1")
angkatan, sumber = st.columns(2)
angkatan.metric("Angkatan", "2022")
with sumber:
    st.write("##")
    st.caption("Sumber data :\n(https://mahasiswa.itenas.ac.id/mahasiswa)")
st.write("---")
    
# Isi Halaman aplikasi
with st.container():
    appdata, appdata_sort = st.columns(2)
    # --- Membuat Program Visualisasi Total Dosen Hadir Kelas DD Angkatan 2022 Semester 1
    with appdata:
        #--- Membuat data sederhana dalam bentuk Dataframe ---
        df_dosenhadir = {
            'Mata Kuliah' : ['Matematika 1', 'Pengantar Transformasi Digital', 
                                'Pengantar Infrastruktur Berkelanjutan', 'Fisika 1',
                                'Ilmu Kebumian', 'Gambar Teknik', 'Gambar Teknik (Asistensi)',
                                'Bahasa Pemrograman bidang Teknik Sipil',
                                'Bahasa Pemrograman bidang Teknik Sipil (Asistensi)'
                                ],
            'Jumlah Kehadiran': [13, 14, 14, 15, 11, 14, 13, 13, 13]
        }
        dataframex = pd.DataFrame(df_dosenhadir)
        df_dosenhadir2 = dataframex.set_index('Mata Kuliah')

        # Visualisasi data dalam bentuk diagram batang
        bag_data = px.bar(
            dataframex,
            x="Mata Kuliah",
            y="Jumlah Kehadiran",
            color="Mata Kuliah",
            text="Jumlah Kehadiran"
        )

        # Menghilangkan Keterangan tiap batang
        bag_data.update_xaxes(title='Mata Kuliah', 
                            title_font_family="Helvetica", 
                            visible=True, 
                            showticklabels=False, 
                            showgrid=True,
                            gridwidth=1,
                            gridcolor='#5B5D5E'
                            )
        bag_data.update_yaxes(showgrid=True,
                            gridwidth=1,
                            gridcolor='#5B5D5E'
                            )
        bag_data.update_layout(
            font_family="Helvetica",
            font_color="white",
            legend_title="<b>Mata Kuliah</br>",
            legend_title_font_color="yellow",
            yaxis_range=[0,20]
        )
        st.plotly_chart(bag_data)
    with appdata_sort:
        #  Proses penyortiran data menurut jumlah hadir
        bag_data_sort = dataframex.sort_values(by=['Jumlah Kehadiran'])
        bag_data_sort_print = px.bar(
            bag_data_sort,
            x="Mata Kuliah",
            y="Jumlah Kehadiran",
            color="Mata Kuliah",
            text="Jumlah Kehadiran"
        )

        # Menghilangkan Keterangan tiap batang
        bag_data_sort_print.update_xaxes(title='Mata Kuliah', 
                            title_font_family="Helvetica", 
                            visible=True, 
                            showticklabels=False, 
                            showgrid=True,
                            gridwidth=1,
                            gridcolor='#5B5D5E'
                            )
        bag_data_sort_print.update_yaxes(showgrid=True,
                            gridwidth=1,
                            gridcolor='#5B5D5E'
                            )
        bag_data_sort_print.update_layout(
            font_family="Helvetica",
            font_color="white",
            legend_title="<b>Mata Kuliah</br>",
            legend_title_font_color="yellow",
            yaxis_range=[0,20]
        )
        st.plotly_chart(bag_data_sort_print)
st.write("---")
st.header("Aplikasi Penghitung Nilai Akhir")


    #d = nilai tugas 25%
tugas = st.number_input(label="Masukkan nilai Tugas")
    # c = nilai kuis 20%
kuis = st.number_input(label="Masukkan nilai Kuis")
    # b = nilai uts 25%
uts = st.number_input(label="Masukkan nilai UTS")
    # a = nilai uas 30%
uas = st.number_input(label="Masukkan nilai UAS")

#proses 
#Rumus Nilai akhir = a*30/100 + b*25/100 + c*20/100 + d*25/100
nilai_akhir=int(tugas)*25/100+int(kuis)*20/100+int(uts)*25/100+int(uas)*30/100

#output
def hitung():
    #nilai akhir tidak valid
    if int(nilai_akhir) < 0 or int(nilai_akhir) > 100:
            hasil=("Nilai tidak valid, silahkan masukkan ulang") 
        #nilai akhir A
    elif int(nilai_akhir) >= 80 and int(nilai_akhir) <=100 :
            hasil=("A")
        #nilai akhir AB
    elif int(nilai_akhir) >=73 and int(nilai_akhir) <=80 :
            hasil=("AB")
        #nilai akhir B
    elif int(nilai_akhir) >=65 and int(nilai_akhir) <=73 :
            hasil=("B")
        #nilai akhir BC
    elif int(nilai_akhir) >=60 and int(nilai_akhir) <=65 :
            hasil=("BC")
        #nilai akhir C
    elif int(nilai_akhir) >=50 and int(nilai_akhir) <=60 :
            hasil=("C")
        #nilai akhir CD = harus ujian ulang
    elif int(nilai_akhir) >=40 and int(nilai_akhir) <=50 :
            hasil=("CD \nAnda harus mengikuti ujian ulang !")
        #nilai akhir E = harus ujian ulang
    elif int(nilai_akhir) <40 :
            hasil=("E \nAnda harus mengikuti ujian ulang !")

    st.write("Nilai Akhir anda")
    if 100 > nilai_akhir > 50:
        st.success(hasil)
    elif nilai_akhir <= 50:
        st.error(hasil)
    else:
        st.error("Nilai tidak valid, silahkan masukkan ulang")

if st.button("Hitung"):
    hitung()
    
    

    
    
    
    
    
