import os
all_files = os.listdir()
try:
    all_files.remove("Arranger.py")
    all_files.remove("Arranger.exe")
except Exception as a:
    pass
soucre_folder = os.getcwd().replace("\\", "/") + "/"

video_format = [".WEBM", ".MPG", ".MP2", ".MPEG", ".MPE", ".MPV", ".OGG",
                ".MP4", ".M4P", ".M4V", ".AVI,", "WMV", ".MOV", ".QT", ".FLV", ".SWF"]
audio_format = [".MP3", ".AAC", ".OGG VORBIS", ".OGG",
                ".FLAC", ".ALAC", ".WAV", ".AIFF", "DSD", ".PCM"]
compressed_format = [".ZIP", ".RAR", ".KGB", ".LZ4", ".7-ZIP", ".7ZIP",
                     ".STUFFIT", ".ARC", "ARJ", ".AS", ".BZ", ".GZ", ".ISO", ".TBZ", "TGZ", ".ZIPX"]
image_format = [".TIFF", ".TIF", ".BMP", ".JPG", ".JPEG",
                ".GIF", ".PNG", ".EPS", ".raw", ".cr2", ".nef", ".orf", ".sr2"]
books_office_format = [".PDF", ".TXT", ".EPUB", ".DOC", ".DOCX",
                       ".RTF", ".ODT", ".PPT", ".PPTX", ".WPD", ".XLS", ".XLSX", ".TEX"]
all_format = [".WEBM", ".MPG", ".MP2", ".MPEG", ".MPE", ".MPV", ".OGG", ".MP4", ".M4P", ".M4V", ".AVI,", "WMV", ".MOV", ".QT", ".FLV", ".SWF", ".MP3", ".AAC", ".OGG VORBIS", ".OGG", ".FLAC", ".ALAC", ".WAV", ".AIFF", "DSD", ".PCM", ".ZIP", ".RAR", ".KGB", ".LZ4", ".7-ZIP", ".7ZIP", ".STUFFIT",
              ".ARC", "ARJ", ".AS", ".BZ", ".GZ", ".ISO", ".TBZ", "TGZ", ".ZIPX", ".TIFF", ".TIF", ".BMP", ".JPG", ".JPEG", ".GIF", ".PNG", ".EPS", ".raw", ".cr2", ".nef", ".orf", ".sr2", ".PDF", ".TXT", ".EPUB", ".DOC", ".DOCX", ".RTF", ".ODT", ".PPT", ".PPTX", ".WPD", ".XLS", ".XLSX", ".TEX"]
try:
    os.mkdir("Video")
    os.mkdir("Audio")
    os.mkdir("Images")
    os.mkdir("Compressed Files")
    os.mkdir("Reading Part")
    os.mkdir("No Idea")
except Exception as a:
    pass
for file in all_files:
    # print(file.upper())
    for extension in all_format:
        if (file.upper()).endswith(extension):
            for vid in video_format:
                if (file.upper()).endswith(vid):
                    # os.mkdir("Video")
                    dv = soucre_folder + "/Video/"
                    os.rename(soucre_folder + file, dv + file)
            for aud in audio_format:
                if (file.upper()).endswith(aud):
                    # os.mkdir("Audio")
                    da = soucre_folder + "/Audio/"
                    os.rename(soucre_folder + file, da + file)
            for img in image_format:
                if (file.upper()).endswith(img):
                    # os.mkdir("Images")
                    di = soucre_folder + "/Images/"
                    os.rename(soucre_folder + file, di + file)
            for compr in compressed_format:
                if (file.upper()).endswith(compr):
                    # os.mkdir("Compressed Files")
                    dc = soucre_folder + "/Compressed Files/"
                    os.rename(soucre_folder + file, dc + file)
            for book in books_office_format:
                if (file.upper()).endswith(book):
                    # os.mkdir("Reading Part")
                    db = soucre_folder + "/Reading Part/"
                    os.rename(soucre_folder + file, db + file)
            
        # else:
        #     destination = soucre_folder + "/No Idea/"
        #     os.rename(soucre_folder + file,destination + file)

# print(type(os.getcwd()))
# os.mkdir("hejo")
remaining_files = os.listdir()
try:
    remaining_files.remove("Arranger.py")
    remaining_files.remove("Arranger.exe")
    remaining_files.remove("Video")
    remaining_files.remove("Audio")
    remaining_files.remove("Reading Part")
    remaining_files.remove("Compressed Files")
    remaining_files.remove("Images")
    remaining_files.remove("No Idea")
except Exception as a:
    pass
for rest in remaining_files:
    dr = soucre_folder + "/No Idea/"
    os.rename(soucre_folder + rest , dr + rest)