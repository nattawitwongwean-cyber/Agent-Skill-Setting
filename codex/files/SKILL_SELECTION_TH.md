# คู่มือเลือกทักษะอัตโนมัติสำหรับ Codex และ Hermes

เป้าหมาย: ผู้ใช้ไม่ต้องจำชื่อทักษะ ระบบต้องเลือกเองจากเจตนางานก่อนเสมอ ถ้าผู้ใช้ต้องการกำหนดเอง ให้ใช้ตารางนี้เป็นคำอธิบายภาษาไทยแบบสั้นและตรง

## หลักการใช้งานอัตโนมัติ

1. ถ้าผู้ใช้บอกงานธรรมชาติ เช่น `ช่วยวางแผน`, `แก้บั๊ก`, `ลดโทเคน`, `ทำงานเป็นทีม`, `ทำข่าว AI`, ระบบต้องเลือกทักษะเอง
2. ถ้าผู้ใช้เรียกชื่อทักษะโดยตรง ให้ใช้ทักษะนั้น แต่ถ้าเป็นชื่อซ้ำ/ชื่อเก่า ให้ resolve ไป canonical skill ก่อน
3. ใช้ทักษะให้น้อยที่สุดที่พอทำงานได้ ไม่โหลดทุกทักษะพร้อมกัน
4. งานยาว งานเสี่ยง งานแก้โค้ด ต้องมี verification ก่อนบอกว่าสำเร็จ
5. ถ้าโควต้าหรือบริบทเริ่มเสี่ยง ให้เปิดทักษะลดโทเคน/บีบบริบท/checkpoint โดยอัตโนมัติ

## ทักษะหลักที่ควรใช้เป็นค่าเริ่มต้น

