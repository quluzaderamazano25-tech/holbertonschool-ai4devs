[System.IO.File]::WriteAllText("$base\bug6_fixed.py", @"
import csv

def process_scores(input_path, output_path):
    results = []
    with open(input_path, 'r') as infile:
        reader = csv.reader(infile)
        for row in reader:
            name = row[0]
            scores = row[1:]
            average = sum(float(s) for s in scores) / len(scores)
            results.append([name, round(average, 2)])
    with open(output_path, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(['Name', 'Average'])
        for result in results:
            writer.writerow(result)

process_scores('scores.csv', 'averages.csv')
"@, [System.Text.Encoding]::ASCII)