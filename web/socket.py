import asyncio
import websockets
import json
import yfinance as yf

async def stream(websocket):
    while True:
        data = yf.download("SPY", interval="1m", period="1d").tail(1)

        price = float(data["Close"].iloc[-1])

        await websocket.send(json.dumps({"price": price}))

        await asyncio.sleep(5)

async def main():
    async with websockets.serve(stream, "0.0.0.0", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())