import streamlit as st
import pandas as pd
from PIL import Image
if 'result_data' not in st.session_state:
    st.session_state.result_data = {}

# Fungsi perpustakaan_umum

#hitung uplm 2
@st.cache_data

def jumlah ():
    
    tenaga_kab = st.number_input("Masukkkan Jumlah Tenaga Perpustakaan Kabupaten ")
    jml_unit_kab = tenaga_kab/angka_pembagi_ratio
    st.write("Jumlah tenaga Kabupaten {:.6f}".format(jml_unit_kab))
    # mendapatkan jml angka_pembagi_ratio tenaga perpustakaan umum kecamatan
    tenaga_kec = st.number_input("Masukkkan Jumlah tenaga Perpustakaan Kecamatan ")
    jml_unit_kec = tenaga_kec/populasi
    st.write("Jumlah tenaga Kecamatan {:.6f}".format(jml_unit_kec))
    tenaga_ds = st.number_input("Masukkkan Jumlah tenaga Perpustakaan Desa/ Kelurahan ")
    jml_unit_ds = tenaga_ds/populasi
    st.write("Jumlah tenaga Desa",jml_unit_ds)
    perpustakaan_umum=(jml_unit_kab + jml_unit_kec + jml_unit_ds)
    st.session_state.result_data['perpustakaan_umum'] = perpustakaan_umum
    return perpustakaan_umum
# Menampilkan input form menggunakan Streamlit
# st.subheader("Perhitungan IPLM")
st.markdown("<h1 style='text-align: center;'>Perhitungan IPLM</h1>", unsafe_allow_html=True)
image= Image.open('uplm.png')
st.image(image)
pilihan_uplm = st.selectbox("**Pilih jenis UPLM :**", ["UPLM 1", "UPLM 2", "UPLM 3", "UPLM 4", "UPLM 5", "UPLM 6", "UPLM 7", "IPLM"])

