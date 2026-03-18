# Phase 3: The Web Interface | Sprint 6: Layout, Routing & Navigation
**Status:** 🟡 In Progress
**Target Date:** March 18, 2026

## 🎯 Sprint Goal
Implement the global sidebar layout, set up dynamic course routing (`/course/[id]`), and apply the "Engineering Dark Mode" theme.

## 🛠 Tasks

### 1. The Global Sidebar Layout
- [x] Create `frontend/src/components/Sidebar.tsx`.
- [x] Implement a collapsible sidebar using Tailwind CSS.
- [x] Add a "New Course" button and a list of mock courses (Math, Physics, Circuits).

### 2. Dynamic Routing
- [x] Move the current Chat logic to `frontend/src/app/course/[id]/page.tsx`.
- [x] Update `frontend/src/app/layout.tsx` to wrap the entire app in the Sidebar.

### 3. Engineering Dark Mode
- [x] Configure `tailwind.config.ts` with a deep charcoal/navy palette.
- [x] Apply global dark styles to `globals.css`.

### 4. Course Context (State)
- [x] Create `frontend/src/store/CourseContext.tsx`.
- [x] Implement a provider to track which course is currently active so the Chat knows which vectors to query.