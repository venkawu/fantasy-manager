from fpl import FPL
import aiohttp, asyncio, os, json
import requests
import json
from typing import Optional, Dict, List
from tabulate import tabulate

email = os.environ.get("FPL_EMAIL", "vince4network@gmail.com")
password = os.environ.get("FPL_PASSWORD", "crespo10FPL!")
gk = defenders = midfielders = strikers = []


async def main():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        player = await fpl.get_player(335)
        print(player)


async def get_all_players():
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        players = await fpl.get_players()
        gk = []
        defenders = []
        midfielders = []
        strikers = []

        for player in players:
            if player.web_name == "Rashford":
                print(player)
                print(vars(player))

            if player.element_type == 1:
                gk.append(player)

            if player.element_type == 2:
                defenders.append(player)

            if player.element_type == 3:
                midfielders.append(player)

            if player.element_type == 4:
                strikers.append(player)

        gk.sort(key=lambda x: x.form, reverse=True)
        defenders.sort(key=lambda x: x.form, reverse=True)
        midfielders.sort(key=lambda x: x.form, reverse=True)
        strikers.sort(key=lambda x: x.form, reverse=True)

        for i in range(10):
            print(i)
            print(gk[i])
            print(defenders[i])
            print(midfielders[i])
            print(strikers[i])

        # print(f"total players = {len(players)}")
        # print(f"total gk = {len(gk)}")
        # print(f"total defenders = {len(defenders)}")
        # print(f"total mids = {len(midfielders)}")
        # print(f"total strikers = {len(strikers)}")


async def my_team():
    print(email, password)
    async with aiohttp.ClientSession() as session:
        fpl = FPL(session)
        await fpl.login(email=email, password=password)
        user = await fpl.get_user()
        team = await user.get_team()
    print(team)


def login():
    import requests

    url = "https://users.premierleague.com/accounts/login/"

    payload = "login=vince4network%40gmail.com&password=crespo10FPL!&app=plfpl-web&redirect_uri=https%3A%2F%2Ffantasy.premierleague.com%2F"
    headers = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "en-US,en;q=0.9",
        "cache-control": "max-age=0",
        "content-type": "application/x-www-form-urlencoded",
        "cookie": '_cb=Cuc46fDUiux2g_FtI; OptanonAlertBoxClosed=2024-03-23T23:59:36.235Z; _chartbeat2=.1702150070160.1711572437244.0000000000010001.9lfeX2-M-JBx5biaByTrZTCqF8qp.1; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgdmluY2U0bmV0d29ya0BnbWFpbC5jb20uIiwiIl1d:1s6IQO:fcBD8t218GX2qtKesSy3PAgdRXMZP2D1OqCmkrM5lls; csrftoken=kcsNrcDJ0SbWU5mbsvLsp2cLkWE4gip7; __gads=ID=c12f81c0941a69fd:T=1711238383:RT=1715555773:S=ALNI_MbvoDfH06NlhOcP1TTnpfEj9AasRA; __gpi=UID=00000dd5152419da:T=1711238383:RT=1715555773:S=ALNI_MbYckDzYOTH-YbWnju47DVSLvYDjw; _gid=GA1.2.1028369643.1723418672; _dc_gtm_UA-33785302-1=1; OptanonConsent=isGpcEnabled=0&datestamp=Sun+Aug+11+2024+18%3A24%3A32+GMT-0500+(Central+Daylight+Time)&version=202302.1.0&isIABGlobal=false&hosts=&consentId=6ba883cc-83f3-454c-80b4-7053774a77be&interactionCount=3&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A1%2CC0003%3A1%2CC0004%3A1&geolocation=US%3BMS&AwaitingReconsent=false; _ga_844XQSF4K8=GS1.1.1723418672.89.0.1723418672.60.0.0; _ga=GA1.1.143822227.1676859538; datadome=fcz38xNE9X0NFqoQqTMknZ6fYcd00gmJHhl2zwLSc93aQKKykSOhK7FGLTEs6YP3f9e4K_R5rsG_XBUHfBnL25ZhGKfdQTRFd8IabIqe0b2wUdMSV4VQYV0ti_kx864n; datadome=XtLmqzOgm3fu01R83bwJsCK_TXtBtkhuagzmhb8rSnTKlsiTxczWBSF9DRUyYSemUw6If7FU2UD9gA7Cakp0fzSwnMp2FOOsaQGPd7kj8dca38VK0RndDLD6eSu7opsu; pl_profile="eyJzIjogIld6SXNPVE16TnpVM09GMDoxc2RIeUg6TFNvU3FVdXNZUWlmM1FIZ0Uyd3hCcDFJbGVCclExMHNsbktnc2F2UkpicyIsICJ1IjogeyJpZCI6IDkzMzc1NzgsICJmbiI6ICJWaW5jZSIsICJsbiI6ICJOa2F3dSIsICJmYyI6IDN9fQ=="; csrftoken=NPpg5X9MW7SmqTw72ptCLHBRQojgzCZP; elevate=GmfWtGzYwJaB:1sdHyH:FaByIUlOUzRnp5fu2DuKLzhE1-m0TFRUEdmWhQ5ckZc; messages=W1siX19qc29uX21lc3NhZ2UiLDAsMjUsIlN1Y2Nlc3NmdWxseSBzaWduZWQgaW4gYXMgdmluY2U0bmV0d29ya0BnbWFpbC5jb20uIiwiIl1d:1sdHyH:kLPqH8XjIGhqzDsieJhK6oSDjrlGOP-Wk1Ll47EBSGc; sessionid=clb0lmb15sjjbtibvkzahi96hcvjucv9',
        "origin": "null",
        "priority": "u=0, i",
        "sec-ch-device-memory": "8",
        "sec-ch-ua": '"Google Chrome";v="125", "Chromium";v="125", "Not.A/Brand";v="24"',
        "sec-ch-ua-arch": '"arm"',
        "sec-ch-ua-full-version-list": '"Google Chrome";v="125.0.6422.113", "Chromium";v="125.0.6422.113", "Not.A/Brand";v="24.0.0.0"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-model": '""',
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "document",
        "sec-fetch-mode": "navigate",
        "sec-fetch-site": "same-site",
        "sec-fetch-user": "?1",
        "upgrade-insecure-requests": "1",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    print(response.text)


