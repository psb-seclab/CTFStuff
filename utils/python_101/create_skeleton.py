

def create_skeleton(filename):
	fi = open(filename, 'rt')
	out_filename = 'python_101_skeleton.py'
	fo = open(out_filename, 'wt')
	for line in fi:
		if '#' in line or 'import' in line or 'def' in line \
		or '__name__' in line or 'return' in line:
			fo.write(line)

	fi.close()
	fo.close()
	return


if __name__ == "__main__":
	create_skeleton('python_101.py')