if pilihan_uplm == "UPLM 1":
    st.subheader("Perhitungan UPLM 1")
    st.markdown(":red[**Perpustakaan Umum**]")

    def perpustakaan_umum(jumlah_unit_perpustakaan_kabkota, jumlah_unit_perpustakaan_kec, jumlah_unit_perpustakaan_desa):
        if angka_pembagi_ratio > 0:
            hitung_jup_kabkota = jumlah_unit_perpustakaan_kabkota / angka_pembagi_ratio
        else:
            hitung_jup_kabkota = 0.0

        if populasi > 0:
            hitung_jup_kec = jumlah_unit_perpustakaan_kec / populasi
        else:
            hitung_jup_kec = 0.0

        if populasi > 0:
            hitung_jup_desa = jumlah_unit_perpustakaan_desa / populasi
        else:
            hitung_jup_desa = 0.0
        return hitung_jup_kabkota, hitung_jup_kec, hitung_jup_desa
    
    def sekolah_madrasah(jumlah_unit_perpustakaan_sdmi, jumlah_unit_perpustakaan_smp, jumlah_unit_perpustakaan_sma,
                        jumlah_civitas_sdmi, jumlah_civitas_smp, jumlah_civitas_sma):
        # Menambahkan pengecekan apakah jumlah_civitas_sdmi lebih besar dari nol
        if jumlah_civitas_sdmi > 0:
            hitung_jup_sdmi = jumlah_unit_perpustakaan_sdmi / jumlah_civitas_sdmi
        else:
            hitung_jup_sdmi = 0.0  # Jika jumlah_civitas_sdmi nol, hasilnya akan diatur menjadi 0

        if jumlah_civitas_smp > 0:
            hitung_jup_smp = jumlah_unit_perpustakaan_smp / jumlah_civitas_smp
        else:
            hitung_jup_smp = 0.0  # Jika jumlah_civitas_sdmi nol, hasilnya akan diatur menjadi 0

        if jumlah_civitas_sma > 0:
            hitung_jup_sma = jumlah_unit_perpustakaan_sma / jumlah_civitas_sma
        else:
            hitung_jup_sma = 0.0  # Jika jumlah_civitas_sdmi nol, hasilnya akan diatur menjadi 0
        return hitung_jup_sdmi, hitung_jup_smp, hitung_jup_sma


    # Fungsi perguruan_tinggi
    def perguruan_tinggi(jumlah_unit_perpustakaan_perguruan_tinggi, jumlah_civitas_perguruan_tinggi):
        if jumlah_civitas_perguruan_tinggi > 0:
            hitung_jup_perguruan_tinggi = jumlah_unit_perpustakaan_perguruan_tinggi / jumlah_civitas_perguruan_tinggi
        else:
            hitung_jup_perguruan_tinggi = 0.0  # Jika jumlah_civitas_sdmi nol, hasilnya akan diatur menjadi 0
        return hitung_jup_perguruan_tinggi

    # Fungsi perpustakaan_khusus
    def perpustakaan_khusus(jumlah_unit_perpustakaan_khusus, jumlah_pegawai):
        if jumlah_pegawai > 0:
            hitung_jup_perpus_khusus = jumlah_unit_perpustakaan_khusus / jumlah_civitas_sdmi
        else:
            hitung_jup_perpus_khusus = 0.0  # Jika jumlah_civitas_sdmi nol, hasilnya akan diatur menjadi 0
        return hitung_jup_perpus_khusus

    # Fungsi uplm1
    @st.cache_data
    def uplm1(perpus_umum, perpus_sekolah_madrasah, perpus_perguruan_tinggi, perpus_khusus):
        hitung_jumlah_total = ((0.5 * total_perpus_umum) + (0.2 * total_perpus_sekolah_madrasah) + 
                            (0.2 * perpus_perguruan_tinggi) + (0.1 * perpus_khusus) * angka_koreksi_uplm1)
        return hitung_jumlah_total

    #uplm 2
    #fungsi hitung  koleksi perpustkaan umum
    
    # Input untuk perpustakaan umum
    perpustakaan_umum_A = st.number_input("Masukkan Jumlah Unit Perpustakaan Kabupaten/kota:" , 0.0, 100000000.0, step=0.00001, format="%.5f")
    angka_pembagi_ratio = st.number_input("Angka Pembagi Ratio Kabupaten/Kota: ", 0.0, 100000000.0, step=0.00001)

    perpustakaan_umum_B = st.number_input("Masukkan Jumlah Unit Perpustakaan Kecamatan:" )
    perpustakaan_umum_C = st.number_input("Masukkan Jumlah Unit Perpustakaan Desa:")
    populasi = st.number_input("Jumlah Populasi Kabupaten/Kota :")

    # Hitung hasil perpustakaan umum
    hasil_jup_A, hasil_jup_B, hasil_jup_C = perpustakaan_umum(perpustakaan_umum_A, perpustakaan_umum_B, perpustakaan_umum_C)

    # Menampilkan hasil perpustakaan umum
    st.write("Hasil Perpustakaan Kabupaten: {:.6f}".format(hasil_jup_A))
    st.write("Hasil Perpustakaan Kecamatan: {:.6f}".format(hasil_jup_B))
    st.write("Hasil Perpustakaan Desa: {:.6f}".format(hasil_jup_C))

    # Hitung total perpustakaan umum
    total_perpus_umum = hasil_jup_A + hasil_jup_B + hasil_jup_C
    st.write("Jumlah Ratio Ketersediaan Layanan Perpustakaan Umum : {:.6f}".format(total_perpus_umum))

    # Input untuk sekolah madrasah
    st.markdown(":red[**Perpustakaan Sekolah / madrasah**]")
    sekolah_madrasah_A = st.number_input("Masukkan Jumlah Unit Perpustakaan SD/MI :", )
    jumlah_civitas_sdmi = st.number_input("Masukkan Jumlah Civitas SD/MI :")

    sekolah_madrasah_B = st.number_input("Masukkan Jumlah Unit Perpustakaan SMP :", )
    jumlah_civitas_smp = st.number_input("Masukkan Jumlah Civitas SMP :")

    sekolah_madrasah_C = st.number_input("Masukkan Jumlah Unit Perpustakaan SMA :", )
    jumlah_civitas_sma = st.number_input("Masukkan Jumlah Civitas SMA :")

    # Hitung hasil sekolah madrasah
    hasil_jup_sdmi, hasil_jup_smp, hasil_jup_sma = sekolah_madrasah(sekolah_madrasah_A, sekolah_madrasah_B, sekolah_madrasah_C,
                                                                    jumlah_civitas_sdmi, jumlah_civitas_smp, jumlah_civitas_sma)

    # Menampilkan hasil sekolah madrasah
    st.write("Hasil Perhitungan SD/MI: {:.6f}".format(hasil_jup_sdmi))
    st.write("Hasil Perhitungan SMP: {:.6f}".format(hasil_jup_smp))
    st.write("Hasil Perhitungan SMA: {:.6f}".format(hasil_jup_sma))

    # Hitung total perpustakaan sekolah madrasah
    total_perpus_sekolah_madrasah = hasil_jup_sdmi + hasil_jup_smp + hasil_jup_sma
    st.write("Jumlah Ratio Ketersediaan Layanan Perpustakaan Sekolah/Madrasah : {:.6f}".format(total_perpus_sekolah_madrasah))

    # Input untuk perguruan tinggi
    st.markdown(":red[**Perpustakaan Perguruan Tinggi**]")
    perguruan_tinggi_A = st.number_input("Masukkan Jumlah Unit Perpustakaan Perguruan Tinggi:", )
    jumlah_civitas_perguruan_tinggi = st.number_input("Masukkan Jumlah Civitas Akademika:", )

    # Hitung hasil perguruan tinggi
    hasil_jup_perguruan_tinggi = perguruan_tinggi(perguruan_tinggi_A, jumlah_civitas_perguruan_tinggi)

    # Menampilkan hasil perguruan tinggi
    st.write("Hasil Perhitungan Perguruan Tinggi: {:.6f}".format(hasil_jup_perguruan_tinggi))

    # Input untuk perpustakaan khusus
    st.markdown(":red[**Perpustakaan Perguruan Khusus**]")
    jumlah_unit_perpus = st.number_input("Masukkan Jumlah Unit Perpustakaan Khusus:", )
    pegawai = st.number_input("Masukkan Jumlah Pegawai/Karyawan:", )

    angka_koreksi_uplm1 = st.number_input("Masukkan Angka Koreksi :")

    # Hitung hasil perpustakaan khusus
    hasil_jup_perpus_khusus = perpustakaan_khusus(jumlah_unit_perpus, pegawai)

    # Menampilkan hasil perpustakaan khusus
    st.write("Hasil Perhitungan Perpustakaan Khusus: {:.6f}".format(hasil_jup_perpus_khusus))

    # Hitung total UPLM1
    hasil_hitung_total_uplm1 = uplm1(total_perpus_umum, total_perpus_sekolah_madrasah, hasil_jup_perguruan_tinggi, hasil_jup_perpus_khusus)

    # Menampilkan hasil UPLM1
    st.write("Hasil UPLM 1: {:.6f}".format(hasil_hitung_total_uplm1))
    
    