def get_league_standings(league_id: Optional[str] = "129957") -> None:
    """
    What is phase? The gameweek?
    really weird api

    This method simply gives us the latest standing
    returning a list of the the player's infomation.

    It doesnt look like one needs to be authenticated to get this information
    [
        {
            "id": 42470631,
            "event_total": 43,
            "player_name": "adeosun olamide",
            "rank": 42,
            "last_rank": 41,
            "rank_sort": 42,
            "total": 124,
            "entry": 1112226,
            "entry_name": "Bells CF"
        }
    ]
    """

    # league_id = "139959"
    # url = f"https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/?page_new_entries=1&page_standings=1&phase=2"
    url = f"https://fantasy.premierleague.com/api/leagues-classic/{league_id}/standings/?page_new_entries=1&page_standings=1&phase=1"

    print(url)
    payload = {}
    headers = {"accept": "*/*", "accept-language": "en-US,en;q=0.9"}

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(json.dumps(response.json(), indent=4))

    return response.json()


def player_pick(entry_id: str, game_week: str):
    """
    This method is used to get player GW details
    it accepts player entry id and GW to provide information
    for the given GW

    Args:
        entry_id (str): the id of a player we want to get information for
        game_week (str): the current game week
    """

    url = f"https://fantasy.premierleague.com/api/entry/{entry_id}/event/{game_week}/picks/"

    payload = {}
    headers = {
        "accept": "*/*",
        "accept-language": "en-US,en;q=0.9",
    }

    response = requests.request("GET", url, headers=headers, data=payload)

    # print(response.text)
    return response.json()


if __name__ == "__main__":
    # asyncio.run(main())
    # asyncio.run(my_team())
    # asyncio.run(get_all_players())

    # login()
    standings = get_league_standings().get("standings", {}).get("results", [])
    GW = []
    current_gameweek = 27
    for player in standings:
        name = player.get("player_name", "").strip()
        team = player.get("entry_name", "").strip()

        entry_id = player.get("entry", "")

        week_result = player_pick(entry_id, current_gameweek)

        week_point = week_result.get("entry_history", {})
        gw_points = int(week_point.get("points", 0))
        transfer_penalty = int(week_point.get("event_transfers_cost", 0))
        points = gw_points - transfer_penalty

        GW.append(
            {
                "player": name,
                "team": team,
                "GW points": gw_points,
                "transfer_penalty": transfer_penalty,
                "points": points,
            }
        )

    GW = sorted(GW, key=lambda player: player["points"], reverse=True)
    GW.insert(
        0,
        {
            "player": "Player",
            "team": "Team",
            "GW points": "GW Point",
            "transfer_penalty": "Transfer Penalty",
            "points": "Total Point",
        },
    )
    # print(json.dumps(GW, indent=4))
    print(tabulate(GW))
