import json
import os
import requests
import sys
import time
from datetime import datetime
from urllib.parse import urlparse


def download_by_url(url, save_path, no_save_mode=False):
    start_time = time.perf_counter()
    response = requests.get(url)
    execution_time = time.perf_counter() - start_time

    if response.status_code != 200:
        return execution_time, -1
    if no_save_mode:
        return execution_time, 0

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    with open(save_path, 'wb') as save_file:
        save_file.write(response.content)

    return execution_time, 0


def download_by_list(links_file, no_save_files=False):
    download_times = dict()
    url_count = 0
    with open(links_file, 'r') as file:
        for url in file:
            if url.isspace():
                continue
            url_count += 1
            save_path = os.path.join(os.getcwd(), urlparse(url).path.strip('/'))
            time, error = download_by_url(url.strip(), save_path, no_save_files)
            if error:
                print('Error download by url: ', url)
                continue

            filename = os.path.basename(save_path)
            download_times[filename] = time
            print(f'{url_count}) {filename} {time}')
    return download_times


def main():
    if len(sys.argv) > 1:
        download_url_list = sys.argv[1]
        print("Используется файл:", download_url_list)
    else:
        print("Не указано имя файла. Укажите имя файла в качестве аргумента командной строки.")
        exit(-1)

    current_date = datetime.strftime(datetime.today(), "%d-%m-%Y")
    log_filename = download_url_list.split(".")[0]
    download_logs_name = f'statistic_{log_filename}_{current_date}.json'

    no_save_mode = True

    results = download_by_list(download_url_list, no_save_mode)
    results['full_download_time'] = sum(results.values())
    print(f'Скачивание завершено за {results["full_download_time"]}')
    with open(download_logs_name, 'w') as file:
        json.dump(results, file)


if __name__ == '__main__':
    main()
