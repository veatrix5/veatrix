import requests
from bs4 import BeautifulSoup
import random
import time
from colorama import Fore, Style, init

# Inisialisasi Colorama untuk warna
init()

# TLD target
TARGET_TLDS = [".go.id", ".ac.id", ".sch.id", ".desa.id"]

# Path yang sering digunakan webshell
SHELL_PATHS = [
    "/dropdown.php",
    "/wp-content/themes/gaukingo/db.php",
    "/wp-includes/wp-class.php",
    "/wp-cron.php?ac=3",
    "/alfa-rex.php7",
    "/dropdown.php",
    "/chosen.php?p=",
    "/ws.php",
    "/.well-known/wp-cron.php?ac=3",
    "/fm1.php",
    "/wso.php",
    "/images/Mhbgf.php",
    "/administrator/",
    "/admin/",
    "/wp-admin/",
    "/upload/",
    "/images/",
    "/index.php",
    "/includes/db.php",
    "/themes/db.php",
    "/css/upload.php",
    "/js/upload.php",
    "/backup/db.php",
    "/sql.php",
    "/shell.php",
    "/config.php",
    "/install.php",
    "/.env",
    "/vendor/.env",
    "/wp-content/uploads/db.php",
    "/wp-includes/widgets/class-wp-widget-categories-character.php", 
    "/wp-includes/class-wp-hook-ajax-response.php", "/shell.php", 
    "/backdoor.php", "/webshell.php", "/cmd.php", "/upload.php", "/exec.php", 
    "/reverse.php", "/adminer.php", "/panel.php", "/deface.php", "/index.php", 
    "/test.php", "/cmd2.php", "/backdoor2.php", "/webbackdoor.php", "/spider.php", 
    "/panelbackdoor.php", "/r57.php", "/c99.php", "/b374k.php", "/pussy.php", 
    "/hacked.php", "/php-reverse-shell.php", "/sh.php", "/mini.php", "/config.php", 
    "/gate.php", "/root.php", "/priv.php", "/access.php", "/shell2.php", "/upl.php", 
    "/load.php", "/system.php", "/connect.php", "/hidden.php", "/stealth.php", 
    "/safe.php", "/error.php", "/pass.php", "/xploit.php", "/bypass.php", "/scan.php", 
    "/inject.php", "/debug.php", "/ghost.php", "/shadow.php", "/proxy.php", "/rootkit.php", 
    "/stealthshell.php", "/ghostshell.php", "/server.php", "/hidden_access.php", 
    "/bypass_auth.php", "/webadmin.php", "/control.php", "/security_breach.php", 
    "/hacktool.php", "/door.php", "/exploit.php", "/anonaccess.php", "/undetected.php", 
    "/command.php", "/gateway.php", "/connection.php", "/remote.php", "/upload_bypass.php", 
    "/terminal.php", "/malicious.php", "/forbidden.php", "/override.php", "/superuser.php", 
    "/intruder.php", "/master.php", "/king.php", "/admin_shell.php", "/server_control.php", 
    "/security_bypass.php", "/hidden_door.php", "/anon_shell.php", "/webmaster.php", 
    "/cmdshell.php", "/supercmd.php", "/php_shell.php", "/backconnect.php", "/connect_back.php", 
    "/revshell.php", "/socket.php", "/tcp_shell.php", "/udp_shell.php", "/bind.php", 
    "/rootdoor.php", "/undetectable.php", "/secure.php", "/fake_login.php", 
    "/php-backdoor.php", "/shell_access.php", "/hidden_script.php", "/safe_mode_bypass.php", 
    "/shell_exec.php", "/reverse_tcp.php", "/remote_access.php", "/ftp_shell.php", 
    "/mysql_shell.php", "/database_shell.php", "/php_webshell.php", "/injector.php", 
    "/php-exploit.php", "/anonhack.php", "/supershell.php", "/ssh_bypass.php", 
    "/c99shell.php", "/r57shell.php", "/r00tshell.php", "/1337shell.php", "/elite.php", 
    "/underground.php", "/trojan.php", "/botnet.php", "/payload.php", "/meterpreter.php", 
    "/rat.php", "/webshell_access.php", "/system_control.php", "/server_root.php", 
    "/admin_cmd.php", "/privilege_escalation.php", "/hidden_service.php", 
    "/anonymous_shell.php", "/remote_cmd.php", "/reverse_access.php", "/bypass_login.php", 
    "/exploit_cmd.php", "/ghost_access.php", "/hidden_gateway.php", "/proxy_bypass.php", 
    "/server_bypass.php", "/rootkit_access.php", "/bypass_root.php", "/root_command.php", 
    "/admin_exploit.php", "/stealth_backdoor.php", "/hacker_access.php", "/anonymous_cmd.php", 
    "/terminal_access.php", "/database_exploit.php", "/php_hidden.php", "/super_admin.php", 
    "/shadow_root.php", "/safe_access.php", "/server_exploit.php", "/hidden_root.php", 
    "/undetectable_shell.php", "/ghost_command.php", "/master_shell.php", "/elite_cmd.php", 
    "/proxy_exploit.php", "/bypass_firewall.php", "/backdoor_access.php", "/root_access.php", 
    "/hacker_panel.php", "/webshell_hidden.php", "/server_cmd.php", "/exploit_root.php", 
    "/php_control.php", "/webmaster_shell.php", "/webshell_bypass.php", "/admin_privileges.php", 
    "/root_server.php", "/webmaster_access.php", "/hidden_panel.php", "/server_inject.php", 
    "/remote_shell_exec.php", "/undetectable_script.php", "/mysql_exploit.php", 
    "/ftp_exploit.php", "/smtp_shell.php", "/telnet_shell.php", "/email_exploit.php", 
    "/apache_exploit.php", "/nginx_exploit.php", "/iis_exploit.php", "/htaccess_bypass.php", 
    "/mod_rewrite_bypass.php", "/hidden_php.php", "/hidden_exploit.php", "/hidden_admin.php", 
    "/stealth_exploit.php", "/elite_shell.php", "/supreme_backdoor.php", "/server_tunnel.php", 
    "/proxy_tunnel.php", "/database_tunnel.php", "/server_rootkit.php", 
    "/php_backdoor_script.php", "/undetectable_payload.php", "/webshell_inject.php", 
    "/firewall_bypass.php", "/malicious_access.php", "/hidden_server.php", 
    "/server_injector.php", "/remote_server.php", "/php_server_exploit.php", 
    "/database_access.php", "/malware_shell.php", "/hacker_exploit.php", "/anonymous_root.php", 
    "/bypass_privileges.php", "/database_root.php", "/system_bypass.php", "/server_hacker.php", 
    "/rootkit_exploit.php", "/superuser_access.php", "/hacker_rootkit.php", "/system_admin.php", 
    "/privileged_shell.php", "/superuser_exploit.php", "/anonymous_exploit.php", 
    "/database_hack.php", "/server_trojan.php", "/anonymous_admin.php", "/ftp_root.php", 
    "/ssh_root.php", "/email_root.php", "/telnet_root.php", "/server_rootkit_bypass.php", 
    "/backdoor_cmd.php", "/rootkit_admin.php", "/system_tunnel.php", "/anonymous_tunnel.php", 
    "/server_breach.php", "/database_trojan.php", "/webshell_tunnel.php", "/php_tunnel.php", 
    "/undetectable_backdoor.php", "/malicious_rootkit.php", "/superuser_bypass.php", 
    "/system_rootkit.php", "/admin_rootkit.php", "/rootkit_server.php", "/php_system.php", 
    "/server_rootkit_exploit.php", "/bypass_access.php", "/hidden_bypass.php", 
    "/server_hijack.php", "/rootkit_bypass_access.php", "/stealth_hacker.php", 
    "/hacker_hidden.php", "/server_exploit_bypass.php", "/server_root_bypass.php", 
    "/php_root_bypass.php", "/webshell_admin.php", "/superuser_panel.php", "/rootkit_control.php", 
    "/stealth_root.php", "/anonymous_panel.php", "/server_command.php", "/superuser_command.php", 
    "/server_root_access.php", "/privilege_root.php", "/admin_root_bypass.php", 
    "/server_rootkit_access.php", "/stealth_exploit_access.php", "/malicious_exploit.php"
]

