import telebot
from pycoingecko import CoinGeckoAPI
from time import sleep
from multiprocessing import Process
import CurrencyPlot

TOKEN = '1248180056:AAFnMlCgD4WaChjloUSQJWDlpjBkAUka6Z0'
bot = telebot.TeleBot(TOKEN)
cg = CoinGeckoAPI()
#Bot testing
GROUP_ID = -491104469
#Test2
#GROUP_ID = -455373776

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello! \nWrite /crypto to see cryptocurrency description.\n'
                                      'Write /social to follow different channels.\n'
                                      'Write /others to see other commands.')
    #print(message.chat.id)


@bot.message_handler(commands=['crypto'])
def crypto_message(message):
    bot.send_message(message.chat.id, 'You can choose such commands: \n'
                                      '/bitcoin BTC description\n'
                                      '/ethereum ETH description\n'
                                      '/rotten ROT description\n'
                                      '/ama AMA description\n'
                                      '/nft NFTs description')

@bot.message_handler(commands=['social'])
def social_message(message):
    bot.send_message(message.chat.id, 'You can choose such commands: \n'
                                      '/twitter Follow twitter\n'
                                      '/youtube Follow YouTube\n'
                                      '/telegram Follow Telegram')

@bot.message_handler(commands=['others'])
def others_message(message):
    bot.send_message(message.chat.id, 'You can choose such commands: \n'
                                      '/r2b Ready to rumble proposal\n'
                                      '/faq FAQ\n'
                                      '/rules Rules')

@bot.message_handler(commands=['bitcoin'])
def bit_message(message):
    bit_usd = cg.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd']
    bit_eth = cg.get_price(ids='bitcoin', vs_currencies='eth')['bitcoin']['eth']
    bit_circ_sup = cg.get_coins_markets(ids='bitcoin', vs_currency='usd')[0]['circulating_supply']
    bit_percent_24 = cg.get_coins_markets(ids='bitcoin', vs_currency='usd')[0]['price_change_percentage_24h']
    price_change_7d = cg.get_coins_markets(ids='bitcoin', vs_currency='usd', price_change_percentage='7d')[0]['price_change_percentage_7d_in_currency']
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

@bot.message_handler(commands=["rotten"])
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
                                                                total_vol, circ_sup,total_sup,
                                                                market_cap))

@bot.message_handler(commands=['etherplot'])
def eth_plot(message):
    CurrencyPlot.paint_plot('ethereum')
    usd = cg.get_price(ids='ethereum', vs_currencies='usd')['ethereum']['usd']
    img = open('foo.png', 'rb')
    bot.send_photo(message.chat.id, img, caption='Price of the last 7 days of ETH\n'
                                                 'Current price: {0}$'.format(usd))
    img.close()

@bot.message_handler(commands=['aaveplot'])
def aave_plot(message):
    CurrencyPlot.paint_plot('aave')
    usd = cg.get_price(ids='aave', vs_currencies='usd')['aave']['usd']
    img = open('foo.png', 'rb')
    bot.send_photo(message.chat.id, img, caption='Price of the last 7 days of AAVE\n'
                                                 'Current price: {0}$'.format(usd))
    img.close()

@bot.message_handler(commands=['compplot'])
def comp_plot(message):
    CurrencyPlot.paint_plot('compound-governance-token')
    usd = cg.get_price(ids='compound-governance-token', vs_currencies='usd')['compound-governance-token']['usd']
    img = open('foo.png', 'rb')
    bot.send_photo(message.chat.id, img, caption='Price of the last 7 days of COMP\n'
                                                 'Current price: {0}$'.format(usd))
    img.close()



@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'bye':
        bot.send_message(message.chat.id, 'Прощай, создатель')


@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    first_name = message.new_chat_members[0].first_name
    bot.send_message(message.chat.id, "Welcome, {0}!".format(first_name))


def ping():
    while True:
        bot.send_message(GROUP_ID, 'Testing message')
        sleep(30*60)

if __name__ == '__main__':
    proc2 = Process(target=ping)
    proc2.start()
    bot.polling(none_stop=True)
