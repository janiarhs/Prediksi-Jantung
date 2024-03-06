# Masukan Library
import pickle
import numpy as np
import streamlit as st

# Load Save Model
model = pickle.load(open('Penyakit_jantung.sav', 'rb'))

# Judul Web
st.title('Prediksi Penyakit Jantung')

# Membagi Kolom
col1, col2, col3 = st.columns(3)

# Membuat form input
with col1 :
    age = st.number_input('Umur')
with col2 :
    sex = st.number_input('Jenis Kelamin')
with col3 :
    cp = st.number_input('Jenis Nyeri Dada')
with col1 :
    trestbps = st.number_input('Tekanan Darah')
with col2 :
    chol = st.number_input('Nilai Kolesterol')
with col3 :
    fbs = st.number_input('Gula Darah')
with col1 :
    restecg = st.number_input('Hasil Electrocardiographic')
with col2 :
    thalach = st.number_input('Detak Jantung Maksimum')
with col3 :
    exang = st.number_input('Induksi Angina')
with col1 :
    oldpeak = st.number_input('ST Depression')
with col2 :
    slope = st.number_input('Slope')
with col3 :
    ca = st.number_input('Nilai CA')
with col1 :
    thal = st.number_input('Nilai Thal')

# Code for Prediction
jantung_diagnosis = ''

# Membuat Tombol untuk Prediction
if st.button('Prediksi Penyakit Jantung') :
    jantung_prediction = model.predict([[age,sex,cp,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
    if(jantung_prediction[0] == 1) :
        jantung_diagnosis = 'Pasien Terkena Penyakit Jantung'
    else :
        jantung_diagnosis = 'Pasien Tidak Terkena Penyakit Jantung'

st.success(jantung_diagnosis)