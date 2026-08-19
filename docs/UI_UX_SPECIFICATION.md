# UI/UX Specification

# Atlas

**Version:** 1.0.0

**Design System:** Atlas Design Language (ADL)

**Frontend Framework:** Next.js

**Component Library:** shadcn/ui + Radix UI

**Styling:** Tailwind CSS

---

# Table of Contents

1. Introduction
2. Design Philosophy
3. Design Principles
4. Design System
5. Color Palette
6. Typography
7. Spacing System
8. Iconography
9. Responsive Design
10. Navigation
11. Application Layout
12. User Flow

---

# 1. Introduction

This document defines the complete User Interface (UI) and User Experience (UX) guidelines for Atlas.

It serves as the reference for:

- UI Development
- Component Design
- User Experience
- Accessibility
- Responsive Behaviour
- Design Consistency

Every screen, component, and interaction should conform to this specification.

---

# 2. Design Philosophy

Atlas is designed around one core idea:

> **Documents should feel conversational, not archival.**

Traditional document management applications prioritize folders and files.

Atlas prioritizes:

- Questions
- Conversations
- Knowledge Retrieval

The interface should always make AI interaction the primary experience while keeping document management simple and unobtrusive.

---

# 3. Design Principles

## Simplicity

Every screen should present only the information required for the current task.

Avoid visual clutter.

---

## Consistency

The same interaction should behave identically throughout the application.

Example

Delete Button

Always

- Red
- Trash Icon
- Confirmation Dialog

---

## Visibility

Users should always know

- Current page
- Processing state
- Upload progress
- AI status

---

## Feedback

Every action should provide immediate feedback.

Examples

Upload

↓

Progress Bar

Processing

↓

Animated Status

Delete

↓

Toast Notification

---

## Accessibility

Atlas should remain usable for all users.

Requirements

- Keyboard Navigation
- Screen Reader Support
- Color Contrast
- Focus Indicators

---

# 4. Design System

Atlas uses a component-driven design system.

```
Pages

↓

Sections

↓

Components

↓

UI Elements
```

---

## Design Tokens

Primary Color

Secondary Color

Spacing

Typography

Radius

Shadows

Transitions

These tokens should be defined centrally and reused throughout the application.

---

# 5. Color Palette

## Primary

```
Blue 600
```

Purpose

- Primary Buttons
- Links
- Active States

---

## Secondary

```
Slate 600
```

Purpose

- Secondary Buttons
- Labels
- Borders

---

## Success

```
Green 600
```

Purpose

- Success Messages
- Completed Jobs

---

## Warning

```
Amber 500
```

Purpose

- Processing
- Pending Tasks

---

## Error

```
Red 600
```

Purpose

- Validation
- Errors
- Delete Actions

---

## Information

```
Sky Blue
```

Purpose

Notifications

Hints

---

## Neutral

```
Gray

Slate

Zinc
```

Purpose

Backgrounds

Cards

Borders

---

# Dark Theme

Background

```
Zinc-950
```

Cards

```
Zinc-900
```

Text

```
Gray-100
```

Primary

```
Blue-500
```

---

# 6. Typography

Primary Font

```
Inter
```

---

## Heading Sizes

| Element | Size |
| ------- | ---- |
| H1      | 36px |
| H2      | 30px |
| H3      | 24px |
| H4      | 20px |
| H5      | 18px |
| H6      | 16px |

---

## Body

16px

---

## Small

14px

---

## Caption

12px

---

## Font Weights

Regular

Medium

Semibold

Bold

---

# 7. Spacing System

Atlas uses an 8-point spacing system.

Examples

```
4px

8px

16px

24px

32px

48px

64px
```

Advantages

- Consistency
- Predictable Layouts
- Easier Responsive Design

---

# 8. Border Radius

Small

```
6px
```

---

Medium

```
10px
```

---

Large

```
16px
```

---

Rounded

```
999px
```

---

# 9. Shadows

Cards

Small Shadow

---

Dialogs

Medium Shadow

---

Dropdowns

Large Shadow

---

# 10. Icons

Atlas uses

```
Lucide Icons
```

---

Examples

Upload

↓

Upload Icon

Delete

↓

Trash Icon

Settings

↓

Gear Icon

Chat

↓

Message Icon

Search

↓

Search Icon

Profile

↓

User Icon

---

# Icon Rules

Always

- Same size
- Same stroke width
- Same spacing

---

# 11. Responsive Design

Atlas supports

Desktop

Tablet

Mobile

---

## Breakpoints

| Device  | Width      |
| ------- | ---------- |
| Mobile  | <640px     |
| Tablet  | 640–1024px |
| Desktop | >1024px    |

---

## Mobile Behaviour

Sidebar

↓

Drawer

Cards

↓

Single Column

Chat

↓

Full Screen

---

## Tablet

Sidebar

↓

Collapsible

Grid

↓

2 Columns

---

## Desktop

Permanent Sidebar

Multi-column Layout

---

# 12. Navigation Structure

```
Dashboard

│

├── Documents

│      ├── Upload

│      ├── Library

│      └── Details

│

├── Chat

│

├── Search

│

├── Settings

│

└── Profile
```

