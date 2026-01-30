import zipfile, os, sys

ZIP_NAME = "rosemary_gaming_safe.zip"
SOURCE_DIR = "rosemary-gaming-module"

print("Folder kerja:", os.getcwd())

if not os.path.isdir(SOURCE_DIR):
    print("❌ Folder sumber tidak ditemukan:", SOURCE_DIR)
    sys.exit(1)

try:
    with zipfile.ZipFile(ZIP_NAME, "w", zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(SOURCE_DIR):
            for file in files:
                fullpath = os.path.join(root, file)
                arcname = fullpath.replace(SOURCE_DIR + os.sep, "")
                zipf.write(fullpath, arcname)
    print("✅ ZIP berhasil dibuat:", ZIP_NAME)
except Exception as e:
    print("❌ Error:", e)
