import time
import json
from pyrogram import Client, filters
from pyrogram.types import Message

API_ID = 23350184
API_HASH = "41f0c2a157268e158f91ab7d59f4fc19"
BOT_TOKEN = "buraya token gircen aq"

app = Client("CapiBot", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

AUTH_FILE = "auth.json"
SUDO_FILE = "sudo.json"
LICENSE_KEYS = {}
USED_KEYS = set()
BANNED_USERS = set()

try:
    with open(SUDO_FILE) as f:
        SUDO_USERS = set(int(uid) for uid in json.load(f).keys())
except:
    SUDO_USERS = set()

# Varsayılan sudo kullanıcı ID'si ekle
SUDO_USERS.add(buraya id ni gir aq)
save_json = lambda path, data: open(path, "w").write(json.dumps(data, indent=2))
save_json(SUDO_FILE, {str(u): True for u in SUDO_USERS})


def load_json(path):
    try:
        with open(path, "r") as f:
            return json.load(f)
    except:
        return {}

def save_json(path, data):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)

def is_authorized(user_id):
    data = load_json(AUTH_FILE)
    u = str(user_id)
    if u in data:
        expire = data[u]["expire"]
        if expire == "unlimited" or time.time() < expire:
            return True
        del data[u]
        save_json(AUTH_FILE, data)
    return False

def get_expire_text(expire):
    if expire == "unlimited":
        return "♾️ Süresiz lisans."
    kalan = int(expire - time.time())
    dakika = kalan // 60
    saniye = kalan % 60
    return f"⏳ Kalan süre: {dakika} dakika {saniye} saniye"

def is_sudo(user_id):
    return user_id in SUDO_USERS

def get_sudo_list():
    return list(SUDO_USERS)

@app.on_message(filters.command("kstart") & filters.private)
async def kstart(client, message: Message):
    await message.reply(
        "👋 *Capi Lisans Botuna Hoşgeldiniz!*\n"
        "🔐 Bu botu kullanmak için *geçerli bir lisans anahtarı* girmeniz gerekiyor.\n"
        "📌 Key yalnızca belirlenen kullanıcı tarafından kullanılabilir. "
        "Başkası kullanırsa hem key sahibi hem kullanan banlanır!"
    )

@app.on_message(filters.command("help") & filters.private)
async def help_cmd(client, message: Message):
    await message.reply(
        "📚 *Komutlar Listesi:*\n"
        "🔑 Key girerek lisans aktif edilir\n"
        "📊 /status - Lisans sürenizi gösterir\n"
        "🧪 /test - Lisans kontrol testi\n"
        "👑 /sudo - Sudo panelini açar (sadece sudo için)\n\n"
        "⛔ Sudo komutlarına sadece yetkililer erişebilir."
    )

@app.on_message(filters.command("status") & filters.private)
async def status_cmd(client, message: Message):
    user_id = str(message.from_user.id)
    data = load_json(AUTH_FILE)
    if user_id not in data:
        return await message.reply("❌ Lisans bulunamadı. Key girin.")
    info = data[user_id]
    await message.reply(
        f"✅ Lisans aktif!\n"
        f"🧾 Key: `{info['key']}`\n"
        f"{get_expire_text(info['expire'])}"
    )

@app.on_message(filters.command("test") & filters.private)
async def test_cmd(client, message: Message):
    if is_authorized(message.from_user.id):
        await message.reply("✅ Lisansınız aktif. Erişim izni var.")
    else:
        await message.reply("❌ Lisansınız geçersiz veya süresi dolmuş.")

