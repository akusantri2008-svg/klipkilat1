@echo off
title Klipkilat
cd /d "%~dp0"

rem 1. Cari Python 3.10 sampai 3.13. Versi 3.14 ke atas belum punya semua paket yang dibutuhkan.
set "PY="
for %%C in ("py -3.12" "py -3.13" "py -3.11" "py -3.10" "python3.12" "python3.13" "python3.11" "python" "python3") do (
  if not defined PY (
    %%~C -c "import sys; raise SystemExit(0 if (3,10)<=sys.version_info[:2]<=(3,13) else 1)" >nul 2>&1
    if not errorlevel 1 set "PY=%%~C"
  )
)
if not defined PY (
  for /d %%D in ("%LOCALAPPDATA%\Microsoft\WindowsApps\PythonSoftwareFoundation.Python.3.1*") do (
    if exist "%%~D\python.exe" if not defined PY set PY="%%~D\python.exe"
  )
)
if not defined PY (
  echo.
  echo Python 3.12 belum terpasang.
  echo Unduh dari python.org/downloads, pilih versi 3.12 untuk Windows, lalu klik file ini lagi.
  echo Saat memasang, centang tulisan Add python.exe to PATH.
  echo.
  pause
  exit /b 1
)

rem 2. Pasang paket Python kalau belum ada
%PY% -c "import uvicorn, starlette, python_multipart, numpy, yt_dlp, faster_whisper" >nul 2>&1
if errorlevel 1 (
  echo Memasang kebutuhan aplikasi. Hanya sekali, tunggu beberapa menit...
  %PY% -m pip install -r requirements.txt
  if errorlevel 1 (
    echo.
    echo Gagal memasang. Cek koneksi internet, lalu klik file ini lagi.
    pause
    exit /b 1
  )
)

rem 3. Pasang ffmpeg kalau belum ada
where ffmpeg >nul 2>&1
if errorlevel 1 (
  echo Memasang ffmpeg, alat pemotong video...
  winget install -e --id Gyan.FFmpeg --accept-source-agreements --accept-package-agreements
  echo.
  echo Selesai. Tutup jendela ini, lalu klik Klipkilat lagi.
  pause
  exit /b 0
)

rem 4. Jalankan
%PY% run.py %*
if errorlevel 1 pause
