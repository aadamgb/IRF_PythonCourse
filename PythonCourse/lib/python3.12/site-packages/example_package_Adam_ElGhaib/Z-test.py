import example

example.save_str2binary('Hello World!!!!!!!!!!')
text = example.read_binary2string('bin_output.bin')

print(text)