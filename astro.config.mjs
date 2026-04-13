import { defineConfig } from 'astro/config';

export default defineConfig({
  // 1. เปลี่ยน 'YOUR_USERNAME' เป็นชื่อบัญชี GitHub ของพี่
  site: 'https://github.com/rkazmipn/my-ai-company/',
  
  // 2. เปลี่ยน 'YOUR_REPO_NAME' เป็นชื่อโปรเจกต์ (Repository) ที่พี่ตั้งไว้
  // เช่น /ai-media-company (ต้องมีเครื่องหมาย / ข้างหน้าด้วย)
  base: '/my-ai-company',
  
  // บอกให้ Astro เก็บไฟล์ที่สร้างเสร็จแล้วไว้ในโฟลเดอร์ dist
  outDir: 'dist',
});
