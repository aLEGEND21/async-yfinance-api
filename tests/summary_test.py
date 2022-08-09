import yfinance as yf
import asyncio
import traceback


async def main():
    async def summary_test(ticker: str, _type: str):
        try:
            output = await yf.fetch_summary(ticker)
            assert output.get("_type") == _type
        except:
            traceback.print_exc()
    await summary_test("AAPL", "stock")
    await summary_test("BTC-USD", "crypto")
    await summary_test("SPY", "etf")

asyncio.run(main())