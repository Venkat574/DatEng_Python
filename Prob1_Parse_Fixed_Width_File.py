import csv

# Helper function to parse the fixed width file based on field lengths
def parse_fixed_width_csv_file(spec, fixed_width_file, output_csv_file, encoding='utf-8'):
    # Extract field lengths from the specification
    field_lengths = [int(offset) for _, offset in spec]
    
    with open(fixed_width_file, 'r', encoding=encoding) as f_in, \
         open(output_csv_file, 'w', newline='', encoding=encoding) as f_out:
        
        csv_writer = csv.writer(f_out)
        
        # Write header
        headers = [field_name for field_name, _ in spec]
        csv_writer.writerow(headers)
        
        # Iterate through each line of the fixed-width file
        for line in f_in:
            row = []
            start = 0
            for length in field_lengths:
                row.append(line[start:start+length].strip())  # Extract and strip extra spaces
                start += length
            csv_writer.writerow(row)

# Example usage
if __name__ == "__main__":
    # Sample spec: list of tuples (field name, length)
    spec = [
        ("f1", 5),
        ("f2", 12),
        ("f3", 3),
	   ("f4", 2),
        ("f5", 13),
        ("f6", 7),
	   ("f7", 10),
        ("f8", 13),
        ("f9", 20),
	   ("f10", 13),

    ]
    
    # Input and output files
    fixed_width_file = "input_fixed_width.txt"
    output_csv_file = "output.csv"
    
    parse_fixed_width_csv_file(spec, fixed_width_file, output_csv_file)
