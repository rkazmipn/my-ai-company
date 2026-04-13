import os
from google import genai # เปลี่ยนเป็นตัวใหม่ล่าสุดปี 2026
from tavily import TavilyClient

# 1. ตั้งค่าการเชื่อมต่อ (Client)
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
tavily = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def create_content(topic):
    print(f"กำลังหาข้อมูลเรื่อง: {topic}...")
    # 2. ค้นหาข้อมูลล่าสุดจาก Tavily
    search_result = tavily.search(query=topic, search_depth="advanced")
    context = str(search_result['results'])
    
    print("กำลังให้ Gemini เขียนบทความ...")
    # 3. ใช้คำสั่งแบบใหม่ของปี 2026
    response = client.models.generate_content(
        model="gemini-1.5-flash",
        contents=f"เขียนบทความภาษาไทยที่น่าสนใจเกี่ยวกับ {topic} โดยใช้ข้อมูลนี้: {context}. เขียนในรูปแบบ Markdown"
    )
    
    # 4. บันทึกไฟล์บทความ
    filename = "src/content/post.md"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        # ใช้ .text เพื่อดึงเนื้อหาออกมา
        f.write(response.text)
    print("✅ บันทึกไฟล์สำเร็จ!")

if __name__ == "__main__":
    create_content("เจาะลึกเทคโนโลยีรถยนต์ไฟฟ้าล่าสุด 2026")
