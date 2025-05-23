from google import genai
import tkinter

winodw = tkinter.Tk()
winodw.title("あいうえお作文生成")


def on_button_click():
    print("ボタンがクリックされました！")


button = tkinter.Button(
    winodw, text="作成！！", width=50, height=2, command=on_button_click
)
button.pack(side=tkinter.BOTTOM, pady=20)
winodw.geometry("400x300")




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
