from extract import extract
from transform import transform
from load import load

def run_pipeline():

    #Extract data
    raw_data = extract()

    #cleaning data
    data_cleaned = transform(raw_data)

    #load data
    load(data_cleaned)


if __name__ == '__main__':
    run_pipeline()