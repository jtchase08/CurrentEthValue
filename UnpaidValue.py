import requests
import json
import tkinter as tk

def draw():
    # build window, label
    global text

    text = tk.Label(main, text='Starting...', font=("Lucida Console", 48))
    text.pack()

def worker():
    global text

    ethermine = requests.get('https://api.ethermine.org/miner/0xdF8551605F433a2Fd8056Ba40DC46D7f76BC7d55/currentStats')
    ethereum = requests.get('https://api.coingecko.com/api/v3/simple/price?ids=ethereum&vs_currencies=USD')

    # get miner unpaid balance, convert from base to actual
    unpaid = ethermine.json()['data']['unpaid']
    actual = unpaid / 1000000000000000000

    # get current ethereum value in USD
    value = ethereum.json()['ethereum']['usd']

    usd_value = '$' + str(round(actual * value, 2))

    text.configure(text=usd_value)
    main.after(10000, worker)

main = tk.Tk()
draw()
worker()

# execute app
main.mainloop()