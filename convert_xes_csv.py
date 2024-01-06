from pm4py.objects.log.importer.xes import importer as xes_importer
from pm4py.objects.conversion.log import converter as log_converter


xes_file_path = 'Datasets/BPI_Challenge_2012.xes.gz'


log = xes_importer.apply(xes_file_path)


dataframe = log_converter.apply(log, variant=log_converter.Variants.TO_DATA_FRAME)


csv_file_path = 'Datasets/BPI_Challenge_2012_csvfile.csv'

dataframe.to_csv(csv_file_path, index=False)

print(f"XES file '{xes_file_path}' has been converted to '{csv_file_path}'.")