elif pilihan_uplm == "UPLM 2":

    st.subheader("Perhitungan UPLM 2")

    def koleksi_pu(jumlah_judul_kab, jumlah_judul_kec, jumlah_judul_desa):
        if populasi > 0:
            hitung_koleksi_kab = jumlah_judul_kab / populasi
        else : 
            hitung_koleksi_kab = 0.0

        if populasi > 0 :
            hitung_koleksi_kec = jumlah_judul_kec / populasi
        else :
            hitung_koleksi_kec = 0.0

        if populasi > 0 :
            hitung_koleksi_desa = jumlah_judul_desa / populasi
        else :
            hitung_koleksi_desa = 0.0
        return hitung_koleksi_kab, hitung_koleksi_kec, hitung_koleksi_desa

    #fungsi hitung koleksi sekolah madrasah
    def koleksi_skmadrasah(jumlah_koleksi_sdmi, jumlah_koleksi_smp, jumlah_koleksi_sma, jumlah_civitas_sdmi,jumlah_civitas_smp, jumlah_civitas_sma):
        if jumlah_civitas_sdmi > 0:
            hitung_koleksi_sdmi = jumlah_koleksi_sdmi / jumlah_civitas_sdmi
        else:
            hitung_koleksi_sdmi = 0.0  # Jika jumlah_civitas_sdmi nol, hasilnya akan diatur menjadi 0

        if jumlah_civitas_smp > 0:
            hitung_koleksi_smp = jumlah_koleksi_smp / jumlah_civitas_smp
        else:
            hitung_koleksi_smp = 0.0  # Jika jumlah_civitas_sdmi nol, hasilnya akan diatur menjadi 0

        if jumlah_civitas_sma > 0:
            hitung_koleksi_sma = jumlah_koleksi_sma / jumlah_civitas_sma
        else:
            hitung_koleksi_sma = 0.0  # Jika jumlah_civitas_sdmi nol, hasilnya akan diatur menjadi 0
        return hitung_koleksi_sdmi, hitung_koleksi_smp, hitung_koleksi_sma

    #hitung koleksi perguruan tinggi 
    def koleksi_pt(jumlah_koleksi_perpustakaan_perguruan_tinggi, jumlah_civitas_perguruan_tinggi):
        if jumlah_civitas_perguruan_tinggi > 0:
            hitung_koleksi_perguruan_tinggi = jumlah_koleksi_perpustakaan_perguruan_tinggi / jumlah_civitas_perguruan_tinggi
        else:
            hitung_koleksi_perguruan_tinggi = 0.0
        return hitung_koleksi_perguruan_tinggi

    #hitung koleksi perpustakaan khusus
    def koleksi_pk(jumlah_koleksi_perpustakaan_khusus, jumlah_pegawai):
        if jumlah_pegawai > 0:
            hitung_koleksi_perpus_khusus = jumlah_koleksi_perpustakaan_khusus / jumlah_pegawai
        else:
            hitung_koleksi_perpus_khusus = 0.0
        return hitung_koleksi_perpus_khusus
    
    def uplm2(koleksi_pu, koleksi_perpus_sekolah_madrasah, koleksi_perpus_perguruan_tinggi, koleksi_perpus_khusus):
        hitung_jumlah_koleksi = ((0.5 * total_koleksi_perpus_umum ) + (0.2 * total_koleksi_sekolah_madrasah) + (0.2 * hasil_koleksi_perguruan_tinggi) + (0.1 * hasil_koleksi_perpus_khusus) * angka_koreksi_uplm2)
        return hitung_jumlah_koleksi
    
    # Input untuk koleksi perpustakaan umum
    st.markdown(":orange[**Perpustakaan Umum**]")
    jumlah_judul_kab = st.number_input("Masukkan jumlah judul koleksi kabupaten:")
    populasi = st.number_input("Jumlah Populasi Kabupaten/Kota :", key="judul_kab")

    jumlah_judul_kec = st.number_input("Masukkan jumlah judul koleksi kecamatan:")
    populasi = st.number_input("Jumlah Populasi Kabupaten/Kota :", key="judul_kec")

    jumlah_judul_desa = st.number_input("Masukkan jumlah judul koleksi desa:")
    populasi = st.number_input("Jumlah Populasi Kabupaten/Kota :", key="judul_desa")


    # Hitung hasil koleksi perpustakaan umum
    hasil_koleksi_kab, hasil_koleksi_kec, hasil_koleksi_desa = koleksi_pu(jumlah_judul_kab, jumlah_judul_kec, jumlah_judul_desa)

    # Menampilkan hasil koleksi perpustakaan umum
    st.write("Hasil Koleksi Kabupaten: {:.6f}".format(hasil_koleksi_kab))
    st.write("Hasil Koleksi Kecamatan: {:.6f}".format(hasil_koleksi_kec))
    st.write("Hasil Koleksi Desa: {:.6f}".format(hasil_koleksi_desa))

    # Hitung total koleksi perpustakaan umum
    total_koleksi_perpus_umum = hasil_koleksi_kab + hasil_koleksi_kec + hasil_koleksi_desa
    st.write("Total Koleksi Perpustakaan Umum: {:.6f}".format(total_koleksi_perpus_umum))

    # Input untuk koleksi sekolah madrasah
    st.markdown(":orange[**Perpustakaan Sekolah**]")
    koleksi_sdmi = st.number_input("Masukkan jumlah koleksi judul SD/MI:")
    koleksi_smp = st.number_input("Masukkan jumlah koleksi judul SMP:")
    koleksi_sma = st.number_input("Masukkan jumlah koleksi judul SMA:")
    jumlah_civitas_sdmi = st.number_input("Masukkan jumlah civitas SD/MI:")
    jumlah_civitas_smp = st.number_input("Masukkan jumlah civitas SMP:")
    jumlah_civitas_sma = st.number_input("Masukkan jumlah civitas SMA:")

    # Hitung hasil koleksi sekolah madrasah
    hasil_koleksi_sdmi, hasil_koleksi_smp, hasil_koleksi_sma = koleksi_skmadrasah(koleksi_sdmi, koleksi_smp, koleksi_sma,
                                                                                jumlah_civitas_sdmi, jumlah_civitas_smp, jumlah_civitas_sma)

    # Menampilkan hasil koleksi sekolah madrasah
    st.write("Hasil Koleksi SD/MI: {:.6f}".format(hasil_koleksi_sdmi))
    st.write("Hasil Koleksi SMP: {:.6f}".format(hasil_koleksi_smp))
    st.write("Hasil Koleksi SMA: {:.6f}".format(hasil_koleksi_sma))

    # Hitung total koleksi sekolah madrasah
    total_koleksi_sekolah_madrasah = hasil_koleksi_sdmi + hasil_koleksi_smp + hasil_koleksi_sma
    st.write("Total Koleksi Sekolah Madrasah: {:.6f}".format(total_koleksi_sekolah_madrasah))

    # Input untuk koleksi perguruan tinggi
    st.markdown(":orange[**Perpustakaan Perguruan Tinggi**]")
    koleksi_perguruan_tinggi = st.number_input("Masukkan jumlah koleksi perpustakaan perguruan tinggi:")
    jumlah_civitas_perguruan_tinggi = st.number_input("Masukkan jumlah civitas perguruan tinggi:")

    # Hitung hasil koleksi perguruan tinggi
    hasil_koleksi_perguruan_tinggi = koleksi_pt(koleksi_perguruan_tinggi, jumlah_civitas_perguruan_tinggi)

    # Menampilkan hasil koleksi perguruan tinggi
    st.write("Hasil Koleksi Perguruan Tinggi: {:.6f}".format(hasil_koleksi_perguruan_tinggi))


    # Input untuk koleksi perpustakaan khusus
    st.markdown(":orange[**Perpustakaan Khusus**]")
    jumlah_koleksi_perpus = st.number_input("Masukkan jumlah koleksi perpustakaan khusus:")
    pegawai = st.number_input("Masukkan jumlah pegawai:")

    angka_koreksi_uplm2 = st.number_input("Masukkan Angka Koreksi : ")

    # Hitung hasil koleksi perpustakaan khusus
    hasil_koleksi_perpus_khusus = koleksi_pk(jumlah_koleksi_perpus, pegawai)

    # Menampilkan hasil koleksi perpustakaan khusus
    st.write("Hasil Koleksi Perpustakaan Khusus: {:.6f}".format(hasil_koleksi_perpus_khusus))

    # Hitung total UPLM2
    hasil_hitung_total_uplm2 = uplm2(total_koleksi_perpus_umum, total_koleksi_sekolah_madrasah, hasil_koleksi_perguruan_tinggi, hasil_koleksi_perpus_khusus)

    # Menampilkan hasil UPLM2
    st.write("Hasil UPLM 2: {:.6f}".format(hasil_hitung_total_uplm2))
    
