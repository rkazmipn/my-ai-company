import os
from google import genai
from tavily import TavilyClient

# 1. ตั้งค่า Client
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])
tavily = TavilyClient(api_key=os.environ["TAVILY_API_KEY"])

def create_content(topic):
    try:
        print(f"🔍 กำลังหาข้อมูลเรื่อง: {topic}...")
        search_result = tavily.search(query=topic, search_depth="advanced")
        
        # กรองเอาแค่เนื้อหาเน้นๆ จะได้ไม่เปลือง Token
        context = "\n".join([f"- {r['content']}" for r in search_result['results']])
        
        print("🤖 กำลังให้ Gemini เขียนบทความ...")
        
        # เปลี่ยนเป็น gemini-2.0-flash (มาตรฐานปี 2026)
        # ถ้าพี่ยังอยากใช้ 1.5 ให้ลองเปลี่ยนเป็น 'gemini-1.5-flash-latest'
        response = client.models.generate_content(
            model="models/gemini-2.5-flash", 
            contents=f"เขียนบทความภาษาไทยที่น่าสนใจเกี่ยวกับ {topic} โดยใช้ข้อมูลนี้:\n{context}\n\nเขียนในรูปแบบ Markdown"
        )
        
        filename = "src/content/post.md"
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, "w", encoding="utf-8") as f:
            f.write(response.text)
            
        print("✅ สำเร็จ! สร้างไฟล์ post.md เรียบร้อย")

    except Exception as e:
        print(f"❌ พังตรงนี้พี่: {str(e)}")
        # ถ้าพังเพราะหาโมเดลไม่เจอ ให้ลองพิมพ์ชื่อโมเดลทั้งหมดที่พี่ใช้ได้ออกมาดู
        print("รายชื่อโมเดลที่พี่ใช้ได้ตอนนี้:")
        for m in client.models.list():
            print(f"- {m.name}")
        raise e

if __name__ == "__main__":
    create_content("เจาะลึกเทคโนโลยีรถยนต์ไฟฟ้าล่าสุด 2026")
