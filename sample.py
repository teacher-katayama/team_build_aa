import tkinter
from tkinter import ttk

from google import genai

winodw = tkinter.Tk()
winodw.title("あいうえお作文生成")

def on_select(event):
    selected = combo.get()
    print(f"選択された文字: {selected}")


winodw.title("ランダム作文")

# 選択肢リスト
choices = [
    "あ行",
    "か行",
    "さ行",
    "た行",
    "な行",
    "は行",
    "ま行",
    "や行",
    "ら行",
    "わ行",
]

combo = ttk.Combobox(
    winodw, values=choices, state="readonly"
)  # readonlyにすると直接入力できない
combo.current(0)  # 初期選択は「あ」
combo.pack(padx=20, pady=20)

combo.bind("<<ComboboxSelected>>", on_select)

winodw.mainloop()

client = genai.Client(api_key="")

response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents="あいうえお作文を作成してください。\
            テーマはあなたが決めてください。\
            いろいろなテーマにしてください。\
            例に習って記述してください。\n\nあ：あなたの笑顔が\nい：いつも私を\nう：嬉しくさせる\nえ：笑顔の理由は\nお：お互いの信頼\
            あいうえお作文のみを記述してください。\
            ひとつのみ記述してください。",
)
print(response.text)