elif pilihan_uplm == "UPLM 3":
    st.subheader("Perhitungan UPLM 3")
    def tenaga_perpus_umum():
        st.markdown(":orange[**Perpustakaan Umum**]")
        populasi = st.number_input("Masukkan Jumlah Populasi Kabupaten/Kota : ")
        tenaga_kab = st.number_input("Masukkan Jumlah Tenaga Perpustakaan Kabupaten ")
        hitung_tenaga_kab = 0 if tenaga_kab == 0 else tenaga_kab / populasi
        st.write("Jumlah tenaga Kabupaten {:.6f}".format(hitung_tenaga_kab))

        tenaga_kec = st.number_input("Masukkan Jumlah tenaga Perpustakaan Kecamatan ")
        hitung_tenaga_kec = 0 if tenaga_kec == 0 else tenaga_kec / populasi
        st.write("Jumlah tenaga Kecamatan {:.6f}".format(hitung_tenaga_kec))

        tenaga_desa = st.number_input("Masukkan Jumlah tenaga Perpustakaan Desa/ Kelurahan ")
        hitung_tenaga_desa = 0 if tenaga_desa == 0 else tenaga_desa / populasi
        st.write("Jumlah tenaga Desa {:.6f}".format(hitung_tenaga_desa))

        rasio_tenaga_p_umum = hitung_tenaga_kab + hitung_tenaga_kec + hitung_tenaga_desa
        st.write("Jumlah perhitungan ratio tenaga perpustakaan umum :", rasio_tenaga_p_umum)
        return rasio_tenaga_p_umum

    def tenaga_perpus_sekolah():
        st.markdown(":orange[**Perpustakaan Sekolah**]")
        tenaga_sd = st.number_input("Masukkan jumlah tenaga perpustakaan sd/MI:")
        civitas_sd = st.number_input("Masukkan jumlah civitas perpustakaan sd/MI:")
        hitung_tenaga_sd = 0 if civitas_sd == 0 else tenaga_sd / civitas_sd
        st.write("Hasil Perhitungan Tenaga Perpustakaan SD/MI : {:.6f}".format(hitung_tenaga_sd))

        tenaga_smp = st.number_input("Masukkan jumlah tenaga perpustakaan smp:")
        civitas_smp = st.number_input("Masukkan jumlah civitas perpustakaan smp:")
        hitung_tenaga_smp = 0 if civitas_smp == 0 else tenaga_smp / civitas_smp
        st.write("Hasil Perhitungan Tenaga Perpustakaan SD/MI : {:.6f}".format(hitung_tenaga_smp))

        tenaga_sma = st.number_input("Masukkan jumlah tenaga perpustakaan SMA:")
        civitas_sma = st.number_input("Masukkan jumlah civitas perpustakaan SMA:")
        hitung_tenaga_sma = 0 if civitas_sma == 0 else tenaga_sma / civitas_sma
        st.write("Hasil Perhitungan Tenaga Perpustakaan SD/MI : {:.6f}".format(hitung_tenaga_sma))


        rasio_tenaga_p_sekolah = hitung_tenaga_sd + hitung_tenaga_smp + hitung_tenaga_sma
        return rasio_tenaga_p_sekolah


    def tenaga_perpus_PT():
        st.markdown(":orange[**Perpustakaan Perguruan Tinggi**]")
        tenaga_pt = st.number_input("Masukkan jumlah tenaga perpustakaan PT : ")
        civitas_pt = st.number_input("Masukkan jumlah civitas PT : ")

        if civitas_pt != 0:
            perhitungan_pt = tenaga_pt / civitas_pt
            st.write("Jumlah perhitungan ratio tenaga perguruan tinggi :", perhitungan_pt)

        else:
            st.write("Error: Division by zero. Masukkan nilai civitas PT yang tidak nol.")
            perhitungan_pt = 0

        return perhitungan_pt


    def tenaga_perpus_khusus():
        try:
            st.markdown(":orange[**Perpustakaan Khusus**]")
            tenaga_khusus = st.number_input("Masukkan jumlah tenaga perpustakaan khusus : ")
            civitas_khusus = st.number_input("Masukkan jumlah pegawai perpustakaan khusus : ")
            perhitungan_khusus = tenaga_khusus / civitas_khusus
            st.write("Jumlah perhitungan ratio tenaga perguruan khusus :", perhitungan_khusus)
            return perhitungan_khusus
        except ZeroDivisionError:
            st.write("Error: Division by zero. Masukkan nilai pegawai perpustakaan khusus yang tidak nol.")
            return 0

    angka_koreksi_uplm3 = st.number_input("Masukkan Angka Koreksi : ")

    total_tenaga_perpustakaan_umum = tenaga_perpus_umum()
    total_tenaga_perpustakaan_sekolah = tenaga_perpus_sekolah()
    total_tenaga_perpustakaan_pt = tenaga_perpus_PT()
    total_tenaga_perpustakaan_khusus = tenaga_perpus_khusus()

    uplm3 = ((0.5 * total_tenaga_perpustakaan_umum) + (0.2 * total_tenaga_perpustakaan_sekolah) + (0.2 * total_tenaga_perpustakaan_pt) + (0.1 * total_tenaga_perpustakaan_khusus)) * angka_koreksi_uplm3

    st.subheader("Hasil Perhitungan:")
    # st.write("Jumlah perhitungan perpustakaan umum :", total_tenaga_perpustakaan_umum)
    # st.write("Jumlah perhitungan perpustakaan sekolah/madrasah :", total_tenaga_perpustakaan_sekolah)
    # st.write("Jumlah perhitungan perguruan tinggi :", total_tenaga_perpustakaan_pt)
    # st.write("Jumlah perhitungan perpustakaan khusus :", total_tenaga_perpustakaan_khusus)
    st.write("Nilai UPLM3 adalah : ", uplm3)


