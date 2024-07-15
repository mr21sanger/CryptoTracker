from django.shortcuts import render
import requests
import datetime
import json
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User

# Create your views here.

def home(request):
    # GETTING GLOBAL DATA FOR GLOBAL BLOCKS
    global_data = globalData()
    global_data = global_data.get("data", {})

    # GETTING TRENDING DATA FOR TRENDING BLOCKS
    trendingData = trending()
    coins = trendingData.get("coins", [])
    nft = trendingData.get("nfts", [])
    category = trendingData.get("categories", [])

    # URL of the CoinGecko API
    url = "https://api.coingecko.com/api/v3/coins/markets"
    currency = "usd"  # Replace with your desired currency or get it from request.GET or request.POST
    parameters = {
        "vs_currency": currency,
        "order": "market_cap_desc",
        "per_page": 100,
        "page": 1,
        "sparkline": "false",
    }

    # Make a GET request to the API
    response = requests.get(url, params=parameters)
    response.raise_for_status()  # Raises HTTPError for bad responses
    coins_data = response.json()

    context = {
        "coins_data": coins_data,
        "trending_coin": coins,
        "trending_nfts": nft,
        "trending_category": category,
        "global_data": global_data,
    }

    if context:
        return render(request, "my_app/index.html", context)
    else:
        return render(request, "my_app/error.html")


# SINGLE COIN DETAIL PAGE
def details(request, id):
    context = getDetail(id)
    print(context)
    if context:
        return render(request, "my_app/details.html", context)
    else:
        return render(request, "my_app/error.html")


def chart(id, days=7, currency="usd"):
    url = f"https://api.coingecko.com/api/v3/coins/{id}/market_chart?vs_currency={currency}&days={days}"

    try:
        response = requests.get(url)
        if response.status_code == 200:
            chart_data = response.json()

            # Extracting data from the API response
            prices = chart_data.get("prices", [])
            market_caps = chart_data.get("market_caps", [])
            total_volumes = chart_data.get("total_volumes", [])

            dates = [
                datetime.datetime.fromtimestamp(entry[0] / 1000).isoformat()
                for entry in prices
            ]
            prices_data = [entry[1] for entry in prices]
            market_caps_data = [entry[1] for entry in market_caps]
            total_volumes_data = [entry[1] for entry in total_volumes]

            context = {
                "id": id,
                "dates": dates,
                "prices_data": prices_data,
                "market_caps_data": market_caps_data,
                "total_volumes_data": total_volumes_data,
            }
            json_data = json.dumps(context)
            return json_data
    except requests.exceptions.RequestException as e:
        return e


def trending():
    url = "https://api.coingecko.com/api/v3/search/trending"
    response = requests.get(url)
    trendingData = response.json()
    return trendingData


def search(request):
    query = request.GET.get("query")
    if query:
        return redirect("details", id=query)
    else:
        return render(request, "my_app/error.html")


def getDetail(id):
    url = f"https://api.coingecko.com/api/v3/coins/{id}"
    chartData = chart(id)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            coin_data = response.json()
            name = coin_data.get("name", "")
            symbol = coin_data.get("symbol", "")
            logo = coin_data.get("image", {}).get("small", "")
            price = (
                coin_data.get("market_data", {}).get("current_price", {}).get("usd", "")
            )
            rank = coin_data.get("market_cap_rank", "")
            total_vol = (
                coin_data.get("market_data", {}).get("total_volume", {}).get("usd", "")
            )
            market_cap = (
                coin_data.get("market_data", {}).get("market_cap", {}).get("usd", "")
            )
            high_24h = (
                coin_data.get("market_data", {}).get("high_24h", {}).get("usd", "")
            )
            low_24h = coin_data.get("market_data", {}).get("low_24h", {}).get("usd", "")
            priceChange_24h = coin_data.get("market_data", {}).get(
                "price_change_percentage_24h", ""
            )
            priceChange_7d = coin_data.get("market_data", {}).get(
                "price_change_percentage_7d", ""
            )
            priceChange_1h = (
                coin_data.get("market_data", {})
                .get("price_change_percentage_1h_in_currency", {})
                .get("usd", "")
            )

            homepage = coin_data.get("links", {}).get("homepage", [])[0]
            circulating_supply = coin_data.get("market_data", {}).get(
                "circulating_supply", ""
            )
            total_supply = coin_data.get("market_data", {}).get("total_supply", "")
            description = coin_data.get("description", {}).get("en", "")

            context = {
                "id": id,
                "name": name,
                "symbol": symbol,
                "logo": logo,
                "price": price,
                "market_cap": market_cap,
                "total_vol": total_vol,
                "high_24h": high_24h,
                "low_24h": low_24h,
                "priceChange_24h": priceChange_24h,
                "priceChange_7d": priceChange_7d,
                "priceChange_1h": priceChange_1h,
                "circulating_supply": circulating_supply,
                "total_supply": total_supply,
                "rank": rank,
                "description": description,
                "homepage": homepage,
                "chartData": chartData,
            }
            return context
    except requests.exceptions.RequestException as e:
        context = {"error_message": f"Request error: {str(e)}"}
        return context


def globalData():
    url = "https://api.coingecko.com/api/v3/global"
    response = requests.get(url)
    globalData = response.json()
    return globalData
