import time

def bar():
  print("")
  print("========================")
  print("")

print("ツンデレな文章を入れてください")
tsundere_word = input()

bar()

print("それを言わせたい萌えるような女の子の名前を入れてください")
girl_name = input()

bar()

print(f'{girl_name}「{tsundere_word}」')
print("")

time.sleep(2)

print("ナイス ツンデレ .ﾟ+.(´∀｀*).+ﾟ.")

