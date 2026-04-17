from data.companies import COMPANIES, COMPANY_LIST


DASHBOARD_RECOMMENDATION_ORDER = ["microsoft", "google", "apple", "nvidia"]

RECENT_ACTIVITY = [
    {
        "title": "Google fit score refreshed",
        "detail": "Systems thinking remains the clearest upgrade area.",
        "time": "2 minutes ago",
    },
    {
        "title": "Microsoft referral preview unlocked",
        "detail": "Two open referral paths are now visible.",
        "time": "14 minutes ago",
    },
    {
        "title": "Nvidia skill gap updated",
        "detail": "Performance and distributed systems remain the biggest gaps.",
        "time": "31 minutes ago",
    },
]


def search_companies(query):
    if not query:
        return COMPANY_LIST

    normalized_query = query.strip().lower()
    results = []

    for company in COMPANY_LIST:
        search_blob = " ".join(
            [
                company["name"],
                company["tagline"],
                company["search_excerpt"],
                company["company_summary"],
                " ".join(company["values_for_engineers"]),
            ]
        ).lower()

        if normalized_query in search_blob:
            results.append(company)

    return results


def get_dashboard_recommendations():
    recommendations = []

    for slug in DASHBOARD_RECOMMENDATION_ORDER:
        company = COMPANIES[slug].copy()
        recommendations.append(company)

    return recommendations


def get_recent_activity():
    return RECENT_ACTIVITY


def get_quick_stats():
    return [
        {
            "value": 18,
            "label": "Tracked companies",
            "detail": "Coverage expanding across top tech employers.",
        },
        {
            "value": 96,
            "label": "Verified insight cards",
            "detail": "Trusted perspective across leading engineering teams.",
        },
        {
            "value": 48,
            "label": "Unlocked referrals",
            "detail": "Warm intro paths surfaced across the network.",
        },
        {
            "value": "6",
            "label": "Resume tracks",
            "detail": "Tailored guidance across multiple target paths.",
        },
    ]
