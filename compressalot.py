import os 
import sys
import zipfile

the_dir = sys.argv[1]
file_threshold = sys.argv[2]

def compress_dir(d, files):
	dir_name = os.path.basename(os.path.normpath(d))
	print("compressing", dir_name)
	zipf = zipfile.ZipFile(d + '/content.zip', 'w', zipfile.ZIP_DEFLATED)
	for f in files:
		full_path = os.path.join(d, f)
		zipf.write(full_path, f)
		os.remove(full_path)
	zipf.close()

for root, dirs, files in os.walk(the_dir):
	if len(files) > file_threshold:
		compress_dir(root, files)


