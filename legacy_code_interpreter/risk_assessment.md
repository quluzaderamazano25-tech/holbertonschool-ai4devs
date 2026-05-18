# Risk Assessment
## Project: `legacy_code_interpreter` — `holbertonschool-ai4devs`

---

## Risk 1 – XSS Vulnerability via Unsanitized User Input

| Field | Detail |
|---|---|
| **Severity** | High |
| **Location** | `TodoView.close()` |
| **Notes** | User-submitted todo titles are stored in the model and rendered into the DOM without any sanitization, allowing script injection attacks. Add DOMPurify sanitization before calling `model.save()` to strip malicious HTML and script tags from user input. |

---

## Risk 2 – jQuery 1.11.1 Known Security Vulnerability

| Field | Detail |
|---|---|
| **Severity** | High |
| **Location** | `bower_components/jquery` |
| **Notes** | jQuery 1.11.1 contains CVE-2015-9251, a known XSS vulnerability in its DOM manipulation methods. Upgrade to jQuery 3.x or remove jQuery entirely in favor of native DOM APIs and a modern framework. |

---

## Risk 3 – No Automated Tests Across the Entire Codebase

| Field | Detail |
|---|---|
| **Severity** | High |
| **Location** | Entire codebase |
| **Notes** | Zero unit, integration, or end-to-end tests mean any change can silently break existing functionality with no safety net. Add a Jest test suite targeting at least 80 percent coverage before any refactoring work begins. |

---

## Risk 4 – Client-Side Only Data Persistence

| Field | Detail |
|---|---|
| **Severity** | High |
| **Location** | `Backbone.LocalStorage` sync adapter |
| **Notes** | All todo data is stored exclusively in the browser's localStorage. Data is permanently lost if the user clears browser storage, uses a private window, or switches to a different device. Migrate to a REST API backend with server-side persistence. |

---

## Risk 5 – Deprecated and Unmaintained Dependencies

| Field | Detail |
|---|---|
| **Severity** | High |
| **Location** | `bower_components/` — Backbone.js, RequireJS, Bower |
| **Notes** | Backbone.js has not received significant updates since 2016. RequireJS and Bower are deprecated. No security patches will be released for vulnerabilities discovered in these libraries. Replace with actively maintained alternatives and migrate to npm for package management. |

---

## Risk 6 – localStorage Quota Exceeded with No Error Handling

| Field | Detail |
|---|---|
| **Severity** | High |
| **Location** | `Backbone.sync` override |
| **Notes** | The localStorage adapter catches errors but only stores the error message string without any recovery logic or user notification. When the 5MB quota is exceeded, todos are silently lost. Add explicit quota exceeded detection and display a user-facing warning message. |

---

## Risk 7 – Full DOM Re-Render on Every Model Change

| Field | Detail |
|---|---|
| **Severity** | Medium |
| **Location** | `AppView.render()` |
| **Notes** | The entire todo list is rebuilt from scratch via `addAll()` on every model event, including changes to a single item. Performance degrades significantly as the list grows. Replace with targeted DOM updates that only modify the element that actually changed. |

---

## Risk 8 – No Content Security Policy Headers

| Field | Detail |
|---|---|
| **Severity** | Medium |
| **Location** | Application server configuration |
| **Notes** | No CSP headers are configured, leaving the application exposed to XSS and code injection attacks that a properly configured policy would block. Configure CSP headers to restrict script sources and disallow inline script execution. |

---

## Risk 9 – Tight Coupling Between Views and Models

| Field | Detail |
|---|---|
| **Severity** | Medium |
| **Location** | `TodoView` and `AppView` |
| **Notes** | View classes directly manipulate model internals and react to all model events with no abstraction layer. Any change to the data structure requires modifying multiple tightly coupled files. Introduce a clear interface between data and presentation layers. |

---

## Risk 10 – Global State Management via Backbone Events

| Field | Detail |
|---|---|
| **Severity** | Medium |
| **Location** | `AppView` event bindings |
| **Notes** | Application state is managed through Backbone's global event system, making it difficult to trace which component triggered a state change and why. Event chains are hard to debug and reason about in complex scenarios. |

---

## Risk 11 – No TypeScript or Type Annotations

| Field | Detail |
|---|---|
| **Severity** | Medium |
| **Location** | Entire JavaScript codebase |
| **Notes** | All JavaScript is untyped, meaning runtime type errors are not caught at development time. A wrong property name or type mismatch surfaces only when a user triggers the affected code path in the browser. Migrate to TypeScript for compile-time type safety. |

---

## Risk 12 – RequireJS AMD Module Format is Deprecated

| Field | Detail |
|---|---|
| **Severity** | Medium |
| **Location** | `js/main.js` RequireJS configuration |
| **Notes** | The AMD module format and RequireJS loader are no longer the industry standard. Developers unfamiliar with AMD syntax face a steep learning curve, and no modern tooling supports tree-shaking or code splitting for AMD modules. Migrate to ES6 native import/export syntax with Vite or Webpack. |

---

## Risk 13 – No Input Validation on Todo Title Length

| Field | Detail |
|---|---|
| **Severity** | Low |
| **Location** | `TodoView.close()` |
| **Notes** | There is no maximum character limit enforced on todo titles. An extremely long title breaks the UI layout without any user feedback or truncation. Add a maximum length validation before saving and display an inline error message when exceeded. |

---

## Risk 14 – No Logging or Error Monitoring

| Field | Detail |
|---|---|
| **Severity** | Low |
| **Location** | Entire codebase |
| **Notes** | Runtime errors and edge cases are completely invisible in production. There is no logging, error tracking, or monitoring integration. Add a lightweight error monitoring tool such as Sentry to capture and report runtime exceptions automatically. |

---

## Risk 15 – Inconsistent Coding Style Mixing ES5 and ES6

| Field | Detail |
|---|---|
| **Severity** | Low |
| **Location** | Entire JavaScript codebase |
| **Notes** | The codebase mixes ES5 patterns like `var` declarations and function expressions with early ES6 features inconsistently. This makes the code harder to read and maintain. Configure ESLint with a consistent ES6+ ruleset and run Prettier for automated formatting. |

---

## Risk 16 – No Linting or Formatting Tools Configured

| Field | Detail |
|---|---|
| **Severity** | Low |
| **Location** | Project root — no `.eslintrc` or `.prettierrc` |
| **Notes** | The absence of ESLint and Prettier allows common JavaScript errors and inconsistent formatting to go undetected before code is committed. Add ESLint with a modern ruleset and Prettier as a pre-commit hook via Husky. |

---

## Risk 17 – No Documentation or Code Comments

| Field | Detail |
|---|---|
| **Severity** | Low |
| **Location** | Entire codebase |
| **Notes** | No functions or modules have JSDoc comments describing their purpose, parameters, or return values. New contributors must read full implementations to understand intent, significantly increasing onboarding time. Add JSDoc comments and a top-level README with architecture overview. |

---

## Summary

| Severity | Count |
|---|---|
| 🔴 High | 6 |
| 🟡 Medium | 6 |
| 🟢 Low | 5 |
| **Total** | **17** |