---

# Sidebar Navigation

Contains

- Logo
- Dashboard
- Documents
- Chat
- Search
- Settings
- Profile

Footer

- Theme Toggle
- Logout

---

# Navbar

Contains

- Breadcrumb
- Search
- Notifications
- User Avatar

---

# 13. Main Layout

```
+---------------------------------------------------+

Sidebar

|

|

| Dashboard

| Documents

| Chat

| Settings

|

+---------------------+-----------------------------+

Navbar

----------------------------------------------

Main Content

----------------------------------------------

Footer
```

---

# 14. User Flow

## Authentication Flow

```
Landing Page

↓

Register

↓

Login

↓

Dashboard
```

---

## Upload Flow

```
Dashboard

↓

Upload

↓

Processing

↓

Library

↓

Ready
```

---

## Chat Flow

```
Library

↓

Open Chat

↓

Ask Question

↓

Receive Response

↓

View Sources
```

---

## Settings Flow

```
Profile

↓

Settings

↓

Update

↓

Save
```

---

# 15. UX Guidelines

Atlas should minimize unnecessary user effort.

Examples:

- Remember the last opened chat.
- Preserve search filters during navigation.
- Show upload progress immediately.
- Allow drag-and-drop uploads.
- Keep AI responses readable with proper spacing and Markdown rendering.
- Display clear loading indicators during processing.

---

# UI Principles Summary

The Atlas interface is designed to be:

- AI-first
- Minimal
- Responsive
- Accessible
- Consistent
- Fast
- Predictable

These principles ensure users focus on interacting with knowledge rather than managing files.

# 16. Landing Page

The Landing Page is the public face of Atlas.

Its purpose is to explain the product and encourage visitors to create an account.

---

## Goals

- Explain Atlas in under 30 seconds.
- Highlight key features.
- Build trust.
- Convert visitors into users.

---

## Layout

```text
+------------------------------------------------------+

Navbar

--------------------------------------------------------

Hero Section

--------------------------------------------------------

Features

--------------------------------------------------------

How Atlas Works

--------------------------------------------------------

Technology Stack

--------------------------------------------------------

FAQ

--------------------------------------------------------

Footer
```

---

## Hero Section

Contains

- Product Name
- Tagline
- Short Description
- Primary CTA
- Secondary CTA
- Hero Illustration

Buttons

```
Get Started

GitHub

Documentation
```

---

## Features Section

Display feature cards.

Examples

- AI Document Chat
- Semantic Search
- Fast Upload
- Source Citations
- Secure Storage
- Multiple File Formats

---

## How It Works

Illustrate the complete RAG pipeline.

```text
Upload

↓

Processing

↓

Embeddings

↓

Search

↓

AI Response
```

---

# 17. Login Screen

## Purpose

Authenticate existing users.

---

## Layout

```text
+-----------------------------+

Logo

Heading

Email

Password

Remember Me

Login Button

Google Login

Forgot Password

Register Link

+-----------------------------+
```

---

## Validation

Email

- Required
- Valid format

Password

- Required
- Minimum length

---

## Error Messages

Examples

- Invalid email.
- Incorrect password.
- Account not found.
- Server unavailable.

---

# 18. Register Screen

Contains

- Name
- Email
- Password
- Confirm Password

Validation

- Strong password
- Email uniqueness
- Matching passwords

---

# 19. Dashboard

The Dashboard is the application's home page.

---

## Goals

Provide an overview of the user's knowledge base.

---

## Layout

```text
+------------------------------------------------------+

Sidebar

|

|

+----------------------+-------------------------------+

Navbar

--------------------------------------------------------

Quick Stats

--------------------------------------------------------

Recent Documents

--------------------------------------------------------

Recent Chats

--------------------------------------------------------

Processing Queue

--------------------------------------------------------

Storage Usage

--------------------------------------------------------
```

---

## Quick Statistics

Cards

- Total Documents
- Processed Documents
- Active Chats
- Storage Used

---

## Recent Documents

Each card displays

- Name
- Upload Time
- Status
- File Type

---

## Recent Chats

Display

- Title
- Last Updated
- Number of Messages

---

## Processing Queue

Shows

- Current Step
- Progress
- Status

---

# 20. Document Library

The document library is the primary workspace.

---

## Layout

```text
+------------------------------------------------------+

Search

Filters

Sort

Upload Button

--------------------------------------------------------

Grid/List Toggle

--------------------------------------------------------

Document Cards

--------------------------------------------------------
```

---

## Document Card

Displays

- File Icon
- Document Name
- File Type
- Upload Date
- Status
- Pages
- Chunk Count

Actions

- Open
- Rename
- Delete
- Download
- Preview

---

## Card States

Ready

Processing

Failed

Uploading

---

## Empty State

Display

```
No documents uploaded.

Upload your first document.
```

Button

```
Upload Document
```

---

# 21. Upload Screen

Purpose

Upload one or more documents.

---

## Layout

