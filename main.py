import re
import datetime
import os

def get_all_files(directory_path):
  """Gets all files in a directory.

  Args:
    directory_path: The path to the directory.

  Returns:
    A list of file paths.
  """

  files = []
  for file in os.listdir(directory_path):
    file_path = os.path.join(directory_path, file)
    if os.path.isfile(file_path):
        if os.path.basename(file_path).startswith("00."): continue
        files.append(file_path)
  return files

def parse_time_log(filename_path):
    """Parses a text file containing time logs in the specified format.

    Args:
        filename: The name of the file to parse.

    Returns:
        A dictionary mapping dates to the total time spent on that date.
    """

    with open(filename_path, encoding="utf8") as f:
        first_line = f.readline()
        date_match = re.search(r'\d{4}-\d{2}-\d{2}', first_line)
        
        if not date_match:
            return datetime.timedelta(0)
        date_str = date_match.group()
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
        segment = 0
        f.seek(0)
        total = datetime.timedelta(0)
        for line in f:
            time_pattern = r'\s{0,1}\d{2}[:\.]\d{2}\s{0,1}'
            all_matches = [item.strip().replace(".",":") for item in re.findall(time_pattern, line)]

            if not all_matches:
               continue
            if len(all_matches) == 1:
                continue
            all_matches = [item for item in all_matches if not item.startswith("[")]
            start_time_match = all_matches[0]
            start_time = datetime.datetime.strptime(start_time_match, '%H:%M').time()

            end_time_match = all_matches[-1]
            end_time = datetime.datetime.strptime(end_time_match, '%H:%M').time()
            
            start_datetime = datetime.datetime.combine(date, start_time)
            end_datetime = datetime.datetime.combine(date, end_time)
            
            if start_datetime > end_datetime:
                end_datetime += datetime.timedelta(days=1)
            time_delta = end_datetime - start_datetime
            if time_delta == datetime.timedelta(0):
                print("For line", line, "time delta is ", time_delta)
                print(filename_raw,"\n")
            total += time_delta
    return total 
    # 2 days, 13:53:00


def print_time_log(time_log, filename):
    """Prints the total time spent on each date in a readable format.

    Args:
        time_log: A dictionary mapping dates to timedeltas.
    """
    total = datetime.timedelta(0)
    total_week = datetime.timedelta(0)
    week_index = 0
    start_date = ""
    for date, time_delta in time_log.items():
        # print(f"{date}: {time_delta}")
        total += time_delta
        total_week += time_delta
        week_index += 1
        if week_index % 7 == 1:
            start_date = date
        week_index %= 7
        if week_index == 0:
            total_week_hours =  total_week.total_seconds() // 3600
            total_week_minutes = total_week.total_seconds() % 3600 // 60
            print(f"From {start_date} to {date} : {int(total_week_hours)}h {int(total_week_minutes)}m")
            total_week = datetime.timedelta(0)
    if week_index != 0:
        total_week_hours =  total_week.total_seconds() // 3600
        total_week_minutes = total_week.total_seconds() % 3600 // 60
        print(f"From {start_date} to {date} : {int(total_week_hours)}h {int(total_week_minutes)}m")

    print(f"Total time: {int(total.total_seconds() // 3600)}h {int(total.total_seconds() % 3600 // 60)}m")

if __name__ == '__main__':
    filename_path = "data3.txt"
    with open(filename_path, encoding="utf8") as f:
        allfiles = get_all_files(f.readline())
    time_log = {}
    for filename in allfiles:
        filename_raw = os.path.basename(filename)
        #filename = 'data2.txt'  # Replace with your actual filename
        time_log[filename_raw] = parse_time_log(filename)
    print_time_log(time_log, filename)
        