# Seed URLs untuk crawling awal
SEED_URLS = [
"https://www.dsihk.se/",
]

# Fungsi untuk memeriksa apakah URL dapat diakses
def check_webshell(base_url, path):
    try:
        url = base_url.rstrip("/") + path
        response = requests.head(url, timeout=5)
        if response.status_code == 200:
            print(Fore.GREEN + f"[✔] Webshell ditemukan: {url}" + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + f"[✘] Tidak ditemukan: {url}" + Style.RESET_ALL)
            return False
    except requests.RequestException as e:
        print(Fore.RED + f"[✘] Error: {base_url}{path} ({str(e)})" + Style.RESET_ALL)
        return False

# Fungsi untuk mendapatkan domain acak dari halaman
def get_random_links(url):
    links = []
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        for a_tag in soup.find_all("a", href=True):
            href = a_tag["href"]
            if any(tld in href for tld in TARGET_TLDS):  # Filter hanya domain target
                links.append(href)
        return random.sample(links, min(len(links), 5))  # Ambil hingga 5 tautan acak
    except requests.RequestException:
        return []

# Fungsi utama untuk mencari webshell
def random_webshell_finder():
    scanned = set()
    to_scan = random.sample(SEED_URLS, len(SEED_URLS))

    while to_scan:
        base_url = to_scan.pop(0)
        if base_url in scanned:
            continue

        print(Fore.CYAN + f"\n[~] Memindai situs: {base_url}" + Style.RESET_ALL)
        scanned.add(base_url)

        # Periksa setiap path di SHELL_PATHS
        for path in SHELL_PATHS:
            check_webshell(base_url, path)

        # Ambil tautan baru dari halaman untuk melanjutkan crawling
        new_links = get_random_links(base_url)
        to_scan.extend(new_links)
        to_scan = list(set(to_scan))  # Hilangkan duplikasi

        # Tunggu sebelum memindai situs berikutnya
        time.sleep(random.uniform(1, 3))

if __name__ == "__main__":
    print(Fore.CYAN + "Random Webshell Finder - Pemindai Domain Target\n" + Style.RESET_ALL)
    random_webshell_finder()
