import json

from WorkFLow.FlexibleProcessingStrategy import FlexibleProcessingStrategy
from WorkFLow.ProcessGenerateReport import generate_report
from WorkFLow.ProcessLoadFiles import load_files


def main(config_file):
    with open(config_file) as f:
        config = json.load(f)

    # Load all files
    data_tables = load_files(config['input_files'])

    # Dynamically process data
    strategy = FlexibleProcessingStrategy()
    processed_data = strategy.process(data_tables, config['operations'])

    # Generate reports
    generate_report(config, processed_data)


if __name__ == "__main__":
    main('config.json')