elif pilihan_uplm == "UPLM 4":
    st.subheader("Perhitungan UPLM 4")
    def kunjungan_perpus_umum():
        st.markdown(":green[**Perpustakaan Umum**]")
        populasi_kun = st.number_input("Jumlah Populasi Kabupaten/Kota")

    if populasi_kun != 0:
        # Pengguna memasukkan kunjungan per hari untuk setiap level perpustakaan
        kunj_kab = st.number_input("Jumlah kunjungan per hari Perpustakaan Kabupaten : ")
        kunj_kec = st.number_input("Jumlah kunjungan per hari Perpustakaan Kecamatan : ")
        kunj_ds = st.number_input("Jumlah kunjungan per hari Perpustakaan Desa/Kelurahan : ")

        # Melakukan perhitungan hanya jika populasi tidak sama dengan nol
        perhitungan_kb_u = kunj_kab / populasi_kun
        perhitungan_kc_u = kunj_kec / populasi_kun
        perhitungan_ds_u = kunj_ds / populasi_kun

        # Menghitung total kunjungan untuk perpustakaan umum
        kunj_umum = perhitungan_kb_u + perhitungan_kc_u + perhitungan_ds_u

        # Menampilkan hasil
        st.write("Hasil Perhitungan Kunjungan Kab : {:.6f}".format(perhitungan_kb_u))
        st.write("Hasil Perhitungan Kunjungan Kec : {:.6f}".format(perhitungan_kc_u))
        st.write("Hasil Perhitungan Kunjungan Desa : {:.6f}".format(perhitungan_ds_u))
        st.write("Ratio Perpustakaan Umum : {:.6f}".format(kunj_umum))

        # Mengembalikan nilai kunjungan umum
        return kunj_umum
    else:
        # Jika populasi adalah nol, tidak ada perhitungan yang dapat dilakukan
        st.write("Populasi Kabupaten/Kota tidak boleh nol")
        return 0
        
    def kunjungan_perpus_sekolah():
        st.markdown(":green[**Perpustakaan Sekolah**]")
        kunj_sd = st.number_input("Jumlah kunjungan per hari Perpustakaan SD/MI : ")
        civitas_sd = st.number_input("Masukkan civitas SD/MI : ")
        hitungan_sd = kunj_sd / (civitas_sd if civitas_sd != 0 else 1)  # Menangani pembagian oleh nol
        st.write("Hasil Perhitungan Kunjungan SD/MI : {:.6f}".format(hitungan_sd))

        kunj_smp = st.number_input("Jumlah kunjungan per hari Perpustakaan SMP : ")
        civitas_smp = st.number_input("Masukkan civitas SMP : ")
        hitungan_smp = kunj_smp / (civitas_smp if civitas_smp != 0 else 1)
        st.write("Hasil Perhitungan Kunjungan SMP: {:.6f}".format(hitungan_smp))

        kunj_sma = st.number_input("Jumlah kunjungan per hari Perpustakaan SMA : ")
        civitas_sma = st.number_input("Masukkan civitas SMA : ")
        hitungan_sma = kunj_sma / (civitas_sma if civitas_sma != 0 else 1)
        st.write("Hasil Perhitungan Kunjungan SMA : {:.6f}".format(hitungan_sma))

        kunj_skl = hitungan_sd + hitungan_smp + hitungan_sma
        st.write("Ratio Kunjungan Perpustakaan Sekolah : {:.6f}".format(kunj_skl))
        return kunj_skl
    
    def kunjungan_perpus_pt(): 
        st.markdown(":green[**Perpustakaan Perguruan Tinggi**]")
        kunjungan_pt = st.number_input("Masukkan jumlah tenaga perpustakaan PT : ")
        civitas_pt = st.number_input("Masukkan jumlah civitas PT : ")

        if civitas_pt != 0:
            perhitungan_pt = kunjungan_pt / civitas_pt
            st.write("Ratio Perhitungan Kunjungan PT : {:.6f}".format(perhitungan_pt))

        else:
            st.write("Error: Division by zero. Masukkan nilai civitas PT yang tidak nol.")
            perhitungan_pt = 0

        return perhitungan_pt 

    def kunjungan_perpus_khusus():
        st.markdown(":green[**Perpustakaan Khusus**]")
        kunjungan_khusus = st.number_input("Masukkan jumlah Kunjungan perpustakaan Khusus : ")
        pegawai_khusus = st.number_input("Masukkan jumlah Pegawai perpustakaan khusus : ")

        if pegawai_khusus != 0:
            perhitungan_khusus = kunjungan_khusus / pegawai_khusus
            st.write("Ratio Perhitungan Kunjungan Khusus : {:.6f}".format(perhitungan_khusus))
        else:
            st.write("Error: Division by zero. Masukkan nilai civitas PT yang tidak nol.")
            perhitungan_khusus = 0

        return perhitungan_khusus

    angka_koreksi_uplm4 = st.number_input("Masukkan Angka Koreksi : ")
    # ... Fungsi-fungsi lainnya ...

    total_kunjungan_perpustakaan_umum = kunjungan_perpus_umum()
    total_kunjungan_perpustakaan_sekolah = kunjungan_perpus_sekolah()
    total_kunjungan_perpustakaan_pt = kunjungan_perpus_pt()
    total_kunjungan_perpustakaan_khusus = kunjungan_perpus_khusus()

    uplm4 = (((0.5 * total_kunjungan_perpustakaan_umum) + (0.2 * total_kunjungan_perpustakaan_sekolah) + (0.2 * total_kunjungan_perpustakaan_pt) + (0.1 * total_kunjungan_perpustakaan_khusus)) * angka_koreksi_uplm4)
    st.write("Hasil UPLM4 : {:.6f}".format(uplm4))

