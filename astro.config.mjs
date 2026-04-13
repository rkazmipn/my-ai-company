import { defineConfig } from 'astro/config';

export default defineConfig({
  // 1. แก้ตรงนี้ครับ: ใส่แค่ URL หลักของ GitHub Pages ของพี่ (ไม่ต้องมีชื่อโปรเจกต์ต่อท้าย)
  site: 'https://rkazmipn.github.io',
  
  // 2. ตรงนี้ถูกต้องแล้วครับ: ชื่อ Repository ของพี่
  base: '/my-ai-company',
  
  // บอกให้ Astro เก็บไฟล์ที่สร้างเสร็จแล้วไว้ในโฟลเดอร์ dist
  outDir: 'dist',
});
