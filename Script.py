#### This Code Was Devloped By @AM_ROBOTS ####

import re
from os import environ

id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

class script(object):
    HOME_BUTTONURL_UPDATES = environ.get("HOME_BUTTONURL_UPDATES", 'https://adpaylink.com')
    START_TXT = environ.get("START_TXT", "HELLO {}")
    HELP_TXT = """HAI {}
PERINTAH COMMANDS."""
    ABOUT_TXT = """<b>✯ 𝙼𝚈 𝙽𝙰𝙼𝙴: {}</b>
<b>✮ 𝙲𝚁𝙴𝙰𝚃𝙾𝚁: </b>
<b>✮ 𝙻𝙸𝙱𝚁𝙰𝚁𝚈: 𝙿𝚈𝚁𝙾𝙶𝚁𝙰𝙼</b>
<b>✮ 𝙻𝙰𝙽𝙶𝚄𝙰𝙶𝙴: 𝙿𝚈𝚃𝙷𝙾𝙽 𝟹</b>
<b>✮ 𝙳𝙰𝚃𝙰 𝙱𝙰𝚂𝙴: 𝙼𝙾𝙽𝙶𝙾-𝙳𝙱</b>
<b>✮ 𝙱𝙾𝚃 𝚂𝙴𝚁𝚅𝙴𝚁: ᴀᴍ_ᴛᴇᴄʜ</b>
<b>✮ 𝙱𝚄𝙸𝙻𝙳 𝚂𝚃𝙰𝚃𝚄𝚂: 𝚅1.0.43 [ 𝙱𝙴𝚃𝙰 ]</b>
<b>✮ 𝚈𝙾𝚄𝚃𝚄𝙱𝙴 𝙲𝙷𝙰𝙽𝙽𝙴𝙻: </b>"""
    SOURCE_TXT = """<b>NOTE:</b>
- Bot ini tidak open source. 
- Source - Kontak Saya @TMID_CSbot

<b>DEVS:</b>
- <a href=https://t.me/TMID_CSbot>Owner</a>"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>

- Filter adalah fitur di mana pengguna dapat mengatur balasan otomatis untuk kata kunci tertentu dan bot akan merespons setiap kali kata kunci ditemukan dalam pesan.

<b>CATATAN:</b>
1. Bot harus memiliki hak admin.
2. Hanya admin yang dapat menambahkan filter dalam grup.
3. Tombol peringatan memiliki batas 64 karakter.

<b>Perintah dan Penggunaan:</b>
• /filter - <code>tambahkan filter dalam grup.</code>
• /filters - <code>daftar semua filter grup.</code>
• /del - <code>hapus filter tertentu dalam grup.</code>
• /delall - <code>hapus seluruh filter dalam grup (khusus pemilik grup).</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- Mendukung tombol inline url dan lansiran.

<b>CATATAN:</b>
1. Telegram tidak akan mengizinkan anda mengirim tombol tanpa konten apa pun, jadi konten adalah wajib.
2. Bot mendukung tombol dengan semua jenis media apa pun.
3. Tombol harus diuraikan dengan benar.

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/TMID_CSbot)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:Ini adalah pesan peringatan)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>CATATAN:</b>
1. Jadikan saya admin saluran anda jika itu saluran private.
2. Pastikan saluran anda tidak berisi file camrips, porno, dan palsu.
3. Teruskan pesan terakhir ke saya dengan tanda kutip.
 Saya akan menambahkan semua file dari saluran itu ke db saya."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Digunakan untuk menghubungkan bot ke PM untuk mengelola filter.
- Membantu untuk menghindari spamming dalam grup.

<b>CATATAN:</b>
1. Hanya admin yang dapat menambahkan koneksi.
2. Kirim <code>/connect</code> untuk menghubungkan saya ke PM anda.

<b>Commands and Usage:</b>
• /connect  - <code>menghubungkan grup tertentu ke PM anda.</code>
• /disconnect  - <code>putuskan sambungan dari grup.</code>
• /connections - <code>daftar semua grup yang koneksi anda.</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>CATATAN:</b>
Fitur tambahan bot.

<b>Perintah dan Penggunaan:</b>
• /id - <code>dapatkan id dari pengguna.</code>
• /info  - <code>mendapatkan informasi tentang pengguna.</code>
• /imdb  - <code>dapatkan informasi film dari sumber IMDb.</code>
• /search  - <code>dapatkan informasi film dari berbagai sumber.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>th

<b>CATATAN:</b>
Modul ini hanya berfungsi untuk owner.

<b>Perintah dan Penggunaan:</b>
• /logs - <code>untuk mendapatkan kesalahan terbaru.</code>
• /stats - <code>untuk mendapatkan status file dalam db.</code>
• /delete - <code>untuk menghapus file tertentu dari db.</code>
• /users - <code>untuk mendapatkan daftar pengguna dan id saya.</code>
• /chats - <code>untuk mendapatkan daftar obrolan dan id saya.</code>
• /leave  - <code>untuk keluar dari obrolan.</code>
• /disable - <code>nonaktifkan obrolan.</code>
• /ban - <code>untuk melarang pengguna.</code>
• /unban - <code>untuk membatalkan pencekalan pengguna.</code>
• /channel - <code>untuk mendapatkan daftar total saluran yang terhubung.</code>
• /broadcast - <code>untuk menyiarkan pesan ke semua pengguna.</code>"""
    STATUS_TXT = """★ 𝚃𝙾𝚃𝙰𝙻 𝙵𝙸𝙻𝙴𝚂: <code>{}</code>
★ Jumlah Pengguna: <code>{}</code>
★ Jumlah Grup: <code>{}</code>
★ Penyimpanan Terpakai: <code>{}</code> 𝙼𝚒𝙱
★ Penyimpanan Bebas: <code>{}</code> 𝙼𝚒𝙱"""
    LOG_TEXT_G = """#𝐍𝐞𝐰𝐆𝐫𝐨𝐮𝐩
    
<b>᚛› Grup ⪼ {}(<code>{}</code>)</b>
<b>᚛› Jumlah Anggota ⪼ <code>{}</code></b>
<b>᚛› Ditambahkan oleh ⪼ {}</b>
"""
    LOG_TEXT_P = """#𝐍𝐞𝐰𝐔𝐬𝐞𝐫  
    
<b>᚛› ID - <code>{}</code></b>
<b>᚛› Nama - {}</b>
"""
