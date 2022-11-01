def format(path_in, path_out):
    file_input = open(path_in, 'r')
    file_output = open(path_out, 'w')
    lines = file_input.read().split('\n')
    i = 1
    for line in lines:        
        acc = line.split('|')
        file_output.write(acc[0] +  "\n")
        print(i)
        print(line + " -> " + acc[0])
        i = i + 1

if __name__ == "__main__":
    path_in = "allacc.txt"
    path_out = "acc_format.txt"
    format(path_in, path_out)