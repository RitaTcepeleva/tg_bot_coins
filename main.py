import telebot
from pycoingecko import CoinGeckoAPI
from time import sleep
from multiprocessing import Process
import mycrawl
import CurrencyPlot


TOKEN = '1248180056:AAFnMlCgD4WaChjloUSQJWDlpjBkAUka6Z0'
bot = telebot.TeleBot(TOKEN)
cg = CoinGeckoAPI()
#Bot testing
#GROUP_ID = -491104469
#Test2
GROUP_ID = -455373776


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Hello! \nWrite /crypto to see cryptocurrency description.\n'
                                      'Write /social to follow different channels.\n'
                                      'Write /others to see other commands.')
    #print(message.chat.id)


@bot.message_handler(commands=['crypto'])
def crypto_message(message):
    bot.send_message(message.chat.id, 'You can choose such commands: \n'
                                      '/list List of supported cryptocurrencies\n'
                                      '/toptvl Top10 Farms\n'
                                      '/topreturns Top Returns Farms\n'
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

@bot.message_handler(commands=['list'])
def list_message(message):
    bot.send_message(message.chat.id, 'Supported cryptocurrencies:\n'
                                      '/eth\n/btc\n/comp\n/aave\n/snx\n/uma\n/link\n/band\n/ampl\n/yfi\n/hex2t\n/renbtc\n'
                                      '/defied\n/sushi\n/dot')

'''@bot.message_handler(commands=['bitcoin'])
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
                                                                 bit_total_supply, bit_market_cap, price_change_7d))'''

@bot.message_handler(commands=['eth'])
def eth_plot(message):
    CurrencyPlot.paint_plot('ethereum')
    usd = cg.get_price(ids='ethereum', vs_currencies='usd')['ethereum']['usd']
    img = open('foo.png', 'rb')
    bot.send_photo(message.chat.id, img, caption='Price of the last 7 days of ETH\n'
                                                 'Current price: {0}$'.format(usd))
    img.close()

@bot.message_handler(commands=['dot'])
def dot_plot(message):
    CurrencyPlot.paint_plot('polkadot')
    usd = cg.get_price(ids='polkadot', vs_currencies='usd')['polkadot']['usd']
    img = open('foo.png', 'rb')
    bot.send_photo(message.chat.id, img, caption='Price of the last 7 days of DOT\n'
                                                 'Current price: {0}$'.format(usd))
    img.close()

@bot.message_handler(commands=['band'])
def band_plot(message):
    CurrencyPlot.paint_plot('band-protocol')
    usd = cg.get_price(ids='band-protocol', vs_currencies='usd')['band-protocol']['usd']
    img = open('foo.png', 'rb')
    bot.send_photo(message.chat.id, img, caption='Price of the last 7 days of BAND\n'
                                                 'Current price: {0}$'.format(usd))
    img.close()

@bot.message_handler(commands=['aave'])
def aave_plot(message):
    CurrencyPlot.paint_plot('aave')
    usd = cg.get_price(ids='aave', vs_currencies='usd')['aave']['usd']
    img = open('foo.png', 'rb')
    bot.send_photo(message.chat.id, img, caption='Price of the last 7 days of AAVE\n'
                                                 'Current price: {0}$'.format(usd))
    img.close()

@bot.message_handler(commands=['comp'])
def comp_plot(message):
    CurrencyPlot.paint_plot('compound-governance-token')
    usd = cg.get_price(ids='compound-governance-token', vs_currencies='usd')['compound-governance-token']['usd']
    img = open('foo.png', 'rb')
    bot.send_photo(message.chat.id, img, caption='Price of the last 7 days of COMP\n'
                                                 'Current price: {0}$'.format(usd))
    img.close()

@bot.message_handler(commands=['btc'])
def btc_plot(message):
    CurrencyPlot.paint_plot('bitcoin')
    usd = cg.get_price(ids='bitcoin', vs_currencies='usd')['bitcoin']['usd']
    img = open('foo.png', 'rb')
    bot.send_photo(message.chat.id, img, caption='Price of the last 7 days of BTC\n'
                                                 'Current price: {0}$'.format(usd))
    img.close()

@bot.message_handler(commands=['renbtc'])
def renbtc_plot(message):
    CurrencyPlot.paint_plot('renbtc')
    usd = cg.get_price(ids='renbtc', vs_currencies='usd')['renbtc']['usd']
    img = open('foo.png', 'rb')
    bot.send_photo(message.chat.id, img, caption='Price of the last 7 days of RenBTC\n'
                                                 'Current price: {0}$'.format(usd))
    img.close()

@bot.message_handler(commands=['snx'])
def snx_message(message):
    CurrencyPlot.paint_plot('havven')
    usd = cg.get_price(ids='havven', vs_currencies='usd')['havven']['usd']
    img = open('foo.png', 'rb')
    bot.send_photo(message.chat.id, img, caption='Price of the last 7 days of SNX\n'
                                                 'Current price: {0}$'.format(usd))
    img.close()

@bot.message_handler(commands=['uma'])
def snx_message(message):
    CurrencyPlot.paint_plot('uma')
    usd = cg.get_price(ids='uma', vs_currencies='usd')['uma']['usd']
    img = open('foo.png', 'rb')
    bot.send_photo(message.chat.id, img, caption='Price of the last 7 days of UMA\n'
                                                 'Current price: {0}$'.format(usd))
    img.close()

@bot.message_handler(commands=['link'])
def snx_message(message):
    CurrencyPlot.paint_plot('chainlink')
    usd = cg.get_price(ids='chainlink', vs_currencies='usd')['chainlink']['usd']
    img = open('foo.png', 'rb')
    bot.send_photo(message.chat.id, img, caption='Price of the last 7 days of LINK\n'
                                                 'Current price: {0}$'.format(usd))
    img.close()

@bot.message_handler(commands=['yfi'])
def yfi_message(message):
    CurrencyPlot.paint_plot('yearn-finance')
    usd = cg.get_price(ids='yearn-finance', vs_currencies='usd')['yearn-finance']['usd']
    img = open('foo.png', 'rb')
    bot.send_photo(message.chat.id, img, caption='Price of the last 7 days of YFI\n'
                                                 'Current price: {0}$'.format(usd))
    img.close()

@bot.message_handler(commands=['sushi'])
def sushi_message(message):
    CurrencyPlot.paint_plot('sushi')
    usd = cg.get_price(ids='sushi', vs_currencies='usd')['sushi']['usd']
    img = open('foo.png', 'rb')
    bot.send_photo(message.chat.id, img, caption='Price of the last 7 days of SUSHI\n'
                                                 'Current price: {0}$'.format(usd))
    img.close()

@bot.message_handler(commands=['ampl'])
def ampl_message(message):
    CurrencyPlot.paint_plot('ampleforth')
    usd = cg.get_price(ids='ampleforth', vs_currencies='usd')['ampleforth']['usd']
    img = open('foo.png', 'rb')
    bot.send_photo(message.chat.id, img, caption='Price of the last 7 days of AMPL\n'
                                                 'Current price: {0}$'.format(usd))
    img.close()


@bot.message_handler(commands=['toptvl'])
def topfram_func(message):
    str = mycrawl.topfarms()
    bot.send_message(message.chat.id, str)

'''@bot.message_handler(commands=['degen'])
def degen_func(message):
    str = mycrawl.degen()
    bot.send_message(message.chat.id, str)'''

@bot.message_handler(commands=['topreturns'])
def degen_func(message):
    str = mycrawl.reorder_farm()
    bot.send_message(message.chat.id, str)

'''@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'hello':
        bot.send_message(message.chat.id, 'Привет, мой создатель')
    elif message.text.lower() == 'bye':
        bot.send_message(message.chat.id, 'Прощай, создатель')'''


@bot.message_handler(content_types=["new_chat_members"])
def handler_new_member(message):
    first_name = message.new_chat_members[0].first_name
    bot.send_message(message.chat.id, "Welcome, {0}!".format(first_name))


def ping():
    while True:
        bot.send_message(GROUP_ID, 'Welcome to CurrySwap.com - The Worlds first HyFi staking Kitchen 👨‍🍳👨‍🌾\n\n'
                                   'Curryswap is a high yield Multi-Dapp ecosystem built specifically for high and sustainable returns.\n\n'
                                   'Our products 🕹🎛 (Testnet is live!)\n\n'
                                   '1.) CurryChef yield farming event 👩‍🌾: User stake LP tokens and earn CURRY rewards.\n\n'
                                   '2.) Auction Lobby 🏦: Earn daily ETH rewards by simply staking your CURRY.\n\n'
                                   '3.)  Static staking pool 💰: Stake CURRY tokens directly into a pool and earn higher APY.\n\n'
                                   '4.) NFT Rewards 🦹🏿: Limited edition NFT tokens will be rewarded to users staking CURRY tokens.\n\n'
                                   'What makes us unique 🧞‍♂️🧚‍♀️🧜‍♂️\n\n'
                                   '- Multi-chain yield farming and staking. Farm on ETH, BNB & TRX! \n\n'
                                   '- Fully audited code ahead of launch. \n\n'
                                   '- Totally transparent and fair launch. \n\n'
                                   '- Full legal, marketing, business development and blockchain developers working on the project full time. \n\n'
                                   'Read more about us: https://medium.com/@curryswap/say-hello-to-curryswap-com-the-first-hyfi-staking-kitchen-1043a84c84f3\n\n'
                                   'Important links 📱⌚️🖥\n\n'
                                   'Website: https://curryswap.com \n'
                                   'Telegram chat: https://t.me/curryswapchat\n'
                                   'Twitter: https://twitter.com/curryswap\n\n'
                                   'Testnet details in pinned message\n\n'
                                   'For marketing, FAQs & business queries, please PM: @currychef')
        sleep(30*60)

if __name__ == '__main__':
    proc2 = Process(target=ping)
    proc2.start()
    bot.polling(none_stop=True)
