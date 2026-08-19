# Day 26 — Responsible AI Case Study

## Case Study: Amazon AI Recruiting Tool

### 1. Overview

Amazon developed an experimental machine-learning system to help evaluate job applicants.

The system was trained using historical resumes submitted to the company over several years.

The purpose was to automatically identify candidates whose resumes appeared suitable for technical jobs.

---

## 2. What Happened?

The historical hiring data reflected the existing gender imbalance in the technology workforce.

Because the machine-learning system learned patterns from historical data, it could also learn unwanted patterns present in that data.

Reports about the system found that the model could penalize resumes containing terms associated with women.

For example, resumes containing references to women's organizations or similar gender-associated information could receive lower scores.

Amazon eventually abandoned the experimental recruiting tool rather than using it as a reliable hiring system.

---

## 3. How the Bias Developed

The basic problem can be represented as:

```text
Historical Hiring Data
        ↓
Existing Human Bias
        ↓
Machine Learning Training
        ↓
Model Learns Biased Patterns
        ↓
Potentially Unfair Recommendations