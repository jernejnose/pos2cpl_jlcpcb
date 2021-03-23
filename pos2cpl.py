import argparse

parser = argparse.ArgumentParser(description='Convert .pos file from KiCad to JLCPCB cpl file')
parser.add_argument('input_file', type=str, help='.pos file from KiCad')
parser.add_argument('output_file', type=str, help='output file, its csv')
args = parser.parse_args()

if __name__ == '__main__':
    output_file = args.output_file
    input_file = args.input_file

    with open(str(output_file), 'w') as output:
        output.write("Designator, Mid X, Mid Y, Layer, Rotation \n")
        with open(str(input_file), 'r') as input:
            for i, line in enumerate(input):
                if line[0] != '#':
                    filtered = list(filter(None, line.split()))
                    if len(filtered) != 7:
                        raise Exception('Error parsing line: ', i)
                    output.write(filtered[0] + ", " + filtered[3] + ", " + filtered[4] + ", " + filtered[6] + ", " + filtered[5] + "\n" )
