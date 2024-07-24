import pickle
import streamlit as st
import numpy as np

# Load model dan scaler
model = pickle.load(open('water_potability.sav', 'rb'))
scaler = pickle.load(open('scaler.sav', 'rb'))

# Judul
st.title('Prediksi Kualitas Air')
st.write('Gunakan web ini untuk memprediksi kualitas air berdasarkan beberapa parameter kimia.')

# Input data dari pengguna
st.sidebar.header('Selamat mencoba')
ph = st.sidebar.text_input('Input nilai pH')
hardness = st.sidebar.text_input('Input nilai Hardness')
solids = st.sidebar.text_input('Input nilai Solids')
chloramines = st.sidebar.text_input('Input nilai Chloramines')
sulfate = st.sidebar.text_input('Input nilai Sulfate')
conductivity = st.sidebar.text_input('Input nilai Conductivity')

# Kode prediksi
water_quality_diagnosis = ''

# Membuat tombol untuk prediksi
if st.sidebar.button('Test Prediksi Kualitas Air'):
    # Validasi input
    if (ph == '' or hardness == '' or solids == '' or chloramines == '' or sulfate == '' or conductivity == ''):
        st.sidebar.warning('Mohon isi semua kolom yang diperlukan.')
    else:
        # Konversi input ke tipe data yang sesuai
        ph = float(ph)
        hardness = float(hardness)
        solids = float(solids)
        chloramines = float(chloramines)
        sulfate = float(sulfate)
        conductivity = float(conductivity)
        
        # Menyusun input ke dalam array
        input_features = np.array([[ph, hardness, solids, chloramines, sulfate, conductivity]])
        
        # Normalisasi atau standardisasi input jika diperlukan
        input_features = scaler.transform(input_features)
        
        # Melakukan prediksi
        water_quality_prediction = model.predict(input_features)
        if water_quality_prediction[0] == 1:
            water_quality_diagnosis = 'HATI-HATI!! Air tidak layak dikonsumsi.'
            st.sidebar.error(water_quality_diagnosis)
        else:
            water_quality_diagnosis = 'SELAMAT!! Air layak dikonsumsi.'
            st.sidebar.success(water_quality_diagnosis)

# Footer
st.markdown("---")
footer = """
    <style>
    .footer {
        left: 0;
        bottom: 0;
        width: 100%;
        color: White;
        text-align: center;
        padding: 10px;
    }
    </style>
"""
st.markdown(footer, unsafe_allow_html=True)

# CSS untuk tema gelap
page_bg_img = '''
<style>
.stApp {
  background: #1e1e1e;
  color: #e0e0e0;
  font-family: 'Arial', sans-serif;
}
</style>
'''
# Menyisipkan CSS ke dalam aplikasi
st.markdown(page_bg_img, unsafe_allow_html=True)