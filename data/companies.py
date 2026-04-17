COMPANIES = {
    "google": {
        "slug": "google",
        "name": "Google",
        "tagline": "Scale-first engineering with high expectations for systems thinking and clarity.",
        "search_excerpt": "Strong for candidates who pair backend fundamentals with systems thinking.",
        "dashboard_reason": "Best for large-scale backend ambition.",
        "company_summary": "Modeled as a scale-first company that values sharp judgment and clear tradeoffs.",
        "hiring_style": "Structured interviews, strong fundamentals, and clean systems thinking.",
        "values_for_engineers": [
            "Systems thinking at scale",
            "Clear written and verbal communication",
            "Ownership beyond a narrow ticket",
            "Comfort with reliability, testing, and operational tradeoffs",
        ],
        "culture": {
            "work_style": "Documentation-heavy, design-oriented, and comfortable with ambiguity when a team is solving for long-term scale.",
            "collaboration": "Cross-functional with product, reliability, and platform stakeholders who expect engineers to influence decisions early.",
            "pace": "Fast but measured. Teams move quickly, but strong reviews and technical alignment still matter.",
            "growth_expectations": "Engineers are expected to deepen systems judgment, communicate clearly, and show ownership over outcomes rather than isolated tasks.",
        },
        "employee_insights": [
            {
                "alias": "Nia R.",
                "role": "Staff Backend Engineer",
                "insight": "Candidates usually stand out when they explain why a design will keep working under growth, not just how to make it work once. Strong tradeoff language matters a lot.",
            },
            {
                "alias": "Omar K.",
                "role": "Site Reliability Engineer",
                "insight": "Interviewers pay attention to how you reason about failure modes. If you can talk through observability, bottlenecks, and recovery paths calmly, your answers feel much stronger.",
            },
            {
                "alias": "Priya S.",
                "role": "Product Infrastructure Engineer",
                "insight": "Preparation lands best when candidates connect technical decisions to user impact. Even very backend-heavy interviews still reward product-aware thinking.",
            },
        ],
        "interview_questions": [
            {
                "question": "Design a globally distributed rate limiter for a public API that serves unpredictable traffic spikes.",
                "tip": "Start with the core constraints, then explain how you would preserve correctness while keeping latency low across regions.",
            },
            {
                "question": "A service rollout caused intermittent latency increases in one region. How would you investigate and stabilize the system?",
                "tip": "Show a structured debugging path. Google-flavored answers feel stronger when you talk through metrics, blast radius, rollback criteria, and verification.",
            },
            {
                "question": "How would you redesign a search indexing pipeline that is falling behind during peak ingestion windows?",
                "tip": "Focus on bottleneck identification, queue behavior, and which parts of the pipeline should scale independently.",
            },
        ],
        "skill_gap": {
            "expected_skills": [
                "Python",
                "Java",
                "Distributed Systems",
                "System Design",
                "Data Structures",
                "Cloud Infrastructure",
                "Testing",
                "REST APIs",
            ],
            "matched_skills": ["Python", "Java", "REST APIs"],
            "missing_skills": ["Distributed Systems", "System Design", "Cloud Infrastructure", "Testing", "Data Structures"],
            "recommendations": [
                "Add a stronger distributed systems project story with scale, tradeoffs, and failure handling.",
                "Show testing depth with concrete integration or reliability examples instead of only project outcomes.",
                "Use one project bullet to demonstrate system design reasoning, not just implementation details.",
            ],
            "match_percent": 38,
        },
        "referral_matches": [
            {
                "name": "Lena W.",
                "role": "Software Engineer II",
                "team": "Ads Infrastructure",
                "note": "Open to reviewing concise outreach focused on backend projects and growth potential.",
                "locked": False,
            },
            {
                "name": "Marcus T.",
                "role": "Platform Engineer",
                "team": "Core Developer Services",
                "note": "Best fit for candidates who can discuss API design and service reliability with confidence.",
                "locked": False,
            },
            {
                "name": "Jules A.",
                "role": "Senior Engineer",
                "team": "Google Cloud Runtime",
                "note": "Premium match with stronger cloud and distributed systems alignment.",
                "locked": True,
            },
            {
                "name": "Rina C.",
                "role": "Engineering Manager",
                "team": "Search Quality",
                "note": "Premium path for candidates with polished system design preparation and strong communication.",
                "locked": True,
            },
        ],
        "ai_summary": "High-upside target. The profile is close on backend fundamentals, but needs stronger distributed systems and reliability signals.",
        "resume_tips": [
            "Replace generic Flask project wording with a bullet that explains traffic assumptions, service boundaries, and performance decisions.",
            "Add one measurable reliability or testing improvement from the internship to strengthen production-readiness signals.",
            "Use a project bullet that highlights collaboration, not only code delivery, since Google values cross-functional clarity.",
        ],
        "job_fit": {
            "score": 78,
            "headline": "Strong upside with targeted systems prep",
            "explanation": "The profile already aligns with backend software engineering fundamentals, but Google-level scale expectations require sharper distributed systems evidence.",
            "reasons": [
                "Good match on core languages and API-focused implementation experience.",
                "Needs stronger cloud infrastructure and large-scale system design signals.",
                "Communication style and technical ownership could become a differentiator with better project framing.",
            ],
        },
    },
    "microsoft": {
        "slug": "microsoft",
        "name": "Microsoft",
        "tagline": "Platform-minded engineering with strong emphasis on collaboration, reliability, and cloud readiness.",
        "search_excerpt": "A steady fit for candidates with solid fundamentals and strong collaboration.",
        "dashboard_reason": "Best overall balance of fit and growth.",
        "company_summary": "Modeled as a platform-minded company that rewards reliable engineering and collaboration.",
        "hiring_style": "Strong fundamentals, dependable execution, and service-minded communication.",
        "values_for_engineers": [
            "Reliable engineering habits",
            "Cross-team collaboration",
            "Cloud service awareness",
            "Clear architectural communication",
        ],
        "culture": {
            "work_style": "Structured and delivery-oriented, with strong emphasis on clarity, maintainability, and dependable shipping habits.",
            "collaboration": "Teams often work across product managers, designers, and adjacent engineering groups, so communication and alignment matter a lot.",
            "pace": "Steady and ambitious. The expectation is not chaos, but consistent progress with strong technical hygiene.",
            "growth_expectations": "Engineers are expected to grow into broader system ownership, stronger architecture judgment, and better collaboration across services.",
        },
        "employee_insights": [
            {
                "alias": "Jordan E.",
                "role": "Cloud Platform Engineer",
                "insight": "The strongest candidates sound dependable. Clear thinking about maintainability, testing, and handoff quality goes a long way here.",
            },
            {
                "alias": "Alicia G.",
                "role": "Software Engineer",
                "insight": "Interview performance improves when candidates connect implementation details to developer experience and customer impact. Practicality matters more than sounding overly theoretical.",
            },
            {
                "alias": "Ben L.",
                "role": "Senior Engineer",
                "insight": "Collaboration is not soft detail. If you can explain how you worked through tradeoffs with teammates, your answers feel more Microsoft-ready.",
            },
        ],
        "interview_questions": [
            {
                "question": "Design a backend service that supports document collaboration across multiple devices with eventual consistency.",
                "tip": "Explain data flow and conflict handling clearly. Microsoft-style answers feel stronger when reliability and user experience show up early.",
            },
            {
                "question": "You are asked to version a public API used by many internal clients. How do you introduce change safely?",
                "tip": "Talk through backward compatibility, rollout sequencing, observability, and communication with dependent teams.",
            },
            {
                "question": "An Azure-like internal service is hitting timeout issues under load. What is your investigation plan?",
                "tip": "Use a calm, layered approach that covers metrics, logs, resource bottlenecks, and whether the issue is code, infrastructure, or dependency related.",
            },
        ],
        "skill_gap": {
            "expected_skills": [
                "Java",
                "Cloud Services",
                "System Design",
                "Testing",
                "Collaboration",
                "Distributed Systems",
                "REST APIs",
            ],
            "matched_skills": ["Java", "REST APIs"],
            "missing_skills": ["Cloud Services", "System Design", "Testing", "Collaboration", "Distributed Systems"],
            "recommendations": [
                "Add one internship bullet that shows collaboration across teams or stakeholders, not only coding output.",
                "Strengthen cloud awareness by describing deployment, hosting, or monitoring choices in a project.",
                "Include a sentence in projects that highlights testing strategy and long-term maintainability.",
            ],
            "match_percent": 43,
        },
        "referral_matches": [
            {
                "name": "Ethan M.",
                "role": "Software Engineer",
                "team": "Developer Division",
                "note": "Good starter match for candidates with strong backend fundamentals and thoughtful teamwork examples.",
                "locked": False,
            },
            {
                "name": "Claire N.",
                "role": "Program Engineer",
                "team": "Azure Core",
                "note": "Likely to respond well to concise messages that connect projects to cloud service reliability.",
                "locked": False,
            },
            {
                "name": "Harper S.",
                "role": "Senior Software Engineer",
                "team": "Microsoft 365 Platform",
                "note": "Premium match focused on scalable collaboration systems and service ownership.",
                "locked": True,
            },
            {
                "name": "Dev P.",
                "role": "Engineering Manager",
                "team": "Azure Developer Tools",
                "note": "Premium route for candidates with stronger architecture and cloud deployment stories.",
                "locked": True,
            },
        ],
        "ai_summary": "Most believable near-term target. The next step is stronger cloud, collaboration, and operational language.",
        "resume_tips": [
            "Add a line that shows how you collaborated with teammates, stakeholders, or reviewers to improve a project outcome.",
            "Use Microsoft-friendly language around maintainability, testing, and long-term service quality.",
            "Show one cloud-related signal, even if it comes from a simple deployment, monitoring, or architecture decision.",
        ],
        "job_fit": {
            "score": 82,
            "headline": "Best overall blend of fit and growth",
            "explanation": "Microsoft feels especially plausible because the current resume already matches dependable backend work, and the next skills to develop are realistic for an early-career candidate.",
            "reasons": [
                "Strong alignment with practical engineering fundamentals and API work.",
                "Clear path to improve fit through cloud, testing, and collaboration examples.",
                "Culture expectations feel achievable for a candidate transitioning from academic projects to professional engineering.",
            ],
        },
    },
    "nvidia": {
        "slug": "nvidia",
        "name": "Nvidia",
        "tagline": "Performance-driven engineering where systems depth and technical rigor matter immediately.",
        "search_excerpt": "Compelling for ambitious candidates drawn to performance and AI infrastructure.",
        "dashboard_reason": "High upside, higher technical bar.",
        "company_summary": "Modeled as a performance-driven company where systems depth matters early.",
        "hiring_style": "Technical rigor, bottleneck thinking, and disciplined optimization.",
        "values_for_engineers": [
            "Performance-oriented reasoning",
            "Technical precision",
            "Systems depth",
            "Comfort with fast-moving AI infrastructure work",
        ],
        "culture": {
            "work_style": "Deeply technical and execution-focused, with a premium on engineers who can reason about bottlenecks and platform tradeoffs.",
            "collaboration": "Engineers often partner with research, platform, and systems teams where precision and technical trust matter.",
            "pace": "Fast and intense. Teams move quickly, but they still expect disciplined thinking and high-quality technical decisions.",
            "growth_expectations": "You are expected to build deeper systems fluency, especially around performance, infrastructure, and complex debugging.",
        },
        "employee_insights": [
            {
                "alias": "Samir D.",
                "role": "Infrastructure Software Engineer",
                "insight": "What helps most in interviews is showing how you isolate a bottleneck. Nvidia discussions often feel stronger when you reason from system behavior instead of naming tools too early.",
            },
            {
                "alias": "Kara Y.",
                "role": "GPU Systems Engineer",
                "insight": "Candidates who can explain throughput, latency, and resource pressure in plain language stand out. Performance work is only impressive if your reasoning is clear.",
            },
            {
                "alias": "Leo P.",
                "role": "Distributed AI Platform Engineer",
                "insight": "Ambition is good here, but interviewers still want disciplined tradeoffs. Clear thinking about scale and operational limits matters more than hype.",
            },
        ],
        "interview_questions": [
            {
                "question": "A training job scheduler is underutilizing GPUs during peak demand. How would you diagnose the bottleneck and improve throughput?",
                "tip": "Break the problem into scheduling, data input, resource contention, and observability instead of treating it as one vague optimization issue.",
            },
            {
                "question": "How would you redesign a data ingestion service that feeds a real-time inference pipeline with inconsistent latency?",
                "tip": "Focus on backpressure, batching strategy, and where queueing or serialization is hurting end-to-end performance.",
            },
            {
                "question": "Describe how you would partner with ML researchers when their model changes keep affecting production stability.",
                "tip": "Show that you can bridge technical rigor and collaboration. Nvidia-ready answers often balance performance goals with reliable operations.",
            },
        ],
        "skill_gap": {
            "expected_skills": [
                "Python",
                "Performance Optimization",
                "Distributed Systems",
                "System Design",
                "Linux",
                "C++",
                "REST APIs",
                "Infrastructure Debugging",
            ],
            "matched_skills": ["Python", "REST APIs"],
            "missing_skills": [
                "Performance Optimization",
                "Distributed Systems",
                "System Design",
                "Linux",
                "C++",
                "Infrastructure Debugging",
            ],
            "recommendations": [
                "Add one performance-focused project story with measurements, bottleneck analysis, and concrete optimization decisions.",
                "Build stronger systems credibility through Linux, distributed systems, or infrastructure tooling exposure.",
                "Translate existing backend experience into more technical language around throughput, reliability, and debugging discipline.",
            ],
            "match_percent": 25,
        },
        "referral_matches": [
            {
                "name": "Anika V.",
                "role": "Software Engineer",
                "team": "AI Platform Tooling",
                "note": "Starter match for candidates who can speak confidently about Python systems and technical growth plans.",
                "locked": False,
            },
            {
                "name": "Victor C.",
                "role": "Build Infrastructure Engineer",
                "team": "Developer Productivity",
                "note": "Useful unlocked path for candidates emphasizing tooling, observability, and backend discipline.",
                "locked": False,
            },
            {
                "name": "Elena R.",
                "role": "Senior Systems Engineer",
                "team": "GPU Resource Scheduling",
                "note": "Premium match for candidates with stronger performance and distributed systems preparation.",
                "locked": True,
            },
            {
                "name": "Tariq H.",
                "role": "Engineering Lead",
                "team": "Inference Infrastructure",
                "note": "Premium route aimed at candidates with convincing infrastructure debugging stories.",
                "locked": True,
            },
        ],
        "ai_summary": "Exciting stretch target. Python helps, but the resume needs stronger performance and infrastructure proof.",
        "resume_tips": [
                "Add performance metrics anywhere possible, even for academic projects, so the resume starts sounding more systems-aware.",
            "Highlight debugging stories that show how you isolated and resolved backend issues under constraints.",
            "Build a stronger bridge from Flask and API work into infrastructure thinking, especially around reliability and throughput.",
        ],
        "job_fit": {
            "score": 68,
            "headline": "Exciting stretch target with bigger technical gaps",
            "explanation": "The ambition makes sense, but Nvidia-level systems and performance depth are not yet fully visible in the sample resume.",
            "reasons": [
                "Python foundation gives a real starting point.",
                "Performance and distributed systems proof points are currently too thin.",
                "This is a credible long-term target once infrastructure projects become stronger.",
            ],
        },
    },
    "apple": {
        "slug": "apple",
        "name": "Apple",
        "tagline": "Precision-focused engineering where polish, reliability, and disciplined execution carry weight.",
        "search_excerpt": "Strong for candidates who value reliability, polish, and product quality.",
        "dashboard_reason": "Promising with sharper quality and ownership language.",
        "company_summary": "Modeled as a precision-focused company that values dependable, polished engineering.",
        "hiring_style": "Disciplined problem solving, quality, and user-trust awareness.",
        "values_for_engineers": [
            "Precision and quality",
            "Reliability under real-world constraints",
            "Strong ownership",
            "Thoughtful product impact awareness",
        ],
        "culture": {
            "work_style": "Focused and detail-oriented, with high expectations for quality, clarity, and intentional engineering decisions.",
            "collaboration": "Cross-functional, but often with a high bar for preparedness and concise communication.",
            "pace": "Demanding but deliberate. Teams care about execution quality as much as forward motion.",
            "growth_expectations": "Engineers are expected to deepen reliability thinking, improve craftsmanship, and make technically sound decisions that protect the user experience.",
        },
        "employee_insights": [
            {
                "alias": "Grace H.",
                "role": "Software Engineer",
                "insight": "Candidates feel stronger when they explain why a system is dependable, not only why it is fast. Reliability language matters a lot here.",
            },
            {
                "alias": "Noah B.",
                "role": "Platform Services Engineer",
                "insight": "Apple-style answers often feel better when they are concise and precise. Clear reasoning usually beats over-explaining every possible path.",
            },
            {
                "alias": "Elise F.",
                "role": "Senior Infrastructure Engineer",
                "insight": "Preparation should highlight craftsmanship. Strong candidates show that they care about correctness, maintainability, and the user impact of backend systems.",
            },
        ],
        "interview_questions": [
            {
                "question": "Design a synchronization service that keeps user data consistent across devices while protecting privacy and reliability.",
                "tip": "Lead with trust, failure handling, and consistency tradeoffs. Apple-style answers feel stronger when user impact is explicit.",
            },
            {
                "question": "A background service is causing intermittent resource spikes on production devices. How would you investigate and resolve it?",
                "tip": "Show disciplined debugging, careful rollout logic, and a bias toward protecting the user experience first.",
            },
            {
                "question": "How would you improve the reliability of a backend feature that supports a polished consumer product launch?",
                "tip": "Talk through quality gates, testing strategy, rollback readiness, and how you would collaborate under a tight launch timeline.",
            },
        ],
        "skill_gap": {
            "expected_skills": [
                "System Design",
                "Reliability",
                "Testing",
                "REST APIs",
                "Cross-functional Communication",
                "Performance Awareness",
                "Ownership",
            ],
            "matched_skills": ["REST APIs"],
            "missing_skills": [
                "System Design",
                "Reliability",
                "Testing",
                "Cross-functional Communication",
                "Performance Awareness",
                "Ownership",
            ],
            "recommendations": [
                "Rewrite project bullets so they emphasize reliability, quality, and the user impact of backend work.",
                "Add one line that shows ownership from idea to testing to final delivery.",
                "Use tighter, more polished wording throughout the resume to better match Apple's precision-oriented tone.",
            ],
            "match_percent": 22,
        },
        "referral_matches": [
            {
                "name": "Sophia C.",
                "role": "Backend Engineer",
                "team": "Apple Services Reliability",
                "note": "Starter path for candidates who can discuss quality, APIs, and polished execution.",
                "locked": False,
            },
            {
                "name": "Daniel R.",
                "role": "Software Engineer",
                "team": "Cloud Services Platform",
                "note": "Unlocked fit for candidates with thoughtful product-oriented backend project stories.",
                "locked": False,
            },
            {
                "name": "Mina T.",
                "role": "Senior Platform Engineer",
                "team": "Identity Services",
                "note": "Premium match for candidates with stronger system reliability and launch-readiness examples.",
                "locked": True,
            },
            {
                "name": "Paul I.",
                "role": "Engineering Manager",
                "team": "Consumer Platform Architecture",
                "note": "Premium route for highly polished candidates with stronger ownership and precision signals.",
                "locked": True,
            },
        ],
        "ai_summary": "Good long-term fit if the resume becomes tighter, more polished, and more reliability-focused.",
        "resume_tips": [
            "Tighten every bullet so it sounds more intentional, polished, and outcome-focused.",
            "Show one example of owning a feature from implementation through testing and validation.",
            "Use language that connects backend work to user trust, reliability, and quality instead of only technical output.",
        ],
        "job_fit": {
            "score": 72,
            "headline": "Promising if the story becomes more polished",
            "explanation": "Apple rewards precise, reliable engineering. The current profile has potential, but it needs stronger craftsmanship and ownership signals to feel more aligned.",
            "reasons": [
                "Backend fundamentals are useful, but the story needs sharper quality and reliability language.",
                "A more polished resume would immediately improve fit perception.",
                "This becomes a stronger target once project bullets sound more intentional and end-user aware.",
            ],
        },
    },
}

for company in COMPANIES.values():
    company["insight_count"] = len(company["employee_insights"])
    company["question_count"] = len(company["interview_questions"])
    company["unlocked_referrals"] = len([match for match in company["referral_matches"] if not match["locked"]])
    company["premium_referrals"] = len([match for match in company["referral_matches"] if match["locked"]])


COMPANY_LIST = list(COMPANIES.values())
