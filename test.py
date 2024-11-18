from openai import OpenAI
client = OpenAI(api_key="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")
system_message={
    "role": "system", "content": "너는 변호사야, 법률상담을 해줘. 주의사항은 말하지마. 한국법을 기준으로 해줘"
}
messages=[system_message]
while True:
    user_input=input("사용자 전달:")
    if user_input.lower()=="exit":
        print("대답: 즐거운 대화였어요! 감사합니다.")
        break
    messages.append({"role":"user","content":user_input})
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=messages
    )
    reply=completion.choices[0].message.content
    print("대답: " +reply)
    messages.append({"role":"assistant","content":reply})