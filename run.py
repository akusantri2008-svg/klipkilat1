"""Jalankan Klipkilat di komputer.

  python run.py        buka sebagai aplikasi di PC ini
  python run.py --hp   sama, plus bisa dibuka dari HP lewat Wi-Fi yang sama
"""
import os
import socket
import subprocess
import sys
import threading
import webbrowser

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
os.chdir(HERE)


def free_port(start: int = 7860) -> int:
    for port in range(start, start + 30):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.3)
            if s.connect_ex(("127.0.0.1", port)) != 0:
                return port
    raise SystemExit("Tidak ada port kosong. Tutup jendela Klipkilat yang lain lalu coba lagi.")


def lan_ip():
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
            s.connect(("10.255.255.255", 1))  # tidak ada paket yang dikirim
            return s.getsockname()[0]
    except OSError:
        return None


def open_app(url: str) -> None:
    if os.name == "nt":
        try:
            # Edge ada di semua Windows 10/11. Mode --app membuka jendela sendiri tanpa kotak alamat.
            subprocess.Popen(["cmd", "/c", "start", "", "msedge", f"--app={url}"])
            return
        except OSError:
            pass
    webbrowser.open(url)


def main() -> None:
    lan = "--hp" in sys.argv
    port = free_port()
    url = f"http://localhost:{port}"
    print()
    print("  Klipkilat berjalan. Jangan tutup jendela ini selama dipakai.")
    print(f"  Di komputer ini : {url}")
    if lan:
        ip = lan_ip()
        if ip:
            print(f"  Di HP (Wi-Fi sama): http://{ip}:{port}")
        print("  Mode HP terbuka untuk semua perangkat di Wi-Fi ini. Pakai hanya di Wi-Fi rumah sendiri.")
        print("  Kalau Windows bertanya soal Firewall, pilih Allow access.")
    print()
    threading.Timer(1.5, open_app, [url]).start()

    import uvicorn
    import main as server

    uvicorn.run(server.app, host="0.0.0.0" if lan else "127.0.0.1", port=port, log_level="info")


if __name__ == "__main__":
    main()
