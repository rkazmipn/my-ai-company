import os
import google.generativeai as genai
from tavily import TavilyClient

# ตั้งค่า API
tavily = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])
genai.configure(api_key=os.environ["GEMINI_API_KEY"])
model = genai.GenerativeModel('gemini-1.5-flash')

def create_content(topic):
    # 1. ค้นหาข้อมูลล่าสุด
    search_result = tavily.search(query=topic, search_depth="advanced")
    context = search_result['results']
    
    # 2. ให้ Gemini เขียนบทความจากข้อมูลที่หาได้
    prompt = f"เขียนบทความภาษาไทยที่น่าสนใจเกี่ยวกับ {topic} โดยใช้ข้อมูลนี้: {context}. เขียนในรูปแบบ Markdown"
    response = model.generate_content(prompt)
    
    # 3. บันทึกเป็นไฟล์ .md เพื่อให้หน้าเว็บนำไปแสดงผล
    filename = f"src/content/post.md"
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w", encoding="utf-8") as f:
        f.write(response.text)

if __name__ == "__main__":
    create_content("เจาะลึกเทคโนโลยีรถยนต์ไฟฟ้าล่าสุด 2026") # เปลี่ยนหัวข้อได้ที่นี่
