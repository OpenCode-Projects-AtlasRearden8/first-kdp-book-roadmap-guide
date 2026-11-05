# 2. Interior Setup, Page by Page

Once you've picked the right project, the interior is where the book gets real. Getting it right page-by-page avoids the most common beginner consequences: a book KDP rejects outright (margins), a look-inside that reads badly, or a finished volume with the wrong template in mind.

This chapter walks the interior of the book in reading order — what belongs on each page, why it's there, and the traps around each.

> **Trim and margin numbers shown here** reflect KDP's widely documented rules as we used them for *The Massive AI Manual*. KDP documents the current authoritative values in its help center ("Paperback and Hardcover Manuscript Specs"). **Verify against that page before finalizing your manuscript** — thresholds change.

## Two books, one decision first: print vs. (or and) ebook?

KDP lets you publish an ebook (Kindle), a paperback (print), or both. Decide early because interiors differ:

- **Ebook (Kindle):** No "pages" in the fixed sense. Readers reflow text, change font size, and your "table of contents" is a *clickable list of links* to chapters. No page numbering, no headers/footers, no margin rules.
- **Paperback:** A fixed, fully laid-out PDF. Every page is exactly what the printer sees: margins, page numbers, headers, a *real* table of contents with *real* page numbers.

We recommend doing the **ebook first, paperback second**, if you're doing both: the Kindle manuscript (a reflow-friendly file) is quicker to get right, the dashboard award is faster feedback about your interior quality and description, and then the print file is a deliberate second pass. That's exactly how we approached *The Massive AI Manual*.

## The Kindle interior, page by page

A Kindle "interior" is a single file — typically a `.docx` or `.epub` — whose structure *is* the navigation. Map your document to the reading order below.

1. **Title page.** Book title, subtitle, author name as you want it to appear on Amazon. No publisher's logo needed, no version number.
2. **Copyright page.** The formal name. Contents: year, name, edition, rights statement. (See Chapter 6 for why this page matters for legal notice, and what a plain statement looks like.)
3. **Disclaimer / "About this book" note.** If your book has boundaries — "educational, not professional advice" — one paragraph belongs here. For *The Massive AI Manual* this was education-only disclaiming, up front.
4. **Dedication (optional).** Short: one or two lines.
5. **Table of contents.** In Word, use Heading 1 for your chapter titles so TOC entries auto-generate and become clickable on Kindle. One entry per major unit (chapter or part). Sub-section lists are recommended more for browsing in print than for Kindle.
6. **Body chapters.** Chapter title as Heading 1, sections as Heading 2, place a hard page break between chapters so each chapter starts at a "page break" on the Kindle also. Keep images inline with their paragraphs, and give each image meaningful alt text.
7. **Glossary, appendix, resources** (if any). Back of book. The link list must be fully typed-out URLs — Kindle tap targets matter.
8. **About the author.** Two short paragraphs, in your voice, without boasting. Same tone as the book.

**Rules of thumb that save you**: use *styles* in Word (Heading 1/2/3, Body) instead of hand-formatting everything; never use multiple space bar presses or manual line breaks to achieve fake indents; check on a Kindle device or the free Kindle app for your phone *before* you publish — "preview" is not optional.

## The paperback interior, page by page

The paperback interior is a fixed-layout PDF uploaded to KDP. Each "page" is a literal printed sheet in a Reading order. Here's reading order.

**Odd pages (right-hand pages) start with:** the title page and any chapter openers. Even pages are their backs.

1. **Title page.** Title, subtitle, author. (Left-hand after this should be blank or carry nothing important — the printer binds here.)
2. **Copyright page.** Follows the title page (always even/verso). Real publishing uses the same notes as above.
3. **Dedication (optional)** — centered, one line or two.
4. **Table of contents.** *Real page numbers* from your final layout. **This must be generated *after* layout is finalized** — this is the page most often out of date in beginner PDFs. Do not hand-type it and re-shuffle body content afterwards without regenerating.
5. **Body.** Chapters open on a right-hand (odd) page with a page break to achieve it: insert a "section break (next page)" or blank even page before it. Use consistent chapter-open layout throughout: chapter number, chapter title, then text.
6. **Appendices, glossary, resources, about the author**, in the order that serves your reader.
7. *(Optional final page)* A closing note or "thank you" — but **no promotional links needing a click**, because there is no click in print. Use short typed URLs the reader can write down.

### Margins, trim size, and the one number everyone gets wrong: the gutter

This is where beginner print files get rejected by KDP's system. The three numbers that matter:

- **Trim size** — the final size of the book after it's cut. Common nonfiction choice: 6"×9" (US). Whatever you choose, set your word processor/indesign page size to *that exact size*, not "Letter" or "A4". Letter-sized PDFs are the #1 sizing error.
- **Outside margins** — a static minimum that depends on whether your trim is without bleed. As a general documented rule: at least 0.25" outside margin with no bleed, and more if you use headers/footers/page numbers (leave room *inside* that margin for running elements). **Verify current margins in KDP's spec page** — it varies by page count and with-bleed/no-bleed.
- **Gutter** — the inside margin, which must be *larger* than the outside margin because binding eats into it. **This size grows with page count** — a 300-page book demands a bigger gutter than a 150-page book. This is why you *finalise page count first* (or get close), then set the gutter, then finalise layout again if the count shifts past a threshold.

Practical workflow: write the whole book, get a near-final page count, check KDP's spec page for your page count, set gutter and outside margins, then finalise layout, then generate the TOC and export your PDF.

### Fonts, images, bleed

- **Fonts must be embedded** in the PDF you export ("save/print as PDF with fonts embedded"). A font not embedded is a common invisible failure: instructions show correctly on your machine, then render incorrectly (or shift page breaks) in the printed proof.
- **Images: 300 DPI** for print. Images pulled from the web are usually 72 DPI and print fuzzy.
- **Bleed** only if you have elements (photos, backgrounds) meant to run to the edge of the page. If all your content sits inside margins, you do *not* need bleed, and no-bleed is the simpler beginner path. "With bleed" means the uploaded page is physically *larger* than the trim by 0.125 on three sides because the printed element extends and gets cut — don't guess; read the spec page.

## What we did for The Massive AI Manual

- Wrote the interior as one continuous manuscript with **Word styles** (Heading 1/2/3, Body), which made both Kindle TOC and paperback TOC cheap to generate.
- **Chose 6"×9" trim**, a standard nonfiction size, and reserved our decisions about margins and gutter until the manuscript had a near-final page count.
- Collected **every "wait, this number/tool changed" moment** in a running errata list — not to fix obsessively, but to know *what* needed fixing at the next revision instead of churning the layout again each week.
- Ordered and read a **physical proof copy** before launch. The proof caught things the on-screen preview never showed (a chapter opener on the wrong side of the spread, a heading whose style was slightly inconsistent, page-to-page spacing drift).

## Common beginner mistakes on the interior

1. **Writing in the wrong template.** Establish trim size, styles, and margin plan early; converting later means re-fit-flowing every page.
2. **Hand-formatting the TOC** and then regenerating layout. Use Word's automatic TOC (based on Heading styles) or your layout app's auto TOC.
3. **Guessing the gutter.** Look it up for your page count; don't guess.
4. **Magical screen-watching.** Read the *proof copy* in your hands. Every author finds something they want in there.
5. **Uploading the "wrong draft" file.** Version your files: `massive-ai-manual_v1.3_kdp.docx`, not `book_final_FINAL2.docx`.
