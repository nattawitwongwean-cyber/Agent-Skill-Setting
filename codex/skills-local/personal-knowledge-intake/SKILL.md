---
name: personal-knowledge-intake
description: >
  Use when the user sends or mentions PDFs, Word/DOCX files, images, screenshots,
  scanned documents, Drive files, school/admin documents, notes, or any data file
  that should be read, summarized, analyzed for user relevance, saved as reusable
  knowledge, and turned into Tasks/Calendar/Kanban items when actionable.
---

# Personal Knowledge Intake

Act as the user's secretary and knowledge intake clerk.

## Trigger
Use this for: PDF, Word/DOCX, images, screenshots, scans, Drive files, school letters,
announcements, forms, lesson material, notes, or any file/data the user wants remembered.

## Workflow
1. Identify source type: PDF / Word / image / screenshot / text / Drive file / unknown.
2. Extract content with the smallest reliable path:
   - PDF/image/scan: use `ocr-and-documents` or `nattawit-pdf-workflow`.
   - Word/DOCX/text/data file: use document extraction or existing file readers.
3. Summarize in Thai:
   - document type
   - key points
   - dates/deadlines/events
   - people/places/classes/courses
   - required actions
   - uncertainty/OCR caveats
4. Analyze relevance to the user:
   - school/admin/personal/project/news/finance/other
   - why it matters
   - what the user may need to do next
5. Save or prepare reusable knowledge:
   - if the user says remember/save/keep/บันทึก/เก็บ/จำไว้, use `ada-reminder-intake` or Google Workspace intake.
   - if it belongs to ongoing work, create/update Kanban or gBrain notes.
6. If actionable, create a draft Task/Calendar plan.
   - OCR-derived dates/times are candidates only.
   - Ask confirmation before creating Calendar events, external sharing, invites, or irreversible changes.

## Output Contract
Reply in Thai with:
- สรุปสำคัญ
- เกี่ยวกับผู้ใช้อย่างไร
- สิ่งที่ต้องทำ / วันที่เกี่ยวข้อง
- บันทึกแล้วหรือรอยืนยัน
- ถามยืนยันสั้น ๆ เฉพาะเมื่อจำเป็น

## Do Not
- Do not ignore attachments.
- Do not answer generically before inspecting/extracting.
- Do not create Calendar/Task from uncertain OCR dates without confirmation.
- Do not dump raw OCR unless asked.
