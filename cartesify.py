import sys


def main(ls_args):
  if len(ls_args) > 2:
    write_ls_to_file(ls_args[0],build_cartesian_list(read_file(ls_args[1]),ls_args[2:]))
  else:
    print("How to use:\n`python cartesify.py <output file name> <input file 1> <input file 2> ... <input file n>`")


def build_cartesian_list(ls_input,ls_filenames):
  ls_input2 = read_file(ls_filenames[0])
  ls_out = list()
  for item in ls_input:
    for item2 in ls_input2:
      if item != "" and item2 != "":
        ls_out.append(item + " " + item2)
        print(ls_out)
  if len(ls_filenames) > 1:
    ls_out = build_cartesian_list(ls_out,ls_filenames[1:])
  return ls_out


def read_file(str_filename):
  file = open(str_filename, "r")
  ls_out = file.read().split("\n")
  file.close()
  return ls_out


def write_ls_to_file(str_filename, ls_input):
  file = open(str_filename, "w")
  for line in ls_input:
    file.write(line + "\n")
    
  file.close()


if __name__ == "__main__":
  main(sys.argv[1:])
