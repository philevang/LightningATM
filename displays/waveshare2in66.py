#!/usr/bin/python3

import time
import math

import config
import utils

from displays import messages

from PIL import Image, ImageFont, ImageDraw


def update_startup_screen():
    """Show startup screen on eInk Display
    """
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.text(
        (20, 4),
        messages.startup_screen_1,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )
    draw.text(
        (4, 30),
        messages.startup_screen_2,
        fill=config.BLACK,
        font=utils.create_font("sawasdee", 48),
    )
    draw.text(
        (8, 130),
        messages.startup_screen_3,
        fill=config.BLACK,
        font=utils.create_font("freemono", 20),
    )

    config.WAVESHARE.init(0)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))

def error_screen(message="ERROR"):
    """Error screen
    """
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.text(
        (18, 13),
        messages.error_screen_1,
        fill=config.BLACK,
        font=utils.create_font("freemono", 25),
    )
    draw.text(
        (12, 30),
        message,
        fill=config.BLACK,
        font=utils.create_font("freemono", 16),
    )

    config.WAVESHARE.init(config.WAVESHARE.FULL_UPDATE)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))
    
    
def update_qr_request():
    # initially set all white background
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.rectangle(
        (2, 2, width - 2, height - 2), fill=config.WHITE, outline=config.BLACK
    )
    draw.text(
        (46, 4),
        messages.qr_request_1,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )
    draw.text(
        (16, 34),
        messages.qr_request_2,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )

    config.WAVESHARE.init(1)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))

    for i in range(0, 3):
        draw.text(
            (122, 70),
            str(3 - i),
            fill=config.BLACK,
            font=utils.create_font("freemono", 84),
        )
        config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))
        draw.rectangle((125, 70, 170, 148), fill=config.WHITE, outline=config.WHITE)
        time.sleep(0.5)

    draw.rectangle(
        (2, 2, width - 2, height - 2), fill=config.WHITE, outline=config.BLACK
    )
    draw.text(
        (16, 35),
        messages.qr_request_3,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )
    draw.text(
        (16, 65),
        messages.qr_request_4 + str(math.floor(config.SATS)) + messages.qr_request_5,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )
    config.WAVESHARE.init(1)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))


def update_qr_failed():
    # initially set all white background
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.rectangle(
        (2, 2, width - 2, height - 2), fill=config.WHITE, outline=config.BLACK
    )

    draw.text(
        (16, 40),
        messages.qr_failed_1,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )
    draw.text(
        (16, 70),
        messages.qr_failed_2,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )

    config.WAVESHARE.init(0)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))


def update_payout_screen():
    """Update the payout screen to reflect balance of deposited coins.
    Scan the invoice??? I don't think so!
    """
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.rectangle(
        (2, 2, width - 2, height - 2), fill=config.WHITE, outline=config.BLACK
    )
    draw.text(
        (16, 40),
        str(math.floor(config.SATS)) + messages.payout_screen_1,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )
    draw.text(
        (16, 70),
        messages.payout_screen_2,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )

    config.WAVESHARE.init(0)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))

    # scan the invoice
    # TODO: I notice this is commented out, I presume this function should _not_ be
    #   scanning a QR code on each update?
    # config.INVOICE = qr.scan()


def update_payment_failed():
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.text(
        (10, 10),
        messages.payment_failed_1,
        fill=config.BLACK,
        font=utils.create_font("freemono", 32),
    )
    draw.text(
        (10, 90),
        messages.payment_failed_2,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )
    draw.text(
        (10, 120),
        messages.payment_failed_3,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )

    config.WAVESHARE.init(0)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))


def update_thankyou_screen():
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.text(
        (12, 15),
        messages.thankyou_screen_1,
        fill=config.BLACK,
        font=utils.create_font("freemono", 32),
    )
    draw.text(
        (47, 47),
        messages.thankyou_screen_2,
        fill=config.BLACK,
        font=utils.create_font("freemono", 32),
    )
    draw.text(
        (15, 125),
        messages.thankyou_screen_3,
        fill=config.BLACK,
        font=utils.create_font("freemono", 24),
    )

    config.WAVESHARE.init(0)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))
    time.sleep(5)


