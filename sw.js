// Service worker sederhana: cuma agar aplikasi bisa dipasang. Semua permintaan tetap ke server (tanpa cache),
// karena hasil analisis dan video selalu harus yang terbaru.
self.addEventListener("install", () => self.skipWaiting());
self.addEventListener("activate", e => e.waitUntil(self.clients.claim()));
self.addEventListener("fetch", () => {});
