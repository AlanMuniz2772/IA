import argparse

class ArgumentParser:
    @staticmethod
    def parse_args():
        parser = argparse.ArgumentParser(description="Process some integers.")

        parser.add_argument("operation", type=int, help="Operation to perform")

        return parser.parse_args()