def update_nocoin_screen():
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.text(
        (15, 15),
        messages.nocoin_screen_1,
        fill=config.BLACK,
        font=utils.create_font("freemonobold", 30),
    )
    draw.text(
        (50, 72),
        messages.nocoin_screen_2,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )
    draw.text(
        (50, 102),
        messages.nocoin_screen_3,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )

    config.WAVESHARE.init(0)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))


def update_lnurl_generation():
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.rectangle(
        (2, 2, width - 2, height - 2), fill=config.WHITE, outline=config.BLACK
    )
    draw.text(
        (14, 40),
        messages.lnurl_generation_1,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )
    draw.text(
        (14, 68),
        messages.lnurl_generation_2,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )

    config.WAVESHARE.init(0)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))


def update_shutdown_screen():
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.text(
        (10, 10),
        messages.shutdown_screen_1,
        fill=config.BLACK,
        font=utils.create_font("freemono", 32),
    )
    draw.text(
        (10, 90),
        messages.shutdown_screen_2,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )
    draw.text(
        (10, 120),
        messages.shutdown_screen_3,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )

    config.WAVESHARE.init(0)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))


def update_wallet_scan():
    # initially set all white background
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.rectangle(
        (2, 2, width - 2, height - 2), fill=config.WHITE, outline=config.BLACK
    )
    draw.text(
        (42, 25),
        messages.wallet_scan_1,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )
    draw.text(
        (42, 55),
        messages.wallet_scan_2,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )
    draw.text(
        (42, 85),
        messages.wallet_scan_3,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )

    config.WAVESHARE.init(0)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))
    time.sleep(2)


def update_lntxbot_balance(balance):
    # initially set all white background
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.rectangle(
        (2, 2, width - 2, height - 2), fill=config.WHITE, outline=config.BLACK
    )
    draw.text(
        (60, 15),
        messages.lntxbot_balance_1,
        fill=config.BLACK,
        font=utils.create_font("freemonobold", 30),
    )
    draw.text(
        (8, 65),
        messages.lntxbot_balance_2,
        fill=config.BLACK,
        font=utils.create_font("freemono", 22),
    )
    draw.text(
        (8, 87),
        str("{:,}".format(balance)) + messages.lntxbot_balance_3,
        fill=config.BLACK,
        font=utils.create_font("freemono", 22),
    )

    config.WAVESHARE.init(0)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))
    time.sleep(3)


def update_btcpay_lnd():
    # initially set all white background
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.rectangle(
        (2, 2, width - 2, height - 2), fill=config.WHITE, outline=config.BLACK
    )
    draw.text(
        (60, 15),
        messages.btcpay_lnd_1,
        fill=config.BLACK,
        font=utils.create_font("freemonobold", 30),
    )
    draw.text(
        (10, 65),
        messages.btcpay_lnd_2,
        fill=config.BLACK,
        font=utils.create_font("freemono", 22),
    )
    draw.text(
        (10, 87),
        messages.btcpay_lnd_3,
        fill=config.BLACK,
        font=utils.create_font("freemono", 22),
    )

    config.WAVESHARE.init(0)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))
    time.sleep(3)


def draw_lnurl_qr(qr_img):
    """Draw a lnurl qr code on the e-ink screen
    """
    image, width, height, draw = init_screen(color=config.BLACK)

    qr_img = qr_img.resize((152, 152), resample=0)

    draw = ImageDraw.Draw(image)
    draw.bitmap((0, 0), qr_img, fill=config.WHITE)
    draw.text(
        (160, 40),
        messages.lnurl_qr_1,
        fill=config.WHITE,
        font=utils.create_font("freemonobold", 28),
    )
    draw.text(
        (160, 68),
        messages.lnurl_qr_2,
        fill=config.WHITE,
        font=utils.create_font("freemonobold", 28),
    )

    config.WAVESHARE.init(0)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))


