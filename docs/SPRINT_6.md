# Phase 3: The Web Interface | Sprint 6: Layout, Routing & Navigation
**Status:** 🟡 In Progress
**Target Date:** March 18, 2026

## 🎯 Sprint Goal
Implement the global sidebar layout, set up dynamic course routing (`/course/[id]`), and apply the "Engineering Dark Mode" theme.

## 🛠 Tasks

### 1. The Global Sidebar Layout
- [ ] Create `frontend/src/components/Sidebar.tsx`.
- [ ] Implement a collapsible sidebar using Tailwind CSS.
- [ ] Add a "New Course" button and a list of mock courses (Math, Physics, Circuits).

### 2. Dynamic Routing
- [ ] Move the current Chat logic to `frontend/src/app/course/[id]/page.tsx`.
- [ ] Update `frontend/src/app/layout.tsx` to wrap the entire app in the Sidebar.

### 3. Engineering Dark Mode
- [ ] Configure `tailwind.config.ts` with a deep charcoal/navy palette.
- [ ] Apply global dark styles to `globals.css`.

### 4. Course Context (State)
- [ ] Create `frontend/src/store/CourseContext.tsx`.
- [ ] Implement a provider to track which course is currently active so the Chat knows which vectors to query.