elif pilihan_uplm == "UPLM 5":
    st.subheader("Perhitungan UPLM 5")
# UNTUK PERPUSTAKAAN UMUM
    st.markdown(":violet[**Perpustakaan Umum**]")
    jml_unit_perp_kabkota_standar = st.number_input("Jumlah perpustakaan kabupaten sesuai standar", )
    jml_unit_perp_kabkota = st.number_input("Jumlah unit perpustakaan kabupaten", )
    jml_unit_perp_kec_standar = st.number_input("Jumlah perpustakaan kecamatan sesuai standar", )
    jml_unit_perp_kec = st.number_input("Jumlah unit perpustakaan kecamatan", )
    jml_unit_perp_desa_standar = st.number_input("Jumlah perpustakaan desa sesuai standar", )
    jml_unit_perp_desa = st.number_input("Jumlah unit perpustakaan desa", )

    # UNTUK PERPUSTAKAAN SEKOLAH
    st.markdown(":violet[**Perpustakaan Sekolah**]")
    jml_unit_perp_sdMi_standar = st.number_input("Jumlah perpustakaan SD/MI sesuai standar", )
    jml_unit_perp_sdMi = st.number_input("Jumlah unit perpustakaan SD/MI", )
    jml_unit_perp_smpMts_standar = st.number_input("Jumlah perpustakaan SMP/MTS sesuai standar", )
    jml_unit_perp_smpMts = st.number_input("Jumlah unit perpustakaan SMP/MTS", )
    jml_unit_perp_smaMa_standar = st.number_input("Jumlah perpustakaan SMA/MA sesuai standar", )
    jml_unit_perp_smaMa = st.number_input("Jumlah unit perpustakaan SMA/MA", )

    # UNTUK PERPUSTAKAAN PERGURUAN TINGGI
    st.markdown(":violet[**Perpustakaan Perguruan Tinggi**]")
    jml_unit_perp_perguruan_standar = st.number_input("Jumlah tenaga perpustakaan perguruan standar", )
    jml_unit_perp_perguruan = st.number_input("Jumlah unit perpustakaan perguruan tinggi", )

    # UNTUK PERPUSTAKAAN KHUSUS
    st.markdown(":violet[**Perpustakaan Khusus**]")
    jml_unit_perp_khusus_standar = st.number_input("Jumlah tenaga perpustakaan khusus standar", )
    jml_unit_perp_khusus = st.number_input("Jumlah unit perpustakaan khusus", )

    angka_koreksi_uplm5 = st.number_input("Masukkan Angka Koreksi : ")

    # Hapus tombol submit
    # submitted = st.form_submit_button("Submit")

    # Hapus bagian ini dan masukkan langsung ke bagian akhir script
    # if submitted:
    def perpustakaan_umum5():
        hitung_kabkota5 = jml_unit_perp_kabkota_standar / jml_unit_perp_kabkota if jml_unit_perp_kabkota != 0    else 0
        (st.write("Hasil perhitungan tenaga perpustakaan Kab/Kota : {:.6f}".format(hitung_kabkota5)))
        hitung_kec5 = jml_unit_perp_kec_standar / jml_unit_perp_kec if jml_unit_perp_kec != 0 else 0
        (st.write("Hasil perhitungan tenaga perpustakaan Kec : {:.6f}".format(hitung_kec5)))
        hitung_desa5 = jml_unit_perp_desa_standar / jml_unit_perp_desa if jml_unit_perp_desa != 0 else 0
        (st.write("Hasil perhitungan tenaga perpustakaan Desa : {:.6f}".format(hitung_desa5)))
        total1 = (hitung_kabkota5 + hitung_kec5 + hitung_desa5)
        return total1

    def perpustakaan_sekolah5():
        hitung_sd5 = jml_unit_perp_sdMi_standar / jml_unit_perp_sdMi if jml_unit_perp_sdMi != 0 else 0
        (st.write("Hasil perhitungan tenaga perpustakaan SD/MI : {:.6f}".format(hitung_sd5)))
        hitung_smp5 = jml_unit_perp_smpMts_standar / jml_unit_perp_smpMts if jml_unit_perp_smpMts != 0 else 0
        (st.write("Hasil perhitungan tenaga perpustakaan SMP : {:.6f}".format(hitung_smp5)))
        hitung_sma5 = jml_unit_perp_smaMa_standar / jml_unit_perp_smaMa if jml_unit_perp_smaMa != 0 else 0
        (st.write("Hasil perhitungan tenaga perpustakaan SMA : {:.6f}".format(hitung_sma5)))
        total2 = (hitung_sd5 + hitung_smp5 + hitung_sma5)
        return total2

    def perpustakaan_perguruan5():
        hitung_perguruan5 = jml_unit_perp_perguruan_standar / jml_unit_perp_perguruan if jml_unit_perp_perguruan != 0 else 0
        return hitung_perguruan5

    def perpustakaan_khusus5():
        hitung_khusus5 = jml_unit_perp_khusus_standar / jml_unit_perp_khusus if jml_unit_perp_khusus != 0 else 0
        return hitung_khusus5

    total_perpustakaan_umum5 = perpustakaan_umum5()
    total_perpustakaan_sekolah5 = perpustakaan_sekolah5()
    total_perpustakaan_perguruan5 = perpustakaan_perguruan5()
    total_perpustakaan_khusus5 = perpustakaan_khusus5()
    angka_koreksi = 2.5

    hasil_uplm5 = (((0.5 * total_perpustakaan_umum5) + (0.2 * total_perpustakaan_sekolah5) +
                    (0.2 * total_perpustakaan_perguruan5) + (0.1 * total_perpustakaan_khusus5)) * angka_koreksi_uplm5)

    st.write("Jumlah ratio ketercukupan koleksi untuk perpustakaan umum adalah : ", total_perpustakaan_umum5)
    st.write("Jumlah ratio ketercukupan koleksi untuk perpustakaan sekolah/madrasah adalah : ", total_perpustakaan_sekolah5)
    st.write("Jumlah ratio perguruan tinggi", total_perpustakaan_perguruan5)
    st.write("Jumlah ratio perpustakaan khusus : ", total_perpustakaan_khusus5)
    st.write("Nilai UPLM5 adalah : ", hasil_uplm5)

