
🛡️ Capi Key Bot - Lisans Yönetim Sistemi  
https://github.com/byblackcapi/Key-bot  

📌 Proje: Gelişmiş kullanıcıya özel lisans anahtarı doğrulama sistemi  
👨‍💻 Geliştirici: Capi — Telegram: @capiyedek | Destek: @capiyedek_support  

────────────────────────────────────────────

🔰 Özellikler
- 🔐 Anahtar tabanlı lisanslama sistemi  
- 👤 Key sadece belirli kullanıcı tarafından kullanılabilir  
- 🚫 Başkası kullanırsa hem kullanan hem de key sahibi banlanır  
- ♾️ Süresiz veya saniye bazlı lisans tanımı  
- 👑 Sudo paneli ile tam yetkili yönetim  
- 📜 JSON tabanlı veri yönetimi  
- 💾 Ekstra veritabanı veya hosting gerektirmez  

────────────────────────────────────────────

🚀 Kurulum
1. Bu repoyu klonla  
```bash
git clone https://github.com/byblackcapi/Key-bot
cd Key-bot
```

2. Gerekli kütüphaneleri yükle  
```bash
pip install pyrogram tgcrypto
```

3. `BOT_TOKEN`, `API_ID`, `API_HASH` bilgilerini `.py` dosyasına gir

4. Çalıştır  
```bash
python bot.py
```

────────────────────────────────────────────

📦 Komutlar

📥 Kullanıcı Komutları:
- `/kstart` – Başlangıç mesajı ve bilgilendirme  
- `/help` – Komut listesini göster  
- `/status` – Lisans süresini göster  
- `/test` – Lisansın aktif olup olmadığını kontrol et  

👑 Sudo Paneli (Yetkili Kullanıcılar):
- `/addkey <key> <süre> <kullanıcı_id>` – Yeni key oluştur  
- `/delkey <key>` – Mevcut key sil  
- `/keys` – Key listesini göster  
- `/ban <kullanıcı_id>` – Kullanıcıyı banla  
- `/unban <kullanıcı_id>` – Ban kaldır  
- `/addsudo <id>` – Yeni sudo kullanıcı ekle  
- `/delsudo <id>` – Sudo kullanıcı sil  
- `/sudolist` – Sudo kullanıcıları listele  
- `/resetkeys` – Kullanılmamış keyleri temizle  
- `/exportauth` – Aktif lisanslı kullanıcıları göster  
- `/banlist` – Banlı kullanıcıları göster  

────────────────────────────────────────────

📌 Lisans Sistemi Nasıl Çalışır?
1. Key sudo kullanıcı tarafından `/addkey` ile oluşturulur  
2. Kullanıcı key’i bota yazar  
3. Eğer key doğruysa, süresi başlar  
4. Başkası kullanırsa → ❌ Ban!  

📝 Süre bilgisi:
- `unlimited` → ♾️ Süresiz  
- `120` → 120 saniyelik geçici lisans  

────────────────────────────────────────────

🧩 Kullanılan Teknolojiler
[![GitHub](https://img.shields.io/badge/GitHub-100000?style=flat-square&logo=github&logoColor=white)](https://github.com/byblackcapi/Key-bot)
[![Python](https://img.shields.io/badge/Python-3670A0?style=flat-square&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=flat-square&logo=telegram&logoColor=white)](https://t.me/capiyedek)

────────────────────────────────────────────

📄 Lisans
Bu proje tamamen açık kaynak olup, Capi tarafından MIT lisansı ile yayınlanmaktadır.  
Dilerseniz çatallayıp geliştirebilir veya botu kendi sisteminize entegre edebilirsiniz.







