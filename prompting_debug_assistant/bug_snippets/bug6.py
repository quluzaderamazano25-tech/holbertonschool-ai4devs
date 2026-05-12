import csv

def process_scores(input_path, output_path):
    infile = open(input_path, "r")
    reader = csv.reader(infile)

    results = []
    for row in reader:
        name = row[0]
        scores = row[1:]
        average = sum(scores) / len(scores)
        results.append([name, average])

    infile.close()

    outfile = open(output_path, "w")
    writer = csv.writer(outfile)
    writer.writerow(["Name", "Average"])

    for result in results:
        writer.writerow(result)


process_scores("scores.csv", "averages.csv")