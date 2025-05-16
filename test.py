from google import genai

client = genai.Client(api_key="API KEY入れてね")

response = client.models.generate_content(
    model="gemini-2.0-flash", 
    contents="あいうえお作文を作成してください。\
            テーマはあなたが決めてください。\
            例に習って記述してください。\n\nあ：あなたの笑顔が\nい：いつも私を\nう：嬉しくさせる\nえ：笑顔の理由は\nお：お互いの信頼\
            あいうえお作文のみを記述してください。",
)
print(response.text)