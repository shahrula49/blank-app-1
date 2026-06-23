import streamlit as st

st.set_page_config(page_title="Mesin Affiliate TikTok Shop", page_icon="🛍️", layout="centered")

st.title("🛍️ TikTok Shop Auto Prompt Generator")
st.write("Isi maklumat produk di bawah. Semua kandungan promosi akan dijana secara automatik!")

# --- SEKSYEN INPUT ---
st.subheader("📋 Maklumat Input Produk")

model = st.selectbox("Pilih Model", ["Malaysian Female Model", "Malaysian Male Model", "Malaysian Girl Model", "Malaysian Boy Model"])
jenis_pakaian = st.selectbox("Jenis Pakaian", ["Blouse", "Baju Kurung", "Jubah", "Abaya", "Dress", "T-Shirt", "Kaftan", "Tudung Sarung"])
lokasi = st.selectbox("Lokasi", ["Modern Living Room", "Cozy Modern Bedroom", "Minimalist Studio", "Luxury Hotel Room", "Premium Boutique", "Cafe Environment"])
style = st.selectbox("Gaya / Style", ["TikTok Shop Affiliate", "Premium Fashion Catalogue", "Lifestyle Casual", "Luxury Brand", "Korean Style"])
pose = st.selectbox("Pose / Action", ["Natural standing pose", "Walking slowly", "Turn left and right", "Smile naturally", "Relaxed casual pose"])
shot = st.selectbox("Jenis Shot", ["Full body shot", "Medium shot", "Close-up fabric details", "Front view", "Side view"])

nama_produk = st.text_input("Nama Produk / Brand", value="OMCORE-MESH LAYER YOGA TOP")
warna = st.text_input("Warna / Corak", value="merah")
material = st.selectbox("Material", ["Soft cotton", "Premium rayon", "Chiffon", "Satin silk", "Linen", "Jersey cotton"])
kelebihan = st.text_input("Kelebihan Utama", value="Mudah renggang")
promo = st.selectbox("Jenis Promosi", ["Best Seller", "Free Shipping", "Voucher Discount", "Limited Stock", "Flash Sale"])
target_customer = st.text_input("Target Customer", value="wanita yang mahukan pakaian selesa dan cantik")
aspect_ratio = st.selectbox("Nisbah Saiz (Aspect Ratio)", ["9:16 (TikTok / Reel Video)", "1:1 (Instagram / TikTok Feed)", "4:5 (Potret Premium)", "16:9 (Skrin Lebar)"])

# --- PROSES LOGIK GABUNGAN TEXT & AR ---
ar_code = "--ar 9:16"
ar_video = "aspect ratio 9:16"
if "1:1" in aspect_ratio:
    ar_code = "--ar 1:1"
    ar_video = "aspect ratio 1:1"
elif "4:5" in aspect_ratio:
    ar_code = "--ar 4:5"
    ar_video = "aspect ratio 4:5"
elif "16:9" in aspect_ratio:
    ar_code = "--ar 16:9"
    ar_video = "aspect ratio 16:9"

jantina_suara = "Suara lelaki Melayu Malaysia"
if "Female" in model or "Girl" in model or "Kaftan" in jenis_pakaian or "Tudung" in jenis_pakaian:
    jantina_suara = "Suara wanita Melayu Malaysia"

# --- JANA OUTPUT ---
st.markdown("---")
st.subheader("🚀 Hasil Kandungan (Tinggal Copy)")

# 1. Prompt Gambar
prompt_gambar = f"[Copy prompt BI ini untuk AI Image] PHOTO PROMPT: Ultra realistic {model} wearing {material} {jenis_pakaian} {nama_produk} in {warna} color, located at {lokasi}. {style} style with {shot}, subject performing {pose}. Premium fabric texture, visible stitching, soft natural lighting, fashion magazine photography quality, highly detailed {ar_code}"
st.text_area("📸 AUTO PROMPT GAMBAR REALISTIC", value=prompt_gambar, height=120)

# 2. Prompt Video
prompt_video = f"[Copy prompt BI ini untuk AI Video] VIDEO PROMPT: Ultra realistic video of {model} wearing {material} {jenis_pakaian} {nama_produk} in {warna} color, at {lokasi}. Video style {style}. Camera movement {shot} focusing on subject doing {pose}. Natural fabric simulation moving with gravity, high-end commercial look, soft cinematic lighting, no AI distortion, 4K, 60fps, {ar_video}"
st.text_area("🎥 AUTO PROMPT VIDEO", value=prompt_video, height=120)

# 3. Prompt Voice
prompt_voice = f"[Gaya Suara: {jantina_suara}, nada santai, mesra, ceria dan memberikan cadangan ikhlas. Sila baca skrip di bawah dengan intonasi semula jadi, ada jeda pada tanda koma dan titik.] SKRIP: Bagi yang sedang mencari {jenis_pakaian} jenis {nama_produk} untuk keselesaan harian, boleh tengok pilihan ini. Material {material} yang digunakan terasa sejuk dan selesa sewaktu digayakan. Sesuai sangat untuk {target_customer}. Anda boleh semak butiran lanjut dan dapatkan warna kegemaran anda melalui beg kuning yang disediakan."
st.text_area("🎙️ PROMT VOICE (SKRIP BM)", value=prompt_voice, height=130)

# 4. Hooks
hook1 = f"STOP SCROLL! {jenis_pakaian} {nama_produk} ni nampak premium, selesa dan memang sesuai untuk anda 😍"
hook2 = f"Kalau anda cari {jenis_pakaian} {nama_produk} yang selesa, yang ini memang patut masuk cart sekarang!"
hook3 = f"Jangan scroll dulu — tengok detail {jenis_pakaian} {nama_produk} ni, cutting dia nampak kemas dan cantik dipakai!"

st.text_input("🎯 HOOK 1", value=hook1)
st.text_input("🎯 HOOK 2", value=hook2)
st.text_input("🎯 HOOK 3", value=hook3)

# 5. CTA & Description
cta1 = f"Klik butang kuning sekarang dan dapatkan {jenis_pakaian} {nama_produk} ini sebelum stok habis!"
cta2 = f"Add to cart sekarang. Gunakan promo {promo} sementara masih available!"
description = f"✨ {jenis_pakaian} {nama_produk} dengan material {material}, warna/corak {warna} dan kelebihan utama: {kelebihan}. Sesuai untuk {target_customer}. Rekaan selesa, kemas dan mudah digayakan untuk kegunaan harian atau acara santai. Beli terus di TikTok Shop dan nikmati promo {promo}."
hashtag = f"#{jenis_pakaian.replace(' ', '')} #{nama_produk.replace(' ', '').replace('-', '')} #TikTokShop #OOTD #FashionMalaysia"

st.text_input("🛒 CTA 1", value=cta1)
st.text_input("🛒 CTA 2", value=cta2)
st.text_area("📝 AUTO DESCRIPTION", value=description, height=100)
st.text_input("🏷️ 5 HASHTAG BERKAITAN", value=hashtag)

# 6. Caption Complete
caption_complete = f"{hook1}\n\n{description}\n\n{cta1}\n\n{hashtag}"
st.text_area("📱 CAPTION COMPLETE TIKTOK SHOP (SIAP GUNA)", value=caption_complete, height=180)