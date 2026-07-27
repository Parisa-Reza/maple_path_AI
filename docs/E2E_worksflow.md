```text
                                           ┌──────────────────────────────────────────┐
                                           │      OFFLINE KNOWLEDGE INGESTION         │
                                           └──────────────────────────────────────────┘

                                      IRCC Visitor Visa Website
                                                 │
                                                 ▼
                                      Seed Visitor Visa URL
                                                 │
                                                 ▼
                                          URL Crawler
                                           (requests)
                                                 │
                                                 ▼
                                     Parse HTML (BeautifulSoup)
                                                 │
                                                 ▼
                                   Remove Header / Footer / Noise
                                                 │
                                                 ▼
                                        Extract Clean Text
                                                 │
                                                 ▼
                                          Chunk Documents
                                                 │
                                                 ▼
                                      Generate Embeddings
                                                 │
                                                 ▼
                                  Store in SurrealDB Knowledge Base
                                                 │
─────────────────────────────────────────────────┼──────────────────────────────────────────────
                                                 │
                                                 ▼
                                      USER APPLICATION FLOW
────────────────────────────────────────────────────────────────────────────────────────────────

User
 │
 ▼
Django UI
 │
 ▼
Create New Tourist Visa Application
 │
 ▼
Start LangGraph Workflow
 │
 ▼
────────────────────────────────────────────────────────────────────────────
│
▼
Applicant Information Node
│
├── Name
├── Nationality
├── Passport Details
├── Occupation
└── Marital Status
│
▼
Trip Information Node
│
├── Purpose of Visit
├── Travel Dates
├── Duration
├── Accommodation
└── Sponsor (Optional)
│
▼
Document Upload Node
│
├── Passport
├── Bank Statement
├── Employment Letter
├── Invitation Letter (Optional)
└── Travel Itinerary
│
▼
Document Validation Node
│
├── Passport Validator
├── Bank Statement Validator
├── Employment Validator
└── File Integrity Check
│
▼
Are ALL Required Documents Present & Valid?
│
├──────────────────────────────┐
│                              │
│ NO                           │ YES
│                              │
▼                              ▼
Notify Applicant          Case Assessment Node
Missing Documents               │
│                               │
│                               ▼
│                    Build Search Query
│                               │
│                               ▼
│                  Retrieve Relevant IRCC Policies
│                               │
│                               ▼
│                  Search SurrealDB Vector Store
│                               │
│                               ▼
│                 Top Relevant IRCC Knowledge Chunks
│                               │
│                               ▼
│                 Gemini Eligibility Assessment
│                               │
│                               ▼
│               Generate Assessment Report
│
│                               │
│                               ▼
│                 AI Confidence Above Threshold?
│
│          ┌────────────────────┴────────────────────┐
│          │                                         │
│          │ NO                                      │ YES
│          │                                         │
│          ▼                                         ▼
│   Human Review Node                        Interview Node
│     interrupt()                                 │
│          │                                      │
│          │                           AI asks questions
│          │                           • Why Canada?
│          │                           • Funding?
│          │                           • Home ties?
│          │                           • Return plan?
│          │                                      │
│          │                                      ▼
│          │                          Interview Summary
│          │                                      │
│          └──────────────┬───────────────────────┘
│                         │
▼                         ▼
Need More Documents?   Recommendation Node
│                         │
├───────────────┐         │
│               │         ▼
│ YES           │ NO   Recommendation Report
│               │         │
▼               │         │
Return to        │         ▼
Document Upload  │  Final Human Review
│                │      interrupt()
└────────────────┼───────────┐
                 │           │
                 ▼           ▼
         Request More Docs   Accept Recommendation
                 │           │
                 ▼           ▼
         Document Upload     Save Application
                 │           │
                 └─────┬─────┘
                       │
                       ▼
                      END

```