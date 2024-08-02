import requests,json,time,sys
from bs4 import BeautifulSoup
import multiprocessing
from concurrent.futures import ThreadPoolExecutor


start = time.time()

def get(addr, extension, name):
	for i in range(len(addr)):
		time.sleep(0.08)
		img = requests.get(addr[i]).content
		with open(f"./scraped/{name[i]}.{extension[i]}", "wb+") as f:
			f.write(img)
		

def download():
	
	# url = "https://wallhaven.cc/api/v1/search?categories=010&purity=100&sorting=random&type=jpg&ratios=landscape&seed=mate47"
	url = "https://wallhaven.cc/api/v1/search?q=nature&categories=010&purity=100&atleast=1920x1080&ratios=16x9&sorting=random&seed=Mate47"
	web = requests.get(url)
	stuff = BeautifulSoup(web.text, "html.parser")

	g = json.loads(stuff.text)

	eh = g["data"]

	links = []
	files = []
	names = []

	for i in eh:
		links.append(i["path"])
		tipe = i["file_type"].split("/")
		files.append(str(tipe[1]))
		names.append(i["id"])

	one = links[:7]
	two = links[7:13]
	three = links[13:19]
	four = links[19:]

	if __name__ == '__main__':
	 	p1 = multiprocessing.Process(target=get, args=(one, files[:7], names[:7]))
	 	p2 = multiprocessing.Process(target=get, args=(two,files[7:13], names[7:13]))
	 	p3 = multiprocessing.Process(target=get, args=(three,files[13:19], names[13:19]))
	 	p4 = multiprocessing.Process(target=get, args=(four,files[19:], names[19:]))
	 	p1.start()
	 	time.sleep(0.1)
	 	p2.start()
	 	time.sleep(0.1)
	 	p3.start()
	 	time.sleep(0.1)
	 	p4.start()
	 	time.sleep(0.1)
	 	p1.join()
	 	p2.join()
	 	p3.join()
	 	p4.join()


download()
with ThreadPoolExecutor(max_workers=4) as executor:
	    executor.submit(download)
	    time.sleep(0.1)
	    executor.submit(download)
	    time.sleep(0.1)
	    executor.submit(download)
	    time.sleep(0.1)
	    executor.submit(download)

print("--- %s seconds ---" % (time.time() - start))