import shutil
import zipfile
import os
comp_file = zipfile.ZipFile('comp_file.zip', 'w')
comp_file.write('test-0.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.write('test-1.txt', compress_type=zipfile.ZIP_DEFLATED)
comp_file.close()

zip_obj = zipfile.ZipFile('comp_file.zip', 'r')
zip_obj.extractall('extracted_content')


# dir_to_zip = os.getcwd() + "\\extracted_content"
# output_filename = 'example'
# shutil.make_archive(output_filename, 'zip', dir_to_zip)
shutil.unpack_archive('example.zip', 'final_unzip', 'zip')
