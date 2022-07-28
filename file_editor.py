import shutil
import os


# TODO Only works once, Will delete all files in old_files
# Takes in a path and renames all files to simple format
def update_filenames(from_url, to_url, scheme, extension):

	for folderName, subfolders, filenames in os.walk(from_url):
		for count, filename in enumerate(filenames, 1):
			try:
				file = os.path.join(from_url, filename)

				new_filename = f"{scheme}{count}.{extension}"
				new_file = os.path.join(to_url, new_filename)

				shutil.move(file, new_file)
				print(f"Renaming {filename} to {new_filename}...")
			except Exception as e:
				pass





def main():

	base = os.getcwd()
	from_url = os.path.join(base, "old_files")
	to_url = os.path.join(base, "new_files")

	update_filenames(from_url, to_url, "img", "jpg")



if __name__ == "__main__":
	main()