elif pilihan_uplm == "UPLM 6":
    st.subheader("Perhitungan UPLM 6")
    populasi_kabkot = st.number_input("Jumlah populasi kabupaten :", )
    
    # UNTUK PERPUSTAKAAN UMUM
    st.markdown(":orange[**Perpustakaan Umum**]")
    jumlah_sosialisasi_kabkota = st.number_input("Jumlah keterlibatan masyarakat sosialisasi perpustakaan kabupaten:", )
    jumlah_sosialisasi_kec = st.number_input("Jumlah keterlibatan masyarakat sosialisasi perpustakaan kecamatan:", )
    jumlah_sosialisasi_desa = st.number_input("Jumlah keterlibatan masyarakat sosialisasi perpustakaan desa:", )

    # UNTUK PERPUSTAKAAN SEKOLAH
    st.markdown(":orange[**Perpustakaan Sekolah**]")
    jumlah_civitas_sosialisasi_sdMi = st.number_input("Jumlah civitas keterlibatan sekolah perpustakaan SD/MI:", )
    jumlah_civitas_sosialisasi_smp = st.number_input("Jumlah civitas keterlibatan sekolah perpustakaan SMP/MTS:", )
    jumlah_civitas_sosialisasi_sma = st.number_input("Jumlah civitas keterlibatan sekolah perpustakaan SMA/MA:", )
    civ_sd = st.number_input("Jumlah populasi kabupaten :", key="input" )
    civ_smp = st.number_input("Jumlah populasi kabupaten :", key="input1")
    civ_sma = st.number_input("Jumlah populasi kabupaten :",key="input2" )
    
    # UNTUK PERPUSTAKAAN PERGURUAN TINGGI
    st.markdown(":orange[**Perpustakaan Perguruan Tinggi**]")
    jumlah_civitas_sosialisasi_peguruan = st.number_input("Jumlah civitas keterlibatan perpustakaan perguruan tinggi:", )
    civ_PT = st.number_input("Jumlah civ PT :", )
    # UNTUK PERPUSTAKAAN KHUSUS
    st.markdown(":orange[**Perpustakaan Khusus**]")
    jumlah_civitas_sosialisasi_khusus = st.number_input("Jumlah civitas keterlibatan perpustakaan khusus:", )
    penduduk_bekerja = st.number_input("Penduduk bekerja :", )
    angka_koreksi_uplm6 = st.number_input("Masukkan Angka Koreksi : ")

    def perpustakaan_umum6():
        hitung_kabkota6 = jumlah_sosialisasi_kabkota / populasi_kabkot if populasi_kabkot != 0 else 0
        st.write("Hasil Perhitungan sosialisasi kab/kota : {:.6f}".format(hitung_kabkota6))
        hitung_kec6 = jumlah_sosialisasi_kec / populasi_kabkot if populasi_kabkot != 0 else 0
        st.write("Hasil Perhitungan sosialisasi kec : {:.6f}".format(hitung_kec6))
        hitung_desa6 = jumlah_sosialisasi_desa / populasi_kabkot if populasi_kabkot != 0 else 0
        st.write("Hasil Perhitungan sosialisasi desa : {:.6f}".format(hitung_desa6))
        total1 = (hitung_kabkota6 + hitung_kec6 + hitung_desa6)
        return total1

    def perpustakaan_sekolah6():
        hitung_sd6 = jumlah_civitas_sosialisasi_sdMi / civ_sd if civ_sd != 0 else 0
        st.write("Hasil Perhitungan SD/MI : {:.6f}".format(hitung_sd6))
        hitung_smp6 = jumlah_civitas_sosialisasi_smp / civ_smp if civ_smp != 0 else 0
        st.write("Hasil Perhitungan SMP : {:.6f}".format(hitung_smp6))
        hitung_sma6 = jumlah_civitas_sosialisasi_sma / civ_sma if civ_sma != 0 else 0
        st.write("Hasil Perhitungan SMA : {:.6f}".format(hitung_sma6))


        total2 = (hitung_sd6 + hitung_smp6 + hitung_sma6)
        return total2

    def perpustakaan_perguruan6():
        hitung_perguruan6 = jumlah_civitas_sosialisasi_peguruan / civ_PT if civ_PT != 0 else 0
        return hitung_perguruan6

    def perpustakaan_khusus6():
        hitung_khusus6 = jumlah_civitas_sosialisasi_khusus / penduduk_bekerja if penduduk_bekerja != 0 else 0
        return hitung_khusus6

    total_perpustakaan_umum6 = perpustakaan_umum6()
    total_perpustakaan_sekolah6 = perpustakaan_sekolah6()
    total_perpustakaan_perguruan6 = perpustakaan_perguruan6()
    total_perpustakaan_khusus6 = perpustakaan_khusus6()
    angka_koreksi = 2.5

    uplm6 = (((0.5 * total_perpustakaan_umum6) + (0.2 * total_perpustakaan_sekolah6) +
            (0.2 * total_perpustakaan_perguruan6) + (0.1 * total_perpustakaan_khusus6)) * angka_koreksi_uplm6)

    st.write("Jumlah ratio ketercukupan koleksi untuk perpustakaan umum :", total_perpustakaan_umum6)
    st.write("Jumlah ratio ketercukupan koleksi untuk perpustakaan sekolah/madrasah :", total_perpustakaan_sekolah6)
    st.write("Jumlah ratio perguruan tinggi : ", total_perpustakaan_perguruan6)
    st.write("Jumlah ratio perpustakaan khusus :", total_perpustakaan_khusus6)
    st.write("Nilai UPLM6 adalah :", uplm6)

