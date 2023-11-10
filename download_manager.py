import argparse
import json
import os
import requests
import sys
import time
from datetime import datetime
from urllib.parse import urlparse


def download_by_url(url, save_path=None):
    start_time = time.perf_counter()
    response = requests.get(url.strip())
    execution_time = time.perf_counter() - start_time

    if response.status_code != 200:
        return execution_time, f'Error downloading {url}'

    if save_path:
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        with open(save_path, 'wb') as save_file:
            save_file.write(response.content)

    return execution_time, 0


def download_files_by_urls(urls_file, save_mode=False):
    download_times = dict()

    with open(urls_file, 'r') as file:
        for url_count, url in enumerate(file, start=1):
            if url.isspace():
                continue

            parsed_url = urlparse(url)

            if not parsed_url.scheme:
                print(f'Error: Invalid URL at line {url_count}) {url}')
                continue

            if save_mode:
                save_path = os.path.join(os.getcwd(), parsed_url.path.strip('/'))
                time, error = download_by_url(url, save_path)
            else:
                time, error = download_by_url(url)

            if error:
                print(error)
                continue

            filename = os.path.basename(url)
            download_times[filename] = time
            print(f'{url_count}) {filename} {time}')
    return download_times


def validate_file(file_path):
    if not os.path.exists(file_path):
        raise argparse.ArgumentTypeError(f'File "{file_path}" does not exist.')
    return file_path


def parse_arguments():
    parser = argparse.ArgumentParser(description='Download files from a list of URLs.')
    parser.add_argument('file', type=validate_file, help='File containing a list of download URLs')
    parser.add_argument('--smode', action='store_true', help='Enable save mode')
    return parser.parse_args()


def main():
    args = parse_arguments()
    print("File used:", args.file)

    if args.smode:
        print('Save mode enabled')

    current_date = datetime.today().strftime("%d-%m-%Y")
    filename = os.path.basename(args.file)
    download_logs_name = f'statistic_{filename}_{current_date}.json'

    results = download_files_by_urls(args.file, args.smode)
    results['full_download_time'] = sum(results.values())

    print(f'Download completed in {results["full_download_time"]}')

    with open(download_logs_name, 'w') as file:
        json.dump(results, file)


if __name__ == '__main__':
    main()