| สถานการณ์ที่ผู้ใช้พูด | ทักษะหลัก | คำอธิบายภาษาไทย | หมายเหตุ |
|---|---|---|---|
| วางแผน, ออกแบบงาน, ทำ roadmap | `writing-plans` | วางแผนเป็นขั้นตอน มีขอบเขต งานย่อย และ test plan | ใช้ก่อนลงมือเมื่อ scope ใหญ่ |
| ยังไม่ชัดว่าจะทำทางไหนดี | `brainstorming` | สำรวจทางเลือกก่อนตัดสินใจ ลดการแก้ผิดทาง | เหมาะกับงานเสี่ยงหรือมีหลายทาง |
| แก้บั๊ก, ระบบพัง, หาสาเหตุ | `systematic-debugging` | ไล่ปัญหาเป็นหลักฐาน ไม่เดาเร็วเกินไป | ต้องมี hypothesis/test/evidence |
| เขียนโค้ดหรือแก้โค้ดที่ต้องมั่นใจ | `test-driven-development` | ให้คิด test/verification ก่อนหรือระหว่างแก้ | ไม่จำเป็นต้อง TDD เต็มทุกงาน แต่ต้องตรวจผล |
| ทำตามแผนที่อนุมัติแล้ว | `executing-plans` | ลงมือทีละขั้นตามแผนและอัปเดตสถานะ | ใช้กับงานยาว/หลายไฟล์ |
| ก่อนบอกว่าเสร็จ | `verification-before-completion` | ห้ามสรุปว่าสำเร็จถ้ายังไม่มีหลักฐานสด | สำคัญมากกับงานโค้ด/deploy |
| รันคำสั่ง shell/terminal/ssh | `rtk-shell-guard` | บังคับใช้ `rtk` เพื่อลด token และจัด output ให้อ่านง่าย | ใช้เสมอกับ shell command |
| ลดโทเคน/ตอบไทยกระชับ | `thai-token-optimizer` | ภาษาไทยกระชับ แต่ไม่ตัดสาระสำคัญ | ค่าเริ่มต้นสำหรับคำตอบภาษาไทย |
| ต้องสั้นมาก/โควต้าเสี่ยง | `caveman` | โหมดอัดสั้นมาก ใช้เมื่อผู้ใช้สั่งหรือ quota pressure สูง | อย่าใช้กับงานที่ต้องอธิบายละเอียด |
| บริบทเริ่มยาว/งานต่อเนื่อง | `context-compression-checkpoint` | บีบบริบทและทำ checkpoint เพื่อทำงานต่อไม่หลุด | canonical ของกลุ่ม context compression |
| เริ่มโปรเจกต์ใหม่/อ่าน repo ใหม่ | `context-bootstrap` | จัดบริบทเริ่มต้นให้สั้นและเป็นระบบ | ใช้ตอน onboarding โปรเจกต์ |
| ส่งต่องาน/ย้ายงาน/สรุปให้ทำต่อ | `handoff` | สรุปสถานะงานเพื่อส่งต่อแบบกระชับ | เหมาะกับย้ายไป Codex/Hermes/เครื่องอื่น |
| รายงานท้ายงาน | `adaptive-task-reporting` | รายงานตามขนาดงาน มี model/route/หลักฐาน/สิ่งที่เปลี่ยน | ลดรายงานย้อนแย้ง |
| รายงานโควต้า/โมเดล/route | `quota-truth-reporting` | รายงานจาก runtime truth/live source เท่านั้น ไม่เดา | ถ้า source stale ต้องบอก stale/unavailable |
| งานใหญ่ อยากให้ทำเป็นทีม | `teamwork-preview-goal` | แตกงานแบบ Antigravity teamwork-preview มีเป้าหมาย/ขอบเขต/ผู้ตรวจ | ใช้ก่อน dispatch งานใหญ่ |
| ส่งงานให้ subagent | `subagent-driven-development` | มอบหมาย subagent แบบ micro-plan มี scope/output/verification | ใช้เมื่อแบ่งงานเป็นอิสระได้ |
| งาน GitHub, repo, issue, PR | `github-workflows` | ใช้ GitHub เป็น source of truth ตรวจ repo/issue/PR/branch | สำหรับ workflow แบบ backup/PR |
| ข่าว AI / NEW AI | `news-new-ai-digest` | สรุปข่าว AI ภาษาไทยสำหรับครู มี glossary และประโยชน์ต่อ Hermes | ห้ามสรุปอังกฤษล้วน |
| งานโรงเรียน/แผนสอน/ข้อสอบ | `teacher-thai-workflow` | จัดงานครูเป็นไทย แยกขั้นตอน งานสอน งานนักเรียน เอกสาร | เหมาะกับ non-technical workflow |
| Google Drive/Docs/Sheets/Calendar/Tasks | `google-workspace-intake` | รับไฟล์/ข้อความ/OCR แล้วแยกเป็น Drive/Docs/Tasks/Calendar | ถ้าวันเวลาไม่มั่นใจต้องถามยืนยัน |
| UI/UX, หน้าเว็บ, dashboard, mobile | `ui-ux-pro-max` | ช่วยออกแบบ UI/UX ให้สวย ใช้งานง่าย มี hierarchy | ใช้ร่วมกับ frontend skills ได้ |
| สร้าง prompt ภาพ/โปสเตอร์/ภาพประกอบ | `gpt-image-prompt-library` | ช่วยทำ prompt ภาพที่ละเอียด คุมสไตล์/องค์ประกอบ | ไม่ใช่ตัว generate ภาพโดยตรงเสมอไป |
| เลือกโมเดล/route/fallback | `adaptive-model-routing` | เลือกโมเดลตามงานและโควต้า ไม่ใช้ตัวใหญ่เกินจำเป็น | ใช้กับคำถามเรื่องโมเดล/route |
| Antigravity proxy/model matrix | `antigravity-proxy-matrix` | รายงาน usable models จาก probe/matrix โดยไม่เดา | ไม่ probe ทุกตัวถี่ ๆ ให้เปลืองโควต้า |
| ตรวจคุณภาพ UI/งานแบบละเอียด | `impeccable` | ตรวจงานละเอียดแบบ quality gate | ใช้เมื่อผู้ใช้ขอคุณภาพสูงหรือ final review |
| โค้ดบวม, over-engineering, YAGNI, ทำให้สั้นที่สุด | `ponytail` / `ponytail-review` | ใช้แนว lazy senior dev: ทำให้ง่ายที่สุดที่ยังถูกต้อง ลด abstraction ที่ไม่จำเป็น | ใช้กับงานโค้ด/รีวิว PR/ลดความซับซ้อน |

