import os 
import sys 
import time 
import base64 
import random 
import shutil
import datetime

sys.path.append(os.path.abspath("assets"))
import console
import script
import install

try:
  import requests
  try:
    import yaml
    try:
      import faker
      from faker import Faker 
      try:
        r = requests.get(script.URLS, timeout=1)
        if r.status_code <= 50 or r.status_code >= 250:
          console.log("[{}] Server tidak ditemukan!".format(datetime.datetime.now().strftime(script.FORMAT)))
        else:
          while True:
            try:
              file = open("{}/.data.txt".format(script.PATH))
              os.system("clear")
              print(script.RANDOM_ICONS)
              print("[ MASUK ]")
              email = raw_input("[?] Email: ")
              try:
                r = requests.get(script.URLS, timeout=1)
                dec_data = base64.b64decode(r.content)
                data = yaml.safe_load(dec_data)
                try:
                  ACCOUNT = data["data"][email]
                  if "Removed" in ACCOUNT:
                    console.log("[{}] Account ini telah di hapus".format(datetime.datetime.now().strftime(script.FORMAT)))
                  else:
                    password = raw_input("[?] Password: ")
                    if password == data["data"][email]["Password"]:
                      os.system("clear")
                      print(script.RANDOM_ICONS)
                      print("\t=[ vhacks v4.0-dev\n+ -- ---=[ Email: {} - Username: {}\n+ -- ---=[ HackCoin: {}".format(email, data["data"][email]["Username"], data["data"][email]["HackCoin"]))
                      while True:
                        p2 = raw_input("\n{}@vhacks ~ #".format(data["data"][email]["Username"]))
                        try:
                          r = requests.get(script.URLS)
                          if p2 == "clear":
                            os.system("clear")
                          elif p2 == "icon":
                            print(script.RANDOM_ICONS)
                          else:
                            console.log("[{}] Command not found!".format(datetime.datetime.now().strftime(script.FORMAT)))
                        except requests.exceptions.ConnectionError:
                          console.log("[{}] Tidak ada koneksi!".format(datetime.datetim.now().strftime(script.FORMAT)))
                    else:
                      console.log("[{}] Password yang anda masukan salah!".format(datetime.datetime.now().strftime(script.FORMAT)))
                except KeyError:
                  console.log("[{}] Email ini belum terdaftar!".format(datetime.datetime.now().strftime(script.FORMAT)))
              except requests.exceptions.ConnectionError:
                console.log("[{}] Tidak ada koneksi!".format(datetime.datetime.now().strftime(script.FORMAT)))
              except requests.exceptions.ReadTimeout:
                console.log("[{}] Meminta waktu habis!".format(datetime.datetime.now().strftime(script.FORMAT)))
            except IOError:
              os.system("clear")
              print(script.RANDOM_ICONS)
              print("[ DAFTAR ]")
              new_email = raw_input("[+] Your Email: ")
              if len(new_email) <= 4:
                console.log("[{}] Email yang anda masukan terlalu pendek!".format(datetime.datetime.now().strftime(script.FORMAT)))
              elif len(new_email) >= 4:
                try:
                  r = requests.get(script.URLS, timeout=1)
                  dec_data = base64.b64decode(r.content)
                  if new_email in dec_data:
                    console.log("[{}] Email ini sudah digunakan!".format(datetime.datetime.now().strftime(script.FORMAT)))
                  else:
                    new_username = raw_input("[+] New Username: ")
                    if len(new_username) <= 4:
                      console.log("[{}] Username yang anda masukan terlalu pendek!".format(datetime.datetime.now().strftime(script.FORMAT)))
                    elif len(new_username) >= 4:
                      try:
                        r = requests.get(script.URLS, timeout=1)
                        dec_data = base64.b64decode(r.content)
                        if new_username in dec_data:
                          console.log("[{}] Username ini sudah digunakan!".format(datetime.datetime.now().strftime(script.FORMAT)))
                        else:
                          new_password = raw_input("[+] New Password: ")
                          if len(new_password) <= 4:
                            console.log("[{}] Password yang anda masukan terlalu pendek!".format(datetime.datetime.now().strftime(script.FORMAT)))
                          elif len(new_password) >= 4:
                            try:
                              r = requests.get(script.URLS, timeout=1)
                              dec_data = base64.b64decode(r.content)
                              data = "\n  {}:\n    Username: {}\n    HackCoin: 0\n    Password: {}\n    IP: {}".format(new_email, new_username, new_password, Faker().ipv4())
                              combine = dec_data + data
                              try:
                                enc_data = base64.b64encode(combine)
                                r = script.SESSION.put(script.URLS,data=enc_data, timeout=1)
                                if r.status_code <= 50 or r.status_code >= 250:
                                  console.log("[{}] Gagal membuat account".format(datetime.datetime.now().strftime(script.FORMAT)))
                                else:
                                  os.makedirs(script.PATH)
                                  save = open("{}/.data.txt".format(script.PATH), "w")
                                  save.write(base64.b64encode("#Don't delete this file!"))
                                  save.close()
                                  console.log("[{}] Berhasil membuat account!".format(datetime.datetime.now().strftime(script.FORMAT)))
                              except requests.exceptions.ConnectionError:
                                console.log("[{}] Tidak ada koneksi!".format(datetime.datetime.now().strftime(script.FORMAT)))
                              except requests.exceptions.ReadTimeout:
                                console.log("[{}] Meminta waktu habis!".format(datetime.datetime.now().strftime(script.FORMAT)))
                            except requests.exceptions.ConnectionError:
                              console.log("[{}] Tidak ada koneksi!".format(datetime.datetime.now().strftime(script.FORMAT)))
                            except requests.exceptions.ReadTimeout:
                              console.log("[{}] Meminta waktu habis!".format(datetime.datetime.now().strftime(script.FORMAT)))
                          else:
                            console.log("[{}] Error!".format(datetime.datetime.now().strftime(script.FORMAT)))
                      except requests.exceptions.ConnectionError:
                        console.log("[{}] Tidak ada koneksi!".format(datetime.datetime.now().strftime(script.FORMAT)))
                      except requests.exceptions.ReadTimeout:
                        console.log("[{}] Meminta waktu habis!".format(datetime.datetime.now().strftime(script.FORMAT)))
                    else:
                      console.log("[{}] Error!".format(datetime.datetime.now().strftime(script.FORMAT)))
                except requests.exceptions.ConnectionError:
                  console.log("[{}] Tidak ada koneksi!".format(datetime.datetime.now().strftime(script.FORMAT)))
                except requests.exceptions.ReadTimeout:
                  console.log("[{}] Meminta waktu habis!".format(datetime.datetime.now().strftime(script.FORMAT)))
      except requests.exceptions.ConnectionError:
        console.log("[{}] Tidak ada koneksi!".format(datetime.datetime.now().strftime(script.FORMAT)))
      except requests.exceptions.ReadTimeout:
        console.log("[{}] Meminta waktu habis!".format(datetime.datetime.now().strftime(script.FORMAT)))
      except KeyboardInterrupt:
        console.log("[{}] System stopped.".format(datetime.datetime.now().strftime(script.FORMAT)))
    except ImportError:
      os.system(install.FAKER)
  except ImportError:
    os.system(install.YAML)
except ImportError:
  os.system(install.REQUESTS)