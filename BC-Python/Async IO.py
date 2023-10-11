import time
import asyncio
import requests,time


async def function1():
    print("func 1")
    URL = "https://wallpaperaccess.in/public/uploads/preview/1920x1200-desktop-background-ultra-hd-wallpaper-wiki-desktop-wallpaper-4k-.jpg"
    response = requests.get(URL)
    open("File/image1.jpg", "wb").write(response.content)

    return "Downloaded First Image"


async def function2():
    print("func 2")
    URL = "https://picsum.photos/2000/3000"
    response = requests.get(URL)
    open("File/image2.jpg", "wb").write(response.content)


async def function3():
    print("func 3")
    URL = "https://picsum.photos/4000/4000"
    response = requests.get(URL)
    open("File/image3.jpg", "wb").write(response.content)


async def main():
    await function1()
    await function2()
    await function3()
    return 3
    L = await asyncio.gather(
        function1(),
        function2(),
        function3(),
    )
    print(type(L))
    print(L)


asyncio.run(main())