def update_amount_screen():
    """Update the amount screen to reflect new coins inserted
    """
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.rectangle(
        (2, 2, width - 2, height - 2), fill=config.WHITE, outline=config.BLACK
    )
    draw.text(
        (12, 12),
        str("{:,}".format(math.floor(config.SATS))) + messages.amount_screen_1,
        fill=config.BLACK,
        font=utils.create_font("dotmbold", 36),
    )
    draw.text(
        (12, 48),
        "%.2f" % round(config.FIAT, 2) + " " + config.conf["atm"]["cur"].upper(),
        fill=config.BLACK,
        font=utils.create_font("dotmbold", 36),
    )
    draw.text(
        (12, 104),
        messages.amount_screen_2,
        fill=config.BLACK,
        font=utils.create_font("freemono", 22),
    )
    draw.text(
        (80, 104),
        messages.amount_screen_3
        + str(math.floor(config.SATPRICE))
        + messages.amount_screen_4
        + config.conf["atm"]["centname"],
        fill=config.BLACK,
        font=utils.create_font("freemono", 22),
    )
    draw.text(
        (12, 126),
        messages.amount_screen_5,
        fill=config.BLACK,
        font=utils.create_font("freemono", 22),
    )
    draw.text(
        (80, 126),
        messages.amount_screen_6
        + config.conf["atm"]["fee"]
        + messages.amount_screen_7
        + str(math.floor(config.SATSFEE))
        + messages.amount_screen_8,
        fill=config.BLACK,
        font=utils.create_font("freemono", 22),
    )

    if config.COINCOUNT == 1:
        config.WAVESHARE.init(0)
        config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))
    else:
        config.WAVESHARE.init(1)
        config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))


def update_lnurl_cancel_notice():
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.text(
        (12, 10),
        messages.lnurl_cancel_notice_1,
        fill=config.BLACK,
        font=utils.create_font("freemono", 27),
    )
    draw.text(
        (8, 105),
        messages.lnurl_cancel_notice_2,
        fill=config.BLACK,
        font=utils.create_font("freemono", 20),
    )
    draw.text(
        (8, 125),
        messages.lnurl_cancel_notice_3,
        fill=config.BLACK,
        font=utils.create_font("freemono", 20),
    )

    config.WAVESHARE.init(0)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))


def update_button_fault():
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.text(
        (15, 15),
        messages.button_fault_1,
        fill=config.BLACK,
        font=utils.create_font("freemonobold", 30),
    )
    draw.text(
        (15, 72),
        messages.button_fault_2,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )
    draw.text(
        (15, 102),
        messages.button_fault_3,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )

    config.WAVESHARE.init(0)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))


def update_wallet_fault():
    image, width, height, draw = init_screen(color=config.WHITE)

    draw.text(
        (15, 15),
        messages.wallet_fault_1,
        fill=config.BLACK,
        font=utils.create_font("freemonobold", 30),
    )
    draw.text(
        (15, 72),
        messages.wallet_fault_2,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )
    draw.text(
        (15, 102),
        messages.wallet_fault_3,
        fill=config.BLACK,
        font=utils.create_font("freemono", 30),
    )

    config.WAVESHARE.init(0)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))


def update_blank_screen():
    image, width, height, draw = init_screen(color=config.WHITE)

    config.WAVESHARE.init(0)
    config.WAVESHARE.display(config.WAVESHARE.getbuffer(image))


def init_screen(color):
    """Prepare the screen for drawing and return the draw variables
    """
    image = Image.new("1", (config.WAVESHARE.height, config.WAVESHARE.width), color)
    # Set width and height of screen
    width, height = image.size
    # prepare for drawing
    draw = ImageDraw.Draw(image)
    return image, width, height, draw
