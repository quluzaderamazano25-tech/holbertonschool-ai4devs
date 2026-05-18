import csv

def process_scores(input_file, output_file):
    """
    CSV-dən xalları oxuyur, ortalamanı hesablayır və yeni fayla yazır.
    Fayl sızmasının qarşısını almaq üçün 'with' bloku istifadə olunur.
    """
    with open(input_file, 'r') as f_in:
        with open(output_file, 'w', newline='') as f_out:
            reader = csv.reader(f_in)
            writer = csv.writer(f_out)
            
            for row in reader:
                name = row[0]
                scores = [float(s) for s in row[1:]]
                average_score = sum(scores) / len(scores)
                writer.writerow([name, round(average_score, 2)])