from fastapi import FastAPI
import yahoo_fin.stock_info as yah

app = FastAPI()


def convert(src, dst, amount):
    symbol = f"{src}{dst}=X"
    latest_data = yah.get_data(symbol)
    latest_price = latest_data.iloc[-1].close
    return latest_price * amount


@app.get("/api/rates")
def show_data(from_cur: str, to_cur: str, value: int):
    result = convert(from_cur, to_cur, value)
    return {'result': result}