```text
+------------------------------------------------------+

Drag & Drop Zone

--------------------------------------------------------

Browse Files

--------------------------------------------------------

Upload Queue

--------------------------------------------------------

Processing Status

--------------------------------------------------------
```

---

## Upload States

Idle

↓

Uploading

↓

Processing

↓

Completed

or

↓

Failed

---

## Validation

Supported

- PDF
- DOCX
- TXT
- Markdown

Reject

- Unsupported format
- Empty file
- Oversized file

---

# 22. Chat Screen

This is the most important page in Atlas.

---

## Layout

```text
+------------------------------------------------------+

Sidebar

|

Conversations

|

+----------------------+-------------------------------+

Chat Messages

--------------------------------------------------------

Sources Panel

--------------------------------------------------------

Input Box

--------------------------------------------------------
```

---

## Chat Message

Each message displays

- Avatar
- Sender
- Timestamp
- Markdown
- Code Blocks

---

## Assistant Response

Includes

- Markdown
- Tables
- Code
- Citations
- Copy Button
- Regenerate Button

---

## Source Panel

Displays

- Document Name
- Page Number
- Chunk Number
- Similarity Score (Optional)

Clicking a source opens the document preview.

---

## Chat States

Loading

Streaming

Completed

Error

---

## Empty Chat

Display

```
Ask Atlas anything about your documents.
```

---

# 23. Search Screen

Purpose

Search documents and indexed knowledge.

---

## Layout

```text
+------------------------------------------------------+

Search Bar

--------------------------------------------------------

Filters

--------------------------------------------------------

Results

--------------------------------------------------------
```

---

## Search Filters

- File Type
- Upload Date
- Document
- Processing Status

---

## Search Result

Displays

- Matching Text
- Document
- Page Number
- Similarity Score

---

# 24. Settings Screen

Organized into sections.

---

## General

- Theme
- Language

---

## AI

- LLM Provider
- Embedding Model
- Temperature
- Maximum Tokens

---

## Retrieval

- Top-K
- Chunk Size
- Overlap
- Similarity Threshold

---

## Security

- Change Password
- Active Sessions
- Delete Account

---

# 25. Profile Screen

Displays

- Avatar
- Name
- Email
- Join Date

Actions

- Edit Profile
- Change Password
- Logout

---

# 26. Global Components

Atlas uses reusable UI components.

## Navigation

- Sidebar
- Navbar
- Breadcrumbs

---

## Forms

- Text Input
- Password Input
- File Upload
- Dropdown
- Checkbox
- Radio Button

---

## Feedback

- Toast
- Alert
- Badge
- Tooltip
- Skeleton Loader

---

## Dialogs

- Confirmation Dialog
- Delete Dialog
- Settings Modal

---

## AI Components

- Chat Bubble
- Source Card
- Citation Badge
- Streaming Cursor
- Token Counter (Future)

---

# 27. Loading States

Atlas never leaves the user waiting without feedback.

Examples

- Skeleton cards while loading documents.
- Progress bars during uploads.
- Spinner during authentication.
- Streaming animation while AI responds.

---

# 28. Error States

Every failure should provide a clear explanation and recovery action.

Examples

### Upload Error

Message

```
This file type is not supported.
```

Action

```
Choose another file.
```

---

### Retrieval Error

Message

```
No relevant information found.
```

Action

```
Try rephrasing your question.
```

---

### AI Error

Message

```
The AI provider is currently unavailable.
```

Action

```
Retry
```

---

# 29. Accessibility Requirements

Atlas should comply with WCAG 2.1 Level AA where practical.

Requirements

- Keyboard navigation
- Visible focus states
- ARIA labels
- Semantic HTML
- Color contrast
- Screen reader compatibility
- Sufficient touch targets on mobile

---

# 30. UI Performance Guidelines

The interface should remain responsive even with large document libraries.

Recommendations

- Virtualize long document lists.
- Lazy-load previews.
- Cache frequently accessed data.
- Debounce search input.
- Optimistically update UI after lightweight actions (e.g., rename).

---

# 31. Animation Guidelines

Animations should communicate state, not distract.

Recommended animations

- Fade in/out for dialogs.
- Slide transitions for sidebar.
- Progress animation during uploads.
- Typing indicator for streaming responses.

Animation duration

- Micro interactions: 100–200 ms
- Page transitions: 200–300 ms

---

# 32. Responsive Behavior Summary

| Feature         | Mobile     | Tablet      | Desktop     |
| --------------- | ---------- | ----------- | ----------- |
| Sidebar         | Drawer     | Collapsible | Fixed       |
| Dashboard Cards | 1 Column   | 2 Columns   | 4 Columns   |
| Chat            | Full Width | Full Width  | Split View  |
| Document Grid   | 1 Column   | 2 Columns   | 3–5 Columns |

---

# 33. UI/UX Summary

Atlas is designed as an **AI-first knowledge workspace** rather than a traditional file manager.

The interface emphasizes:

- Fast document ingestion
- Clear processing feedback
- Conversational interaction
- Source transparency
- Consistent navigation
- Accessibility
- Responsive layouts

Every interaction should reduce friction and keep users focused on extracting knowledge from their documents instead of managing files.