@app.on_message(filters.command("sudo") & filters.private)
async def sudo_menu(client, message: Message):
    if not is_sudo(message.from_user.id):
        return await message.reply("⛔ Bu komut sadece sudo kullanıcılar içindir.")
    await message.reply(
        "👑 *Sudo Paneli:*\n"
        "➕ /addkey <SÜRE> <USER_ID> - Key ekle\n"
        "🗑️ /delkey <KEY> - Key sil\n"
        "📋 /keys - Tüm keyleri göster\n"
        "🚫 /ban <USER_ID> - Kullanıcı banla\n"
        "✅ /unban <USER_ID> - Ban kaldır\n"
        "➕ /addsudo <USER_ID> - Sudo ekle\n"
        "➖ /delsudo <USER_ID> - Sudo çıkar\n"
        "📜 /sudolist - Sudo listesini göster\n"
        "🗑️ /resetkeys - Kullanılmamış keyleri temizle\n"
        "📤 /exportauth - Aktif lisanslıları göster\n"
        "📛 /banlist - Banlı kullanıcıları listele"
    )

@app.on_message(filters.command("addkey") & filters.private)
async def add_key_cmd(client, message: Message):
    if not is_sudo(message.from_user.id):
        return await message.reply("⛔ Bu komut sadece sudo kullanıcılar içindir.")
    try:
        _, key, sure, uid = message.text.split()
        expire = int(sure) if sure != "unlimited" else "unlimited"
        LICENSE_KEYS[key] = {"expire": expire, "user_id": uid, "used": False}
        await message.reply(f"✅ Key eklendi: `{key}` süresi: {sure} sn kullanıcı: `{uid}`")
    except:
        await message.reply("❌ Kullanım: /addkey <KEY> <SÜRE> <USER_ID>")

@app.on_message(filters.command("delkey") & filters.private)
async def del_key_cmd(client, message: Message):
    if not is_sudo(message.from_user.id):
        return await message.reply("⛔ Bu komut sadece sudo kullanıcılar içindir.")
    try:
        _, key = message.text.split()
        if key in LICENSE_KEYS:
            del LICENSE_KEYS[key]
            await message.reply(f"🗑️ Key silindi: `{key}`")
        else:
            await message.reply("❌ Key bulunamadı.")
    except:
        await message.reply("❌ Kullanım: /delkey <KEY>")

@app.on_message(filters.command("keys") & filters.private)
async def keys_list(client, message: Message):
    if not is_sudo(message.from_user.id):
        return await message.reply("⛔ Bu komut sadece sudo kullanıcılar içindir.")
    if not LICENSE_KEYS:
        return await message.reply("📋 Key listesi boş.")
    text = "📋 *Key Listesi:*\n"
    for k, v in LICENSE_KEYS.items():
        status = "✅ Kullanılmadı" if not v.get("used") else "❌ Kullanıldı"
        exp = "♾️" if v["expire"] == "unlimited" else f"{v['expire']} sn"
        text += f"- `{k}` → {exp} hedef: `{v['user_id']}` → {status}\n"
    await message.reply(text)

@app.on_message(filters.command("ban") & filters.private)
async def ban_user(client, message: Message):
    if not is_sudo(message.from_user.id):
        return await message.reply("⛔ Bu komut sadece sudo kullanıcılar içindir.")
    try:
        _, uid = message.text.split()
        BANNED_USERS.add(int(uid))
        await message.reply(f"🚫 Kullanıcı `{uid}` banlandı.")
    except:
        await message.reply("❌ Kullanım: /ban <USER_ID>")

@app.on_message(filters.command("unban") & filters.private)
async def unban_user(client, message: Message):
    if not is_sudo(message.from_user.id):
        return await message.reply("⛔ Bu komut sadece sudo kullanıcılar içindir.")
    try:
        _, uid = message.text.split()
        BANNED_USERS.discard(int(uid))
        await message.reply(f"✅ Kullanıcı `{uid}` ban kaldırıldı.")
    except:
        await message.reply("❌ Kullanım: /unban <USER_ID>")

@app.on_message(filters.command("addsudo") & filters.private)
async def add_sudo(client, message: Message):
    if not is_sudo(message.from_user.id):
        return await message.reply("⛔ Bu komut sadece sudo kullanıcılar içindir.")
    try:
        _, uid = message.text.split()
        SUDO_USERS.add(int(uid))
        save_json(SUDO_FILE, {str(u): True for u in SUDO_USERS})
        await message.reply(f"✅ `{uid}` sudo olarak eklendi.")
    except:
        await message.reply("❌ Kullanım: /addsudo <USER_ID>")

