import sys
import keyring
import keyring.backend
import json
import xerox
import pyotp
import datetime
import sys
from urllib.parse import parse_qs, urlparse
from pynput.keyboard import Key, Controller
from time import sleep


class LocalKeyring(keyring.backend.KeyringBackend):
    priority = 1

    def set_password(self, servicename, username, password):
        try:
            with open("./keyring.json", "r") as f:
                keyring = json.loads(f.read())
        except:
            keyring = dict()
        if servicename not in keyring:
            keyring[servicename] = dict()
        keyring[servicename][username] = password
        with open("./keyring.json", "w") as f:
            f.write(json.dumps(keyring))

    def get_password(self, servicename, username):
        with open("./keyring.json", "r") as f:
            keyring = json.loads(f.read())
        return keyring[servicename][username]

    def delete_password(self, servicename, username):
        with open("./keyring.json", "r") as f:
            keyring = json.loads(f.read())
        if servicename in keyring:
            keyring[servicename].pop(username, None)
        with open("./keyring.json", "w") as f:
            f.write(json.dumps(keyring))


def set_keyring():
    # Set the keyring backend to a local file if a credential store is not installed.
    try:
        keyring.set_password("test", "test", "test")
        keyring.delete_password("test", "test")
    except:
        keyring.set_keyring(LocalKeyring())


def c():
    set_keyring()
    keyring.set_password(sys.argv[1], sys.argv[2], sys.argv[3])


def u():
    set_keyring()
    output = keyring.get_password("u", sys.argv[1])
    out(output)


def p():
    set_keyring()
    output = keyring.get_password("p", sys.argv[1])
    out(output)


def o():
    set_keyring()
    otp_url = keyring.get_password("o", sys.argv[1])
    secret = parse_qs(urlparse(otp_url).query)["secret"][0]
    totp = pyotp.TOTP(secret)
    totp.interval - datetime.datetime.now().timestamp() % totp.interval
    output = totp.now()
    out(output)


def out(output):
    keyboard = Controller()
    for character in output:
        if character.isupper():
            keyboard.press(Key.shift)
            sleep(0.05)
            keyboard.press(character.lower())
            sleep(0.02)
            keyboard.release(character.lower())
            keyboard.release(Key.shift)
            sleep(0.05)
        else:
            keyboard.type(character)
        sleep(0.05)
    xerox.copy(output)


if __name__ == "__main__":
    sys.argv.pop(0)
    if sys.argv[0] == "c":
        c()
    elif sys.argv[0] == "u":
        u()
    elif sys.argv[0] == "p":
        p()
    elif sys.argv[0] == "o":
        o()
