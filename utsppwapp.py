{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": "none",
   "id": "a5f7896d-89e3-4d11-8b2c-e7b21942b89d",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2024-10-29 18:37:34.960 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 18:37:34.961 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 18:37:34.963 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 18:37:34.964 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 18:37:34.965 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 18:37:34.966 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 18:37:34.967 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 18:37:34.967 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 18:37:34.968 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 18:37:34.969 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 18:37:34.969 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 18:37:34.970 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2024-10-29 18:37:34.970 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import pickle\n",
    "from sklearn.feature_extraction.text import TfidfVectorizer\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "\n",
    "# Load model dan vectorizer\n",
    "with open('model_logreg.pkl', 'rb') as model_file:\n",
    "    model = pickle.load(model_file)\n",
    "    \n",
    "with open('tfidf_vectorizer.pkl', 'rb') as vectorizer_file:\n",
    "    vectorizer = pickle.load(vectorizer_file)\n",
    "\n",
    "# Judul aplikasi\n",
    "st.title(\"Klasifikasi Kategori Berita\")\n",
    "\n",
    "# Masukan teks berita\n",
    "input_text = st.text_area(\"Masukkan teks berita yang ingin diklasifikasikan:\")\n",
    "\n",
    "# Proses prediksi ketika pengguna mengisi teks berita\n",
    "if st.button(\"Klasifikasikan\"):\n",
    "    if input_text:\n",
    "        # Transformasi teks menggunakan TF-IDF\n",
    "        input_vector = vectorizer.transform([input_text])\n",
    "        \n",
    "        # Prediksi kategori menggunakan model\n",
    "        prediction = model.predict(input_vector)\n",
    "        \n",
    "        # Tampilkan hasil prediksi\n",
    "        st.write(\"Kategori Berita:\", prediction[0])\n",
    "    else:\n",
    "        st.warning(\"Masukkan teks berita untuk klasifikasi.\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": "none",
   "id": "a707cd2e-2b74-4c45-a33c-27164d04c511",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": "none",
   "id": "0d9b866a-23dc-4339-9b01-cc89a7e55619",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