@app.on_message(filters.command("delsudo") & filters.private)
async def del_sudo(client, message: Message):
    if not is_sudo(message.from_user.id):
        return await message.reply("⛔ Bu komut sadece sudo kullanıcılar içindir.")
    try:
        _, uid = message.text.split()
        SUDO_USERS.discard(int(uid))
        save_json(SUDO_FILE, {str(u): True for u in SUDO_USERS})
        await message.reply(f"🧹 `{uid}` sudo listesinden çıkarıldı.")
    except:
        await message.reply("❌ Kullanım: /delsudo <USER_ID>")

@app.on_message(filters.command("sudolist") & filters.private)
async def sudolist(client, message: Message):
    if not is_sudo(message.from_user.id):
        return await message.reply("⛔ Bu komut sadece sudo kullanıcılar içindir.")
    users = get_sudo_list()
    await message.reply("👑 *Sudo Kullanıcıları:*\n" + "\n".join(f"• {u}" for u in users))

@app.on_message(filters.command("resetkeys") & filters.private)
async def reset_keys(client, message: Message):
    if not is_sudo(message.from_user.id):
        return await message.reply("⛔ Bu komut sadece sudo kullanıcılar içindir.")
    LICENSE_KEYS.clear()
    await message.reply("🔄 Tüm kullanılmamış keyler sıfırlandı.")

@app.on_message(filters.command("exportauth") & filters.private)
async def export_auth(client, message: Message):
    if not is_sudo(message.from_user.id):
        return await message.reply("⛔ Bu komut sadece sudo kullanıcılar içindir.")
    data = load_json(AUTH_FILE)
    await message.reply(f"📤 Aktif Lisanslı Kullanıcılar:\n`json\n{json.dumps(data, indent=2)}`")

@app.on_message(filters.command("banlist") & filters.private)
async def banlist(client, message: Message):
    if not is_sudo(message.from_user.id):
        return await message.reply("⛔ Bu komut sadece sudo kullanıcılar içindir.")
    if not BANNED_USERS:
        return await message.reply("📛 Banlı kullanıcı yok.")
    await message.reply("📛 *Banlı Kullanıcılar:*\n" + "\n".join(f"• {u}" for u in BANNED_USERS))

@app.on_message(filters.private & ~filters.command([
    "kstart", "help", "status", "sudo", "addkey", "delkey", "ban", "unban",
    "addsudo", "delsudo", "sudolist", "keys", "test", "resetkeys", "exportauth", "banlist"
]))
async def key_check(client, message: Message):
    try:
        user_id = str(message.from_user.id)
        key = message.text.strip()

        if int(user_id) in BANNED_USERS:
            return await message.reply("🚫 Bot kullanımınız engellenmiş.")
        if is_authorized(user_id):
            return await message.reply("✅ Lisansınız zaten aktif.")
        if key not in LICENSE_KEYS:
            return await message.reply("❌ Geçersiz key.")
        key_info = LICENSE_KEYS[key]
        if key_info.get("used"):
            return await message.reply("❌ Bu key zaten kullanıldı.")
        if key_info["user_id"] and str(key_info["user_id"]) != user_id:
            BANNED_USERS.add(int(user_id))
            BANNED_USERS.add(int(key_info["user_id"]))
            return await message.reply("🚫 Bu key size ait değil. Hem siz hem key sahibi banlandı.")

        expire = key_info["expire"]
        expire_time = time.time() + expire if expire != "unlimited" else "unlimited"

        data = load_json(AUTH_FILE)
        data[user_id] = {"key": key, "expire": expire_time}
        save_json(AUTH_FILE, data)

        LICENSE_KEYS[key]["used"] = True
        USED_KEYS.add(key)

        await message.reply(f"🔓 Lisans başarıyla aktifleştirildi!\n{get_expire_text(expire_time)}")

    except Exception as e:
        await message.reply("⚠️ Anahtar doğrulama sırasında hata oluştu.")
        print(f"[key_check] HATA: {e}")

print("✅ Bot çalışıyor...")
app.run()
