import time 
import json
from datetime import datetime

# Sort Functions
def date_sort(db:list):
    'sorts by the "Date" key'
    return sorted(db, key=lambda x: datetime.strptime(x["Date"], '%m-%d-%Y'))

def priority_sort(db:list):
    'sorts between high, medium and low using the "Priority" key '
    highs, meds, lows = [],[],[]
    for task in db:
        if task["Priority"].lower().strip() == "high":
            highs.append(task)
        elif task["Priority"].lower().strip() == "medium":
            meds.append(task)
        else:
            lows.append(task)

    return highs + meds +lows

def both_sort(db:list):
    'sorts by the "Date" and "Priority" keys'
    db = date_sort(db)
    return priority_sort(db)

def sort_tasks(method:str, tasks:list):
    "applys the requested sort"
    match method:
        case "1":
            return date_sort(tasks)
        case "2":
            return priority_sort(tasks)
        case "3":
            return both_sort(tasks)
        case _:
            print(f"method error. received: {method}")
            return None
# Communication Functions
def read_request(request_file:str):
    "reads and returns contents of request file"
    with open(request_file, 'r') as f:
        method = f.readline().strip()
        data = f.readline().strip()
    if method:
        print("Request Received")
        try:
            tasks = json.loads(data)
        except json.JSONDecodeError as e:
            print(f"Decoding error {e}")
        # clear requests file for future use
        with open(request_file, 'w') as f:
            pass
        return method, tasks
    return None, None

def send_response(response_file:str, data:list):
    "writes sorted data to response file"
    with open(response_file, 'w') as f:
        f.write(json.dumps(data, indent=2))
    print("Response Sent")


def main():
    # Specify communication pipes
    request_file = "request.txt"
    response_file = "sorted.txt"

    while True:
        # timer - change as needed
        time.sleep(.333334)
        # read contents
        sort_type, data = read_request(request_file)
        # if request was found
        if sort_type:
            # sort the data
            sorted_data = sort_tasks(sort_type, data)
            # send back sorted data
            send_response(response_file, sorted_data)

        
if __name__ == "__main__":
    main()