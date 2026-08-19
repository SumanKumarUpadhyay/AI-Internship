# Day 26 — Responsible AI Guidelines

## Purpose

These guidelines define basic principles for developing and using AI systems responsibly within the company.

The goal is to make AI systems fair, safe, transparent, reliable, and respectful of user privacy.

---

## 1. Fairness and Bias

AI systems should be tested for unfair bias before and after deployment.

Developers should:

- Review training data for possible bias.
- Test model performance across relevant groups.
- Avoid using biased data without evaluation.
- Monitor the system for unfair outcomes.

---

## 2. Privacy

User and personal information must be handled carefully.

Developers should:

- Collect only necessary information.
- Avoid exposing personal information in AI responses.
- Do not store sensitive information unnecessarily.
- Protect user data from unauthorized access.

---

## 3. Accuracy and Hallucination

AI-generated information should not automatically be treated as fact.

For important applications:

```text
AI Response
    ↓
Verify Information
    ↓
Final Response