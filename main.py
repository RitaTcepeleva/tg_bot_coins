import telebot
from pycoingecko import CoinGeckoAPI

bot = telebot.TeleBot('TOKEN')
cg = CoinGeckoAPI()
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello! Write /menu to see menu')

@bot.message_handler(commands=['menu'])
def menu_message(message):
    bot.send_message(message.chat.id, 'You can choose such commands: \n'
                                      '/bitcoin BTC description\n'
                                      '/ethereum ETH description\n'
                                      '/rotten ROT description\n')

@bot.message_handler(commands=['bitcoin'])
def bit_message(message):
    bit_usd = cg.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd']
    bit_eth = cg.get_price(ids='bitcoin', vs_currencies='eth')['bitcoin']['eth']
    bit_circ_sup = cg.get_coins_markets(ids='bitcoin', vs_currency='usd')[0]['circulating_supply']
    bit_percent_24 = cg.get_coins_markets(ids='bitcoin', vs_currency='usd')[0]['price_change_percentage_24h']
    price_change_7d = cg.get_coins_markets(ids='bitcoin', vs_currency='usd',price_change_percentage='7d')[0]['price_change_percentage_7d_in_currency']
    bit_total_volume = cg.get_coins_markets(ids='bitcoin', vs_currency='usd')[0]['total_volume']
    bit_total_supply = cg.get_coins_markets(ids='bitcoin', vs_currency='usd')[0]['total_supply']
    bit_market_cap = cg.get_coins_markets(ids='bitcoin', vs_currency='usd')[0]['market_cap']
    bot.send_message(message.chat.id, "Bitcoin | BTC \n"
                                      "USD: {0}$ \n"
                                      "ETH: {1} \n\n"
                                      "Price Change 24H: {4}% \n"
                                      "Price Change 7D: {7}%\n"
                                      "Total Volume: {3}$ \n"
                                      "Circulating / Total Supply: {2} / {5} \n"
                                      "Market Cap: {6}$".format(bit_usd, bit_eth, bit_circ_sup,
                                                                 bit_total_volume, bit_percent_24,
                                                                 bit_total_supply, bit_market_cap, price_change_7d))

@bot.message_handler(commands=['ethereum'])
def eth_message(message):
    usd = cg.get_price(ids='ethereum', vs_currencies='usd')['ethereum']['usd']
    btc = cg.get_price(ids='ethereum', vs_currencies='btc')['ethereum']['btc']
    price_change = cg.get_coins_markets(ids='ethereum', vs_currency='usd')[0]['price_change_percentage_24h']
    total_vol = cg.get_coins_markets(ids='ethereum', vs_currency='usd')[0]['total_volume']
    total_sup = cg.get_coins_markets(ids='ethereum', vs_currency='usd')[0]['total_supply']
    market_cap = cg.get_coins_markets(ids='ethereum', vs_currency='usd')[0]['market_cap']
    circ_sup = cg.get_coins_markets(ids='ethereum', vs_currency='usd')[0]['circulating_supply']
    price_change_7d = cg.get_coins_markets(ids='ethereum', vs_currency='usd', price_change_percentage='7d')[0]['price_change_percentage_7d_in_currency']
    bot.send_message(message.chat.id, "Ethereum | ETH \n"
                                      "USD: {0}$ \n"
                                      "BTC: {1} \n\n"
                                      "Price Change 24H: {2}%\n"
                                      "Price Change 7D: {6}%\n"
                                      "Total Volume: {3}$\n"
                                      "Circulating / Total Supply: {7} / {4}\n"
                                      "Market Cap: {5}$".format(usd, btc, price_change,
                                                                total_vol, total_sup, market_cap,
                                                                price_change_7d, circ_sup))

@bot.message_handler(commands="rotten")
def rot_message(message):
    usd = cg.get_price(ids='rotten', vs_currencies='usd')['rotten']['usd']
    eth = cg.get_price(ids='rotten', vs_currencies='eth')['rotten']['eth']
    btc = cg.get_price(ids='rotten', vs_currencies='btc')['rotten']['btc']
    price_24 = cg.get_coins_markets(ids='rotten', vs_currency='usd')[0]['price_change_percentage_24h']
    price_7 = cg.get_coins_markets(ids='rotten', vs_currency='usd', price_change_percentage='7d')[0]['price_change_percentage_7d_in_currency']
    total_vol = cg.get_coins_markets(ids='rotten', vs_currency='usd')[0]['total_volume']
    circ_sup = cg.get_coins_markets(ids='rotten', vs_currency='usd')[0]['circulating_supply']
    total_sup = cg.get_coins_markets(ids='rotten', vs_currency='usd')[0]['total_supply']
    market_cap = cg.get_coins_markets(ids='rotten', vs_currency='usd')[0]['market_cap']
    bot.send_message(message.chat.id, "Rotten | ROT\n"
                                      "USD: {0}$\n"
                                      "BTC: {1}\n"
                                      "ETH: {2}\n\n"
                                      "Price Change 24H: {3}%\n"
                                      "Price Change 7D: {4}%\n"
                                      "Total Volume: {5}$\n"
                                      "Circulating / Total Supply: {6} / {7}\n"
                                      "Market Cap: {8}$".format(usd, btc, eth,
                                                                price_24, price_7,
                                                                total_vol, circ_sup,total_sup,market_cap))

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'bye':
        bot.send_message(message.chat.id, 'Прощай, создатель')

@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    first_name = message.new_chat_members[0].first_name
    bot.send_message(message.chat.id, "Glad to see you, {0}!".format(first_name))

if __name__ == '__main__':
    bot.polling(none_stop=True)