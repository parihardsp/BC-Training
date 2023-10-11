"""
Navigate to the desired directory using cd command.

python -m venv myenv        --creates the virtual env named myenv
myenv\Scripts\activate      --activates the virtual env myenv
pip install package-name    --installs the differnet dependencies
deactivate                  -- deactivating the virtual env

Installing specific version:
pip install library_name == version
pip install pandas==2.0.0


- `pip list`: Lists installed packages.
- `pip freeze > requirements.txt`: Creates a list of installed packages in a file.
- `pip install -r requirements.txt`: Installs packages from a requirements file.
- `deactivate`: Deactivates the virtual environment.

"""


import threading, time

def counter():
    global total
    for _ in range(10000000):
        if total >= 10000000:
            break
        total += 1

total = 0

if __name__ == "__main__":
    time1=time.perf_counter()
    thread1 = threading.Thread(target=counter)
    thread2 = threading.Thread(target=counter)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    time2 = time.perf_counter()
    print("Total:", total)
    print("time taken:", time2-time1)



import threading

def counter(start, end):
    global total
    for i in range(start, end + 1):
        total += 1

total = 0

if __name__ == "__main__":
    time1 = time.perf_counter()
    midpoint = 5000000
    thread1 = threading.Thread(target=counter, args=(1, midpoint))
    thread2 = threading.Thread(target=counter, args=(midpoint + 1, 10000000))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
    time2 = time.perf_counter()
    print("Total:", total)
    print("time taken:", time2-time1)


import inflect

def int_to_words(number):
    p = inflect.engine()
    return p.number_to_words(number)

if __name__ == "__main":
    number = 250
    words = int_to_words(number)
    print(f"{number} in words: {words}")

print('Over')


