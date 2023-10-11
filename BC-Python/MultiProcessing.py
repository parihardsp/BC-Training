# import multiprocessing
# import requests
#
# url= "https://picsum.photos/2000/3000"
# def download_file(url, name):
#     print(f"Started downloading file{name}")
#     response= requests.get(url)
#     open(f"File/file{name}.jpg", "wb").write(response.content)
#     print(f"Finished downloading file{name}")
#
# if __name__ == '__main__':
#     pros=[]
#     for _ in range(5):
#         p=multiprocessing.Process(target= download_file, args=(url,_))
#         p.start()
#         pros.append(p)
#
#     for p in pros:
#         p.join()
#
#
# """
# Error in this prog is
#
# The error you're encountering is related to running multiprocessing code in an environment that uses the "spawn" method for creating child processes,
# which is the default on Windows.
# The error message suggests that you should use the if __name__ == '__main__': (in  line 10)  idiom to ensure that the code for creating
# and running child processes is only executed when the script is run directly as the main program, not when it's imported as a module.
#
#
# """
#
# import multiprocessing
# import requests
# import os
# import time
#
# url = "https://picsum.photos/2000/3000"
#
# def download_file(url, name):
#     try:
#         print(f"Started downloading {name}")
#         response = requests.get(url)
#         response.raise_for_status()  # Raise an exception for HTTP errors
#         with open(f"File/file{name}.jpg", "wb") as file:
#             file.write(response.content)
#         print(f"Finished downloading {name}")
#     except Exception as e:
#         print(f"Error downloading {name}: {e}")
#
#
# if __name__ == '__main__':
#     if not os.path.exists("File"):
#         os.makedirs("File", exist_ok=True)
#
#     processes = []
#     for i in range(5):
#         p = multiprocessing.Process(target=download_file, args=(url, str(i)))
#         p.start()
#         processes.append(p)
#
#     for p in processes:
#         p.join()
#
#     print("All downloads completed.")
#