elif pilihan_uplm == "UPLM 7":
    st.subheader("Perhitungan UPLM 7")
    st.markdown(":blue[**Perpustakaan Umum**]")
    populasi_kabkot = st.number_input("Masukkan jumlah populasi kabupaten/kota:", )
    anggota_kab = st.number_input("Masukkan jumlah anggota perpustakaan kabupaten/kota:", )
    anggota_kec = st.number_input("Masukkan jumlah anggota perpustakaan kecamatan:", )
    anggota_ds = st.number_input("Masukkan jumlah anggota perpustakaan desa:", )
    # perpustakaan sekolah
    st.markdown(":blue[**Perpustakaan Sekolah**]")
    anggota_sd = st.number_input("Masukkan jumlah anggota perpustakaan SD:", )
    civ_sd = st.number_input("Masukkan jumlah civitas SD:", )
    anggota_smp = st.number_input("Masukkan jumlah anggota perpustakaan SMP:", )
    civ_smp = st.number_input("Masukkan jumlah civitas SMP:", )
    anggota_sma = st.number_input("Masukkan jumlah anggota perpustakaan SMA:", )
    civ_sma = st.number_input("Masukkan jumlah civitas SMA:", )
    st.markdown(":blue[**Perpustakaan Perguruan Tinggi**]")
    anggota_pt = st.number_input("Masukkan jumlah anggota perpustakaan PT:", )
    civ_PT = st.number_input("Masukkan jumlah civitas PT:", )
    st.markdown(":blue[**Perpustakaan Khusus**]")
    anggota_k = st.number_input("Masukkan jumlah anggota perpustakaan khusus:", )
    peg_k = st.number_input("Masukkan jumlah pegawai/karyawan:", )

    # Menangani division by zero
    
    angka_koreksi_uplm7 = st.number_input("Masukkan Angka Koreksi : ")

    # Fungsi-fungsi perhitungan
    def anggota_per_u():
        hitung_anggota_kb = anggota_kab / populasi_kabkot if populasi_kabkot != 0 else 0
        st.write("Hasil perhitungan perpustakaan kab/kota :", hitung_anggota_kb)
        hitung_anggota_kec = anggota_kec / populasi_kabkot if populasi_kabkot != 0 else 0
        st.write("Hasil perhitungan perpustakaan kec :", hitung_anggota_kec)
        hitung_anggota_ds = anggota_ds / populasi_kabkot if populasi_kabkot != 0 else 0
        st.write("Hasil perhitungan perpustakaan desa :", hitung_anggota_ds)

        ang_perpustakaan_umum = (hitung_anggota_kb + hitung_anggota_kec + hitung_anggota_ds)
        st.write("Jumlah ratio anggota perpustakaan umum :", ang_perpustakaan_umum)
        return ang_perpustakaan_umum

    def anggota_per_sk():
        hitung_anggota_sd = anggota_sd / civ_sd if civ_sd != 0 else 0
        st.write("Hasil perhitungan anggota perpustakaan SD/MI :", hitung_anggota_sd)
        hitung_anggota_smp = anggota_smp / civ_smp if civ_smp != 0 else 0
        st.write("Hasil perhitungan anggota perpustakaan SMP :", hitung_anggota_smp)
        hitung_anggota_sma = anggota_sma / civ_sma if civ_sma != 0 else 0
        st.write("Hasil perhitungan anggota perpustakaan SMA :", hitung_anggota_sma)
        ang_perpustakaan_sk = (hitung_anggota_sd + hitung_anggota_smp + hitung_anggota_sma)
        st.write("Jumlah ratio anggota perpustakaan sekolah :", ang_perpustakaan_sk)
        return ang_perpustakaan_sk

    def anggota_per_pt():
        hitung_anggota_pt = anggota_pt / civ_PT if civ_PT != 0 else 0
        st.write("Hasil Perhitungan Anggota Perpustakaan Perguruan Tinggi :", hitung_anggota_pt)
        return hitung_anggota_pt

    def anggota_per_k():
        hitung_anggota_k = anggota_k / peg_k if peg_k != 0 else 0
        st.write("Hasil Perhitungan Anggota Perpustakaan Khusus :", hitung_anggota_k)
        return hitung_anggota_k

    # Menghitung total
    total_umum = anggota_per_u()
    total_skl = anggota_per_sk()
    total_pt = anggota_per_pt()
    total_k = anggota_per_k()

    # Menghitung hasil UPLM7
    hasil_uplm7 = (((0.5 * total_umum) + (0.2 * total_skl) + (0.2 * total_pt) + (0.1 * total_k)) * angka_koreksi_uplm7)

    # Menampilkan hasil
    # st.write("Jumlah ratio anggota perpustakaan umum :", total_umum)
    # st.write("Jumlah ratio anggota perpustakaan sekolah :", total_skl)
    # st.write("Jumlah ratio anggota perpustakaan PT :", total_pt)
    # st.write("Jumlah ratio anggota perpustakaan khusus :", total_k)
    st.write("Nilai UPLM7 adalah:", hasil_uplm7)

elif pilihan_uplm == "IPLM":
    st.subheader(':green[Perhitungan IPLM]')
    hasil_baru_uplm1 =  st.number_input("Masukkan Jumlah hasil UPLM 1:", 0.0, 100000000.0, step=0.00001, format="%.5f")
    hasil_baru_uplm2 =  st.number_input("Masukkan Jumlah hasil UPLM 2:", 0.0, 100000000.0, step=0.00001, format="%.5f" )
    hasil_baru_uplm3 =  st.number_input("Masukkan Jumlah hasil UPLM 3:", 0.0, 100000000.0, step=0.00001, format="%.5f" )
    hasil_baru_uplm4 =  st.number_input("Masukkan Jumlah hasil UPLM 4:", 0.0, 100000000.0, step=0.00001, format="%.5f" )
    hasil_baru_uplm5 =  st.number_input("Masukkan Jumlah hasil UPLM 5:", 0.0, 100000000.0, step=0.00001, format="%.5f" )
    hasil_baru_uplm6 =  st.number_input("Masukkan Jumlah hasil UPLM 6:", 0.0, 100000000.0, step=0.00001, format="%.5f" )
    hasil_baru_uplm7 =  st.number_input("Masukkan Jumlah hasil UPLM 7:", 0.0, 100000000.0, step=0.00001, format="%.5f" )

    def iplm_total():
        hitung_iplm = (((hasil_baru_uplm1+hasil_baru_uplm2+hasil_baru_uplm3+hasil_baru_uplm4+hasil_baru_uplm5+hasil_baru_uplm6+hasil_baru_uplm7)/7) * 100)
        return hitung_iplm
    
    hasil_iplm = iplm_total()  
    st.write("Hasil IPLM adalah : ",  hasil_iplm)