## Trigger ภาษาไทยที่ควรเข้าใจทันที

- `วางแผน`, `แผน`, `roadmap` -> `writing-plans`
- `แก้บั๊ก`, `แก้ปัญหา`, `ทำไมพัง`, `ตรวจระบบ` -> `systematic-debugging`
- `เขียนโค้ด`, `แก้ไฟล์`, `ทำ test` -> `test-driven-development`, `verification-before-completion`
- `รันคำสั่ง`, `ssh`, `systemctl`, `journalctl`, `terminal` -> `rtk-shell-guard`
- `ลดโทเคน`, `ประหยัดโควต้า`, `ภาษาไทยกระชับ` -> `thai-token-optimizer`
- `สั้นมาก`, `อัดสั้น` -> `caveman`
- `บีบบริบท`, `checkpoint`, `ทำต่อ`, `บริบทเต็ม` -> `context-compression-checkpoint`, `handoff`
- `ทำงานเป็นทีม`, `แตกงาน`, `subagent`, `รุมทำงาน`, `teamwork-preview` -> `teamwork-preview-goal`, `subagent-driven-development`
- `รายงานท้ายงาน`, `โควต้า`, `ใช้โมเดลอะไร`, `route` -> `adaptive-task-reporting`, `quota-truth-reporting`, `adaptive-model-routing`
- `GitHub`, `repo`, `issue`, `PR`, `backup` -> `github-workflows`
- `ข่าว`, `NEW AI`, `NEW | AI`, `สรุปข่าว AI` -> `news-new-ai-digest`
- `งานโรงเรียน`, `แผนสอน`, `ข้อสอบ`, `ใบงาน` -> `teacher-thai-workflow`
- `Drive`, `Docs`, `Sheets`, `Calendar`, `Tasks`, `PDF`, `OCR` -> `google-workspace-intake`
- `UI`, `UX`, `หน้าเว็บ`, `dashboard`, `mobile`, `ออกแบบเว็บ` -> `ui-ux-pro-max`
- `ponytail`, `YAGNI`, `ง่ายที่สุด`, `ไม่ over-engineer`, `โค้ดบวม`, `รีวิวโค้ดบวม` -> `ponytail`, `ponytail-review`

## กฎเลือกเมื่อมีทักษะซ้ำ

1. ใช้ canonical skill ก่อนเสมอ
2. Skill ที่ import จาก Codex/Antigravity ใช้เป็น reference ได้ แต่ไม่ควรเป็น primary ถ้ามี Hermes native/protected skill แล้ว
3. `headroom-context-compression` เป็นเครื่องมือ/engine ที่ดี แต่ routing หลักควรเรียกผ่าน `context-compression-checkpoint`
4. `caveman` ใช้เฉพาะโหมดสั้นมาก ไม่แทน `thai-token-optimizer`
5. `subagent-development` เป็นชื่อ wrapper; routing หลักควรไป `subagent-driven-development`
6. ถ้าไม่แน่ใจ ให้เลือก `using-superpowers` เพื่อบังคับคิดว่าจะใช้ skill อะไรก่อนทำงาน

## รูปแบบคำตอบเมื่อผู้ใช้ถามว่าใช้ทักษะอะไร

ตอบสั้น ๆ แบบนี้:

```text
ทักษะที่ระบบควรใช้:
- primary: <canonical skill> — <เหตุผลสั้น ๆ>
- supporting: <skill เสริมถ้ามี>
- verification: <วิธีตรวจว่างานสำเร็จ>
```

ห้ามตอบเป็นรายชื่อยาวทั้งระบบ เว้นแต่ผู้ใช้ขอ inventory ทั้งหมด
