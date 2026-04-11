import streamlit as st
import serial
import time

# ganti COM sesuai port Arduino kamu
PORT = "COM3"
BAUD = 9600

st.title("Kontrol LED Arduino dengan Password")

password = st.text_input("Masukkan Password", type="password")

if st.button("Kirim ke Arduino"):

    try:
        arduino = serial.Serial(PORT, BAUD, timeout=1)
        time.sleep(2)

        arduino.write((password + "\n").encode())

        st.success("Password berhasil dikirim ke Arduino")

        response = arduino.readline().decode().strip()

        if response:
            st.write("Respon Arduino:", response)

        arduino.close()

    except:
        st.error("Arduino tidak terhubung")
